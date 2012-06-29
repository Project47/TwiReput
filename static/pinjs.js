
window.onload=doFirst;

function doFirst(){

login=document.getElementById("login");
lab=document.getElementById("lab1");
pin=document.getElementById("pin1");
x1=document.getElementById("p1");
x2=document.getElementById("p2");
x3=document.getElementById("p3");
x4=document.getElementById("p4");
y4=document.getElementById("i4");
y1=document.getElementById("i1");
y2=document.getElementById("i2");
y3=document.getElementById("i3");
url=document.getElementById("url");
sect=document.getElementById("section");
sect1=document.getElementById("top10");
sect2=document.getElementById("section3");
img=document.getElementById("image");
list1=sect1.innerHTML
sect1.innerHTML=""



x1.addEventListener("mousemove",function show(){y1.style.visibility='visible';} ,false);
x1.addEventListener("mouseout",function show(){y1.style.visibility='hidden'; } ,false);
x2.addEventListener("mousemove",function show(){y2.style.visibility='visible';} ,false);
x2.addEventListener("mouseout",function show(){y2.style.visibility='hidden';} ,false);
x3.addEventListener("mousemove",function show(){y3.style.visibility='visible' ;} ,false);
x3.addEventListener("mouseout",function show(){y3.style.visibility='hidden';} ,false);
x4.addEventListener("mousemove",function show(){y4.style.visibility='visible' ;} ,false);
x4.addEventListener("mouseout",function show(){y4.style.visibility='hidden';} ,false);

x2.addEventListener("click",how,false);
x1.addEventListener("click",rate,false);
x3.addEventListener("click",aboutUs ,false);
login.addEventListener("click",loading ,false);
x4.addEventListener("click",top10 ,false);

login.style.visibility='visible';
lab.style.visibility='visible';
sect2.style.visibility='visible';
x1.style.background='#5FB7E3';
x1.style.border='4px solid #5C95D1';
}



function top10(){
url.style.visibility='hidden';
login.style.visibility='hidden';
lab.style.visibility='hidden';
pin.style.visibility='hidden';
sect.style.visibility='visible';
sect2.style.visibility='hidden';
sect1.style.visibility='visible';
x4.style.background='#5FB7E3';
x4.style.border='4px solid #5C95D1';
x2.style.border='4px solid #5FB7E3'
x3.style.border='4px solid #5FB7E3';
x1.style.border='4px solid #5FB7E3';
x1.style.background='none';
x2.style.background='none';
x3.style.background='none';
sect.innerHTML=list1;


//sect1.innerHTML="<div id=\"section1\"><table align=\"center\"><tr><th>User</th><th>Score</th></tr>{% for u in arr   %}<tr>	{% for v in u   %}	<td>{{ v }}</td>{% endfor %}</tr>{% endfor %}<table/></div>";
//sect.style.height="100px"
//tab.style.height="40px"


}



function rate(){
url.style.visibility='visible';
login.style.visibility='visible';
lab.style.visibility='visible';
pin.style.visibility='visible';
sect1.style.visibility='hidden';
sect.style.visibility='hidden';
sect2.style.visibility='visible';
x1.style.background='#5FB7E3';
x1.style.border='4px solid #5C95D1';
x2.style.border='4px solid #5FB7E3';
x3.style.border='4px solid #5FB7E3';
x4.style.border='4px solid #5FB7E3';
x4.style.background='none';
x2.style.background='none';
x3.style.background='none';
sect.innerHTML=""

}
function how(){
url.style.visibility='hidden';
login.style.visibility='hidden';
lab.style.visibility='hidden';
sect1.style.visibility='hidden';
pin.style.visibility='hidden';
sect2.style.visibility='hidden';
sect.style.visibility='visible';
sect.innerHTML="<br />TwiReput is an online application which rates your twitter account on basis of various factors.<br /><br />These factors are:<br /><br />No of followersNo of Retweets<br /><br />Your mentions in lists<br /><br />No of friends<br /><br />The people who are following you"
x2.style.background='#5FB7E3';
x2.style.border='4px solid #5C95D1';
x1.style.border='4px solid #5FB7E3';
x3.style.border='4px solid #5FB7E3';
x1.style.background='none';
x3.style.background='none';


x4.style.border='4px solid #5FB7E3';
x4.style.background='none';


}
function aboutUs(){
url.style.visibility='hidden';
login.style.visibility='hidden';
sect1.style.visibility='hidden';
lab.style.visibility='hidden';
pin.style.visibility='hidden';
sect2.style.visibility='hidden';
sect.style.visibility='visible';
sect.innerHTML="<br />We are: <br /><br />Anuj Gandhi<br /><br />Ajay Nair<br /><br />Shreyas Panigrahi<br /><br />Partha Veerkar<br /><br /><br /> We all are students of PICT, Pune. We developed this website as a mini project for Infinitely Beta selection.";
x3.style.background='#5FB7E3';
x3.style.border='4px solid #5C95D1';
x1.style.border='4px solid #5FB7E3';
x2.style.border='4px solid #5FB7E3';
x1.style.background='none';
x2.style.background='none';
x4.style.border='4px solid #5FB7E3';
x4.style.background='none';

}

function loading(){
img.style.visibility='visible';
}

