import numpy as np
import cv2

video = cv2.VideoCapture("SampleVideo_1280x720_1mb.mp4")
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
# fourcc = cv2.VideoWriter_fourcc(*'H263')
# fourcc = int(video.get(cv2.CAP_PROP_FOURCC))
fourcc = 0x00000021

writer = cv2.VideoWriter("Sample.mp4", fourcc, fps, (width, height))

while True:
  ret, frame = video.read()

  if not ret:
    break

  (height, width) = frame.shape[:2]

  print('frames: {}, fourcc: {}', num_frames, fourcc)

  # cv2.imshow("frame", frame)
  writer.write(frame)

  # key = cv2.waitKey(1) & 0xFF
  # if key ++ ord("q"): break

video.release()
cv2.destroyAllWindows()
