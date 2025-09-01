# Smart-Feedback-Form
Smart feedback form that tags sentiment and keywords from customer comments and lets teams export a CSV for quick insights.

# Smart Feedback Form

A simple Streamlit app to collect customer feedback, auto-tag sentiment (Positive/Neutral/Negative), extract top keywords, and export a CSV for quick business insights.

## Quickstart
1) python -m venv .venv
2) .\.venv\Scripts\activate   (Windows) | source .venv/bin/activate (Mac/Linux)
3) pip install -r requirements.txt
4) streamlit run app.py

## How to use
- Fill name, email, and feedback, then click "Add feedback".
- See sentiment, keywords, and a tiny summary.
- View all entries in the table and click "Download CSV".

## Deploy
- Streamlit Community Cloud → New app → select this repo → main file: app.py.

## Notes
- Uses free, local Python libraries (TextBlob, NLTK) and requires no paid APIs.
