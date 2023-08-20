# Face-Reconization-Attendace-System
This is a project for creating a face recognition-based attendance system. The system utilizes computer vision and machine learning techniques to recognize faces and mark attendance.
Face recognition attendance system used back-end python, oracle
## Features

- Face detection and recognition using OpenCV, Dlib, and FaceNet
- Attendance tracking and recording using Oracle 11g database
- GUI interface using Tkinter
- Real-time video capture using webcam
- Email notification for absentees
- Faculty wise Attendance reports
## Getting Started

### Prerequisites
- Python 3.7 or higher
- OpenCV 4.5.3 or higher
- Dlib 19.22.0 or higher
- FaceNet 1.0.5 or higher
- SQLite 3.36.0 or higher
- Tkinter 8.6 or higher
- Smtplib 3.9.6 or higher

### Installation

1. Clone the repository: `git clone https://github.com/basavaraj1997/Face-Reconization-Attendace-System.git`
2. Navigate to the project directory: `cd Face-Reconization-Attendace-System`
3. Install the required packages: `pip install -r requirements.txt`

### Usage

1. Run the main.py file: `python main.py`
2. Enter your email and password for sending notifications (optional)
3. Click on the Train button to train the face recognition model on the images in the dataset folder
4. Click on the Recognize button to start the face recognition and attendance system
5. Click on the Quit button to exit the program

## Configuration

- You can add or remove images of students or employees in the ImageData folder
- You can change the email settings in the email.py file
- You can change the database settings in the database.py file
- You can change the face recognition settings in the face_recognition.py file

## Contributing

Contributions are welcome! Here's how you can get involved:
1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Create a pull request

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions, feel free to contact me:
- Name: Basavaraj Loni
- Email: basavarajloni1997@gmail.com
