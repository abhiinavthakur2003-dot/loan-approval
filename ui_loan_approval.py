import streamlit as st
import joblib

model=joblib.load('loanaprv.joblib')



st.set_page_config(page_title = "Loan", page_icon = "💰", layout = "centered")

st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1689028294160-e78a88abcb19?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjN8fHVpJTIwYmFja2dyb3VuZHxlbnwwfHwwfHx8MA%3D%3D");
    background-size: cover;
    background-position: center;
}
</style>
""", unsafe_allow_html=True)



st.title('Loan Approval 🏦💰')

st.divider()
st.image('https://www.olyv.co.in/wp-content/uploads/freepik__apply-all-confirmed-edits-to-the-provided-horizont__1892-1300x867.jpeg',width=1000)
st.divider()
st.markdown("""
### 🏦 About this App
Enter your financial details below and instantly find out if your loan will be **Approved ✅** or **Rejected ❌** using a Machine Learning model.
""")
st.divider()
name=st.text_input('What is your name?')
if name:
    st.subheader(f'Hey {name} , fill out the details below 📝')
    

    col1=st.selectbox('Number of dependencies',[0,1,2,3,4,5])
    col2_input=st.selectbox('Self Employeed?',['Yes','No'])
    col2=1 if col2_input=='Yes' else 0
    try:
        col3str=st.text_input('Annual Income',placeholder='e.g. 500000')
        col3=int(col3str or 0)


        col4str=st.text_input('Loan Amount',placeholder='e.g. 100000')
        col4=int(col4str or 0)

        col5=st.selectbox('Loan Term',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        col6str=st.text_input('CIBIL Score',placeholder='e.g. 750')
        col6=int(col6str or 0)
    
        col7str=st.text_input('Residential Assets Value',placeholder='e.g. 200000')
        col7=int(col7str or 0)

        col8str=st.text_input('Commercial Assets Value',placeholder='e.g. 100000')
        col8=int(col8str or 0)

        col9str=st.text_input('Luxury Assets Value',placeholder='e.g. 50000')
        col9=int(col9str or 0)

        col10str=st.text_input('Bank Asset Value',placeholder='e.g. 80000')
        col10=int(col10str or 0)
    except:
        st.error('Do not leave empty⚠️')

    st.divider()
    approval=st.button('Check Status⁉️')
    try:
        if approval:
            result=model.predict([[col1,col2,col3,col4,col5,col6,col7,col8,col9,col10]])
            if result[0]=='Approved':
                st.balloons()
                st.success('Loan Approved✅')
                st.image('https://img.magnific.com/free-photo/loan-approved-application-form-concept_53876-127383.jpg?semt=ais_hybrid&w=740&q=80',width=1000)

            else:
                st.error('Loan Rejected❌')
                st.image('https://images.cnbctv18.com/wp-content/uploads/2019/08/personal-loan-application-declined.jpg',width=1000)
    except:
        st.error('Fill the details above ⬆️')