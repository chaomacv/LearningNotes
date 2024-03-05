from PIL import Image

# 定义文件路径
background_path = 'D:\\learn\\script\\sample\\0004.jpg'
obstacle_path = 'D:\\learn\\script\\Data\\obstacle.v1i.coco-segmentation\\original\\124.png'
obstacle_alpha_path = 'D:\\learn\\script\\Data\\obstacle.v1i.coco-segmentation\\alpha\\124.png'
output_path = 'D:\\learn\\script\\Data\\result\\1.jpg'

# 打开背景图和障碍物图
background = Image.open(background_path)
obstacle = Image.open(obstacle_path)
obstacle_alpha = Image.open(obstacle_alpha_path)

# 指定障碍物的目标大小
target_obstacle_size = (200, 200)  # 你可以根据需要调整大小

# 调整障碍物大小
obstacle = obstacle.resize(target_obstacle_size, Image.ANTIALIAS)
obstacle_alpha = obstacle_alpha.resize(target_obstacle_size, Image.LANCZOS)



# 获得调整大小后的障碍物图的大小
obstacle_width, obstacle_height = obstacle.size

# 计算将障碍物放置到背景图中央的位置
x_position = (background.width - obstacle_width) // 3
y_position = (background.height - obstacle_height) // 1

# 将障碍物图粘贴到背景图中央
background.paste(obstacle, (x_position, y_position), obstacle_alpha)

# 保存结果
background.save(output_path)
