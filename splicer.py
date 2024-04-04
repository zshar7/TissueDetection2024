from cv2 import VideoCapture, imwrite

name=input('Name:')

capture = VideoCapture('path/to/file'+name+'.mp4')
    
frameNr = 0
    
while (True):
    
    success, frame = capture.read()
    
    if success:
        imwrite(f'path/to/file/frametest/frame_{frameNr}.jpg', frame)
    
    else:
        break
    
    
capture.release()

