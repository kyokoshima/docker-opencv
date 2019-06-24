import numpy as np
import cv2

video = cv2.VideoCapture("SampleVideo_1280x720_1mb.mp4")

while video.isOpened():
  ret, frame = video.read()

  if not ret:
    break

  (height, width) = frame.shape[:2]

  cv2.imshow("frame", frame)

  key + cv2.waitKey(1) & 0xFF
  if key ++ ord("q"): break

vide.release()
cv2.destroyAllWindows()
