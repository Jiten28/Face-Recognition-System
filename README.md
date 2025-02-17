# **Facial Recognition Attendance System**
AEHN
### **Overview**
This project implements a Facial Recognition Attendance System, leveraging Python and computer vision libraries to ensure efficient attendance tracking and management. Integrated with Firebase, the system enables real-time data management, making it reliable and scalable for institutional or organizational use.

### **Key Features**
- **Facial Recognition**: Accurately identifies and recognizes faces in real-time.
- **Attendance Tracking**: Automates attendance marking for efficiency and accuracy.
- **Firebase Integration**: Stores and retrieves attendance data in real-time, ensuring seamless data management.
- **Real-time Feedback**: Displays live recognition feedback, including recognized names and timestamps.
- **Cross-platform Compatibility**: Compatible with Windows and other operating systems.

### **Challenges**
- **Module Installation on Windows**: Installation of `dlib` and `face-recognition` can be challenging on Windows systems.
- **Recognition Accuracy**: Ensuring high accuracy in diverse lighting conditions and varying facial features.
- **Real-time Performance**: Balancing recognition accuracy with processing speed for smooth real-time operation.

### **Future Enhancements**
- **Multi-face Recognition**: Enhance the system to recognize and manage multiple faces simultaneously.
- **Cloud Backup**: Add automated backups of attendance data to secure cloud storage.
- **Emotion Recognition**: Integrate emotion detection for additional use cases, like mood analysis during attendance.
- **Smart Alerts**: Notify users of anomalies, such as unrecognized faces or frequent absenteeism.

### **Python Version**
- Python 3.11.9 or higher.

### **Steps to Start the Project**
1. **Install Python**: Ensure Python version 3.11.9 or higher is installed.
2. **Install Required Libraries**: Use the installation commands provided below to set up the necessary Python modules.
3. **Setup Firebase**: Configure Firebase for real-time attendance data management.
4. **Run the Program**: Execute the Python script to start the facial recognition system.
5. **Interact with the System**: The program will recognize faces and update attendance records in Firebase in real-time.
6. **Exit the Program**: Stop the system after completing attendance management.

### **Libraries and Installation Commands**

1. **OpenCV (cv2)**
   - **Install Command**:  
     ```bash
     pip install opencv-python
     ```
   - **Use**: For image and video processing.

2. **cvzone**
   - **Install Command**:  
     ```bash
     pip install cvzone
     ```
   - **Use**: Provides computer vision utilities to simplify development.

3. **Mediapipe**
   - **Install Command**:  
     ```bash
     pip install mediapipe
     ```
   - **Use**: Facilitates facial landmark detection and tracking.

4. **Face Recognition**
   - **Install Command**:  
     ```bash
     pip install face-recognition
     ```
   - **Use**: Enables facial recognition and comparison.
   - **Note**: For Windows users, follow the detailed installation guide:
     [GeeksforGeeks Face Recognition Installation Guide](https://www.geeksforgeeks.org/how-to-install-face-recognition-in-python-on-windows/)

5. **CMake**
   - **Install Command**:  
     ```bash
     pip install cmake
     ```
   - **Use**: Required for compiling the `dlib` library.

6. **dlib**
   - **Install Command**:  
     ```bash
     pip install dlib
     ```
   - **Use**: Provides tools for facial feature extraction and recognition.
   - **Troubleshooting**: If issues arise during installation, refer to the repository:
     [Dlib Installation Guide](https://github.com/Cfuhfsgh/Dlib-library-Installation)
