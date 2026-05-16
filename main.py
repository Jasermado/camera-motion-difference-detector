import cv2

BLUR_INTENSITY = 5
THRESHOLD_VALUE = 25
CAMERA_INDEX = 1

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    print("Could not open camera")
    exit()

ret, previous_frame = cap.read()

if not ret:
    print("Could not read camera")
    cap.release()
    exit()

previous_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
previous_gray = cv2.GaussianBlur(
    previous_gray,
    (BLUR_INTENSITY, BLUR_INTENSITY),
    0
)

while True:
    ret, current_frame = cap.read()

    if not ret:
        break

    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    current_gray = cv2.GaussianBlur(
        current_gray,
        (BLUR_INTENSITY, BLUR_INTENSITY),
        0
    )

    diff = cv2.absdiff(current_gray, previous_gray)

    _, motion_mask = cv2.threshold(
        diff,
        THRESHOLD_VALUE,
        255,
        cv2.THRESH_BINARY
    )

    cv2.imshow("Motion Difference Detector", motion_mask)

    previous_gray = current_gray.copy()

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
