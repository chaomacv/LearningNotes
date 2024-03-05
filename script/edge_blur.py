import cv2
import numpy as np

import cv2
import numpy as np
from PIL import Image

import cv2
import numpy as np
from PIL import Image

def contours_blur(obstacle,alpha,thickness=10):
    """为background添加轮廓图"""
    # 将图像转换为 NumPy 数组
    obstacle_np = np.array(obstacle)
    alpha_np = np.array(alpha)
    print(obstacle_np.shape,alpha_np.shape)
    

    # 阈值化处理
    ret, binary_image = cv2.threshold(alpha_np, 127, 255, cv2.THRESH_BINARY)

    # 寻找轮廓
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 创建一个空白图像用于绘制轮廓
    contour_image = np.zeros_like(binary_image)

    # 绘制轮廓
    cv2.drawContours(contour_image, contours, -1, (255, 255, 255), thickness)

    #显示轮廓
    #image_contour = Image.fromarray(contour_image.astype(np.uint8))
    #image_contour.show()


    # 将contour_image扩展为三通道
    contour_image_color = cv2.merge([contour_image, contour_image, contour_image])
    # 将图像和掩码相乘，保留轮廓区域
    contour_image = cv2.bitwise_and(obstacle_np, contour_image_color)


    # 对轮廓周围的区域进行模糊处理
    blurred_contour = cv2.GaussianBlur(contour_image, (5, 5), 0)

    # 将模糊的轮廓区域放回原始图像
    result = obstacle_np.copy()
    result[contour_image > 0] = blurred_contour[contour_image > 0]

    # 将 NumPy 数组转换回 PIL 图像
    result = Image.fromarray(result.astype(np.uint8))

    return result


# 示例使用
obstacle_path = 'D:\\learn\\script\\demo\\data\\obstacle\\128.png'
alpha_path = 'D:\\learn\\script\\demo\\data\\alpha\\128.png'
obstacle = Image.open(obstacle_path)
alpha = Image.open(alpha_path)



#插入
result_image = contours_blur(obstacle, alpha)
# 显示结果图像
result_image.show()
obstacle.show()



# 示例使用
background_path = 'D:\\learn\\script\\demo\\data\\background\\0007.jpg'
obstacle_path = 'D:\\learn\\script\\demo\\data\\obstacle\\128.png'
alpha_path = 'D:\\learn\\script\\demo\\data\\alpha\\128.png'
insert_position = (500, 500)





