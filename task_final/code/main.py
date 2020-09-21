'''
Descripttion : 
Author       : 傅宇千
Date         : 2020-09-09 17:17:19
LastEditors  : 傅宇千
LastEditTime : 2020-09-21 00:26:41
'''
'''
Function:
    paper named  "Combining Sketch and Tone for Pencil Drawing Production-Cewu Lu, Li Xu, Jiaya Jia".
	This is the main function.
Author:
	FYQ
'''

import cfg
import argparse
from utils.drawing import PencilDrawing
'''main'''


def main(image_path, mode, cfg, savename='output.jpg'):
    drawer = PencilDrawing(kernel_size_scale=cfg.kernel_size_scale,
                           stroke_width=cfg.stroke_width,
                           weights_color=cfg.weights_color,
                           weights_gray=cfg.weights_gray,
                           texture_path=cfg.texture_path,
                           color_depth=cfg.color_depth)
    drawer.draw(image_path=image_path, mode=mode, savename=savename)


'''run'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="PencilDrawing")
    parser.add_argument('-i',
                        dest='image_path',
                        help='the path of image need to be processed')
    parser.add_argument('-m',
                        dest='mode',
                        help='color or gray',
                        default='gray')
    parser.add_argument('-s',
                        dest='savename',
                        help='filename of output',
                        default='output.jpg')
    args = parser.parse_args()
    if args.mode and args.image_path and args.savename:
        main(args.image_path, args.mode, cfg, args.savename)
