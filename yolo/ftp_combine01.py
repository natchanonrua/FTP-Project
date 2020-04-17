from __future__ import division

from datetime import datetime

# import ui as interface
import calendar
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
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

th = 0
people_number = 0
duration = 0


def get_test_input(input_dim, CUDA):
    img = cv2.imread("dog-cycle-car.png")
    img = cv2.resize(img, (input_dim, input_dim))
    img_ = img[:, :, ::-1].transpose((2, 0, 1))
    img_ = img_[np.newaxis, :, :, :] / 255.0
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
    img_ = img[:, :, ::-1].transpose((2, 0, 1)).copy()
    img_ = torch.from_numpy(img_).float().div(255.0).unsqueeze(0)
    return img_, orig_im, dim


def write(x, img):
    c1 = tuple(x[1:3].int())
    # print(x[1:3].int())
    # print(x[1])
    # print('++++++')
    # print(x[2])
    # print(c1)
    c2 = tuple(x[3:5].int())
    # print(c2)
    # print(x[3:5].int())
    cls = int(x[-1])
    label = "{0}".format(classes[cls])
    color = random.choice(colors)

    # Writing solid box -1 and the name of that object
    cv2.rectangle(img, c1, c2, color, 1)
    t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 1, 1)[0]
    c2 = c1[0] + t_size[0] + 3, c1[1] + t_size[1] + 4

    cv2.rectangle(img, c1, c2, color, -1)
    cv2.putText(img, label, (c1[0], c1[1] + t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 1, [225, 255, 255], 1);

    return img


def write_heatmap(x, img):
    startpoint = x[1:3].int()
    endpoint = x[3:5].int()

    startpointX = startpoint[0] + ((endpoint[0] - startpoint[0]) * 0.4)
    startpointY = startpoint[1] + 180
    endpointX = endpoint[0] - ((endpoint[0] - startpoint[0]) * 0.4)
    endpointY = startpointY + ((endpoint[1] - startpointY) * .1) - 20

    startpoint[0] = startpointX.int()
    startpoint[1] = startpointY.int()
    endpoint[0] = endpointX.int()
    endpoint[1] = endpointY.int()

    c1 = tuple(startpoint)
    c2 = tuple(endpoint)

    color = (255, 255, 255)
    # Draw box
    cv2.rectangle(img, c1, c2, color, -1)
    # cv2.rectangle(img, c3, c4,color, -1)

    return img


def arg_parse():
    """
    Parse arguements to the detect module
    
    """

    parser = argparse.ArgumentParser(description='YOLO v3 Video Detection Module')

    parser.add_argument("--video", dest='video', help=
    "Video to run detection upon",
                        default="video.avi", type=str)
    parser.add_argument("--dataset", dest="dataset", help="Dataset on which the network has been trained",
                        default="pascal")
    parser.add_argument("--confidence", dest="confidence", help="Object Confidence to filter predictions", default=0.5)
    parser.add_argument("--nms_thresh", dest="nms_thresh", help="NMS Threshhold", default=0.4)
    parser.add_argument("--cfg", dest='cfgfile', help=
    "Config file",
                        default="cfg/yolov3.cfg", type=str)
    parser.add_argument("--weights", dest='weightsfile', help=
    "weightsfile",
                        default="yolov3.weights", type=str)
    parser.add_argument("--reso", dest='reso', help=
    "Input resolution of the network. Increase to increase accuracy. Decrease to increase speed",
                        default="416", type=str)
    return parser.parse_args()


if __name__ == '__main__':
    args = arg_parse()
    confidence = float(args.confidence)
    nms_thesh = float(args.nms_thresh)

    # fig = plt.figure()
    # ax1 = fig.add_subplot(1,1,1)
    start = 0

    floor = 0

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


    zone_time = 0
    point_x1 = 0
    zone = open('zone_position.txt', 'r').read()
    lines = zone.split('\n')
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            if zone_time == 0:
                point_x1 = int(x)
                point_y1 = int(y)
                zone_time = 1
            else:
                point_x2 = int(x)
                point_y2 = int(y)


    f = open('soul.txt', 'r').read()
    lines = f.split('\n')
    for line in lines:
        if len(line) > 0:
            x, y = line.split(',')

    start = time.gmtime(int(y))

    first_iteration_indicator = 1

    count = 0
    num_count = 0

    fgbg = cv2.createBackgroundSubtractorMOG2()

    file_name = datetime.now().strftime("%Y%m%d-%H%M%S")

    # output_fps = cap.get(cv2.CAP_PROP_FPS)

    output_fps = 2.0

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    width_video = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    height_video = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frame_size = (width_video, height_video)

    output_video = cv2.VideoWriter(file_name + ".avi", fourcc, output_fps, frame_size)

    calculated_fps = float("{0:.1f}".format(cap.get(cv2.CAP_PROP_FPS)))

    print(calculated_fps)

    no_fps = float(calculated_fps / 2) - 1

    grab_fps = True

    if (no_fps % 1) != 0:
        odd_fps = True
        checked_fps = False
    else:
        odd_fps = False

    print(no_fps)

    while cap.isOpened():
        #
        # if not grab_fps:
        #     if odd_fps is True:
        #         if checked_fps is False:
        #             no_fps = no_fps + 1
        #             checked_fps = True
        #         else:
        #             no_fps = no_fps - 1
        #             checked_fps = False
        #     print(no_fps)
        #     for x in range(int(no_fps)):
        #         cap.grab()
        #     grab_fps = True
        #     print("Grab")
        # else:
        #     print("Not Grab")
        #     grab_fps = False

        if first_iteration_indicator == 1:
            # print(start)
            ret, frame = cap.read()
            first_frame = copy.deepcopy(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            height, width = gray.shape[:2]
            accum_image = np.zeros((height, width), np.float64)
            first_iteration_indicator = 0
            if count == 0:
                f = open("count.txt", "w+")
                count = 1
            grab_fps = True
        else:
            for x in range(int(no_fps)):
                cap.grab()
            ret, frame = cap.read()
            if ret:

                img, orig_im, dim = prep_image(frame, inp_dim)

                im_dim = torch.cuda.FloatTensor(dim).repeat(1, 2)

                if CUDA:
                    im_dim = im_dim.cuda()
                    img = img.cuda()

                with torch.no_grad():
                    output = model(Variable(img), CUDA)

                output = write_results(output, confidence, num_classes, nms=True, nms_conf=nms_thesh)
                # print(output[1])
                f = open("doujin.txt", "w+")
                f.write("%s \r\n" % (output))

                if type(output) == int:
                    frames += 1
                    # print("FPS of the video is {:5.2f}".format( frames / (time.time() - start)))
                    # cv2.imshow("frame", orig_im)
                    key = cv2.waitKey(1)
                    if key & 0xFF == ord('q'):
                        break
                    continue

                im_dim = im_dim.repeat(output.size(0), 1)
                scaling_factor = torch.min(inp_dim / im_dim, 1)[0].view(-1, 1)

                output[:, [1, 3]] -= (inp_dim - scaling_factor * im_dim[:, 0].view(-1, 1)) / 2
                output[:, [2, 4]] -= (inp_dim - scaling_factor * im_dim[:, 1].view(-1, 1)) / 2

                output[:, 1:5] /= scaling_factor

                for i in range(output.shape[0]):
                    if(point_x1 != 0):
                        x_start = torch.clamp(output[i, [1]], 0.0).int()
                        x_end = torch.clamp(output[i, [3]], 0.0).int()
                        y_start = torch.clamp(output[i, [2]], 0.0).int()
                        y_end = torch.clamp(output[i, [4]], 0.0).int()
                        if point_x1 <= x_start <= point_x2 or point_x1 <= x_end <= point_x2:
                            # print('num 1')
                            if point_y1 <= y_start <= point_y2 or point_y1 <= y_end <= point_y2:
                                floor = floor + 1
                            # if(point_y1 <= y_start <=point_y2 and point_y1 <= y_end <= point_y2):
                            #    print('num 2')

                    # print('x_start')
                    # print(x_start)
                    # print('x_end')
                    # print(x_end)
                    # print('------------1')
                    # print('y_start')
                    # print(y_start)
                    # print('y_end')
                    # print(y_end)
                    # print('------------2')
                    output[i, [1, 3]] = torch.clamp(output[i, [1, 3]], 0.0, im_dim[i, 0])
                    output[i, [2, 4]] = torch.clamp(output[i, [2, 4]], 0.0, im_dim[i, 1])

                # print(floor)
                count_z = floor
                if (count_z != 0):
                    floor = 0

                classes = load_classes('data/coco.names')
                colors = pkl.load(open("pallete", "rb"))

                m = list(map(lambda x: write(x, orig_im), output))

                # cv2.imshow("frame", orig_im)
                output_video.write(orig_im)
                orig_im.fill(0)

                h = list(map(lambda x: write_heatmap(x, orig_im), output))

                # print(count_z)
                if(point_x1 != 0):
                    s_z = count_z
                    print(s_z)
                    if (s_z != 0):
                        count_z = 0
                else:
                    s_z = len(m)

                # interface.Ui_main().set_number(s)

                if (count == 1):
                    num_count += 1
                    i = time.strftime("%H:%M:%S", start)
                    h = calendar.timegm(start)
                    f = open("count.txt", "a+")
                    f.write("%s,%d,%d \r\n" % (i, s_z, num_count))
                    h = h + 0.5 * count
                    count = 2
                    start = time.gmtime(h)
                else:
                    num_count += 1
                    i = time.strftime("%H:%M:%S", start)
                    h = calendar.timegm(start)
                    f = open("count.txt", "a+")
                    f.write("%s,%d,%d \r\n" % (i, s_z, num_count))
                    h = h + 0.5 * count
                    count = 1
                    start = time.gmtime(h)

                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break
                frames += 1
                # print("FPS of the video is {:5.2f}".format( frames / (time.time() - start)))
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                fgmask = fgbg.apply(gray)

                thresh = 100
                maxValue = 10
                ret, th1 = cv2.threshold(fgmask, thresh, maxValue, cv2.THRESH_BINARY)

                cv2.imwrite('diff-th1.jpg', th1)

                accum_image = cv2.add(accum_image, th1, dtype=cv2.CV_64F)
            else:
                break

    accum_image = np.uint8(accum_image)
    color_image = im_color = cv2.applyColorMap(accum_image, cv2.COLORMAP_JET)
    # overlay the color mapped image to the first frame
    result_overlay = cv2.addWeighted(first_frame, 0.4, color_image, 0.4, 0)

    # save the final overlay image
    cv2.imwrite(file_name + '-heatmap.jpg', result_overlay)

    graph_data = open('count.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    zs = []
    ms = []
    us = []
    temp = 0
    p = len(lines) / 10
    c = 0
    m = 0
    num = 0
    # blank = string.whitespace
    for line in lines:
        num += 1
        if len(line) > 1:
            x, y, z = line.split(',')
            result = time.strptime(x, "%H:%M:%S")
            if temp == 0:
                xs.append(int(z))
                ys.append(int(y))
                zs.append(x)
                temp = 1
            else:
                if c >= 0 and c < p:
                    m = m + int(y)
                    c += 1
                else:
                    m = m + int(y)
                    c += 1
                    m = m / c
                    xs.append(int(z))
                    print(z)
                    ys.append(int(m))
                    print(",")
                    zs.append(x)
                    print(x)
                    m = 0
                    c = 0
        if num >= len(lines):
            m = m + int(y)
            c += 1
            m = m / c
            xs.append(int(z))
            print(z)
            ys.append(int(m))
            print(",")
            zs.append(x)
            print(x)

    plt.xticks(xs, zs)
    plt.plot(xs, ys)
    plt.savefig(file_name + '-graph.jpg')

    # cleanup1
    output_video.release()
    cap.release()
    cv2.destroyAllWindows()
