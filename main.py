import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PyQt5.QtMultimedia import QCamera, QCameraInfo, QCameraImageCapture
from PyQt5.QtMultimediaWidgets import QCameraViewfinder

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webcam Camera")
        self.setGeometry(100, 100, 640, 480)
        self.camera = QCamera(QCameraInfo.defaultCamera())
        self.viewfinder = QCameraViewfinder()
        self.camera.setViewfinder(self.viewfinder)
        self.image_capture = QCameraImageCapture(self.camera)
        self.image_capture.imageCaptured.connect(self.save_image)
        layout = QVBoxLayout()
        layout.addWidget(self.viewfinder)

        self.capture_button = QPushButton("Capture")
        self.capture_button.clicked.connect(self.capture_image)
        layout.addWidget(self.capture_button)

        self.camera_combo = QComboBox()
        self.camera_combo.addItem("Off")
        self.camera_combo.addItem("On")
        self.camera_combo.currentIndexChanged.connect(self.toggle_camera)
        layout.addWidget(self.camera_combo)
        
        self.setLayout(layout)

    def capture_image(self):
        self.image_capture.capture()

    def save_image(self, id, preview):
        file_path = "photo.jpg"
        if preview.save(file_path, "JPG"):
            QMessageBox.information(self, "Success", f"Photo saved as {file_path}")
        else:
            QMessageBox.warning(self, "Error", "Failed to save photo")

    def toggle_camera(self, index):
        if index == 0:  
            self.camera.stop()
        elif index == 1:
            self.camera.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec_())
