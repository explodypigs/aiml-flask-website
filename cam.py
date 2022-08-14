import cv2

class VideoCamera(object):
    def __init__(self):
      self.video = cv2.VideoCapture(0)

    def __del__(self):
      self.video.release()

    def get_frame(self):
      ret, frame = self.video.read()

      faceCascade = cv2.CascadeClassifier('face_detector.xml')

      imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = faceCascade.detectMultiScale(imgGray, 1.1, 3)

      for (x, y, w, h) in faces:
          cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 1)
          cv2.rectangle(frame, (x, y+h+16), (x+62,y+h), (255, 255, 0), -1)
          cv2.putText(frame,'Human',(x,y+h+13),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0),2)

      ret, jpeg = cv2.imencode('.jpg', frame)
      return jpeg.tobytes()