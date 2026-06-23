# Biceps_Curl_Counter
# Fatıh Cagan Ozkaptan / Deniz Can Corduk / Zehra Sadak

import cv2
import mediapipe as mp
import numpy as np

# MediaPipe settings
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Reps counter
counter = 0
stage = None


# Angle function
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(
        c[1] - b[1],
        c[0] - b[0]
    ) - np.arctan2(
        a[1] - b[1],
        a[0] - b[0]
    )

    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180:
        angle = 360 - angle

    return round(angle, 2)


# Camera Start
cap = cv2.VideoCapture(0)

with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            print("Kamera görüntüsü alınamadı!")
            break

        # BGR -> RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Pose detection
        results = pose.process(image)

        # RGB -> BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark

            # Left Shoulder
            shoulder = [
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
            ]

            # Left Elbow
            elbow = [
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
            ]

            # Left Wrist
            wrist = [
                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y
            ]

            # Calculate Angle
            angle = calculate_angle(
                shoulder,
                elbow,
                wrist
            )

            # Biceps Curl Mean
            if angle > 160:
                stage = "DOWN"

            if angle < 30 and stage == "DOWN":
                stage = "UP"
                counter += 1

            # Showing Elbow Angle
            cv2.putText(
                image,
                str(int(angle)),
                tuple(np.multiply(elbow, [640, 480]).astype(int)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2,
                cv2.LINE_AA
            )

        except:
            pass


        cv2.rectangle(image, (0, 0), (250, 80), (245, 117, 16), -1)

        # Reps
        cv2.putText(
            image,
            'REPS',
            (15, 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        cv2.putText(
            image,
            str(counter),
            (15, 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        # Movement Situation

        cv2.putText(
            image,
            'STAGE',
            (120, 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        cv2.putText(
            image,
            str(stage),
            (120, 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        # Landmarks
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(thickness=2, circle_radius=2)
            )

        cv2.imshow("Biceps Curl Counter", image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()