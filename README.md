ELBOW EXERCISE TRACKER
Real-Time Exercise Monitoring and Repetition Counting Using Computer Vision
Project Documentation & README
Authors
Deniz Can Çördük
Fatih Çağan Özkaptan
Zehra Sadak
Hochschule Emden/Leer
Table of Contents
1.
Project Overview
2.
Motivation and Objectives
3.
System Features
4.
Technologies Used
5.
System Architecture
6.
Angle Calculation Logic
7.
Installation Guide
8.
Usage Instructions
9.
Testing and Performance
10.
Limitations
11.
Future Improvements
12.
Authors
1. Project Overview
The Elbow Exercise Tracker is a computer vision application developed to analyze elbow-based movements in real time. The system utilizes a webcam to detect human body landmarks and calculate the elbow joint angle continuously. By monitoring the movement of the arm, the application can determine whether an exercise repetition has been completed successfully and increment the repetition counter automatically. The project demonstrates how modern computer vision technologies can be applied to sports and fitness scenarios. Instead of relying on wearable sensors or specialized hardware, the application only requires a standard laptop camera, making it accessible and easy to use.
2. Motivation and Objectives
Fitness applications increasingly rely on automated movement analysis. However, many existing systems require expensive hardware or dedicated sensors. The goal of this project was to create a lightweight and affordable alternative. The primary objectives were: • Detect arm movements in real time. • Calculate elbow angles accurately. • Count exercise repetitions automatically. • Provide immediate visual feedback. • Operate efficiently on standard laptop hardware.
3. System Features
The developed system includes several core features: • Real-time pose detection using a webcam. • Continuous elbow angle monitoring. • Automatic repetition counting. • Visual display of angle values. • Lightweight processing pipeline. • Easy installation and execution. These features make the application suitable for educational demonstrations and simple exercise tracking scenarios.
4. Technologies Used
The application was developed using Python because of its extensive ecosystem for computer vision and numerical computing. Main technologies: • Python • MediaPipe Pose • OpenCV • NumPy MediaPipe Pose is responsible for landmark detection, OpenCV handles image acquisition and visualization, while NumPy performs the mathematical calculations required for angle computation.
5. System Architecture
The architecture follows a simple processing pipeline. First, the webcam captures a video frame. The frame is then processed by MediaPipe Pose to identify body landmarks. The coordinates of the shoulder, elbow, and wrist are extracted and used to calculate the elbow angle. The calculated angle is evaluated continuously. When predefined movement conditions are satisfied, the repetition counter is updated. The resulting information is displayed on the screen in real time.
6. Angle Calculation Logic
The core functionality of the project relies on geometric angle calculations. Using the coordinates of the shoulder, elbow, and wrist, two vectors are constructed. Mathematical trigonometric operations are applied to determine the angle between these vectors. This approach enables precise measurement of elbow flexion and extension throughout the exercise. The calculated angle is updated for every processed frame, allowing smooth and responsive movement tracking.
7. Installation Guide
Requirements: • Python 3.x • OpenCV • MediaPipe • NumPy
After installing Python, the required libraries can be installed using pip. Once the dependencies are available, the application can be started by running the main Python file.
8. Usage Instructions
1. Launch the application. 2. Position yourself in front of the camera. 3. Ensure the arm remains visible during the exercise. 4. Begin the movement. 5. Observe the displayed angle and repetition counter. For optimal performance, sufficient lighting and a stable camera position are recommended.
9. Testing and Performance
The application was tested under various conditions to evaluate reliability and usability. The system successfully detected complete repetitions and ignored incomplete movements. Real-time performance was achieved on standard laptop hardware without noticeable delays. The simplified focus on elbow-based movements contributes to the overall responsiveness of the application.
10. Limitations
Several limitations remain. Performance may decrease under poor lighting conditions, extreme viewing angles, or situations where the elbow is partially hidden from the camera. Rapid movements can also reduce landmark detection quality. Additionally, the current version focuses exclusively on elbow-based exercises and does not analyze other joints.
11. Future Improvements
Future development could extend the system in multiple directions. Potential enhancements include: • Support for additional exercises. • Multi-joint movement analysis. • Personalized exercise feedback. • Workout history and statistics. • Mobile and web deployment. • Improved robustness against occlusions and lighting variations. These improvements would significantly increase the practical usefulness of the application.
12. Authors
Deniz Can Çördük
Fatih Çağan Özkaptan
Zehra Sadak
