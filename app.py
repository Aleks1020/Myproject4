import streamlit as st
import pandas as pd

st.title("🎮 Brawl Stars – Типове герои")

st.write("Избери тип герой и виж примери от играта!")

# Данни за типовете герои и примери
brawler_types = {
    "Support": ["Poco", "Byron", "Gus", "Pam"],
    "Assassin": ["Leon", "Crow", "Mortis", "Fang"],
    "Tank": ["El Primo", "Bull", "Frank", "Rosa"],
    "Sharpshooter": ["Piper", "Brock", "Belle", "Bea"],
    "Controller": ["Spike", "Sandy", "Emz", "Lou"]
}

# Инициализация на брояча
if "votes" not in st.session_state:
    st.session_state.votes = {key: 0 for key in brawler_types.keys()}

st.subheader("🕹️ Избор на тип герой")

selected_type = st.selectbox(
    "Избери тип герой:",
    list(brawler_types.keys())
)

# Показване на героите
st.subheader(f"⭐ Герои от тип **{selected_type}**")
for brawler in brawler_types[selected_type]:
    st.write(f"- {brawler}")

# Бутон за гласуване
if st.button("✅ Харесвам този тип"):
    st.session_state.votes[selected_type] += 1
    st.success("Изборът е записан!")

st.divider()

# Резултати
st.subheader("📊 Популярност на типовете герои")

votes_df = pd.DataFrame.from_dict(
    st.session_state.votes,
    orient="index",
    columns=["Брой гласове"]
)

st.bar_chart(votes_df)
