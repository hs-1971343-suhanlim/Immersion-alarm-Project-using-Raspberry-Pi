import time
import RPi.GPIO as GPIO

trig = 20; echo = 16 # 초음파 센서를 대한 전역 변수 선언 및 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)

def measureDistance():
        global trig, echo
        time.sleep(0.5)
        GPIO.output(trig, True) # 신호 1 발생
        time.sleep(0.00001) # 짧은 시간을 나타내기 위함
        GPIO.output(trig, False) # 신호 0 발생

        while(GPIO.input(echo) == 0):
                pass
        pulse_start = time.time() # 신호 1을 받았던 시간
        while(GPIO.input(echo) == 1):
                pulse_end = time.time() # 신호 0을 받았던 시간

        pulse_duration = pulse_end - pulse_start
        return 340*100/2*pulse_duration

led = 6 # LED 점등을 위한 전역 변수 선언 및 초기화
GPIO.setup(led, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정.
# 1이면 LED on 0이면 LED off
def controlLED(led = 6, onOff =0 ): # led 번호의 핀에 onOff(0/1) 값 출력
        GPIO.output(led, onOff)

if __name__ == "__main__":
        led_status = 0
        while(True):
        	led_status = 0 if led_status == 1 else 1
        	controlLED(onOff = led_status)
        	distance = measureDistance()
        	print("distance=%f" % distance)
