
import html
import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# CONFIGURACIÓN DE STREAMLIT
# ==========================================

st.set_page_config(
    page_title="Feliz cumpleaños, Bry 🎂",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 15% 10%, #3e2b73 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, #72335c 0%, transparent 45%),
        linear-gradient(135deg, #10152e, #21183c);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 1rem;
    max-width: 850px;
}

/* Ocultar elementos innecesarios */
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stHeader"] {
    background: transparent;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# PERSONALIZACIÓN DIRECTAMENTE EN EL CÓDIGO
# ==========================================

nombre = "Bry!"

remitente = "Por mas dias de racha! 💖"

mensaje = """
¡Feliz cumpleaños, Bry! 🎂💖

Hoy es un día muy especial y quiero desearte
toda la felicidad del mundo.

Espero que cumplas con muchos años mas,
que Diosito te bendiga, y la pases bonito
en tu dia!

Aunque no nos conozcamso quiero que sepas,
que aprecio muchísimo tu amistad. Gracias por
ser una chica tan amable y tierna siempre!

Nunca dejes de ser tú ni de brillar
con esa luz tan bonita que te caracteriza. ✨

¡Disfruta muchísimo tu día! 🎉
"""

# Proteger el contenido insertado en HTML
nombre = html.escape(nombre)
remitente = html.escape(remitente)
mensaje = html.escape(mensaje.strip()).replace("\n", "<br>")


# ==========================================
# HTML + CSS + JAVASCRIPT
# ==========================================

page = r'''
<!doctype html>
<html lang="es">

<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: 'Trebuchet MS', Verdana, sans-serif;
    color: #fff;
    overflow-x: hidden;
}

/* ESCENARIO PRINCIPAL */

.scene {
    position: relative;
    min-height: 720px;
    border: 1px solid #ffffff35;
    border-radius: 28px;
    overflow: hidden;

    background:
        radial-gradient(
            circle at 50% 30%,
            #7454ae 0%,
            #392359 43%,
            #17152f 100%
        );

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    padding: 32px 18px;
    isolation: isolate;
}

/* ESTRELLAS ANIMADAS */

.stars {
    position: absolute;
    inset: 0;
    pointer-events: none;

    background-image:
        radial-gradient(#fff 1px, transparent 1px);

    background-size: 43px 43px;

    opacity: .3;
    animation: twinkle 3s infinite alternate;
}

@keyframes twinkle {
    to {
        opacity: .65;
        transform: scale(1.015);
    }
}

/* RESPLANDOR */

.glow {
    position: absolute;
    top: 20%;
    height: 380px;
    width: 380px;
    background: #ff8ccc60;
    filter: blur(90px);
    border-radius: 100%;
    z-index: -1;
}

/* ENCABEZADO */

.eyebrow {
    font-size: 13px;
    letter-spacing: 4px;
    color: #ffd8ee;
    text-transform: uppercase;
    margin: 4px 0 15px;
    text-align: center;
}

/* TARJETA */

.card {
    position: relative;
    width: min(100%, 530px);
    min-height: 430px;
    border-radius: 25px;

    background:
        linear-gradient(145deg, #fff3fb, #f7dcf2);

    box-shadow:
        0 20px 60px #0a031c88,
        inset 0 1px #fff;

    color: #5a2854;

    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;

    padding: 27px;

    transition:
        transform .65s ease,
        box-shadow .5s;

    transform-style: preserve-3d;
}

.card:hover {
    transform: translateY(-5px) rotate(-1deg);
    box-shadow: 0 26px 80px #0a031ca8;
}

/* CARAS DE LA TARJETA */

.face {
    width: 100%;
    animation: arrive .6s both;
}

@keyframes arrive {
    from {
        opacity: 0;
        transform: translateY(15px) scale(.96);
    }

    to {
        opacity: 1;
        transform: none;
    }
}

/* PASTEL ANIMADO */

.cake {
    font-size: 75px;
    filter: drop-shadow(0 8px 6px #b5548e44);
    animation: bob 2.6s ease-in-out infinite;
}

@keyframes bob {
    50% {
        transform: translateY(-10px);
    }
}

/* TÍTULOS */

h1 {
    font-family: Georgia, serif;
    font-size: clamp(34px, 7vw, 53px);
    line-height: 1.05;
    margin: 15px 0 10px;
    color: #912c7a;
}

h2 {
    font-family: Georgia, serif;
    font-size: clamp(26px, 5vw, 38px);
    margin: 10px 0;
    color: #972c81;
}

.name {
    font-size: 25px;
    font-weight: 700;
    color: #b34487;
    overflow-wrap: anywhere;
}

.card p {
    font-size: 16px;
    line-height: 1.65;
    margin: 16px auto;
    max-width: 435px;
    overflow-wrap: anywhere;
}

.from {
    font-size: 13px;
    color: #975b85;
    font-style: italic;
    margin-top: 18px;
}

/* MENSAJE LARGO */

#inside {
    padding: 5px 0;
}

#inside p {
    font-size: 15px;
    line-height: 1.75;
}

/* BOTÓN */

.btn {
    position: relative;
    border: 0;
    border-radius: 100px;

    padding: 14px 27px;
    margin-top: 25px;

    cursor: pointer;
    font-weight: 800;
    font-size: 15px;

    color: #512448;

    background:
        linear-gradient(120deg, #ffdd87, #ff9fc6);

    box-shadow: 0 8px 24px #10051b55;

    transition:
        transform .2s,
        filter .2s;
}

.btn:hover {
    transform: translateY(-3px);
    filter: brightness(1.08);
}

.hint {
    font-size: 13px;
    color: #ebd8f6;
    margin-top: 16px;
    text-align: center;
}

/* GLOBOS FLOTANTES */

.balloon {
    position: absolute;
    bottom: -110px;

    width: 52px;
    height: 67px;

    border-radius: 50% 50% 45% 45%;
    opacity: .85;

    animation: float 12s linear infinite;
    pointer-events: none;
    z-index: -1;
}

.balloon::before {
    content: '';
    position: absolute;
    bottom: -7px;
    left: 23px;

    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 9px solid currentColor;
}

.balloon::after {
    content: '';
    position: absolute;
    top: 70px;
    left: 26px;

    width: 1px;
    height: 78px;

    background: #ffffff80;
}

@keyframes float {
    to {
        transform: translateY(-860px) rotate(17deg);
    }
}

/* CONFETI */

.confetti {
    position: absolute;
    top: -16px;

    width: 9px;
    height: 15px;

    pointer-events: none;

    animation:
        fall var(--t) linear forwards;

    z-index: 8;
}

@keyframes fall {
    to {
        transform:
            translate(var(--dx), 1200px)
            rotate(var(--r));

        opacity: .15;
    }
}

/* OCULTAR ELEMENTOS */

.hidden {
    display: none;
}

/* PIE DE TARJETA */

.footer {
    margin-top: 20px;
    font-size: 14px;
    color: #ffcfdf;
    opacity: .95;
}

/* ADAPTACIÓN A CELULARES */

@media (max-width: 480px) {

    .scene {
        min-height: 750px;
        padding: 24px 12px;
    }

    .card {
        min-height: 430px;
        padding: 20px;
    }

    .cake {
        font-size: 60px;
    }

    #inside p {
        font-size: 14px;
    }

    .eyebrow {
        letter-spacing: 2px;
    }
}

</style>
</head>

<body>

<div class="scene" id="scene">

    <div class="stars"></div>
    <div class="glow"></div>

    <!-- GLOBOS -->

    <div class="balloon"
         style="left:8%;
                background:#fa96c4;
                color:#fa96c4;
                animation-delay:-1s">
    </div>

    <div class="balloon"
         style="left:23%;
                background:#9ed5ff;
                color:#9ed5ff;
                animation-delay:-6s;
                animation-duration:15s">
    </div>

    <div class="balloon"
         style="left:78%;
                background:#ffdc8b;
                color:#ffdc8b;
                animation-delay:-4s;
                animation-duration:13s">
    </div>

    <div class="balloon"
         style="left:91%;
                background:#bca5ff;
                color:#bca5ff;
                animation-delay:-8s;
                animation-duration:16s">
    </div>

    <div class="eyebrow">
        ✧ Un pequeña sorpresa ✧
    </div>

    <!-- TARJETA -->

    <div class="card" id="card">

        <!-- PORTADA -->

        <section id="cover" class="face">

            <div class="cake">🎂</div>

            <h1>¡Feliz cumpleaños!</h1>

            <div class="name">
                __NOMBRE__
            </div>

            <p>
                Hoy es un dia especial ✨
            </p>

            <div class="from">
                Tienes un mensaje esperando
                dentro de esta tarjeta 💌
            </div>

        </section>

        <!-- MENSAJE INTERIOR -->

        <section id="inside" class="face hidden">

            <div style="font-size:49px">
                💖 🌟 💖
            </div>

            <h2>¡Pide un deseo!</h2>

            <p>
                __MENSAJE__
            </p>

            <div class="from">
                Con mucho cariño,
                <br>
                <strong>__REMITENTE__</strong>
            </div>

        </section>

    </div>

    <!-- BOTÓN -->

    <button
        id="open"
        class="btn"
        onclick="toggleCard()">

        💌 Abrir mi sorpresa

    </button>

    <div class="hint" id="hint">
        :3
    </div>

    <div class="footer">
        Hecho con mucho cariño ♡
    </div>

</div>

<script>

/* ESTADO DE LA TARJETA */

let opened = false;

/* LLUVIA DE CONFETI */

function confetti() {

    const scene = document.getElementById('scene');

    const colors = [
        '#ffb8d5',
        '#fbe39a',
        '#aaabff',
        '#a8f5e0',
        '#ffffff'
    ];

    for (let i = 0; i < 110; i++) {

        const s = document.createElement('span');

        s.className = 'confetti';

        s.style.left =
            (Math.random() * 100) + '%';

        s.style.background =
            colors[i % colors.length];

        s.style.borderRadius =
            (i % 3 === 0 ? '50%' : '2px');

        s.style.setProperty(
            '--t',
            (2.4 + Math.random() * 2.2) + 's'
        );

        s.style.setProperty(
            '--dx',
            (Math.random() * 230 - 115) + 'px'
        );

        s.style.setProperty(
            '--r',
            (Math.random() * 1100 - 550) + 'deg'
        );

        scene.appendChild(s);

        setTimeout(() => {
            s.remove();
        }, 5000);
    }
}

/* ABRIR Y CERRAR LA TARJETA */

function toggleCard() {

    const button = document.getElementById('open');
    const hint = document.getElementById('hint');
    const cover = document.getElementById('cover');
    const inside = document.getElementById('inside');

    if (opened) {
        confetti();
        return;
    }

    opened = true;

    cover.classList.add('hidden');
    inside.classList.remove('hidden');

    button.textContent = '🎉 ¡Otra lluvia de alegría!';

    hint.textContent =
        '✨ Nunca cambies! ✨';

    inside.style.animation = 'none';

    void inside.offsetHeight;

    inside.style.animation = 'arrive .6s both';

    confetti();

    /* Ajustar la altura del contenido al abrir la carta */
    setTimeout(adjustHeight, 100);
}

/* ADAPTAR ALTURA DEL ESCENARIO */

function adjustHeight() {

    const scene = document.getElementById('scene');

    scene.style.minHeight = opened
        ? 'auto'
        : '720px';
}

</script>

</body>
</html>
'''

# ==========================================
# INSERTAR DATOS PERSONALIZADOS
# ==========================================

page = (
    page.replace("__NOMBRE__", nombre)
        .replace("__MENSAJE__", mensaje)
        .replace("__REMITENTE__", remitente)
)

# ==========================================
# MOSTRAR TARJETA EN STREAMLIT
# ==========================================

components.html(
    page,
    height=1100,
    scrolling=True
)
