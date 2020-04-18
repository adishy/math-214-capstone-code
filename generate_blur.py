import cv2
import os
import sys
import numpy as np
from matplotlib import pyplot as plt

def blur_and_write_image(img_src, dst_dir, kernel_size): 
    img_src = os.path.abspath(img_src)
    img_dst = os.path.join(os.path.abspath(dst_dir), f"blurred_{kernel_size}.png")
    img = cv2.imread(img_src)   
    blur = cv2.blur(img, (kernel_size,kernel_size))
    cv2.imwrite(img_dst, blur)

def repeat_blurs_and_write_image(img_src, dst_dir, repeat, kernel_size = 15):
    img_src = os.path.abspath(img_src)
    img_dst = os.path.join(os.path.abspath(dst_dir), f"repeated_{repeat}_times.png")
    img = cv2.imread(img_src)
    for i in range(repeat):
        blur = cv2.blur(img, (kernel_size,kernel_size)) 
    cv2.imwrite(img_dst, blur)
        
def create_increasing_kernels(img_src, dst_dir, start = 10, end = 90, delta = 20):
    output_dir = os.path.join(dst_dir, f"{img_src.split('.')[0]}_inc_kernels")
    img_src = os.path.abspath(img_src)
    os.makedirs(os.path.abspath(output_dir), exist_ok=True)

    for i in range(start, end, delta):
        blur_and_write_image(img_src, output_dir, i)


def create_repeated_blurs(img_src, dst_dir, start = 1, end = 5, delta = 1):
    output_dir = os.path.join(dst_dir, f"{img_src.split('.')[0]}_repeated_blurs")
    img_src = os.path.abspath(img_src)
    os.makedirs(os.path.abspath(output_dir), exist_ok=True)

    for i in range(start, end, delta):
        repeat_blurs_and_write_image(img_src, output_dir, i)


def main():
    if len(sys.argv) < 2:
        print("Not enough arguments")
        return 1
    filename = sys.argv[1]
    output_directory = os.path.join(".", f'{os.path.basename(filename)}_output'.replace('.', '_'))
    os.makedirs(output_directory, exist_ok=True)
    create_increasing_kernels(filename, output_directory)
    create_repeated_blurs(filename, output_directory)

if __name__ == '__main__':
    main()
