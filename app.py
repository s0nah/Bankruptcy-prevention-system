import streamlit as st
import pickle
import pandas as pd



def load_model():
    with open("logistic_regression_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model
# Function to make predictions
def predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk):
    input_data = pd.DataFrame({
        'industrial_risk': [industrial_risk],
        'management_risk': [management_risk],
        'financial_flexibility': [financial_flexibility],
        'credibility': [credibility],
        'competitiveness': [competitiveness],
        'operating_risk': [operating_risk]
    })
    model = load_model()
    prediction = model.predict(input_data)
    return prediction[0]


# Streamlit app
def main():
    # Set page configuration with background color and image
    st.set_page_config(page_title="Bankruptcy Prediction", layout="wide")

    # Custom CSS styling
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://m.economictimes.com/thumb/msid-97241776,width-1200,height-900,resizemode-4,imgsize-820265/bankruptcy.jpg");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)


    # Add a title and description
    st.title('Bankruptcy Prediction')
    st.subheader('Predict if a business will go bankrupt based on input features.')
    st.markdown("---")

    # Add a sidebar for input fields
    st.sidebar.title('Input Features')
    industrial_risk = st.sidebar.slider('Industrial Risk', min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    management_risk = st.sidebar.slider('Management Risk', min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    financial_flexibility = st.sidebar.slider('Financial Flexibility', min_value=0.0, max_value=1.0, value=0.5,
                                              step=0.1)
    credibility = st.sidebar.slider('Credibility', min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    competitiveness = st.sidebar.slider('Competitiveness', min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    operating_risk = st.sidebar.slider('Operating Risk', min_value=0.0, max_value=1.0, value=0.5, step=0.1)

    # Make predictions
    if st.sidebar.button('Predict'):
        prediction = predict_bankruptcy(industrial_risk, management_risk, financial_flexibility, credibility,
                                        competitiveness, operating_risk)
        result = "Bankruptcy" if prediction == 1 else "Non-Bankruptcy"

        # Styling based on prediction result
        if result == "Bankruptcy":
            label_style = 'background-color: rgba(171, 9, 31, 0.2); color: rgb(255, 75, 75); padding: 16px ;border-radius:5px ; font-weight:bold; border: 1px solid rgba(171, 9, 16, 0.2)'
        else:
            label_style = 'background-color: rgba(9, 171, 59, 0.2); color: rgb(33, 195, 84); padding: 16px ;border-radius:5px; font-weight:bold; border: 1px solid rgba(9, 171, 59, 0.2)'

        st.markdown("---")
        st.markdown(f'<p style="{label_style}"> Status : {result}</p>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()