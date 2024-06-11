import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_developer_pro_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data
# Execute

data = load_model()

estimator_model_loaded = data["model"]
le_country = data["labelencoder_co"]
le_education = data["labelencoder_ed"]

# Create prediction page
def show_predicted_page():
    st.title("Softwere Developer Salary Predition")

    st.write("""### We need some information to predict the salary""")

# Create selection box for the user
countries = ("United States",
             "Germany",
             "United Kingdom",
             "India",
             "Canada",
             "France",
             "Brazil",
             "Spain",
             "Netherlands",
             "Australia",
             "Italy",
             "Poland",
             "Sweden",
             "Russian Federation",
             "Switzerland"
)

education = ("Master’s degree", 
             "Bachelor’s degree",
             "Less than a Bachelors",
             "Post Graduate"
)

# select box
country = st.selectbox("Country",countries)
education = st.selectbox("Education Level",education)

experience = st.slider("Years of Experience", 0, 50, 1)

# Create button
ok = st.button("Calculate Salary")    # if we dont click on the button it is false and if click it is true
if ok:
    x = np.array([[country, education, experience]])
    x[:, 0] = labelencoder_co.transform(x[:,0])
    x[:, 1] = labelencoder_ed.transform(x[:,1])
    x = x.astype(float)

    salary = estimator.predict(x)
    st.subheader(f"The Estimated Salary is ${salary[0]:.2f}")



















































