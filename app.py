import streamlit as st
import pandas as pd
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

# one-time download (safe to re-run)
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

st.set_page_config(page_title="Smart Feedback Form", page_icon="📝", layout="wide")
st.title("Smart Feedback Form")
st.caption("Collect feedback, auto‑tag sentiment and keywords, and export CSV — no paid APIs.")

# Session data
if "rows" not in st.session_state:
    st.session_state.rows = []

def clean_text(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def analyze(feedback):
    polarity = TextBlob(feedback).sentiment.polarity
    if polarity > 0.2:
        sentiment = "Positive"
    elif polarity < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    words = clean_text(feedback).split()
    sw = set(stopwords.words("english"))
    tokens = [w for w in words if w not in sw and len(w) > 2]
    top = [w for w, c in Counter(tokens).most_common(5)]
    summary = " ".join(top[:3]) if top else ""
    return sentiment, ", ".join(top), summary

with st.form("fb"):
    name = st.text_input("Customer name")
    email = st.text_input("Email")
    feedback = st.text_area("Feedback", height=150, placeholder="Type feedback here...")
    submitted = st.form_submit_button("Add feedback")
    if submitted and feedback.strip():
        sent, keys, summ = analyze(feedback)
        st.session_state.rows.append({
            "name": name, "email": email, "feedback": feedback,
            "sentiment": sent, "keywords": keys, "summary": summ
        })
        st.success(f"Saved with sentiment: {sent}")

st.subheader("Collected feedback")
df = pd.DataFrame(st.session_state.rows)
if not df.empty:
    st.dataframe(df, use_container_width=True)
    st.download_button("Download CSV", df.to_csv(index=False).encode("utf-8"), "feedback.csv", "text/csv")
else:
    st.info("No feedback yet. Add one above.")

with st.expander("How this helps businesses"):
    st.write("- Quickly see which comments are positive or negative.")
    st.write("- Spot common issues via keywords.")
    st.write("- Export CSV and share with support or product teams.")
