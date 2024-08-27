import torch
import aestream
import cv2
import numpy as np
import math
import argparse


def parse_args():

    parser = argparse.ArgumentParser(description='Automatic Coordinate Location')

    parser.add_argument('-p', '--port', type= int, help="Port for events", default=5050)
    parser.add_argument('-s', '--scale', type=int, help="Image scale", default=1)
    parser.add_argument('-x', '--res-x', type=int, help="Image X resolution", default=1280)
    parser.add_argument('-y', '--res-y', type=int, help="Image Y resolution", default=720)

    return parser.parse_args()

if __name__ == '__main__':

    args = parse_args()

    new_l = math.ceil(args.res_x*args.scale)
    new_w = math.ceil(args.res_y*args.scale)
    window_name = 'My Display'
    cv2.namedWindow(window_name)

    # Stream events from UDP port 3333 (default)
    frame = np.zeros((args.res_x, args.res_y, 3))

    with aestream.UDPInput((args.res_x, args.res_y), device = 'cpu', port=args.port) as stream1:
                
        while True:


            frame[0:args.res_x,0:args.res_y,1] =  stream1.read().numpy() 
            image = cv2.resize(frame.transpose(1,0,2), (new_l, new_w), interpolation = cv2.INTER_AREA)
            cv2.imshow(window_name, image)
            cv2.waitKey(1)


        