import cv2
import os


class VideoProcessor:
    def __init__(self, videoPath, outputDir, frameInterval=150):
        self.videoPath = videoPath
        self.outputDir = outputDir
        self.frameInterval = frameInterval

    def process_video(self):
        video = cv2.VideoCapture(self.videoPath)
        frame_count = 0

        while True:
            ret, frame = video.read()
            if not ret:
                break
            if frame_count % self.frameInterval == 0:
                frame_path = os.path.join(self.outputDir, f"frame_{frame_count}.jpg")
                cv2.imwrite(frame_path, frame)
            frame_count += 1
        print("\033[94m" + f"Total frames extracted: {frame_count}" + "\033[0m")
        video.release()


if __name__ == "__main__":
    videoPath, outputDir, frameInterval = "vid.mp4", "./frames", 60
    processor = VideoProcessor(videoPath, outputDir, frameInterval)
    processor.process_video()
    print(
        "\033[92m" + "Frames extracted, and saved in ./frames successfully!" + "\033[0m"
    )
