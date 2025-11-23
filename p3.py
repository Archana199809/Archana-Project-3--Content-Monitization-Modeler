import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn 
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


# Initialize StandardScaler
with open("C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Project 3-Youtube/scaler.pkl", 'rb') as file:
    ss = joblib.load(file)

# Load the model from file
with open("C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Project 3-Youtube/linearregression_model.pkl", 'rb') as file:
    model = joblib.load(file)
# Load the feature columns 
with open("Project 3-Youtube/feature_col.pkl", 'rb') as file:
    feature_col = joblib.load(file)
    print(feature_col)
    # Load the categoric columns 
with open("C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Project 3-Youtube/categoric_col.pkl", 'rb') as file:
    categoric_cols = joblib.load(file)
    # Load the encoder  
with open("C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Project 3-Youtube/encoder.pkl", 'rb') as file:
   encoder = joblib.load(file)

st.sidebar.title('Navigation')
selection = st.sidebar.radio('Go to', ['Home','Estimate Revenue'])
if selection == 'Home':
    st.title(' ▶️YouTube Ad Revenue Estimation')
    st.image("C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Project 3-Youtube/YouTube ad revenue.jpeg")
    st.write("""This application leverages machine learning techniques to estimate the youtube ad revenue based on various features from given datasets. By analyzing datasets features, our model builds to estimate the revenue . Builded a Linear Regression model that can accurately 
             estimate YouTube ad revenue for individual videos based on various performance and contextual features, and 
             implemented the results in this Streamlit web application.""")
    

 
elif selection == 'Estimate Revenue':
    st.title('Estimate Revenue')
    st.subheader("Enter Feature Values")
    # Respective Inputs from user to predict revenue

    views = st.number_input("Views", min_value=0, step=1000, value=10000)
    likes = st.number_input("Likes", min_value=0, step=10, value=500)
    comments = st.number_input("Comments", min_value=0, step=5, value=50)
    watch_time_minutes = st.number_input("Watch Time (minutes)", min_value=0.0, step=10.0, value=500.0)
    video_length_minutes = st.number_input("Video Length (minutes)", min_value=0.1, step=0.1, value=10.0)
    subscribers = st.number_input("Subscribers", min_value=0, step=100, value=10000)
    engagement_rate =(likes+comments)/subscribers
    category = st.selectbox("📂 Select Category", ['Entertainment', 'Gaming', 'Education', 'Music', 'Tech'])
    device = st.selectbox("📱 Select Device", ['Mobile', 'Desktop', 'TV', 'Tablet'])
    country = st.selectbox("🌍 Select Country", ['US', 'UK', 'CA', 'IN', 'AU'])
    
    category_df= pd.DataFrame({'category':[category],'device':[device],'country':[country]})

    if st.button('$ ESTIMATE REVENUE'):
    
        user_inputs =pd.DataFrame({'views':[views],'likes':[likes],'comments':[comments],'watch_time_minutes':[watch_time_minutes],
                                      'video_length_minutes':[video_length_minutes],'subscribers':[subscribers],'engagement_rate':[engagement_rate]})
        
        encoded_category = encoder.transform(category_df[categoric_cols]) # Encoder is a loaded model of OneHotEncoding()
        feature_names = encoder.get_feature_names_out(categoric_cols)
        user_inputs[feature_names] = pd.DataFrame(encoded_category,columns=feature_names)                                       

        st.subheader("Processed Input Data (ready for model):")
        st.write(user_inputs)

            
        # Align with model features
        scaler=ss.transform(user_inputs)
        prediction = model.predict(scaler)
        print("prediction",type(prediction))
        st.success(f"Predicted Ad Revenue: **${prediction[0]:,.2f}**",icon="✅")


            
