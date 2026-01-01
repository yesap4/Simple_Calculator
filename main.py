# Import Module
import streamlit as st

# Page Header
st.set_page_config('Simple Calculator')

# Page Title

st.title('Simple Calculator')

# Description
st.info('Enter Your First Number and Second Number, add select an operation. Get The Results')


# Taking Input

first_num = st.number_input('Enter Your First Number: ',min_value=0)

sec_num = st.number_input('Enter Your Second Number: ',min_value=0)

# Operation Option

operation = st.selectbox('Select An Operation',['+','-','*','/'])

# Checking Which operation is selected and what happens

if operation == '+':
    result = first_num + sec_num
    st.success(f'The Sum of {first_num} and {sec_num} is = {result}')

elif operation == '-':
    result = first_num - sec_num
    st.success(f'The difference between {sec_num} and {first_num} is  = {result} ')    
elif operation == '*':
    result = first_num * sec_num
    st.success(f'The Product of {first_num} and {sec_num} is = {result}')
elif operation == '/': # The result is in decimal to avoid it we use floor division (//)
    result = first_num // sec_num
    st.success(f'The Quotient = {result}')


# Thanks 