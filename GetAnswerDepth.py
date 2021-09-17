import argparse
import cv2
import os

parser = argparse.ArgumentParser()
parser.add_argument("AviFilePath", help="path_to_stereo_camera_avi",
                    default='/home/ubuntu/Sayama/data/StereoVideo/V2-mv-20200716103312-ulrg.avi', type=str)
parser.add_argument("video_name", help="path_to_output_CSV_and_JPG_Dir",
                    default='video1', type=str)
parser.add_argument("FrameDir", help="path_to_output_Frame_Dir",
                    default='/home/ubuntu/Sayama',type=str)
args = parser.parse_args()

AviFilePath = args.AviFilePath
video_name = args.video_name
FrameDir = args.FrameDir


def extractFrames(pathIn, pathOut, option):
    num = 0
    if not os.path.exists(pathOut):
        os.mkdir(pathOut)

    cap = cv2.VideoCapture(pathIn)
    count = 0

    while cap.isOpened():

        ret, frame = cap.read()

        if ret:
            num += 1
            # Convert to 30fps stereo video to 10fps
            if num % 3 == 0:
                init_height, init_width = frame.shape[:2]
                HEIGHT = init_height // 3
                WIDTH = init_width
                if option == "top":
                    frame = frame[0:HEIGHT, 0:WIDTH]
                if option == "middle":
                    frame = frame[HEIGHT:(HEIGHT * 2), 0:WIDTH]
                if option == "bottom":
                    frame = frame[(HEIGHT * 2):(HEIGHT * 3), 0:WIDTH]
                cv2.imwrite(os.path.join(pathOut, "frame_{:06d}.png".format(count)), frame)
                count += 1
            if num % 300 == 0:
                print(count)
        else:
            break
    cap.release()


def main(AviFilePath, video_name, FrameDir):

    # Prepare directory to save the extracted frames
    if not os.path.exists(FrameDir + "/" + video_name + "/"):
        os.makedirs(FrameDir + "/" + video_name + "/")
    if not os.path.exists(FrameDir + "/" + video_name + "top_png/"):
        os.makedirs(FrameDir + "/" + video_name + "top_png/")
    if not os.path.exists(FrameDir + "/" + video_name + "middle_png/"):
        os.makedirs(FrameDir + "/" + video_name + "middle_png/")
    if not os.path.exists(FrameDir + "/" + video_name + "bottom_png/"):
        os.makedirs(FrameDir + "/" + video_name + "bottom_png/")

    # Extract Frames
    extractFrames(AviFilePath,
                  FrameDir + "/" + video_name + "top_png/", "top")
    extractFrames(AviFilePath,
                  FrameDir + "/" + video_name + "middle_png/", "middle")
    extractFrames(AviFilePath,
                  FrameDir + "/" + video_name + "bottom_png/", "bottom")


main(AviFilePath, video_name, FrameDir)
