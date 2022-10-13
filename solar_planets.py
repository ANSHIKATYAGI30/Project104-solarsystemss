import cv2
import numpy as np

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "Sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Mercury",
    (40,300),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Venus",
    (60,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Earth",
    (80,300),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Mars",
    (100,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Jupiter",
    (120,300),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Saturn",
    (140,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Uranus",
    (160,300),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Neptune",
    (180,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.imshow("Output", img)
print(img)
cv2.waitKey(0)

