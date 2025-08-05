import streamlit as st

st.set_page_config(page_title="Ramnath's Pivot", layout="centered")

st.title("📈 Ramnath's Pivot Calculator")

# --- Input Section ---
st.header("Enter High and Low Prices")
high = st.number_input("High", min_value=0.0, step=0.1)
low = st.number_input("Low", min_value=0.0, step=0.1)

if high > 0 and low > 0 and high > low:
    diff = high - low
    central_pivot = low + diff / 2
    top_central = high
    bottom_central = low
    R1 = high + (diff / 4)
    R2 = R1 + (diff / 4)
    R3 = R2 + (diff / 4)
    S1 = low - (diff / 4)
    S2 = S1 - (diff / 4)
    S3 = S2 - (diff / 4)

    # --- Output Section ---
    st.subheader("🧮 Pivot Levels")
    st.write(f"**Central Pivot**: {central_pivot:.2f}")
    st.write(f"**Top Central**: {top_central:.2f}")
    st.write(f"**Bottom Central**: {bottom_central:.2f}")
    st.write("---")
    st.write(f"**R1**: {R1:.2f}")
    st.write(f"**R2**: {R2:.2f}")
    st.write(f"**R3**: {R3:.2f}")
    st.write("---")
    st.write(f"**S1**: {S1:.2f}")
    st.write(f"**S2**: {S2:.2f}")
    st.write(f"**S3**: {S3:.2f}")
else:
    st.warning("Please enter valid High > Low to compute pivot levels.")
