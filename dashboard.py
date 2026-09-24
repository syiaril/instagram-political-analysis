import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Instagram Political Comment Analysis", layout="wide")

st.title("Instagram Political Comment Analysis")

# Load data
@st.cache_data
def load_data():
    processed_path = os.path.join("data", "processed", "comments_processed.csv")
    if not os.path.exists(processed_path):
        return pd.DataFrame()
    return pd.read_csv(processed_path)

df = load_data()

if df.empty:
    st.warning("No processed data found. Please run the main pipeline first.")
else:
    # Sidebar Filters
    st.sidebar.header("Filters")
    selected_sentiment = st.sidebar.multiselect("Sentiment", df['sentiment'].unique(), default=["negative"])
    
    # Filtering Data
    filtered_df = df[df['sentiment'].isin(selected_sentiment)]
    
    total_comments = len(df)
    negative_comments = len(df[df['sentiment'] == 'negative'])
    negative_rate = (negative_comments / total_comments * 100) if total_comments > 0 else 0
    
    # Top Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Comments", total_comments)
    col2.metric("Negative Comments", negative_comments)
    col3.metric("Negative Rate", f"{negative_rate:.1f}%")
    
    st.divider()
    
    if 'negative' in selected_sentiment and negative_comments > 0:
        st.subheader("Composition of Negative Comments")
        
        # Isolate negative comments for the pie chart
        neg_df = df[df['sentiment'] == 'negative']
        classification_counts = neg_df['classification'].value_counts().reset_index()
        classification_counts.columns = ['Classification', 'Count']
        
        # Pie Chart
        fig = px.pie(
            classification_counts, 
            values='Count', 
            names='Classification', 
            title="Account Classification Distribution",
            color='Classification',
            color_discrete_map={
                "ANIES": "#1f77b4",
                "NEUTRAL": "#7f7f7f",
                "PRIVATE": "#d62728"
            }
        )
        st.plotly_chart(fig, use_container_width=True)
        
    st.divider()
    st.subheader("Sample Data")
    st.dataframe(filtered_df[['username', 'comment_text', 'sentiment', 'classification', 'classification_reason']].head(50))
