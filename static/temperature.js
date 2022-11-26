function visible(temp, humi){         //온습도를 출력하고 이미지를 보이는 코드
        // 기온 출력
        var div = document.getElementById("info");
        div.innerHTML = "현재 기온은 <strong>"+Math.round(temp)+"</strong>도, "
        div.innerHTML += "습도는 <strong>"+Math.round(humi)+"%</strong>입니다."
        div.innerHTML += "<br>"

}