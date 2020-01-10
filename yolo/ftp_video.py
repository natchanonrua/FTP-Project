from __future__ import division
import time
import torch 
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import cv2 
from util import *
from darknet import Darknet
from preprocess import prep_image, inp_to_image, letterbox_image
import pandas as pd
import random 
import pickle as pkl
import argparse
import copy

th1 = 0
count = 0

def get_test_input(input_dim, CUDA):
    img = cv2.imread("dog-cycle-car.png")
    img = cv2.resize(img, (input_dim, input_dim)) 
    img_ = img[:,:,::-1].transpose((2,0,1))
    img_ = img_[np.newaxis,:,:,:]/255.0
    img_ = torch.from_numpy(img_).float()
    img_ = Variable(img_)
    
    if CUDA:
        img_ = img_.cuda()
    
    return img_

def prep_image(img, inp_dim):
    """
    Prepare image for inputting to the neural network. 
    
    Returns a Variable 
    """
    
    orig_im = img
    dim = orig_im.shape[1], orig_im.shape[0]
    img = (letterbox_image(orig_im, (inp_dim, inp_dim)))    
    img_ = img[:,:,::-1].transpose((2,0,1)).copy()
    img_ = torch.from_numpy(img_).float().div(255.0).unsqueeze(0)
    return img_, orig_im, dim

def write(x, img,accum_image,th1):
    startpoint = x[1:3].int() 
    endpoint = x[3:5].int()
    # startpointN = x[1:3].int()
    # endpointN = x[2:4].int()

    startpointX = startpoint[0]+((endpoint[0]-startpoint[0])*0.4)
    startpointY = startpoint[1]+180
    endpointX = endpoint[0]-((endpoint[0]-startpoint[0])*0.4)
    endpointY = startpointY+((endpoint[1]-startpointY)*.1)-20
    
    startpoint[0] = startpointX.int()
    startpoint[1] = startpointY.int()
    endpoint[0] = endpointX.int()
    endpoint[1] = endpointY.int()

    c1 = tuple(startpoint)
    c2 = tuple(endpoint)
    # c3 = tuple(startpointN)
    # c4 = tuple(endpointN)

    # Something something classes
    cls = int(x[-1])
    # Tell classes ex.person car bag
    label = "{0}".format(classes[cls])

    # cv2.rectangle(img, (0, 0), (1979, 1079), (0, 0, 0), -1)

    # Rainbow color box every frame
    # color = random.choice(colors)
    color = (255, 255, 255) 
    # Draw box 
    cv2.rectangle(img, c1, c2,color, -1)
    # cv2.rectangle(img, c3, c4,color, -1)

    # # Text font size
    # t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 1 , 1)[0]
    # # Text box size
    # c2 = c1[0] + t_size[0] + 3, c1[1] + t_size[1] + 4
    # # Writing solid box -1 and the name of that object
    # cv2.rectangle(img, c1, c2,color, -1)
    # # Put text ex.person
    # cv2.putText(img, label, (c1[0], c1[1] + t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 1, [225,255,255], 1);
    
    # accum_image = cv2.add(img, th1, dtype = cv2.CV_64F)

    return img

def arg_parse():
    """
    Parse arguements to the detect module
    
    """
    
    
    parser = argparse.ArgumentParser(description='YOLO v3 Video Detection Module')
   
    parser.add_argument("--video", dest = 'video', help = 
                        "Video to run detection upon",
                        default = "video.avi", type = str)
    parser.add_argument("--dataset", dest = "dataset", help = "Dataset on which the network has been trained", default = "pascal")
    parser.add_argument("--confidence", dest = "confidence", help = "Object Confidence to filter predictions", default = 0.5)
    parser.add_argument("--nms_thresh", dest = "nms_thresh", help = "NMS Threshhold", default = 0.4)
    parser.add_argument("--cfg", dest = 'cfgfile', help = 
                        "Config file",
                        default = "cfg/yolov3.cfg", type = str)
    parser.add_argument("--weights", dest = 'weightsfile', help = 
                        "weightsfile",
                        default = "yolov3.weights", type = str)
    parser.add_argument("--reso", dest = 'reso', help = 
                        "Input resolution of the network. Increase to increase accuracy. Decrease to increase speed",
                        default = "416", type = str)
    return parser.parse_args()


