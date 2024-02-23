import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils  # For visualizing landmarks
mp_pose = mp.solutions.pose

# Initialize video capture (use 0 for default webcam)
cap = cv2.VideoCapture(0)

# Configure MediaPipe Pose 
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:

    while cap.isOpened():
        success, image = cap.read()

        if not success:
            print("Error: Cannot read from video source.") 
            break 

        # Convert image from BGR (OpenCV default) to RGB (MediaPipe needs RGB)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image with MediaPipe
        results = pose.process(image)

        # Extract landmarks (if a person is detected)
        if results.pose_landmarks:
            # Choose a landmark of interest to track 
            # (e.g., right shoulder, index fingertip, etc.)
            landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]

            # Calculate coordinates
            x = int(landmark.x * image.shape[1])  
            y = int(landmark.y * image.shape[0])  

            # Do something with the coordinates (x, y) - this is your position data
            print("Position: ", (x, y))  

            # Visualize on the image 
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Convert image back to BGR for display
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Show the output
        cv2.imshow('MediaPipe Pose Tracking', image)

        # Exit on pressing 'q'
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()