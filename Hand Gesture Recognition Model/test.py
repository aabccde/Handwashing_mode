import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 이미지 경로
hand_model_path = "/mnt/data/A_simple_2D_digital_illustration_depicts_an_open_h.png"

# 이미지 로드
hand_img = cv2.imread(hand_model_path)
hand_img = cv2.cvtColor(hand_img, cv2.COLOR_BGR2RGB)

# 손 부위 시각화를 위한 더미 데이터 (예: palm, fingers, thumb 등)
# 예제이므로 대략적인 위치에 색상을 칠함
overlay = hand_img.copy()
height, width, _ = hand_img.shape

# 간단한 부위 마킹 (직사각형 영역 예시)
regions = {
    "palm": ((int(width * 0.35), int(height * 0.55)), (int(width * 0.65), int(height * 0.75))),
    "fingers": ((int(width * 0.4), int(height * 0.1)), (int(width * 0.6), int(height * 0.3))),
    "thumb": ((int(width * 0.15), int(height * 0.4)), (int(width * 0.3), int(height * 0.6))),
    "nail": ((int(width * 0.4), int(height * 0.05)), (int(width * 0.6), int(height * 0.1))),
    "back": ((int(width * 0.35), int(height * 0.35)), (int(width * 0.65), int(height * 0.5))),
    "between": ((int(width * 0.42), int(height * 0.3)), (int(width * 0.58), int(height * 0.4)))
}

# 색상 설정 (BGR -> RGB 변환됨)
colors = {
    "palm": (0, 255, 0),
    "fingers": (255, 255, 0),
    "thumb": (255, 0, 255),
    "nail": (0, 128, 255),
    "back": (255, 0, 0),
    "between": (0, 255, 255)
}

# 각 영역에 색상 칠하기
for region, ((x1, y1), (x2, y2)) in regions.items():
    cv2.rectangle(overlay, (x1, y1), (x2, y2), colors[region], -1)

# 반투명 시각화
alpha = 0.4
visualized_img = cv2.addWeighted(overlay, alpha, hand_img, 1 - alpha, 0)

# 시각화
plt.figure(figsize=(8, 8))
plt.imshow(visualized_img)
plt.title("WHO 6-Stage Hand Washing Regions")
plt.axis('off')
plt.show()

