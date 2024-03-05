import os

def rename_and_sort_png(input_folder):
    # 获取文件夹中所有的.png文件
    png_files = [file for file in os.listdir(input_folder) if file.lower().endswith('.png')]

    # 按照文件大小排序
    sorted_png_files = sorted(png_files, key=lambda file: os.path.getsize(os.path.join(input_folder, file)))

    # 重命名并保存
    for index, file_name in enumerate(sorted_png_files):
        old_file_path = os.path.join(input_folder, file_name)
        new_file_name = f"{index + 1}.png"
        new_file_path = os.path.join(input_folder, new_file_name)

        # 重命名文件
        os.rename(old_file_path, new_file_path)
        #print(f"文件 {file_name} 已重命名为 {new_file_name}")

if __name__ == "__main__":
    # 替换以下路径为你的实际路径
    input_folder = 'D:\\learn\\script\\obstacle.v1i.coco-segmentation\\alpha'

    rename_and_sort_png(input_folder)
