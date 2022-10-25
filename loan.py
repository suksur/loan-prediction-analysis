import pickle
import streamlit as st
import numpy as np
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married,Education ,SelfEmployed ,dependent,Loan_Amount_Term_Log,ApplicantIncomeLog, LoanAmountLog,Total_Income_Log, Property_Area,Credit_History):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    
 

    # ApplicantIncomeLog= np.log([ApplicantIncome]+1)
    # LoanAmountLog= np.log([LoanAmount]+1)
    # Loan_Amount_Term_Log = np.log([Loan_Amount_Term]+1)
    # Total_Income_Log=np.log(Total_Income+1)
   

    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married,Education ,SelfEmployed ,dependent,Loan_Amount_Term_Log,ApplicantIncomeLog, LoanAmountLog,Total_Income_Log, Property_Area,Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:red;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.radio('Gender',("Male","Female"))
    Married = st.radio('Marital Status',("Unmarried","Married")) 
    Education = st.radio('Education Status',("Graduate","Non-Graduate")) 
    SelfEmployed = st.radio('Employment Status',("Self Employed","Non-Employed")) 
    dependent=st.selectbox('No:of dependents',("0","1","2","3"))
    ApplicantIncome = st.number_input("Applicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Loan_Amount_Term = st.number_input("Total loan amount term")
    Credit_History = st.slider('Credit_History',0.0,1.0)
    Property_Area	= st.selectbox('Property_Area',("urban","Semi Urban","rural"))
    TotalIncome = st.number_input("Total Income")
    
    result =""
    
    def check_urban(x):
        if x == "Urban":
            return 2
        elif x == "Semi Urban":
            return 1
        else :
            return 0

      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        

        result = prediction(Gender, Married,dependent,Education == "Graduate" ,SelfEmployed=="Self Employed" ,Credit_History, check_urban(Property_Area),  np.log(ApplicantIncome + 1, dtype="float64") ,np.log(LoanAmount + 1, dtype="float64") ,np.log(Loan_Amount_Term+1, dtype="float64"), np.log(TotalIncome+1, dtype="float64")) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()
