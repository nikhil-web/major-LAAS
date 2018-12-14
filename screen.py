import numpy as np 
import cv2 
# for windows, mac users
from PIL import ImageGrab
# for linux users
#import pyscreenshot as ImageGrab

import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error.msg:
    print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit();
 
print ('Socket Created')

host = '172.16.85.170'
port = 8000
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
     
print ('Ip address of ' + host + ' is ' + remote_ip)

#Connect to remote server
s.connect((remote_ip , port))
 
print ('Socket Connected to ' + host + ' on ip ' + remote_ip)
#Send some data to remote server



def sendframe(frame):
    try :
        #Set the whole string
        frame.encode()
        s.sendall(frame)
    except socket.error:
        #Send failed
        print ('Send failed')
        sys.exit()

 
print ('Message send successfully')


# four character code object for video writer
fourcc = cv2.VideoWriter_fourcc(*'H264')


# video writer object
out = cv2.VideoWriter("output.mp4", fourcc, 60.0, (1366,768))

while True:
	# capture computer screen
	img = ImageGrab.grab()
	# convert image to numpy array
	img_np = np.array(img)
	# convert color space from BGR to RGB
	frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
	# show image on OpenCV frame
	sendframe(frame)
	# write frame to video writer
	out.write(frame)
  
	if cv2.waitKey(1) == 27:
		break

out.release()
cv2.destroyAllWindows()

