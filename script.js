var content;
function one(){
	content = `<iframe src=" https://replit.com/@NamNguyen56/MMEx1?lite=true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals" scrolling="no" allowtransparency="true" allowfullscreen="true" height="550px" frameborder="0"></iframe><div class="img"><img src="img/Exercise1.png"></div>`;
	document.getElementById('container').innerHTML = content;
	clear();
	document.getElementById('ex1').classList.add('curr');
}
function two(){
	content = `<iframe src=" https://replit.com/@NamNguyen56/MMEx2?lite=true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals" scrolling="no" allowtransparency="true" allowfullscreen="true" height="550px" frameborder="0"></iframe><div class="img"><img src="img/Exercise2.png"></div>`;

	document.getElementById('container').innerHTML = content;
	clear();
	document.getElementById('ex2').classList.add('curr');
}
function three(){
	content = `<iframe src=" https://replit.com/@NamNguyen56/MMEx3?lite=true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals" scrolling="no" allowtransparency="true" allowfullscreen="true" height="550px" frameborder="0"></iframe><div class="img"><img src="img/Exercise4.png"></div>`;
	document.getElementById('container').innerHTML = content;
	clear();
	document.getElementById('ex3').classList.add('curr');
}
function four(){
	content = `<div class="img" style="text-align: center; width: 70%; margin: auto;">During process</div><div class="img"><img src="img/Exercise4.png"></div>`;
	document.getElementById('container').innerHTML = content;
	clear();
	document.getElementById('ex4').classList.add('curr');
}

function clear(){
	document.getElementById('ex1').classList.remove('curr');
	document.getElementById('ex2').classList.remove('curr');
	document.getElementById('ex3').classList.remove('curr');
	document.getElementById('ex4').classList.remove('curr');
}