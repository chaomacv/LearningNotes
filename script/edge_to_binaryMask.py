import cv2
import numpy as np

# 读取图像
image = cv2.imread('Data\\obstacle\\1.jpg', cv2.IMREAD_GRAYSCALE)

# 进行 Canny 边缘检测
edges = cv2.Canny(image, 100, 200)  # 调整阈值以获得适当的边缘检测效果

# 寻找轮廓
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 创建空白图像作为掩码
mask = np.zeros_like(image)

# 在掩码上只绘制最外侧轮廓并填充为白色
cv2.drawContours(mask, [max(contours, key=cv2.contourArea)], -1, 255, thickness=cv2.FILLED)

# 反转掩码，使最外侧轮廓内部为白色
mask = cv2.bitwise_not(mask)

# 将原始图像和反转后的掩码相与，得到结果
result = cv2.bitwise_and(image, mask)

# 保存边缘图像和生成的结果
#cv2.imwrite('Data\\edge\\edges.jpg', edges)
#cv2.imwrite('Data\\result\\result.jpg', result)

# 显示图像
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.imshow('Filled Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
