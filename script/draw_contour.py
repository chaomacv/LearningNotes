import cv2
import numpy as np

# 读取二值图像
image = cv2.imread('D:\\learn\\script\\demo\\data\\alpha\\124.png', cv2.IMREAD_GRAYSCALE)

# 阈值化处理
ret, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 寻找轮廓
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 创建一个空白图像用于绘制轮廓
contour_image = np.zeros_like(binary_image)

# 绘制轮廓
cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 2)

# 显示原始图像和提取的轮廓
cv2.imshow('Original Image', binary_image)
cv2.imshow('Contour Image', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



# 示例使用
background_path = 'D:\\learn\\script\\demo\\data\\background\\0007.jpg'
obstacle_path = 'D:\\learn\\script\\demo\\data\\obstacle\\128.png'
alpha_path = 'D:\\learn\\script\\demo\\data\\alpha\\124.png'
insert_position = (500, 500)



