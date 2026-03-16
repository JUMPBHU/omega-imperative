import streamlit as st
import pandas as pd
from omega_imperative import load_themes, validate_and_score, ALLOWED_DOMAINS

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Omega Imperative | Truth Engine", page_icon="👁️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    h1, h2, h3 { color: #00FF00 !important; font-family: monospace;}
    .stDataFrame { border: 1px solid #333333; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("👁️ THE OMEGA IMPERATIVE")
st.markdown("**Cryptographically Validated Ontological Architecture (v8.1)**")
st.markdown("We process ancient texts and eliminate AI hallucination using strict primary-source provenance and mathematical bias scoring. Zero theater. Just truth.")

# --- RUN THE ENGINE ---
@st.cache_data
def fetch_data():
    themes = load_themes()
    validated, failures = validate_and_score(themes)
    return validated, failures

validated, failures = fetch_data()

# --- METRICS ---
st.divider()
col1, col2, col3 = st.columns(3)
col1.metric("Total Themes Validated", len(validated))
col2.metric("Failed Validation (Anomalies)", len(failures))
if validated:
    avg_bias = sum(t["bias_score"] for t in validated) / len(validated)
    col3.metric("Average System Bias", f"{avg_bias:.2f}")

# --- CORRELATION MATRIX ---
st.subheader("TEXT CORRELATION MAP")
if validated:
    traditions = list(ALLOWED_DOMAINS.keys())
    matrix_data = []
    
    for th in validated:
        row = {"Theme": th.get("theme_name", "Unknown")}
        for trad in traditions:
            # Check if there is a valid connection for this tradition
            match = any(c.get("tradition_id") == trad for c in th.get("tradition_connections", []))
            row[trad] = "●" if match else "○"
        matrix_data.append(row)
        
    df_matrix = pd.DataFrame(matrix_data)
    st.dataframe(df_matrix, use_container_width=True, hide_index=True)

# --- PAYWALL / MONETIZATION ---
st.divider()
st.subheader("🔓 UNLOCK THE FULL DATABASE")
st.markdown("Download the complete, hyper-validated `omega_export.csv` containing all cross-referenced nodes, verbatim quotes, explicit matches, and bias scores.")

# Replace with your actual Stripe Payment Link
STRIPE_LINK = "https://buy.stripe.com/test_your_link_here"
st.markdown(f'<a href="{STRIPE_LINK}" target="_blank"><button style="width:100%; padding:15px; background-color:#00FF00; color:#000000; border:none; border-radius:5px; font-size:18px; font-weight:bold; cursor:pointer;">Pay $19.00 to Download CSV Vault</button></a>', unsafe_allow_html=True)