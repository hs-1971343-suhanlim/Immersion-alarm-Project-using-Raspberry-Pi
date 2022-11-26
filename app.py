from flask import Flask, render_template, request
import temperature
app = Flask(__name__)

@app.route('/')
def index():
        temp = temperature.getTemperature()	#접속하는 순간의 온도 측정
        humi = temperature.getHumidity()	#접속하는 순간의 습도 측정
        print("test %d %d" %(temp, humi))	#개발자가 확인 하도록 출력
        return render_template('image.html', temp=temp, humi=humi)

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080)
