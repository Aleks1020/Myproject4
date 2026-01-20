import streamlit as st
import pandas as pd

st.title("🎮 Brawl Stars – Избор на герой")

st.write("Избери тип герой, след това конкретен герой от този тип.")

# Данни за типовете и героите
brawler_types = {
    "Support": ["Poco", "Byron", "Gus", "Pam"],
    "Assassin": ["Leon", "Crow", "Mortis", "Fang"],
    "Tank": ["El Primo", "Bull", "Frank", "Rosa"],
    "Sharpshooter": ["Piper", "Brock", "Belle", "Bea"],
    "Controller": ["Spike", "Sandy", "Emz", "Lou"]
}

# Инициализация на броячите
if "type_votes" not in st.session_state:
    st.session_state.type_votes = {key: 0 for key in brawler_types.keys()}

if "hero_votes" not in st.session_state:
    st.session_state.hero_votes = {}

st.subheader("🕹️ Стъпка 1: Избери тип герой")

selected_type = st.selectbox(
    "Тип герой:",
    list(brawler_types.keys())
)

st.subheader("⭐ Стъпка 2: Избери герой")

selected_hero = st.selectbox(
    "Герой:",
    brawler_types[selected_type]
)

# Записване на избора
if st.button("✅ Потвърди избора"):
    st.session_state.type_votes[selected_type] += 1

    if selected_hero not in st.session_state.hero_votes:
        st.session_state.hero_votes[selected_hero] = 0
    st.session_state.hero_votes[selected_hero] += 1

    st.success(
        f"Ти избра **{selected_hero}** от тип **{selected_type}**!"
    )

st.divider()

# Графики
st.subheader("📊 Статистика")

col1, col2 = st.columns(2)

with col1:
    st.write("Популярност по типове")
    type_df = pd.DataFrame.from_dict(
        st.session_state.type_votes,
        orient="index",
        columns=["Избори"]
    )
    st.bar_chart(type_df)

with col2:
    st.write("Популярност по герои")
    if st.session_state.hero_votes:
        hero_df = pd.DataFrame.from_dict(
            st.session_state.hero_votes,
            orient="index",
            columns=["Избори"]
        )
        st.bar_chart(hero_df)
    else:
        st.write("Все още няма избрани герои.")
