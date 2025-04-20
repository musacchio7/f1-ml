import streamlit as st
import pandas as pd

# 📂 Load preprocessed data
@st.cache_data

def load_data():
    df = pd.read_csv("../data/processed/driver_final_profiles_weighted.csv")
    return df

df = load_data()

st.write("✅ Data loaded, dashboard rendering...")

st.title("🏎️ F1 Driver Career Profiles")

# 🔍 Sidebar filters
with st.sidebar:
    st.header("🔢 Filter")
    selected_profile = st.selectbox("Select a career profile", options=["All"] + sorted(df["final_profile"].unique().tolist()))
    min_score = st.slider("Minimum profile score", min_value=1.0, max_value=5.0, value=1.0, step=0.1)

# ⚖️ Apply filters
filtered_df = df.copy()
if selected_profile != "All":
    filtered_df = filtered_df[filtered_df["final_profile"] == selected_profile]

filtered_df = filtered_df[filtered_df["mean_profile_score"] >= min_score]

# 📊 Show results
st.subheader(f"🔍 Showing {len(filtered_df)} drivers")
st.dataframe(filtered_df.sort_values("mean_profile_score", ascending=False), use_container_width=True)

# 📊 Bar chart of profile distribution
st.subheader("🌍 Distribution by Profile")
profile_counts = df["final_profile"].value_counts().sort_index()
st.bar_chart(profile_counts)

# 🎭 Footer
st.markdown("---")
st.markdown("Created by [Your Name] | F1 ML Project")
