import re
import streamlit as st
#page styling
st.set_page_config(page_title="Password Strenght Meter",layout="centered")

#custom css
st.markdown("""
<style>
        .main {text-align: center;}
        .stTextInput {widht: 60% !important; margin:auto;}
        .stButton button {widht:50%; background-color: blue; color:white; font-size:18px;}
        .stButton button:hover {background-color: red; color:white;}
</style>
""", unsafe_allow_html=True)


#page title and description
st.title("Password Strenght Generator")
st.write("Enter your password below to check its security level.")

#Function to check password strenght
def pass_strengh_check(password):
    score = 0
    feedback = []

    if len(password)>=8:
        score+=1 #increased score by 1
    else:
        feedback.append("Password should be **atleast 8 character long**")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score +=1
    else:
        feedback.append("Password should include **both uppercase (A-Z) and lowercase (a-z) letters**")

    if re.search(r"\d",password):
        score+=1
    else:
        feedback.append("Password should include **At least one Numbers (0-9)**")

   #special Characters
    if re.search(r"[!@#$%^&*]",password):
        score +=1
    else:
        feedback.append("Include **Atleast one special character(!@#$%^&*)**")

  #display password Strenght
    if score == 4:
        st.success("**Strong password** - your password is secure")
    elif score == 3:
        st.info("**Moderate password** - consider improving security by adding more feature")
    else:
        st.error("**Weak Password** - follow the suggestion below to strengh it")

   #Feedback
    if feedback:
      with st.expander("**Improve your password**"):
        for item in feedback:
            st.write(item)
password = st.text_input("Enter your password:",type="password",help="Ensure your password is Secure")

#button working
if st.button("check strengh"):
    if password:
        pass_strengh_check(password)
    else:
        st.warning("**please enter a password**")

    