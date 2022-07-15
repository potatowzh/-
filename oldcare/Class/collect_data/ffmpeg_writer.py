"""
python ffmpeg_rtmp.py
"""
from os import write
import subprocess as sp
import cv2


class ffmpeg_writer:
    def __init__(self, rtmpUrl, fps, width, height):
        # ffmpeg command
        command = ['ffmpeg',
                   '-y',
                   '-f', 'rawvideo',
                   '-vcodec', 'rawvideo',
                   '-pix_fmt', 'bgr24',
                   '-s', "{}x{}".format(width, height),
                   '-r', str(fps),
                   '-i', '-',
                   '-c:v', 'libx264',
                   '-pix_fmt', 'yuv420p',
                   # '-preset', 'ultrafast',
                   '-f', 'flv',
                   '-flvflags', 'no_duration_filesize',
                   rtmpUrl]
        self.pipe = sp.Popen(command, stdin=sp.PIPE)

    def write(self, frame):
        self.pipe.stdin.write(frame.tostring())

    def release(self):
        self.pipe.terminate()


    def process(cap):
        rtmpUrl = "rtmp://106.14.78.63:1935/rtmplive/123"
        # camera_path = "output.mp4"
        # cap = cv2.VideoCapture(camera_path)

        # Get video information
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 管道配置
        writer = ffmpeg_writer(rtmpUrl, fps, width, height)

        # read webcamera
        while (cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                print("Opening camera is failed")
                break

            writer.write(frame)

    def run(self):
        self.process()

