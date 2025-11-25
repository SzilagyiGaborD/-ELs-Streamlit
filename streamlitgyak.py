import streamlit as st

# Alkalmazás címe
st.title("Alapvető HTML Elemek Streamlit-ben")

# 1. Színválasztó - ezt feljebb helyezzük, hogy korábban legyen
st.header("1. Színválasztó")
szin = st.color_picker("Válassz egy színt a háttérhez:", "#00ffaa")
st.write(f"A kiválasztott szín: **{szin}**")
st.markdown(f'<div style="width: 100px; height: 100px; background-color: {szin};"></div>', unsafe_allow_html=True)

# CSS a háttérszín beállításához
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {szin};
        background-image: linear-gradient(45deg, {szin} 0%, {szin}99 100%);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Legördülő lista (Selectbox)
st.header("2. Legördülő lista")
opciok = ["Válassz egy opciót!", "Python", "JavaScript", "Java", "C#", "Go"]
valasztott_nyelv = st.selectbox("Válaszd ki a kedvenc programozási nyelvedet:", opciok)

if valasztott_nyelv != "Válassz egy opciót!":
    st.write(f"A kedvenc nyelved: **{valasztott_nyelv}**")

# 3. Checkbox (Jelölőnégyzet)
st.header("3. Checkbox")
if st.checkbox("Elfogadom a feltételeket"):
    st.success("Köszönjük, hogy elfogadta a feltételeket!")
else:
    st.warning("Kérjük, fogadja el a feltételeket!")

# 4. Radio gombok
st.header("4. Választási lehetőség")
nem = st.radio("Neme:", ("Férfi", "Nő", "Helikopter", "Kenyér", "ATGM rakéta Vető"))

st.write(f"A kiválasztott nem: **{nem}**")

# 5. Szövegbevitel
st.header("5. Szövegbevitel")
nev = st.text_input("Add meg a neved:")
if nev:
    st.write(f"Üdvözöllek, **{nev}**!")

# 6. Számbevitel
st.header("6. Számbevitel")
kor = st.number_input("Add meg az életkorod:", min_value=0, max_value=120, value=25)
st.write(f"Az életkorod: **{kor}**")

# 7. Csúszka (Slider)
st.header("7. Csúszka")
ertekeles = st.slider("Értékeld az alkalmazást (1-10):", 1, 10, 5)
st.write(f"Az értékelésed: **{ertekeles}**")

# 8. Dátum választó
st.header("8. Dátum választó")
datum = st.date_input("Válassz egy dátumot:")
st.write(f"A kiválasztott dátum: **{datum}**")

# Eredmények összefoglalása
st.header("Összefoglalás")
if st.button("Mutasd az eredményeket"):
    st.subheader("Kiválasztott beállítások:")
    
    osszefoglalo = f"""
    - Kedvenc programozási nyelv: {valasztott_nyelv}
    - Neme: {nem}
    - Neve: {nev if nev else "Nem megadva"}
    - Életkora: {kor}
    - Értékelés: {ertekeles}/10
    - Dátum: {datum}
    - Háttérszín: {szin}
    """
    
    st.text(osszefoglalo)

# További CSS az olvashatóság érdekében (opcionális)
st.markdown(
    """
    <style>
    /* A szöveg olvasható maradjon sötét háttéren */
    .stApp {
        color: #333333;
    }
    
    /* A kártyák háttérszíne kissé átlátszó fehér */
    .css-1d391kg, .css-12oz5g7 {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Oldal vége
st.markdown("---")
st.markdown("*Készítette Streamlit segítségével*")