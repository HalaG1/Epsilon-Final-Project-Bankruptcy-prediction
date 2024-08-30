import joblib
import pandas as pd
import streamlit as st
import xgboost as xgb


model = joblib.load("model.pkl")


st.set_page_config(page_title="Companies Bankruptcy Prediction")

def predict(year, Current_assets, COGS, EBITDA, Inventory, Net_Income,
            Receivables, Market_value, Total_assets, Longterm_debt, EBIT,
            Gross_Profit, Current_Liabilities, Retained_Earnings,
            Total_Liabilities, Operating_Expenses, Equity, Current_Ratio):
    
    row_to_predict = [[
        year, Current_assets, COGS, EBITDA, Inventory, Net_Income,
        Receivables, Market_value, Total_assets, Longterm_debt, EBIT,
        Gross_Profit, Current_Liabilities, Retained_Earnings,
        Total_Liabilities, Operating_Expenses, Equity, Current_Ratio
    ]]
    d_test = pd.DataFrame(row_to_predict, columns=model.feature_names_in_)
    
    
    pred = model.predict(d_test)
    return int(pred[0])

def Home():
    
    st.title("Companies Bankruptcy Prediction")
    st.image("https://fashionangelwarrior.com/wp-content/uploads/2019/02/shutterstock_423291892.jpg", width=400)
    st.header("Alive or Failed?")
    st.subheader("Test Your Company")


def Inputs():
    
    st.title("Start Prediction")
    year = st.number_input("Year", min_value=1999)
    Current_assets = st.number_input("Current Assets")
    COGS = st.number_input("COGS")
    EBITDA = st.number_input("EBITDA")
    Inventory = st.number_input("Inventory")
    Net_Income = st.number_input("Net Income")
    Receivables = st.number_input("Receivables")
    Market_value = st.number_input("Market Value")
    Total_assets = st.number_input("Total Assets")
    Longterm_debt = st.number_input("Long-term Debt")
    EBIT = st.number_input("EBIT")
    Gross_Profit = st.number_input("Gross Profit")
    Current_Liabilities = st.number_input("Current Liabilities")
    Retained_Earnings = st.number_input("Retained Earnings")
    Total_Liabilities = st.number_input("Total Liabilities")
    Operating_Expenses = st.number_input("Operating Expenses")
    Equity = st.number_input("Equity")
    Current_Ratio = st.number_input("Current Ratio")
    
    if st.button("Predict"):
        
        result = predict(year, Current_assets, COGS, EBITDA, Inventory, Net_Income,
                         Receivables, Market_value, Total_assets, Longterm_debt, EBIT,
                         Gross_Profit, Current_Liabilities, Retained_Earnings,
                         Total_Liabilities, Operating_Expenses, Equity, Current_Ratio)
        
       
        st.session_state.result = result
        

def Result():
    
    st.title("Result")
    st.markdown("1 = Alive, 0 = Failed") 
    
    if 'result' in st.session_state:
        st.markdown(f"The Company's status: **{st.session_state.result}**")
    else:
        st.markdown("No result to display yet.")
    
   

page = st.sidebar.selectbox("Select page", ["Home", "Predict"])
st.session_state.page = page


if page == 'Home':
    Home()
elif page == "Predict":
    Inputs()
    Result()

    


    