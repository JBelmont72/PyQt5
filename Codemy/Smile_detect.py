import cv2      ## detects faces but not smiles
# Smile detection using OpenCV and PyQt5    

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
import time

class FacialRecognitionSystem:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        self.face_cascade = cv2.CascadeClassifier(
            '/Users/judsonbelmont/Documents/SharedFolders/Pico/PyQt5/haar/haarcascade_frontalface_default.xml'
        )
        self.face_rect = None
        self.running = True

    def run(self):
        app = QApplication(sys.argv)
        window = QWidget()
        layout = QVBoxLayout()

        # Just a placeholder label (OpenCV handles the video window)
        self.camera_view = QLabel("Camera view is in OpenCV window")
        layout.addWidget(self.camera_view)

        self.smile_label = QLabel("Smile Detected: No")
        self.smile_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.smile_label)

        window.setLayout(layout)
        window.setWindowTitle("Face Detection with Smile Detection")
        window.show()

        while self.running:
            ret, frame = self.cap.read()

            # Debug 1: Confirm frame is being read
            print(f"[DEBUG] Frame read successful: {ret}, Frame shape: {frame.shape if ret else 'None'}")

            if not ret:
                print("[ERROR] Failed to grab frame")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)

            # Debug 2: Print number of faces detected
            print(f"[DEBUG] Faces detected: {len(faces)}")

            for (x, y, w, h) in faces:
                # Debug 3: Print dimensions of each face
                print(f"[DEBUG] Face bounds: x={x}, y={y}, w={w}, h={h}")
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Debug 4: Smile detection heuristic
                if w > h:
                    print("[DEBUG] Smile detected (w > h condition)")
                    self.smile_label.setText("Smile Detected: Yes")
                    self.smile_label.setStyleSheet("color: green;")
                else:
                    print("[DEBUG] No smile detected (w <= h condition)")
                    self.smile_label.setText("Smile Detected: No")
                    self.smile_label.setStyleSheet("color: red;")

            cv2.imshow('Face Detection', frame)
            time.sleep(0.1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    system = FacialRecognitionSystem()
    system.run()
