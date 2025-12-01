*MASODIK STREAMLIT*

import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Legendás Hadi Technika Lexikon", page_icon="🛡️")

st.title("🛡️ Legendás Hadi Technika Lexikon")
st.write("Válassz egy kategóriát, és nézzünk rá a történelem menő vasaira.")

# --- Adatbázis (egyszerű, beégetett) ---

DATA = {
    "Második világháborús tankok": {
        "Panzer IV": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/2/23/PzKpfw_IV_Ausf_G.jpg",
            "desc": "A Panzer IV Németország egyik legsokoldalúbb harckocsija volt, a háború teljes időtartama alatt szolgált.",
            "fact": "Eredetileg gyalogság-támogató tanknak szánták, de végül a német páncélos erők gerince lett."
        },
        "T-34": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/7/70/T-34-85_cfb_borden_1.jpg",
            "desc": "A szovjet T-34 a modern harckocsik ősének számít, ferde páncélzata korát megelőzte.",
            "fact": "Az egyszerű szerkezet miatt tömegesen gyártották — a mennyiség és minőség comboját hozta."
        },
    },
    "Történelmi repülők": {
        "Spitfire": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Spitfire_VB_BM597.jpg",
            "desc": "A legendás brit vadászrepülő, amely kulcsszerepet játszott a Brit csatában.",
            "fact": "A szárnyformája miatt elképesztően fordulékony volt."
        },
        "P-51 Mustang": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/1/1e/P-51_Mustang_near_Grefrath_%28cropped%29.jpg",
            "desc": "Az egyik leghíresebb amerikai vadászgép, hosszú hatótávval és megbízhatósággal.",
            "fact": "A Mustang kísérte el a bombázókat Németország fölé — életmentő volt."
        }
    },
    "Hadihajók": {
        "Bismarck": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Bundesarchiv_Bild_146-1984-055-16%2C_Schlachtschiff_Bismarck.jpg",
            "desc": "A német Bismarck csatahajó rettegett volt rövid, de intenzív pályafutása alatt.",
            "fact": "Elsüllyesztése hatalmas presztízsveszteség volt a német flottának."
        },
        "Yamato": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Yamato_during_trials_1941.jpg",
            "desc": "A japán Yamato a valaha épített legnehezebb csatahajó.",
            "fact": "1937-ben kezdték építeni, hogy felvegye a versenyt bármely amerikai hadihajóval."
        }
    }
}

# --- Kategória és típus választása ---

category = st.selectbox("Kategória:", list(DATA.keys()))

item = st.selectbox("Eszköz:", list(DATA[category].keys()))

info = DATA[category][item]

# --- Megjelenítés ---

st.header(item)
st.image(info["img"], use_container_width=True)
st.write(f"**Leírás:** {info['desc']}")
st.write(f"**Érdekesség:** {info['fact']}")

st.divider()

# --- Szavazás ---

st.subheader("Értékeld, mennyire ikonikus! (1–10)")

rating = st.slider("Pontszám:", 1, 10, 5)
if st.button("Mentés"):
    row = {
        "timestamp": datetime.now().isoformat(),
        "category": category,
        "item": item,
        "rating": rating,
    }

    if os.path.exists("ratings.csv"):
        df = pd.read_csv("ratings.csv")
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_csv("ratings.csv", index=False)
    st.success("Elmentve! 🚀")

# --- Eddigi toplista ---

if os.path.exists("ratings.csv"):
    st.subheader("Top ikonikus eszközök (átlag alapján)")
    df = pd.read_csv("ratings.csv")
    top = df.groupby("item")["rating"].mean().sort_values(ascending=False).head(5)
    st.dataframe(top)
