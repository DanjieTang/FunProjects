import cv2
import mediapipe as mp

pos_tracking = mp.solutions.pose # Position tracking model
video = cv2.VideoCapture(0)

with pos_tracking.Pose() as pose:
    while video.isOpened():
        # Read from camera
        success, image = video.read()

        if not success:
            print("Error: Cannot read from video source.") 
            break 
        
        # Convert image from BGR (OpenCV default) to RGB (MediaPipe needs RGB)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image with MediaPipe
        results = pose.process(image)
        
        # Current implementation only trackes 1 person.
        if results.pose_landmarks:
            # Access nose position in the returned results
            nose = results.pose_landmarks.landmark[pos_tracking.PoseLandmark.NOSE] # Look into source code for other positions to track
            
            # Calculate coordinates
            x = int(nose.x * image.shape[1])  
            y = int(nose.y * image.shape[0])
            
            print(x)
            print(y)
        
        k=cv2.waitKey(1000) # Wait for 1 second (1000ms) before continuing.
        
        # If user pressed on q then exit program.
        if k == ord('q'):
            break
        
video.release()
cv2.destroyAllWindows()
