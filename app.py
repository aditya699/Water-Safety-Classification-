# Importing required libraries
import streamlit as st
import  joblib

# Loading the pickle file

model = joblib.load('artifacts/model.pkl')
def main():
    # Streamlit App
    st.title("Water Safety Prediction Application")
    st.image("https://cdn.pixabay.com/photo/2015/09/03/18/04/water-921067_960_720.jpg",width=700)
    st.subheader("Enter the following details to get the prediction")

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


# Create a function to predict whether the water is safe or not
    if st.button("Check if your water is safe or not", key='predict'):
        try:
            Model = model  #get_model()
            prediction = Model.predict([[aluminum,ammonia,arsenic,barium,cadmium,chloramine,chromium,copper,fluoride,bacteria,viruses,lead,nitrates,nitrites,mercury,perchlorate,radium,selenium,silver,uranium]])
            output =prediction
            if output<0:
                st.warning("Some error is there !!")
            if output==0:
                st.warning("Your Water is not Safe to drink")
            else:
                st.success("Your Water is Safe to drink")
           
        except:
            st.warning("Opps!! Something went wrong\nTry again")


if __name__ == '__main__':
    main()
