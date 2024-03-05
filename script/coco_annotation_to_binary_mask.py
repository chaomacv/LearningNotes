import json
import os
import numpy as np
from PIL import Image, ImageDraw

def create_binary_mask(annotation_file, image_folder, output_folder):
    # 读取COCO格式的JSON文件
    with open(annotation_file, 'r') as f:
        annotations = json.load(f)

    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 处理每个图像
    for image_info in annotations['images']:
        image_id = image_info['id']
        image_file_name = image_info['file_name']
        image_path = os.path.join(image_folder, image_file_name)

        # 创建和初始化二进制掩码
        image = Image.open(image_path)
        width, height = image.size
        binary_mask = np.zeros((height, width), dtype=np.uint8)

        # 找到与当前图像相关的所有标注
        for annotation in annotations['annotations']:
            if annotation['image_id'] == image_id:
                segmentation = annotation['segmentation']
                
                # 使用PIL库的ImageDraw.polygon方法创建掩码
                mask = Image.new('L', (width, height), 0)
                ImageDraw.Draw(mask).polygon(segmentation[0], outline=1, fill=1)
                binary_mask += np.array(mask)

        # 将二进制掩码保存为图像
        binary_mask[binary_mask > 0] = 255
        binary_mask_image = Image.fromarray(binary_mask)

        # 获取图像文件名（去掉路径）
        image_base_name = os.path.basename(image_file_name)

        # 保存二进制掩码文件，文件名与原图像文件名相同
        output_path = os.path.join(output_folder, f"{image_base_name}.png")
        binary_mask_image.save(output_path)

if __name__ == "__main__":
    # 替换以下路径为你的实际路径
    annotation_file = 'D:\\learn\\script\\obstacle.v1i.coco-segmentation\\_annotations.coco.json'
    image_folder = 'D:\\learn\\script\\obstacle.v1i.coco-segmentation\\valid'
    output_folder = 'D:\\learn\\script\\obstacle.v1i.coco-segmentation\\mask'

    create_binary_mask(annotation_file, image_folder, output_folder)
