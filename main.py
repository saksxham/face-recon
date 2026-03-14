import cv2

# This project performs **live webcam smile detection** using OpenCV Haar cascades.
# It does not require any external ML models and works purely with OpenCV's built-in
# face + smile detectors.


def main():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    smile_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_smile.xml"
    )

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open webcam")
        return

    print("Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))

        for (x, y, w, h) in faces:
            face_roi_gray = gray[y : y + h, x : x + w]
            smiles = smile_cascade.detectMultiScale(
                face_roi_gray,
                scaleFactor=1.7,
                minNeighbors=20,
                minSize=(25, 25),
            )

            label = "Smiling" if len(smiles) > 0 else "Not smiling"
            color = (0, 255, 0) if len(smiles) > 0 else (0, 0, 255)

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(
                frame,
                label,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                color,
                2,
            )

        cv2.imshow("Live Expression (Smile) Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
