import cv2
import os

def extract_frames(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4") or filename.endswith(".avi"):
            video_path = os.path.join(input_folder, filename)
            # print(video_path)
            output_subfolder = os.path.join(output_folder, os.path.splitext(filename)[0])
            # print(output_folder)

            # 确保子文件夹存在
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)

            # 打开视频文件
            cap = cv2.VideoCapture(video_path)
            #print(cap)

            # 获取视频的帧率和总帧数
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            # print(total_frames,fps)





            # 每分钟抽一帧fps * 60
            frame_interval = 20

            # 初始化帧计数器
            frame_count = 0
            count=0

            while True:
                # 读取视频帧
                ret, frame = cap.read()

                # 如果视频帧读取失败，退出循环
                if not ret:
                    break

                # 每隔一定帧数保存一帧图像
                if frame_count % frame_interval == 0:
                    # 构造输出图像的文件名
                    output_path = os.path.join(output_subfolder, f"frame_{frame_count // frame_interval}.png")
                    # 保存图像
                    cv2.imencode('.png', frame)[1].tofile(output_path)
                    count+=1


                # 增加帧计数器
                frame_count += 1

                # 如果到达视频末尾，退出循环
                if frame_count >= total_frames:
                    break

            # 释放视频流
            cap.release()

if __name__ == "__main__":
    # 输入文件夹路径，包含视频文件
    input_folder = "G:\\铁路障碍检测\\外发数据2\\xiangzi\\"

    # 输出文件夹路径，保存抽帧结果
    output_folder = "G:\\铁路障碍检测\\外发数据2\\xiangzi_frame\\"

    # 执行抽帧
    extract_frames(input_folder, output_folder)
