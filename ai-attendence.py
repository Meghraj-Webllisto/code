import cv2

stream = cv2.VideoCapture(0)

while True:
    ret, frame = stream.read()
    cv2.imshow("frame", frame)

st.release()
cv2.destroyAllWindows()
