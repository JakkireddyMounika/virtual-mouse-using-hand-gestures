import cv2

import mediapipe as mp

import pyautogui

import time

import numpy as np



cap = cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands(max_num_hands=1)

drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

prev_click_time = 0

dragging = False



def get_distance(p1, p2):

    return np.linalg.norm(np.array(p1) - np.array(p2))



def fingers_up(landmarks):

    finger_tips = [8, 12, 16, 20]

    fingers = []

    for tip in finger_tips:

        if landmarks[tip].y < landmarks[tip - 2].y:

            fingers.append(1)

        else:

            fingers.append(0)

    return fingers



while True:

    ret, frame = cap.read()

    if not ret:

        print("Failed to capture video")

        break



    frame = cv2.flip(frame, 1)

    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = hand_detector.process(rgb_frame)

    hands = output.multi_hand_landmarks



    if hands:

        for hand in hands:

            drawing_utils.draw_landmarks(frame, hand)

            landmarks = hand.landmark



            index_finger = landmarks[8]

            thumb_tip = landmarks[4]

            middle_finger = landmarks[12]



            index_x = int(index_finger.x * frame_width)

            index_y = int(index_finger.y * frame_height)

            screen_x = int(index_finger.x * screen_width)

            screen_y = int(index_finger.y * screen_height)



            # Move cursor

            pyautogui.moveTo(screen_x, screen_y, duration=0.1)



            # Click Gesture

            click_distance = get_distance(

                [index_finger.x, index_finger.y], [thumb_tip.x, thumb_tip.y])

            if click_distance < 0.03:

                if time.time() - prev_click_time > 1:

                    pyautogui.click()

                    prev_click_time = time.time()



            # Drag Gesture

            if click_distance < 0.03:

                if not dragging:

                    pyautogui.mouseDown()

                    dragging = True

            else:

                if dragging:

                    pyautogui.mouseUp()

                    dragging = False



            # Scroll Gesture (Index and Middle fingers up)

            fingers = fingers_up(landmarks)

            if fingers[0] == 1 and fingers[1] == 1 and sum(fingers) == 2:

                if middle_finger.y < index_finger.y:

                    pyautogui.scroll(20)

                else:

                    pyautogui.scroll(-20)



            # Screenshot Gesture (All fingers up)

            if sum(fingers_up(landmarks)) == 4:

                if time.time() - prev_click_time > 2:

                    pyautogui.screenshot("screenshot.png")

                    print("Screenshot Taken")

                    prev_click_time = time.time()



            # Draw circles on key points

            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)

            cv2.circle(frame, (int(thumb_tip.x * frame_width), int(thumb_tip.y * frame_height)), 10, (255, 0, 0), -1)



    cv2.imshow('Virtual Mouse', frame)



    if cv2.waitKey(1) == 27:  # ESC key

        break



cap.release()

cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import pyautogui
import time
import numpy as np

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
prev_click_time = 0
dragging = False

def get_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def fingers_up(landmarks):
    finger_tips = [8, 12, 16, 20]
    fingers = []
    for tip in finger_tips:
        if landmarks[tip].y < landmarks[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video")
        break

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            index_finger = landmarks[8]
            thumb_tip = landmarks[4]
            middle_finger = landmarks[12]

            index_x = int(index_finger.x * frame_width)
            index_y = int(index_finger.y * frame_height)
            screen_x = int(index_finger.x * screen_width)
            screen_y = int(index_finger.y * screen_height)

            # Move cursor
            pyautogui.moveTo(screen_x, screen_y, duration=0.1)

            # Click Gesture
            click_distance = get_distance(
                [index_finger.x, index_finger.y], [thumb_tip.x, thumb_tip.y])
            if click_distance < 0.03:
                if time.time() - prev_click_time > 1:
                    pyautogui.click()
                    prev_click_time = time.time()

            # Drag Gesture
            if click_distance < 0.03:
                if not dragging:
                    pyautogui.mouseDown()
                    dragging = True
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging = False

            # Scroll Gesture (Index and Middle fingers up)
            fingers = fingers_up(landmarks)
            if fingers[0] == 1 and fingers[1] == 1 and sum(fingers) == 2:
                if middle_finger.y < index_finger.y:
                    pyautogui.scroll(20)
                else:
                    pyautogui.scroll(-20)

            # Screenshot Gesture (All fingers up)
            if sum(fingers_up(landmarks)) == 4:
                if time.time() - prev_click_time > 2:
                    pyautogui.screenshot("screenshot.png")
                    print("Screenshot Taken")
                    prev_click_time = time.time()

            # Draw circles on key points
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)
            cv2.circle(frame, (int(thumb_tip.x * frame_width), int(thumb_tip.y * frame_height)), 10, (255, 0, 0), -1)

    cv2.imshow('Virtual Mouse', frame)

    if cv2.waitKey(1) == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()