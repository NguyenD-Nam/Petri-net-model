var content;
function final(){
	content = `<iframe src=" https://replit.com/@DuongTran6/AssMM?lite=true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals" scrolling="no" allowtransparency="true" allowfullscreen="true" height="750px" frameborder="0"></iframe><div class="img" id="img"><img src="img/Exercise1.png"><br><img src="img/Exercise2.png"><br><img src="img/Exercise4.png"></div>`;
	document.getElementById('container').innerHTML = content;
	clear();
	document.getElementById('fn').classList.add('curr');
	document.getElementById('img').style.height = "750px";
}
function one(){
	content = `<iframe src=" https://replit.com/@NamNguyen56/MMEx1?lite=true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals" scrolling="no" allowtransparency="true" allowfullscreen="true" height="550px" frameborder="0"></iframe><div class="img" id="img"><img src="img/Exercise1.png"></div>`;
	document.getElementById('container').innerHTML = content;
	clear();
	document.getElementById('ex1').classList.add('curr');
	document.getElementById('img').style.height = "550px";
}
function two(){
	content = `<iframe src=" https://replit.com/@NamNguyen56/MMEx2?lite=true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals" scrolling="no" allowtransparency="true" allowfullscreen="true" height="550px" frameborder="0"></iframe><div class="img" id="img"><img src="img/Exercise2.png"></div>`;

	document.getElementById('container').innerHTML = content;
	clear();
	document.getElementById('ex2').classList.add('curr');
	document.getElementById('img').style.height = "550px";
}
function three(){
	content = `<iframe src=" https://replit.com/@NamNguyen56/MMEx3?lite=true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals" scrolling="no" allowtransparency="true" allowfullscreen="true" height="550px" frameborder="0"></iframe><div class="img" id="img"><img src="img/Exercise4.png"></div>`;
	document.getElementById('container').innerHTML = content;
	clear();
	document.getElementById('ex3').classList.add('curr');
	document.getElementById('img').style.height = "550px";
}

function clear(){
	document.getElementById('ex1').classList.remove('curr');
	document.getElementById('ex2').classList.remove('curr');
	document.getElementById('ex3').classList.remove('curr');
	document.getElementById('fn').classList.remove('curr');
}
