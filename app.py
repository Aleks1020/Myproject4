import streamlit as st
import pandas as pd

st.title("🎮 Brawl Stars – Избор на герой")

# Данни за типовете и героите
brawler_types = {
    "Support": ["Poco", "Byron", "Gus", "Pam"],
    "Assassin": ["Leon", "Crow", "Mortis", "Fang"],
    "Tank": ["El Primo", "Bull", "Frank", "Rosa"],
    "Sharpshooter": ["Piper", "Brock", "Belle", "Bea"],
    "Controller": ["Spike", "Sandy", "Emz", "Lou"]
}

# Информация за героите (Level 11)
brawler_stats_lvl11 = {
    "Mortis": {
        "Тип": "Assassin",
        "Живот": 7600,
        "Атака": 1350,
        "Скорост": "Много бърза",
        "Супер": "Dash + Damage",
        "Gadget": "Survival Shovel",
        "Star Power": "Coiled Snake"
    },
    "Leon": {
        "Тип": "Assassin",
        "Живот": 6400,
        "Атака": 1920,
        "Скорост": "Много бърза",
        "Супер": "Невидимост",
        "Gadget": "Clone Projector",
        "Star Power": "Smoke Trails"
    },
    "Poco": {
        "Тип": "Support",
        "Живот": 7400,
        "Атака": 1200,
        "Скорост": "Нормална",
        "Супер": "Лекуване",
        "Gadget": "Tuning Fork",
        "Star Power": "Da Capo"
    }
}

# Инициализация на броячите
if "type_votes" not in st.session_state:
    st.session_state.type_votes = {key: 0 for key in brawler_types.keys()}

if "hero_votes" not in st.session_state:
    st.session_state.hero_votes = {}

# Избор
st.subheader("🕹️ Стъпка 1: Избери тип герой")
selected_type = st.selectbox("Тип герой:", list(brawler_types.keys()))

st.subheader("⭐ Стъпка 2: Избери герой")
selected_hero = st.selectbox("Герой:", brawler_types[selected_type])

# Потвърждение
if st.button("✅ Потвърди избора"):
    st.session_state.type_votes[selected_type] += 1
    st.session_state.hero_votes[selected_hero] = (
        st.session_state.hero_votes.get(selected_hero, 0) + 1
    )
    st.success(f"Избра **{selected_hero}**!")

# --- ИНФОРМАЦИЯ ЗА ГЕРОЯ (ПРЕДИ СТАТИСТИКАТА) ---
st.divider()
st.subheader(f"📋 Информация за {selected_hero} (Level 11)")

if selected_hero in brawler_stats_lvl11:
    hero_info = brawler_stats_lvl11[selected_hero]
    hero_df = pd.DataFrame(
        hero_info.items(),
        columns=["Показател", "Стойност"]
    )
    st.table(hero_df)
else:
    st.write("ℹ️ Няма налична информация за този герой.")

# --- СТАТИСТИКА ---
st.divider()
st.subheader("📊 Статистика от изборите")

col1, col2 = st.columns(2)

with col1:
    st.write("Типове герои")
    type_df = pd.DataFrame.from_dict(
        st.session_state.type_votes,
        orient="index",
        columns=["Избори"]
    )
    st.bar_chart(type_df)

with col2:
    st.write("Герои")
    if st.session_state.hero_votes:
        hero_df = pd.DataFrame.from_dict(
            st.session_state.hero_votes,
            orient="index",
            columns=["Избори"]
        )
        st.bar_chart(hero_df)
    else:
        st.write("Все още няма избрани герои.")
