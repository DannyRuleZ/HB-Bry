import html
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Un cumpleaños mágico 🎂", page_icon="🎉", layout="centered")

st.markdown("""
<style>
.stApp { background: radial-gradient(circle at 15% 10%, #3e2b73 0%, transparent 40%),
                    radial-gradient(circle at 85% 85%, #72335c 0%, transparent 45%),
                    linear-gradient(135deg, #10152e, #21183c); }
.block-container { padding-top: 2rem; max-width: 850px; }
h1, p, label { color: #fff !important; }
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
    background: #ffffff12; color: white; border: 1px solid #ffffff44;
}
</style>
""", unsafe_allow_html=True)

st.title("✨ Un pequeño regalo digital")
st.write("Personaliza los detalles y abre la tarjeta para descubrir la sorpresa.")

with st.expander("💌 Personalizar tarjeta", expanded=False):
    nombre = st.text_input("Nombre de quien cumple años", "Persona especial", max_chars=60)
    remitente = st.text_input("De parte de", "Alguien que te quiere mucho", max_chars=60)
    mensaje = st.text_area(
        "Dedicatoria",
        "Que este nuevo año de vida te traiga aventuras inolvidables, sueños cumplidos y muchísimas razones para sonreír. ¡Nunca dejes de brillar! 💖",
        max_chars=500,
    )

nombre = html.escape(nombre.strip() or "Persona especial")
remitente = html.escape(remitente.strip() or "Alguien que te quiere mucho")
mensaje = html.escape(mensaje.strip() or "¡Que todos tus sueños se hagan realidad!").replace("\n", "<br>")

