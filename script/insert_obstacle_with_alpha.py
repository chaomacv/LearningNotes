import cv2
import numpy as np

def merge_with_alpha(image_path, alpha_path):
    img = cv2.imread(image_path)
    alpha = cv2.imread(alpha_path, 0) #读取灰度图像
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
    return dstt

def insert_obstacle_with_parameters(background_path, obstacle_path, obstacle_alpha_path, output_path, position=(100, 100), obstacle_size=(200, 200), hsv_values=(0, 255, 255)):
    # 读取背景图像和带有透明通道的障碍物图像
    background = cv2.imread(background_path)
    obstacle_image = merge_with_alpha(obstacle_path, obstacle_alpha_path)

    # 获取插入位置
    x, y = position
    

    # 获取调整后的障碍物大小
    obstacle = cv2.resize(obstacle_image, (obstacle_size[0], obstacle_size[1]))

    # 获取障碍物的宽度和高度
    h, w = obstacle.shape[:2]

    # 限制插入位置，确保不超出背景图像范围
    x = max(0, min(x, background.shape[1] - w))
    y = max(0, min(y, background.shape[0] - h))

    # 提取障碍物的透明通道
    alpha_channel = obstacle[:, :, 3] / 255.0

    # 调整障碍物的HSV值
    #hsv_obstacle = cv2.cvtColor(obstacle[:, :, :3], cv2.COLOR_BGR2HSV)
    #hsv_obstacle[:, :, 0] = hsv_values[0]  # 设定色调
    #hsv_obstacle[:, :, 1] = hsv_values[1]  # 设定饱和度
    #hsv_obstacle[:, :, 2] = hsv_values[2]  # 设定明度

    # 将调整后的障碍物插入背景图像
    for c in range(0, 3):
        background[y:y+h, x:x+w, c] = (1 - alpha_channel) * background[y:y+h, x:x+w, c] + alpha_channel #* hsv_obstacle[:, :, c]

    # 保存结果
    cv2.imwrite(output_path, background)

if __name__ == "__main__":
    # 替换以下路径为你的实际路径
    background_path = 'D:\\learn\\script\\sample\\0004.jpg'
    obstacle_path = 'D:\\learn\\script\\Data\\obstacle.v1i.coco-segmentation\\original\\124.png'
    obstacle_alpha_path = 'D:\\learn\\script\\Data\\obstacle.v1i.coco-segmentation\\alpha\\124.png'
    output_path = 'D:\\learn\\script\\Data\\result\\1.jpg'

    # 插入位置（矩形的左上角坐标）
    insertion_position = (100, 100)

    # 障碍物大小
    obstacle_size = (300, 300)

    # HSV值
    hsv_values = (0, 0, 0)  

    insert_obstacle_with_parameters(background_path, obstacle_path, obstacle_alpha_path, output_path, insertion_position, obstacle_size, hsv_values)
