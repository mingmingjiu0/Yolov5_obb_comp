import os
import sys
import cv2
import argparse
from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
from utils.plots import Annotator, colors




def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--srcpath',
                        default='/home/hzm/Datasets/comp_test/images/',
                        help='test config file path')
    parser.add_argument('--labelpath',
                        default='/home/hzm/PycharmProjects/yolov5_obb/runs/'
                                'detect/exp7/labels_merged_final/',
                        help='test config file path')
    args = parser.parse_args()
    return args


def main(srcpath, labelpath):
    filelist = os.listdir(labelpath)
    for files in filelist:
        labelfilepath = os.path.join(labelpath, files)
        imgfilepath = os.path.join(srcpath,files.split('.')[0] + '.jpg')
        img = cv2.imread(imgfilepath)
        print(imgfilepath, labelfilepath)
        with open(labelfilepath, 'r') as f_in:
            lines = f_in.readlines()
            splitlines = [x.strip().split(' ') for x in lines]
            annotator = Annotator(img)
            if len(splitlines):
                for cls, conf, *poly in splitlines:
                    c = int(cls)  # integer class
                    annotator.poly_label(list(map(float,poly)), None, color=colors(c, True))
        im0 = annotator.result()
        cv2.imshow(str(imgfilepath), im0)
        cv2.waitKey(0)  # 1 millisecond


if __name__ == "__main__":
    args = parse_args()
    main(args.srcpath, args.labelpath)
    print('Result Merge Done!')
