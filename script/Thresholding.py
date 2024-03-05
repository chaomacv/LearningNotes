import os
import cv2
import numpy as np

def Threshold_image(image_path,output_folder):
    # 读取图像
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 将图像转为灰度
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #  使用阈值处理（这里使用大津法）
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 反转图像颜色
    inverted_image = cv2.bitwise_not(binary_image)
    output_folder = os.path.join(output_folder,os.path.basename(image_path))
    cv2.imwrite(output_folder,inverted_image)

    # 显示结果
    #cv2.imshow('Threshold Image', inverted_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()



if __name__ == "__main__":
    # 输入文件夹路径
    image_dir = "D:\\learn\\script\\Data\\obstacle"

    # 输出文件夹路径
    output_folder = "D:\\learn\\script\\Data\\mask_threshold\\"
    image_list=[]
    image_list = [os.path.join(image_dir, file) for file in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, file))]

    for image_path in image_list:
        Threshold_image(image_path, output_folder)