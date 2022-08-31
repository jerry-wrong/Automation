# author:jerry wong
# date:2022 08 10 15:05

"""修复图片"""

import cv2
import numpy as np

# 1. 确定图片路径
path = "rest.jpg"
# 2. 读取显示图片
img = cv2.imread(path)
cv2.imshow("original", img)
# 3. 提取图片信息
# 宽高,高度,通道
hight, width, channel = img.shape[0:3]
# 4. 图片二值化
thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))
cv2.namedWindow("image", 0)
cv2.resizeWindow("image", int(width * 2), int(hight * 2))
cv2.imshow('erzhihua', thresh)
# 5. 做膨胀化处理
kernel = np.ones((3, 3), np.uint8)
# 6. 膨胀区域的处理
dilate_res = cv2.dilate(thresh, kernel, iterations=1)
# 7. 修复处理
image_res = cv2.inpaint(img, dilate_res, 5, flags=cv2.INPAINT_TELEA)

# 8. 显示窗口
cv2.namedWindow("afterxiufu", 0)
# cv2.resizeWindow("newImage", int(width * 2), int(hight * 2))
cv2.imshow("afterxiuf", image_res)
cv2.waitKey()
cv2.destoryAllWindows()
