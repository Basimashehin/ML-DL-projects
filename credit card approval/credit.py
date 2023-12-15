import streamlit as st
import pandas as pd
import pickle


st.title('credit card approval')

# Load your saved model


data = pickle.load(open(r'C:\Users\Lenovo\Downloads\model&scaler.pkl','rb') )
model=data['model']
scaler=data['scaler']


# Sidebar with user input
st.sidebar.header('Enter applicant details')

def user_input_features():
    # Add input elements as needed
    Gender=st.sidebar.text_input('Gender', 1)
    Age=st.sidebar.text_input('Age',30.83)
    Debt=st.sidebar.text_input('Debt',0.000)
    Married=st.sidebar.text_input('Married',1)
    BankCustomer=st.sidebar.text_input('BankCustomer',0)
    EducationLevel=st.sidebar.text_input('EducationLevel',12)
    Ethnicity=st.sidebar.text_input('Ethnicity',7)
    YearsEmployed=st.sidebar.text_input('YearsEmployed',1.25)
    PriorDefault=st.sidebar.text_input('PriorDefault', 1)
    Employed=st.sidebar.text_input('Employed',1)
    CreditScore=st.sidebar.text_input('CreditScore', 1)
    DriversLicense=st.sidebar.text_input('DriversLicense',0)
    Citizen=st.sidebar.text_input('Citizen',0)
    ZipCode=st.sidebar.text_input('ZipCode',202.0)
    Income=st.sidebar.text_input('Income',0)

    data = {'Gender':Gender,
            'Age':Age,
            'Debt':Debt,
            'Married':Married,
            'BankCustomer':BankCustomer,
            'EducationLevel':EducationLevel,
            'Ethnicity':Ethnicity,
            'YearsEmployed':YearsEmployed,
            'PriorDefault':PriorDefault,
            'Employed':Employed,
            'CreditScore':CreditScore,
            'DriversLicense':DriversLicense,
            'Citizen':Citizen,
            'ZipCode':ZipCode,
            'Income':Income,
            }
    features = pd.DataFrame(data, index=[0])
    return features
def prediction():

    # Display user input
    st.subheader('Applicant details:')
    st.write(df)

    # # Make predictions
    prediction = model.predict(scaler.transform(df))
    # # Display prediction
    st.subheader('Status:')
    st.write('The approval status is:')
    if(prediction==1):
        st.write('Approved')
    else:
        st.write('Rejected')
    
   
df = user_input_features()
if st.button("check approval"):
     prediction()
    
   