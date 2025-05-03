import streamlit as st
# load dataset
data_path = os.path.join(base_dir, "data", "processed", "combined_data.csv")
data_df = pd.read_csv(data_path)

flight_details = {
        "origin": None,
        "destination": None,
        "departure_time": None,
    }

col1, col2 = st.columns(2)

with col1:
    origin = st.selectbox("Origin Airport", ["Select..."])
    destination = st.selectbox("Destination Airport", ["Select..."])
with col2:
    departure_time = st.number_input("Departure Time (e.g., 1430 for 2:30 PM)", min_value=0, max_value=2359, step=5)
    
    if  st.button("Predict Incident Probability"):
        st.warning("Prediction logic not implemented.")
        
with st.form(key="user_flight_details"):
    flight_details["origin"] = st.selectbox(label="Enter the departure airport: ", options=data_df['origin'].unique(), placeholder='LGA')
    flight_details["destination"] = st.selectbox(label="Enter the destination airport: ", options=data_df['destination'].unique(), placeholder='ORF')
    flight_details["departure_time"] = st.time_input("Enter your departure time (use military time): ",)

    submit = st.form_submit_button("Submit")

if submit:
    if not all(flight_details.values()):
        st.warning("Please fill in all of the fields")
    else:
        # Convert departure_time (which is a time object) to string
        df = pd.DataFrame({
            "origin": [flight_details["origin"]],
            "destination": [flight_details["destination"]],
            "departure_time": [flight_details["departure_time"].strftime("%H:%M")]
        })
        # create and encode route
        route_frequency = data_df['origin'] + '_' + data_df['destination']
        route_frequency = route_frequency.value_counts().to_dict()
        df['route'] = df['origin'] + '_' + df['destination']
        df['route_encoded'] = df['route'].map(route_frequency)
        df['route_encoded'].fillna(0, inplace=True)
        df.drop(columns=['route'], inplace=True)
        print(df)

        # create and encode time-sin and time-cosine
        def hhmm_to_minutes(hhmm):
            hours, minutes = map(int, hhmm.split(":"))
            return hours * 60 + minutes  
        
        df['Time'] = df['departure_time'].apply(hhmm_to_minutes)
        df['time_sin'] = np.sin(2 * np.pi * df['Time'] / 1440)  # 1440 minutes in a day
        df['time_cos'] = np.cos(2 * np.pi * df['Time'] / 1440)
        
        df = df[['time_sin', 'time_cos', 'route_encoded']]
        
        # Load the trained model
        model_path = os.path.join(base_dir, "models", "model.pkl")
        

        if not os.path.exists(model_path):
            st.error(f"Model file not found: {model_path}")
            st.stop()

        with open(model_path, "rb") as f:
            model = pickle.load(f)
        
        # make the predictions
        probability = model.predict_proba(df)
        percent_probability = probability[:, 1] * 100
        print(percent_probability)

        # Display predictions
        st.write(f"The probability of your plane crashing is {percent_probability.item():.2f}%")