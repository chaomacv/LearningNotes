import os
import shutil

def remove_nonexistent_files(source_folder, target_folder):
    # 获取源文件夹和目标文件夹中的文件列表
    source_files = set(os.listdir(source_folder))
    target_files = set(os.listdir(target_folder))

    # 找到源文件夹中不存在于目标文件夹的文件
    non_existent_files = source_files - target_files

    # 从源文件夹中删除不存在于目标文件夹的文件
    for file_name in non_existent_files:
        file_path_source = os.path.join(source_folder, file_name)
        os.remove(file_path_source)
        print(f"文件 '{file_name}' 从文件夹 '{source_folder}' 中成功删除")

# 指定文件夹路径
#source_folder_path = 'D:\\learn\\script\\obstacle.v1i.coco-segmentation\\trimap'
#source_folder_path = 'D:\\learn\\script\\obstacle.v1i.coco-segmentation\\mask'
#target_folder_path = 'D:\\learn\\script\\obstacle.v1i.coco-segmentation\\alpha'
source_folder_path = 'D:\learn\script\新建文件夹\\alpha'
target_folder_path = 'D:\learn\script\新建文件夹\original'

# 调用函数删除不存在于目标文件夹的文件
remove_nonexistent_files(source_folder_path, target_folder_path)
