var numKeys = [];
var opns = [];
var res = document.querySelector("#resultArea");
var clrBtn = document.querySelector("#clrTxt");
var okBtn = document.querySelector("#ok");
var form = document.querySelector("#form");
var dados = document.querySelector("#dados");
var resetBtn = document.querySelector("#reset");

//var delBtn = document.querySelector("#del");
//var eqBtn = document.querySelector("#eq");
//var decPoint = document.querySelector("#decp");
//var opnSyms = ["+", "-", "*", "/"];

// Inicializacao dos butoes numericos
for(var i=0;i<=9;i++){
	(function(i){
    	qs = "#num" + i;
		numKeys.push(document.querySelector(qs));
        numKeys[i].addEventListener("click", function(){

            // Alterando o conteudo e formatacao do "guess" para o input
            if(res.style.color == "")
            {
                res.style.color = "black";
                res.textContent = "";
            }
            
            // impedir que o usuario entre com um valor maior que 100:
            if(parseInt(0+res.textContent+i)<=100)
            {
                res.textContent += i;
            }
		});
  	}(i));
}

// Inicializacao do botao de limpar 
clrBtn.addEventListener("click", function(){
	res.textContent = "";
});

// Inicializacao do botao que computa o input
okBtn.addEventListener("click", function(){
    // quando nao e o primeiro input:
	if(dados.value.length>0)
	{
		dados.value += "," + res.textContent ; 
	}
	else
    // quando e o primeiro input:
	{
		dados.value +=  res.textContent ; 
    }
    form.submit();
});

// Inicializacao do botao que limpa todos os inputs
resetBtn.addEventListener("click",function(){
    dados.value = 0;
    form.submit();
});

// Função que introduz o "guess" como sugestao no campo de resultado:
function makeEducatedGuess(guess) {
    res.textContent = guess;
}

