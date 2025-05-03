import configuration as config 
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath("app.py")))

# ---------------------------
# PAGE CONFIG & BANNER IMAGE
# ---------------------------
# Set page config
st.set_page_config(
    page_title="Flight Incident Predictor",
    page_icon="✈️",
    layout="wide"
)
# ---------------------------
# MAIN APP
# ---------------------------
def main():    
    #st.title("✈️ Flight Incident Predictor", anchor="center")
    #st.markdown('<h1 class="centered-title">✈️ Flight Incident Predictor</h1>', unsafe_allow_html=True)
    #st.markdown('<p class="centered-text">This app predicts the likelihood of a flight incident based on origin, destination, and departure time information</p>', unsafe_allow_html=True)
    
    # Create two columns for parallel display
    col1, col2, col3 = st.columns([1,2,1])

    # Display GIFs in respective columns
    with col1:
        st.image(os.path.join(os.path.dirname(__file__), "static", "take_off_1.gif"), use_container_width=True)
    with col2:
        # Add custom CSS with more styling options
        st.markdown("""
            <style>
            .centered-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: #1E88E5;
            margin-bottom: 1rem;
            padding: 1rem;
            border-bottom: 2px solid #1E88E5;
            }
            </style>
            """, unsafe_allow_html=True)
        # Use the styled title
        st.markdown('<h1 class="centered-title">✈️ Flight Incident Predictor</h1>', unsafe_allow_html=True) 
        
        st.markdown("""
            <style>
            .centered-text {
            text-align: center;
            font-size: 2.5rem;
            font-weight: plain;
            color: white;
            }
            </style>
            """, unsafe_allow_html=True)
        # Use the styled title
        st.markdown('<p class="centered-text">This app predicts the likelihood of a flight incident based on origin, destination, and departure time information</p>', unsafe_allow_html=True)
    with col3:
        st.image(os.path.join(os.path.dirname(__file__), "static", "crash_1.gif"), use_container_width=True)
    st.divider()
    # ---------------------------
    # TABS
    # ---------------------------
    tab1, tab2, tab3 = st.tabs(["Incident Predictor", "Model Performance", "Data Exploration"])

    # TAB 1: Incident Predictor UI Skeleton
    with tab1:
        st.header("Predict Flight Incident Risk")

        col1, col2 = st.columns(2)

        with col1:
            origin = st.selectbox("Origin Airport", ["Select..."])
            destination = st.selectbox("Destination Airport", ["Select..."])

        with col2:
            departure_time = st.number_input("Departure Time (e.g., 1430 for 2:30 PM)", min_value=0, max_value=2359, step=5)

        if st.button("Predict Incident Probability"):
            st.warning("Prediction logic not implemented.")
    # TAB 2: Model Performance UI Skeleton
    with tab2:
        st.header("Model Performance Metrics")
        st.info("Model evaluation metrics and visualizations will appear here.")

    # TAB 3: Data Exploration UI Skeleton
    with tab3:
        st.header("Data Exploration")
        st.info("Raw data views, visualizations, and correlation plots will be added here.")


if __name__ == "__main__":
    main()