import os; import io; import time
import cv2
import numpy as np; from PIL import Image

fileName = ""
stream = io.BytesIO()
camera = cv2.VideoCapture(0, cv2.CAP_V4L) # 카메라 객체 생성
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
bufferSize = int(camera.get(cv2.CAP_PROP_BUFFERSIZE)) # 사진 데이터가 쌓일 버퍼 
print(bufferSize)
time.sleep(1)
# 수업 ppt 내용과 달리진 점은 없습니다.
def takePicture() :
        global fileName, stream, camera

        if len(fileName) != 0:
                os.remove(fileName)

        stream.seek(0)
        stream.truncate()
        
        for i in range(bufferSize+1): # 2개를 연달아 읽어서 옛날에 있던 사진은 버리고 현재 사진을 보낸다.
                ret, frame = camera.read()
        Image.fromarray(frame).save(stream, format='JPEG')
        stream.seek(0)

        data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data, 1)
        takeTime = time.time()
        fileName = "./static/%d.jpg" % (takeTime * 10)
        cv2.imwrite(fileName, image)
        return fileName

if __name__ == '__main__' :
        count = 0
        while(True):
                name = takePicture()
                print("fname= %s" % name)
                count += 1
                if(count == 5):
                      break