page = r'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
* {box-sizing:border-box}
body {margin:0;font-family:'Trebuchet MS',Verdana,sans-serif;color:#fff;overflow-x:hidden}
.scene {position:relative;min-height:650px;border:1px solid #ffffff35;border-radius:28px;overflow:hidden;
 background:radial-gradient(circle at 50% 30%,#7454ae 0%,#392359 43%,#17152f 100%);display:flex;
 flex-direction:column;align-items:center;justify-content:center;padding:32px 18px;isolation:isolate}
.stars{position:absolute;inset:0;pointer-events:none;background-image:radial-gradient(#fff 1px,transparent 1px);background-size:43px 43px;opacity:.3;animation:twinkle 3s infinite alternate}
@keyframes twinkle{to{opacity:.65;transform:scale(1.015)}}
.glow{position:absolute;inset:auto;top:20%;height:380px;width:380px;background:#ff8ccc60;filter:blur(90px);border-radius:100%;z-index:-1}
.eyebrow{font-size:13px;letter-spacing:4px;color:#ffd8ee;text-transform:uppercase;margin:4px 0 15px;text-align:center}
.card{position:relative;width:min(100%,530px);min-height:365px;border-radius:25px;
 background:linear-gradient(145deg,#fff3fb,#f7dcf2);box-shadow:0 20px 60px #0a031c88, inset 0 1px #fff;
 color:#5a2854;display:flex;align-items:center;justify-content:center;text-align:center;padding:27px;
 transition:transform .65s ease,box-shadow .5s;transform-style:preserve-3d}
.card:hover{transform:translateY(-5px) rotate(-1deg);box-shadow:0 26px 80px #0a031ca8}
.face{width:100%;animation:arrive .6s both}
@keyframes arrive{from{opacity:0;transform:translateY(15px) scale(.96)}to{opacity:1;transform:none}}
.cake{font-size:75px;filter:drop-shadow(0 8px 6px #b5548e44);animation:bob 2.6s ease-in-out infinite}
@keyframes bob{50%{transform:translateY(-10px)}}
h1{font-family:Georgia,serif;font-size:clamp(34px,7vw,53px);line-height:1.05;margin:15px 0 10px;color:#912c7a}
h2{font-family:Georgia,serif;font-size:clamp(26px,5vw,38px);margin:10px 0;color:#972c81}
.name{font-size:22px;font-weight:700;color:#b34487;overflow-wrap:anywhere}
.card p{font-size:16px;line-height:1.65;margin:16px auto;max-width:435px;overflow-wrap:anywhere}
.from{font-size:13px;color:#975b85;font-style:italic;margin-top:18px}
.btn{position:relative;border:0;border-radius:100px;padding:14px 27px;margin-top:25px;cursor:pointer;
 font-weight:800;font-size:15px;color:#512448;background:linear-gradient(120deg,#ffdd87,#ff9fc6);
 box-shadow:0 8px 24px #10051b55;transition:transform .2s,filter .2s}
.btn:hover{transform:translateY(-3px);filter:brightness(1.08)}
.hint{font-size:13px;color:#ebd8f6;margin-top:16px;text-align:center}
.balloon{position:absolute;bottom:-110px;width:52px;height:67px;border-radius:50% 50% 45% 45%;opacity:.85;
 animation:float 12s linear infinite;pointer-events:none;z-index:-1}
.balloon::before{content:'';position:absolute;bottom:-7px;left:23px;border-left:4px solid transparent;border-right:4px solid transparent;border-top:9px solid currentColor}
.balloon::after{content:'';position:absolute;top:70px;left:26px;width:1px;height:78px;background:#ffffff80}
@keyframes float{to{transform:translateY(-860px) rotate(17deg)}}
.confetti{position:absolute;top:-16px;width:9px;height:15px;pointer-events:none;animation:fall var(--t) linear forwards;z-index:8}
@keyframes fall{to{transform:translate(var(--dx),760px) rotate(var(--r));opacity:.15}}
.hidden{display:none}
.footer{margin-top:20px;font-size:14px;color:#ffcfdf;opacity:.95}
@media(max-width:480px){.scene{min-height:680px;padding:24px 12px}.card{min-height:390px;padding:20px}.cake{font-size:60px}}
</style></head><body>
<div class="scene" id="scene">
<div class="stars"></div><div class="glow"></div>
<div class="balloon" style="left:8%;background:#fa96c4;color:#fa96c4;animation-delay:-1s"></div>
<div class="balloon" style="left:23%;background:#9ed5ff;color:#9ed5ff;animation-delay:-6s;animation-duration:15s"></div>
<div class="balloon" style="left:78%;background:#ffdc8b;color:#ffdc8b;animation-delay:-4s;animation-duration:13s"></div>
<div class="balloon" style="left:91%;background:#bca5ff;color:#bca5ff;animation-delay:-8s;animation-duration:16s"></div>
<div class="eyebrow">✧ Una sorpresa hecha para ti ✧</div>
<div class="card" id="card">
 <section id="cover" class="face">
  <div class="cake">🎂</div>
  <h1>¡Feliz cumpleaños!</h1>
  <div class="name">__NOMBRE__</div>
  <p>Hoy el universo celebra que existes. ✨</p>
  <div class="from">Tienes un mensaje esperando dentro de esta tarjeta 💌</div>
 </section>
 <section id="inside" class="face hidden">
  <div style="font-size:49px">💖 🌟 💖</div>
  <h2>¡Pide un deseo!</h2>
  <p>__MENSAJE__</p>
  <div class="from">Con mucho cariño,<br><strong>__REMITENTE__</strong></div>
 </section>
</div>
<button id="open" class="btn" onclick="toggleCard()">💌 Abrir mi sorpresa</button>
<div class="hint" id="hint">Hay cosas bonitas que merecen celebrarse ✨</div>
<div class="footer">Hecho con mucho cariño ♡</div>
</div>
<script>
let opened=false;
function confetti(){
 const scene=document.getElementById('scene');
 const colors=['#ffb8d5','#fbe39a','#aaabff','#a8f5e0','#fff'];
 for(let i=0;i<110;i++){
  const s=document.createElement('span');s.className='confetti';
  s.style.left=(Math.random()*100)+'%';s.style.background=colors[i%colors.length];
  s.style.borderRadius=(i%3===0?'50%':'2px');
  s.style.setProperty('--t',(2.4+Math.random()*2.2)+'s');
  s.style.setProperty('--dx',(Math.random()*230-115)+'px');
  s.style.setProperty('--r',(Math.random()*1100-550)+'deg');
  scene.appendChild(s);setTimeout(()=>s.remove(),5000);
 }
}
function toggleCard(){
 opened=!opened;
 document.getElementById('cover').classList.toggle('hidden',opened);
 document.getElementById('inside').classList.toggle('hidden',!opened);
 document.getElementById('open').textContent=opened?'🎉 ¡Otra lluvia de alegría!':'💌 Abrir mi sorpresa';
 document.getElementById('hint').textContent=opened?'✨ Que la magia te acompañe todo el año ✨':'Hay cosas bonitas que merecen celebrarse ✨';
 document.querySelector('.face:not(.hidden)').style.animation='none';
 void document.querySelector('.face:not(.hidden)').offsetHeight;
 document.querySelector('.face:not(.hidden)').style.animation='arrive .6s both';
 if(opened){confetti();}else{confetti();}