if __name__ == '__main__':
    args = arg_parse()
    confidence = float(args.confidence)
    nms_thesh = float(args.nms_thresh)
    start = 0

    CUDA = torch.cuda.is_available()

    num_classes = 80

    CUDA = torch.cuda.is_available()
    
    bbox_attrs = 5 + num_classes
    
    print("Loading network.....")
    model = Darknet(args.cfgfile)
    model.load_weights(args.weightsfile)
    print("Network successfully loaded")

    model.net_info["height"] = args.reso
    inp_dim = int(model.net_info["height"])
    assert inp_dim % 32 == 0 
    assert inp_dim > 32

    if CUDA:
        model.cuda()
        
    model(get_test_input(inp_dim, CUDA), CUDA)

    model.eval()
    
    videofile = args.video
    
    cap = cv2.VideoCapture(videofile)
    
    assert cap.isOpened(), 'Cannot capture source'
    
    frames = 0
    start = time.time()

    first_iteration_indicator = 1

    fgbg = cv2.createBackgroundSubtractorMOG2()

    while cap.isOpened():
        
        for x in range(11): cap.grab()

        # ret, frame = cap.read()
        
        
        if (first_iteration_indicator == 1):
            ret, frame = cap.read()
            first_frame = copy.deepcopy(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            color = (255, 255, 255)

            height, width = gray.shape[:2]
            accum_image = np.zeros((height, width), np.float64)

            # cv2.rectangle(accum_image, (0, 0), (1979, 1079), color, -1)

            # cv2.imread('accum_image',accum_image)

            first_iteration_indicator = 0

        else:
            ret, frame = cap.read() 
            
           
            if ret:
                # cv2.imshow('img', frame)
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     break

                img, orig_im, dim = prep_image(frame, inp_dim)
                
                im_dim = torch.FloatTensor(dim).repeat(1,2)                        
                
                
                if CUDA:
                    im_dim = im_dim.cuda()
                    # cv2.imshow('img', img)
                    img = img.cuda()
                    
                
                with torch.no_grad():   
                    output = model(Variable(img), CUDA)
                output = write_results(output, confidence, num_classes, nms = True, nms_conf = nms_thesh)

                if type(output) == int:
                    frames += 1
                    print("FPS of the video is {:5.2f}".format( frames / (time.time() - start)))
                    cv2.imshow("frame", orig_im)
                    key = cv2.waitKey(1)
                    if key & 0xFF == ord('q'):
                        break
                    continue
                        
                im_dim = im_dim.repeat(output.size(0), 1)
                scaling_factor = torch.min(inp_dim/im_dim,1)[0].view(-1,1)
                
                output[:,[1,3]] -= (inp_dim - scaling_factor*im_dim[:,0].view(-1,1))/2
                output[:,[2,4]] -= (inp_dim - scaling_factor*im_dim[:,1].view(-1,1))/2
                
                output[:,1:5] /= scaling_factor
        
                for i in range(output.shape[0]):
                    output[i, [1,3]] = torch.clamp(output[i, [1,3]], 0.0, im_dim[i,0])
                    output[i, [2,4]] = torch.clamp(output[i, [2,4]], 0.0, im_dim[i,1])
                
                classes = load_classes('data/coco.names')
                colors = pkl.load(open("pallete", "rb"))

                orig_im.fill(0)
                
                list(map(lambda x: write(x, orig_im,accum_image,th1), output))

                cv2.imshow("frame", orig_im)
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break
                frames += 1
                print("FPS of the video is {:5.2f}".format( frames / (time.time() - start)))
            
            
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  

                fgmask = fgbg.apply(gray)  # remove the background

                # for testing purposes, show the result of the background subtraction
                # cv2.imshow('diff-bkgnd-frame', fgmask)

                thresh = 150
                maxValue = 10
                ret, th1 = cv2.threshold(fgmask, thresh, maxValue, cv2.THRESH_BINARY)
                # for testing purposes, show the threshold image
                cv2.imwrite('diff-th1.jpg', th1)

                # add to the accumulated image
                # cv2.imshow('accum_image',accum_image)
                accum_image = cv2.add(accum_image, th1, dtype = cv2.CV_64F)
                # for testing purposes, show the accumulated image
                # cv2.imwrite('diff-accum.jpg', accum_image)

                # for testing purposes, control frame by frame
                # raw_input("press any key to continue")

            else:
                break

            # for testing purposes, show the current frame
            # cv2.imshow('frame', gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # if ret:
            
        #     img, orig_im, dim = prep_image(frame, inp_dim)
            
        #     im_dim = torch.FloatTensor(dim).repeat(1,2)                        
            
            
        #     if CUDA:
        #         im_dim = im_dim.cuda()
        #         img = img.cuda()
            
        #     with torch.no_grad():   
        #         output = model(Variable(img), CUDA)
        #     output = write_results(output, confidence, num_classes, nms = True, nms_conf = nms_thesh)

        #     if type(output) == int:
        #         frames += 1
        #         print("FPS of the video is {:5.2f}".format( frames / (time.time() - start)))
        #         cv2.imshow("frame", orig_im)
        #         key = cv2.waitKey(1)
        #         if key & 0xFF == ord('q'):
        #             break
        #         continue
            
            

            
        #     im_dim = im_dim.repeat(output.size(0), 1)
        #     scaling_factor = torch.min(inp_dim/im_dim,1)[0].view(-1,1)
            
        #     output[:,[1,3]] -= (inp_dim - scaling_factor*im_dim[:,0].view(-1,1))/2
        #     output[:,[2,4]] -= (inp_dim - scaling_factor*im_dim[:,1].view(-1,1))/2
            
        #     output[:,1:5] /= scaling_factor
    
        #     for i in range(output.shape[0]):
        #         output[i, [1,3]] = torch.clamp(output[i, [1,3]], 0.0, im_dim[i,0])
        #         output[i, [2,4]] = torch.clamp(output[i, [2,4]], 0.0, im_dim[i,1])
               
        #     classes = load_classes('data/coco.names')
        #     colors = pkl.load(open("pallete", "rb"))
            
        #     list(map(lambda x: write(x, orig_im,accum_image,th1), output))
            
            
        #     cv2.imshow("frame", orig_im)
        #     key = cv2.waitKey(1)
        #     if key & 0xFF == ord('q'):
        #         break
        #     frames += 1
        #     print("FPS of the video is {:5.2f}".format( frames / (time.time() - start)))

            
        # else:
        #     break
    
    # #MOTION###################################################################################################3
    # cap = cv2.VideoCapture('TownCentreXVID.avi')
    # # pip install opencv-contrib-python
    # fgbg = cv2.createBackgroundSubtractorMOG2()

    # # number of frames is a variable for development purposes, you can change the for loop to a while(cap.isOpened()) instead to go through the whole video
    # num_frames = 1500

    # first_iteration_indicator = 1
    # for i in range(0, num_frames):
    #     '''
    #     There are some important reasons this if statement exists:
    #         -in the first run there is no previous frame, so this accounts for that
    #         -the first frame is saved to be used for the overlay after the accumulation has occurred
    #         -the height and width of the video are used to create an empty image for accumulation (accum_image)
    #     '''
    #     if (first_iteration_indicator == 1):
    #         ret, frame = cap.read()
    #         first_frame = copy.deepcopy(frame)
    #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #         height, width = gray.shape[:2]
    #         accum_image = np.zeros((height, width), np.float64)
    #         first_iteration_indicator = 0
    #     else:
    #         ret, frame = cap.read()  # read a frame
    #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to grayscale

    #         fgmask = fgbg.apply(gray)  # remove the background

    #         # for testing purposes, show the result of the background subtraction
    #         # cv2.imshow('diff-bkgnd-frame', fgmask)

    #         # apply a binary threshold only keeping pixels above thresh and setting the result to maxValue.  If you want
    #         # motion to be picked up more, increase the value of maxValue.  To pick up the least amount of motion over time, set maxValue = 1
    #         thresh = 150
    #         maxValue = 1
    #         ret, th1 = cv2.threshold(fgmask, thresh, maxValue, cv2.THRESH_BINARY)
    #         # for testing purposes, show the threshold image
    #         cv2.imwrite('diff-th1.jpg', th1)

    #         # add to the accumulated image
    #         # cv2.imshow('accum_image',accum_image)
    #         accum_image = cv2.add(accum_image, th1, dtype = cv2.CV_64F)
    #         # for testing purposes, show the accumulated image
    #         # cv2.imwrite('diff-accum.jpg', accum_image)

    #         # for testing purposes, control frame by frame
    #         # raw_input("press any key to continue")

    #     # for testing purposes, show the current frame
    #     # cv2.imshow('frame', gray)

    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

    # apply a color map
    # COLORMAP_PINK also works well, COLORMAP_BONE is acceptable if the background is dark
    accum_image = np.uint8(accum_image)
    color_image = im_color = cv2.applyColorMap(accum_image, cv2.COLORMAP_JET)
    # for testing purposes, show the colorMap image
    # cv2.imwrite('diff-color.jpg', color_image)

    # overlay the color mapped image to the first frame
    result_overlay = cv2.addWeighted(first_frame, 0.4, color_image, 0.4, 0)

    # save the final overlay image
    cv2.imwrite('diff-overlay.jpg', result_overlay)

    # cleanup
    cap.release()
    cv2.destroyAllWindows()
    

    
    

