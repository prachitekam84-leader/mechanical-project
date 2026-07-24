# import packages
import streamlit as st # frontend userinterface design
import numpy as np # it is used fo scintific calculation
import pandas as pd # it is used for data analysis

st.title("Hello , streamlit")
st. write(" : streamlit: Tis is your first streamlit app")
st.("lets go started")
st. write("my name is prachi")

 # conditional loic
 name = st. text_input("Enter Your Name")
if st.button ("Greet"):
  st.success(f"Hello{name}")

  #Displaying data and charts
  df = pd.DataFrame(np.random.randn(10, 2), columns=["A","B"])
  st.line_chart(pdf)
  st.bar_chart(pdf)

  #File iuploading and catching
  upload_file = st.file_uploader("Upload File",type="csv")
  if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

    # all the userinterface of 
    # streamlit
    st.header("This is a subheader")
    st.markdown("**Bold**, *Italic*,[Link](https://www.help4code.com/)")
    st.text_area("write your message")
    st.number_input("pick a number" , min_value=0, max_value=100)
    st. slider("choose a range",o,100)
    st.selectbox("select a fruit", ["aplle","banana","mango"])
    st.multiselect("choose toppings", ["cheese","tomato","olives"])
    st.radio("pick one",["option A", "option B"])
    st.checkbox("I agree terms and condition")

    # form code
    with st.form("Login form")
        username = st.text_input("username")
        password = st.text_input("password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
          st.success(f"welcome,{username}")
    #
    #check radio button
    option = st.radio("choose view",["show chart","show table"])
    if option =="show chart":
       st.write("chart would be appear here")
    else:
       st.write("table would be appear here")

    if st.checkbox("show details"):
       st.info("here are more details")

       #Media layout and advance widget
       st.sidebar.title("view chat")
       st.image("https://www.bing.com/images/search?view=detailV2&ccid=%2B1r19HZX&id=A8F08F5CCF5011BF3BAD010154B336875421EA1B&thid=OIP.-1r19HZXrhisw-IlgCtRnAHaFK&mediaurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.fb5af5f47657ae18acc3e225802b519c%3Frik%3DG%252bohVIc2s1QBAQ%26riu%3Dhttp%253a%252f%252fupload.wikimedia.org%252fwikipedia%252fcommons%252f0%252f09%252fWoolly_Mammoth-RBC.jpg%26ehk%3DHqv%252flO2OQ3af5G43vW9jRpH5y6aEgCPPgiSeV9hZgb8%253d%26risl%3D%26pid%3DImgRaw%26r%3D0&exph=1424&expw=2040&q=mammoth&FORM=IRPRST&ck=365CE963D08382299C9A7994BDED2869&selectedIndex=0&itb=0&cw=1145&ch=541&ajaxhist=0&ajaxserp=0")
       st.video("https://www.youtube.com/results?search_query=terracotta+army")