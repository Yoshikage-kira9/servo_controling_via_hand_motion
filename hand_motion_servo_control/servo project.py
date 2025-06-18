import cv2
import mediapipe as mp
import time
import serial

arduino = serial.Serial('COM3', 9600)  # Adjust COM port as necessary

capture = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_drawing = mp.solutions.drawing_utils

pTime =0
cTime = 0

while True:
    success, img = capture.read()
    color_rgb  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(color_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, handLms , mp_hands.HAND_CONNECTIONS)

            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 8:
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                    angle = int(cx / w * 180)  # Example angle calculation based on x position
                    print(f"Sending angle: {angle}")
                    arduino.write(f"{angle}\n".encode())



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
