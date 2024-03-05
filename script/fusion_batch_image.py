import cv2
import numpy as np
import os
from PIL import Image
from os.path import join as opj
import argparse

def main(image_dir, alpha_dir, output_dir):
    # 在这里执行你的主程序逻辑
    print("Image Directory:", image_dir)
    print("alpha Directory:", alpha_dir)
    print("output Directory:", output_dir)



def fusion(img_dir,alpha_dir,output_dir,num):

    img = cv2.imread(img_dir)
    alpha = cv2.imread(alpha_dir, 0) #读取灰度图像
    #print("img.shape(),alpha.shape():")
    #print(img.shape,alpha.shape)
 
    height,width,channel=img.shape
    b, g, r = cv2.split(img)
 
    #-----------------1.获取透明的前景图像-----------
    dstt = np.zeros((4,height,width),dtype=img.dtype)
    dstt[0][0:height,0:width] = b
    dstt[1][0:height,0:width] = g
    dstt[2][0:height,0:width] = r
    dstt[3][0:height,0:width] = alpha
    #获取透明的前景图像
    #cv2.imwrite(f"{output_dir}/fore_{num}.png", cv2.merge(dstt))
    cv2.imwrite(f"{output_dir}/{os.path.basename(img_dir)}", cv2.merge(dstt))

    """
    #-----------------2.与新背景图像合成-----------
    bg= np.zeros((3,height,width),dtype=img.dtype)  #生成背景图像
    bg[2][0:height,0:width] = 255 #背景图像采用红色
 
    dstt = np.zeros((3,height,width),dtype=img.dtype)
 
    for i in range(3):
        dstt[i][:,:] = bg[i][:,:]*(255.0-alpha)/255
        dstt[i][:,:] += np.array(img[:,:,i]*(alpha/255), dtype=np.uint8)
    cv2.imwrite(f"{output_dir}/{os.path.basename(img_dir)}", cv2.merge(dstt))
    """

if __name__ == '__main__':
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description='Process images.')
    # 添加命令行参数
    parser.add_argument('--image_dir', type=str, default='ImgData/original',help='Path to image directory')
    parser.add_argument('--alpha_dir', type=str, default='ImgData/alpha',help='Path to alpha directory')
    parser.add_argument('--output_dir', type=str, default='ImgData/output',help='Path to output directory')
    # 解析命令行参数
    args = parser.parse_args()
    # 将参数传递给主程序
    args.image_dir = "D:\\learn\\script\\Data\\obstacle.v1i.coco-segmentation\\original"
    args.alpha_dir = "D:\\learn\\script\\Data\\obstacle.v1i.coco-segmentation\\alpha"
    args.output_dir = "D:\\learn\\script\\Data\\obstacle.v1i.coco-segmentation\\result_0"

    main(args.image_dir, args.alpha_dir, args.output_dir)


    image_list=[]
    image_list = [os.path.join(args.image_dir, file) for file in os.listdir(args.image_dir) if os.path.isfile(os.path.join(args.image_dir, file))]

    alpha_list=[]
    alpha_list = [os.path.join(args.alpha_dir, file) for file in os.listdir(args.alpha_dir) if os.path.isfile(os.path.join(args.alpha_dir, file))]
    #for i,(image_dir, alpha_dir) in enumerate(zip(image_list,alpha_list)):
    #    print(image_dir,alpha_dir,"\n")
    
    for i,(image_dir, alpha_dir) in enumerate(zip(image_list,alpha_list)):
        fusion(image_dir,alpha_dir,args.output_dir,i)