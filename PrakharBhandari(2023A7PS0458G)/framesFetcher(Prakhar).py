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

        videoName = self.videoPath.split("/")[-1].split(".")[0]
        while True:
            ret, frame = video.read()
            if not ret:
                break
            if frame_count % self.frameInterval == 0:
                fileName = f"{videoName}_frame_{frame_count}.jpg"
                frame_path = os.path.join(self.outputDir, fileName)
                cv2.imwrite(frame_path, frame)
            frame_count += 1
        print("\033[94m" + f"Total frames extracted: {frame_count}" + "\033[0m")
        video.release()


if __name__ == "__main__":
    outputDir, frameInterval = "./frames", 39
    # select all the files which end with .mp4
    videos = [f for f in os.listdir() if f.endswith(".mp4")]
    if not videos:
        print("\033[91m" + "No video files found in the current directory!" + "\033[0m")
        exit()
    for i, videoPath in enumerate(videos):
        print(f"{i+1}. {videoPath}")
        processor = VideoProcessor(videoPath, outputDir, frameInterval)
        processor.process_video()
        print(
            "\033[92m"
            + "Frames extracted, and saved in ./frames successfully!"
            + "\033[0m"
        )
    # print the number of files in frames directory
    print(
        "\n\033[93m"
        + f"Total frames extracted: {len(os.listdir(outputDir))}"
        + "\033[0m"
    )
