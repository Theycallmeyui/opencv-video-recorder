import cv2 as cv

print("Program started")

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Cannot open camera")
    exit()

print("Camera opened successfully")
print("Controls:")
print("SPACE = Start/Stop Recording")
print("G = Toggle Black & White Filter")
print("ESC = Exit")

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fps = 20.0


fourcc = cv.VideoWriter_fourcc(*'XVID')


writer = cv.VideoWriter('output.avi', fourcc, fps, (width, height))

recording = False
gray_mode = False

while True:

   
    ret, frame = cap.read()

    if not ret:
        print("ERROR: Cannot receive frame")
        break

   
    if gray_mode:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

    
    if recording:
        cv.circle(frame, (30, 30), 10, (0, 0, 255), -1)
        cv.putText(frame, "REC", (50, 35),
                   cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        writer.write(frame)

    else:
        cv.putText(frame, "PREVIEW", (20, 35),
                   cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    
    if gray_mode:
        cv.putText(frame, "BLACK & WHITE", (20, 70),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

 
    cv.imshow("Video Recorder", frame)

  
    key = cv.waitKey(1) & 0xFF


    if key == 27:
        print("ESC pressed. Exiting...")
        break

    # SPACE to toggle recording
    elif key == ord(' '):
        recording = not recording

        if recording:
            print("Recording started")
        else:
            print("Recording stopped")

    
    elif key == ord('g'):
        gray_mode = not gray_mode

        if gray_mode:
            print("Black & White filter ON")
        else:
            print("Black & White filter OFF")


cap.release()
writer.release()
cv.destroyAllWindows()

print("Program ended")