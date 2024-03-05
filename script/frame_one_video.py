import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=1):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 获取视频的帧率
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # 计算每隔多少帧抽取一帧
    frame_interval = int(fps / frame_rate)

    # 初始化帧计数器
    frame_count = 0

    while True:
        # 读取视频帧
        ret, frame = cap.read()

        # 如果视频帧读取失败，退出循环
        if not ret:
            break

        # 每隔一定帧数保存一帧图像
        if frame_count % frame_interval == 0:
            # 构造输出图像的文件名
            output_path = os.path.join(output_folder, f"frame_{frame_count // frame_interval}.png")

            # 保存图像
            cv2.imwrite(output_path, frame)
            print("+1")

        # 增加帧计数器
        frame_count += 1

    # 释放视频流
    cap.release()

if __name__ == "__main__":
    # 视频文件路径
    video_path = "G:/岔道1/IK014687上行-宁武北关沟大桥桥尾_20230401162526/IK014687上行-宁武北关沟大桥桥尾_20230331234501-20230401000001_1.mp4"

    # 输出文件夹路径
    output_folder = "G:/railway"

    # 抽帧的帧率，例如每秒1帧
    frame_rate = 1

    # 执行抽帧
    extract_frames(video_path, output_folder, frame_rate)
