# Importing required libraries
import streamlit as st
import  joblib

# Loading the pickle file
model = joblib.load('artifacts/model.pkl')
def main():
    # Streamlit App
    st.title("Water Safety Prediction App")
    st.image("https://cdn.pixabay.com/photo/2015/09/03/18/04/water-921067_960_720.jpg",width=700)
    st.subheader("Please enter the following details to get the prediction")

    # Get input from the user
    aluminum = st.slider("Aluminum", 0.0,100.00)
    ammonia = st.slider("Ammonia", 0.0,100.00)
    arsenic = st.slider("Arsenic", 0.0,100.00)
    barium = st.slider("Barium", 0.0,100.00)
    cadmium = st.slider("Cadmium", 0.0,100.00)
    chloramine = st.slider("Chloramine", 0.0,100.00)
    chromium = st.slider("Chromium", 0.0,100.00)
    copper = st.slider("Copper", 0.0,100.00)
    fluoride = st.slider("Fluoride", 0.0,100.00)
    bacteria = st.slider("Bacteria", 0.0,100.00)
    viruses = st.slider("Viruses", 0.0,100.00)
    lead = st.slider("Lead", 0.0,100.00)
    nitrates = st.slider("Nitrates", 0.0,100.00)
    nitrites = st.slider("Nitrites", 0.0,100.00)
    mercury = st.slider("Mercury", 0.0,100.00)
    perchlorate = st.slider("Perchlorate", 0.0,100.00)
    radium = st.slider("Radium", 0.0,100.00)
    selenium = st.slider("Selenium", 0.0,100.00)
    silver = st.slider("Silver", 0.0,100.00)
    uranium = st.slider("Uranium", 0.0,100.00)

    # Create a predict button
    predict_btn = st.button("Predict")

# Create a function to predict whether the water is safe or not
    if predict_btn:
        Model=model
        inputs = [aluminum, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper, fluoride, bacteria, viruses, lead, nitrates, nitrites, mercury, perchlorate, radium, selenium, silver, uranium]
        inputs = [float(i) for i in inputs]
        prediction = Model.predict([inputs])

        if prediction == 0:
            st.success("The water is **safe**")
        else:
            st.error("The water is **not safe**")

if __name__ == '__main__':
    main()