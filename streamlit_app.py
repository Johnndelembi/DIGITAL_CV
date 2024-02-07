from pathlib import Path
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="DIGITAL CV",
    page_icon=":wave:",
)
a = st.sidebar.selectbox("Menu:", ["Home","Data Projects","Contacts"])

col1, col2 = st.columns(2, gap="small")
tab1, tab2, tab5 = st.tabs(["Home","Data Projects","Contacts"])

#-------HERO SECTION----------

with col1:  
    st.title('MY DIGITAL RESUME/CV')  
    st.image('profile-pic.png', width=200)
    st.markdown("[Email](https://williamjohnie61@gmail.com)")

  
    
with col2:
    st.header("| ***John Ndelembi*** ",":wave:")
    st.write("Junior Data analyst supporting enteprises and companies make data-driven decisions and drive growth ")
    st.text("Follow me and discover my journey")

with tab1:
    tab1.title("***Experience and Qualifications***")
    tab1.text(" >>> 16 months of experience in extracting actionable insights from data")
    tab1.text(" >>> Strong hands on experience in Python and R and STATA")
    tab1.write("This is my current project that i've been working on")
    tab1.video("legends.mp4")
    tab1.caption("My Signature Project")
     

with tab2:
    tab2.header("***DATA SCIENCE PROJECT***")
    tab2.write("I conducted a data science project on survey results data conducted to developers. i developed a model for prediting their avergae salary after extensive model training using the data")
    tab2.subheader("Dataset Introduction")
    tab2.write("I found the data on the internet and i choose the data because it seemed a good type to build my model on and its variables are precise")

    df = pd.read_csv("survey_results_public.csv")
    df = df.rename(columns={"ConvertedComp": "Salary"})
    df = df.drop(columns={'Respondent'})
    df = df[df["Salary"].notnull()]
    
    st.dataframe(df.head(50))

    st.caption("Rows: 64461, Columns: 61")
    
    col3, col4 = st.columns(2, gap='small')

    line_chart = col3.write("A line chart of Salary distribution")
    line_chart = col3.line_chart(df["Salary"].head(60))
    
    bar_chart = col4.write("A bar chart of Salary distribution")
    bar_chart = col4.bar_chart(df["Salary"].head(100))
    
    scatter = col3.write("A scatter plot showing how salary is distributed along the dataset")
    scatter = col3.scatter_chart(df["Salary"].head(60))

    descriptive = col4.write("A descriptive analysis of the data")
    descriptive_data = col4.write(df.describe())

with tab5:
    tab5.header("Contacts")
