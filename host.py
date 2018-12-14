import base64
import cv2
import zmq
import pyautogui
import imutils
import numpy as np

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://192.168.2.3:5555')

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

while True:
    try:
        frame = image
        # grab the current frame
        frame = cv2.resize(frame, (640, 480))
        # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text)
        print ("Sending frame")

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break
