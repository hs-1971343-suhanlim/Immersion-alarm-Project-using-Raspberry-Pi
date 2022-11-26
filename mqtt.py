# publisher/subscriber
import time
import paho.mqtt.client as mqtt
import mycamera # 카메라 사진 보내기
import circuit # 초음파 센서 입력 모듈 임포
flag = False
# LED 와 웹캠의 작동 신호를 받기 위한 토픽 등록
def on_connect(client, userdata, flag, rc):
        client.subscribe("facerecognition", qos = 0)
        client.subscribe("led", qos = 0)
def on_message(client, userdata, msg) :
        global flag
        command = msg.payload.decode("utf-8")
        if command == "action" :#카메라 촬영 시작
                print("action msg received..")
                flag = True
        elif command == "stop" :#카메라 촬영 종료
                print("action msg received..")
                flag = False
        elif command == "on":#LED 불 켜기
                print("LED on")
                circuit.controlLED(6,1)
        elif command == "off":#LED 전원 끄기
                print("LED off")
                circuit.controlLED(6,0)

broker_ip = "localhost" # 현재 이 컴퓨터를 브로커로 설정
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_ip, 1883)
client.loop_start()
while True :
        if flag==True :
                imageFileName = mycamera.takePicture() # 카메라 사진 촬영
                print(imageFileName)
                client.publish("image", imageFileName, qos=0)
                # flag 값이 True라면 동영상 처럼 계속 해서 사진 전송
        distance = circuit.measureDistance() #실시간 거리 측정 값
        client.publish("ultrasonic", distance, qos=0)# 거리 값 전송
        time.sleep(1)
client.loop_end()
client.disconnect()
