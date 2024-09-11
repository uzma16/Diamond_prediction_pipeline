import pandas as pd
import streamlit as st
from src.pipelines.prediction_pipeline import PredictPipeline, CustomData  # Replace with the actual module name

# Create an instance of the prediction pipeline
prediction_model = PredictPipeline()

# Streamlit App
def main():
    # Set the title of the web app
    st.title("Diamond Price Prediction App 💎")

    # Add a brief description
    st.write("Welcome to the Diamond Price Prediction App! Select your diamond features and click the button to predict the price.")

    # Add input fields for the user to input features
    carat = st.number_input("Carat", min_value=0.2, max_value=5.0, step=0.1, value=1.0)
    cut = st.selectbox("Cut", ["Ideal", "Premium", "Very Good", "Good", "Fair"])
    color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox("Clarity", ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"])

    # Create a CustomData object
    user_input = CustomData(
        carat=carat,
        depth=st.number_input("Depth", min_value=0.0, max_value=100.0, step=0.1, value=0.0),
        table=st.number_input("Table", min_value=0.0, max_value=100.0, step=0.1, value=0.0),
        x=st.number_input("X", min_value=0.0, max_value=100.0, step=0.1, value=0.0),
        y=st.number_input("Y", min_value=0.0, max_value=100.0, step=0.1, value=0.0),
        z=st.number_input("Z", min_value=0.0, max_value=100.0, step=0.1, value=0.0),
        cut=cut,
        color=color,
        clarity=clarity
    )

    # Get data as a DataFrame
    user_df = user_input.get_data_as_dataframe()

    # Add a prediction button
    if st.button("Predict Diamond Price 🚀"):
        # Make prediction using the pipeline
        predicted_price = prediction_model.predict(user_df)

        # Display the prediction
        st.subheader("Predicted Diamond Price:")
        st.write(f"${predicted_price[0]:,.2f}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
