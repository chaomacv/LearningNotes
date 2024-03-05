import os
import shutil

def remove_duplicate_files(folder1, folder2):
    # 获取两个文件夹中的文件列表
    files_folder1 = set(os.listdir(folder1))
    files_folder2 = set(os.listdir(folder2))

    # 找到两个文件夹中相同的文件名
    duplicate_files = files_folder1.intersection(files_folder2)

    # 从第一个文件夹中删除相同的文件
    for file_name in duplicate_files:
        file_path_folder1 = os.path.join(folder1, file_name)
        os.remove(file_path_folder1)
        print(f"文件 '{file_name}' 从文件夹 '{folder1}' 中成功删除")

# 指定文件夹路径
#source_folder_path = 'D:\\learn\\script\\obstacle.v1i.coco-segmentation\\trimap'
source_folder_path = 'D:\\learn\\script\\obstacle.v1i.coco-segmentation\\original'
target_folder_path = 'D:\\learn\\script\\obstacle.v1i.coco-segmentation\\alpha'

# 调用函数删除相同文件名的文件
remove_duplicate_files(source_folder_path, target_folder_path)
