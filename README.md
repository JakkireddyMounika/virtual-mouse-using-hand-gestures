# Virtual Mouse Using Hand Gestures 🖐️🖱️

A computer vision–based system that allows users to control mouse operations using hand gestures captured via a webcam. This project eliminates the need for physical mouse devices.

---

## ✨ Features

- Move cursor using hand movements  
- Left & right click using gestures  
- Drag and drop functionality  
- Scroll up and down  
- Take screenshots  
- Real-time gesture recognition  

---

## 🛠️ Tech Stack

- **Language:** Python 3.7+  
- **Libraries:** OpenCV, MediaPipe, NumPy, PyAutoGUI  
- **Hardware:** Webcam  

---

## ⚙️ How It Works

1. Captures real-time video from webcam  
2. Detects hand landmarks using MediaPipe  
3. Maps hand gestures to mouse actions  
4. Executes mouse operations using PyAutoGUI  

---

## ▶️ How to Run

```bash
pip install opencv-python mediapipe pyautogui numpy
python virtual_mouse.py
