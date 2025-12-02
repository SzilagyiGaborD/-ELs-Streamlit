import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Az oldal beállításai
st.set_page_config(
    page_title="Másodfokú Függvény Ábrázoló",
    page_icon="📈",
    layout="wide"
)

# Cím és leírás
st.title("📈 Másodfokú Függvény Ábrázoló")
st.markdown("""
Ez az alkalmazás **Ax² + Bx + C** alakú másodfokú függvényeket ábrázol.
A jobb oldalon beállíthatod az **A**, **B** és **C** paramétereket.
""")

# Oldalsáv a paraméterek beállításához
with st.sidebar:
    st.header("⚙️ Paraméterek")
    
    # Paraméterek beállítása csúszkákkal
    a = st.slider(
        "A (másodfokú tag együtthatója)",
        min_value=-10.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
        help="Az x² együtthatója. Ha A > 0, a parabola felfelé nyitott, ha A < 0, lefelé."
    )
    
    b = st.slider(
        "B (elsőfokú tag együtthatója)",
        min_value=-20.0,
        max_value=20.0,
        value=0.0,
        step=0.1,
        help="Az x együtthatója. Befolyásolja a parabola szimmetriatengelyének helyét."
    )
    
    c = st.slider(
        "C (konstans tag)",
        min_value=-20.0,
        max_value=20.0,
        value=0.0,
        step=0.1,
        help="A konstans tag. Ez az y-tengelymetszet értéke."
    )
    
    # X tartomány beállítása
    st.subheader("📊 Ábrázolási tartomány")
    x_min = st.number_input("X minimum", value=-10.0, step=0.5)
    x_max = st.number_input("X maximum", value=10.0, step=0.5)
    
    # Vonalvastagság beállítása
    line_width = st.slider("Vonalvastagság", 1, 5, 2)
    
    # További információk a függvényről
    st.subheader("ℹ️ Függvény információk")
    st.info(f"**Függvény:** y = {a:.1f}x² + {b:.1f}x + {c:.1f}")

# Fő tartalom
col1, col2 = st.columns([2, 1])

with col1:
    # Függvény értékek kiszámítása
    x = np.linspace(x_min, x_max, 1000)
    y = a * x**2 + b * x + c
    
    # Ábra létrehozása
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Függvény ábrázolása
    ax.plot(x, y, linewidth=line_width, color='blue', label=f'y = {a:.1f}x² + {b:.1f}x + {c:.1f}')
    
    # Tengelyek és rács
    ax.axhline(y=0, color='black', linewidth=0.5, alpha=0.7)
    ax.axvline(x=0, color='black', linewidth=0.5, alpha=0.7)
    ax.grid(True, alpha=0.3)
    
    # Cím és feliratok
    ax.set_title(f"y = {a:.1f}x² + {b:.1f}x + {c:.1f}", fontsize=14, fontweight='bold')
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    
    # Tengely határok
    ax.set_xlim([x_min, x_max])
    
    # Legenda
    ax.legend(loc='best')
    
    # Stílus beállítások
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    # Ábra megjelenítése
    st.pyplot(fig)

with col2:
    st.subheader("📊 Függvény tulajdonságai")
    
    # Diszkrimináns és gyökök számítása
    D = b**2 - 4*a*c
    
    # Információk kijelzése
    st.markdown(f"""
    **Paraméterek:**
    - A = {a:.2f}
    - B = {b:.2f}
    - C = {c:.2f}
    
    **Diszkrimináns (D):**
    - D = {D:.2f}
    """)
    
    # Gyökök meghatározása
    if a == 0:
        st.warning("⚠️ Ha A = 0, akkor nem másodfokú függvényről van szó!")
    elif D > 0:
        x1 = (-b + np.sqrt(D)) / (2*a)
        x2 = (-b - np.sqrt(D)) / (2*a)
        st.success(f"✅ Két valós gyök van:")
        st.write(f"x₁ = {x1:.2f}")
        st.write(f"x₂ = {x2:.2f}")
    elif D == 0:
        x = -b / (2*a)
        st.info(f"ℹ️ Egy valós gyök van (dupla gyök):")
        st.write(f"x = {x:.2f}")
    else:
        st.error("❌ Nincs valós gyök")
    
    # További információk
    if a != 0:
        # Tengelypont
        vertex_x = -b / (2*a)
        vertex_y = a * vertex_x**2 + b * vertex_x + c
        
        # Nyitási irány
        if a > 0:
            direction = "felfelé nyitott"
        else:
            direction = "lefelé nyitott"
        
        st.markdown(f"""
        **További információk:**
        - Nyitási irány: {direction}
        - Tengelypont: ({vertex_x:.2f}, {vertex_y:.2f})
        - Y-tengelymetszet: (0, {c:.2f})
        """)

# Footer
st.markdown("---")
st.caption("Másodfokú Függvény Ábrázoló | Készült Streamlit-tel")