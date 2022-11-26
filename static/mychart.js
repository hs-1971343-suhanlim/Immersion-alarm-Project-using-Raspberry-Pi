// Chart 객체에 넘겨줄 차트에 대한 정보들을 정의한 객체. 명품 html5의 7장 프로토타입 참고
var config = {
	// type은 차트 종류 지정
	type: 'line', /* line 등으로 바꿀 수 있음 */

	// data는 차트에 출력될 전체 데이터 표현
	data: {
		// labels는 배열로 데이터의 레이블들
		labels: [],

		// datasets 배열로 이 차트에 그려질 모든 데이터 셋 표현. 아래는 그래프 1개만 있는 경우
		datasets: [{
			label: '실시간 물 높이',
			backgroundColor: 'yellow',
			borderColor: 'blue',
			borderWidth: 2,
			data: [], /* 각 레이블에 해당하는 데이터 */
			fill : false, /* 그래프 아래가 채워진 상태로 그려집니다. 해보세요 */
		}]
	},
	//  차트의 속성 지정
	options: {
		responsive : false, // 크기 조절 금지
		scales: { /* x축과 y축 정보 */
			xAxes: [{
				display: true,
				scaleLabel: { display: true, labelString: '시간' },
			}],
			yAxes: [{
				ticks: {
					min: 0
				},
				display: true,
				scaleLabel: { display: true, labelString: '거리(cm)' }
			}]
		}
	}
};
var ctx = null
var chart = null
var LABEL_SIZE = 20; // 차트에 그려지는 데이터의 개수 
var tick = 0; // 도착한 데이터의 개수임, tick의 범위는 0에서 99까지만 
var cutline = 70; // 장치가 설치된 높이의 값 현재 70cm 위에 설치됨
function drawChart() {
	ctx = document.getElementById('canvas').getContext('2d');
	chart = new Chart(ctx, config);
	init();
} // end of drawChart()


// chart의 차트에 labels의 크기를 LABEL_SIZE로 만들고 0~19까지 레이블 붙이기
function init() {
	for(let i=0; i<LABEL_SIZE; i++) {
		chart.data.labels[i] = i;
	}
	chart.update();
}
// 바탕화면색을 빨간색으로 바꾸는 함수
function changeWallning(){
	document.body.style.backgroundColor = "red";
}
// 바탕화면색을 원래대로 돌리는 함수
function changeNormal(){
	document.body.style.backgroundColor = "white";
}
function addChartData(value) {
	// 물의 높이 = 장치가 설치된 높이 - 측정된 거리
	// -(value-cutline) = (cutline-value)
	if(-(value-cutline)>50){ // 수위50cm 초과
		changeWallning() // 바탕색 빨간색으로 바꾸기
		publish('led', "on") // LED 불켜기
	}
	else{
		changeNormal() // 수위 50cm 미만 원래 색으로 변경
		publish('led', "off") // LED 불끄기
	}
	tick++; // 도착한 데이터의 개수 증가
	tick %= 100; // tick의 범위는 0에서 99까지만. 100보다 크면 다시 0부터 시작
	let n = chart.data.datasets[0].data.length; // 현재 데이터의 개수 
	if(n < LABEL_SIZE) 
		chart.data.datasets[0].data.push(-(value-cutline));
	else {
		// 새 데이터 value 삽입
		chart.data.datasets[0].data.push(-(value-cutline));
		chart.data.datasets[0].data.shift();

		// 레이블 삽입
		chart.data.labels.push(tick);
		chart.data.labels.shift();
	}
	chart.update();
}

function hideshow() { // 캔버스 보이기 숨기기 
	var canvas = document.getElementById('canvas');
	if(canvas.style.display == "none") 	canvas.style.display = "block"
	else canvas.style.display = "none"  
}

window.addEventListener("load", drawChart); // load 이벤트가 발생하면 drawChart() 호출하도록 등록