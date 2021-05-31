import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("placement.csv")
x = df[['ssc_p', 'hsc_p', 'degree_p', 'etest_p', 'mba_p', 'M',
        'Central', 'Central', 'Arts', 'Commerce', 'Science', 'Comm&Mgmt',
        'Sci&Tech', 'worked_yes', 'Mkt&HR']]
y = df['Placed']
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, train_size=0.8)
Model = DecisionTreeClassifier()
Model.fit(X_train, Y_train)


def prediction(ssc_p, hsc_p, degree_p, etest_p, mba_p, M,
               Central_s, Central_h, Arts, Commerce, Science, Comm_and_Mgmt,
               Sci_and_Tech, worked_yes, Mkt_and_HR):
    pre = Model.predict([[ssc_p, hsc_p, degree_p, etest_p, mba_p, M,
                          Central_s, Central_h, Arts, Commerce, Science, Comm_and_Mgmt,
                          Sci_and_Tech, worked_yes, Mkt_and_HR]])
    return pre


st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://i.gifer.com/76YS.gif")
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: white;'>XYZ COMPANY</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>PLACEMENT APP</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>FIL THIS FORM</h3>", unsafe_allow_html=True)
M = 0
ssc_Central = 0
hsc_Central = 0
art = 0
science = 0
commerce = 0
sci_tech = 0
comm_man = 0
work = 0
Mark_HR = 0
gender = st.radio("Gender", ("Male", "Female"))
if gender == "Male":
    M = 1
elif gender == "Female":
    M = 0
st.write("Senior Secondary Certificate info")
col1, col2, col6 = st.beta_columns(3)
ssc_p = col6.text_input("SSC PERCENTAGE", 91.5)
try:
    ssc_p = float(ssc_p)
except ValueError as e:
    col6.error("Invalid input")

ssc_board = col1.radio("SSC BOARD", ("Central", "Other"))
if ssc_board == "Central":
    ssc_Central = 1
elif ssc_board == 'Other':
    ssc_Central = 0
st.write("Higher Secondary Certificate Information")
col3, col4, col5 = st.beta_columns(3)
hsc_b = col3.radio("HSC Board", ("Central", "Other"))
if hsc_b == 'Central':
    hsc_Central = 1
elif hsc_b == 'Other':
    hsc_Central = 0
hsc_subject = col4.radio("HSC Subject ", ("Science", "Commerce", "Arts"))
if hsc_subject == "Science":
    science = 1
    commerce = 0
    art = 0
elif hsc_subject == 'Commerce':
    science = 0
    commerce = 0
    art = 0
elif hsc_subject == 'Arts':
    science = 0
    commerce = 0
    art = 1
hsc_p = col5.text_input("HSC Percentage", 91.3)
try:
    hsc_p = float(hsc_p)
except ValueError as e:
    col5.error("Invalid input")

st.write("Degree Information")
col7, col8, col9 = st.beta_columns(3)
degree_t = col7.radio("Degree at", ("Science & Tech", "Commerce & Management", "Others"))
if degree_t == 'Science & Tech':
    sci_tech = 1
    comm_man = 0
elif degree_t == "Commerce & Management":
    sci_tech = 1
    comm_man = 0
elif degree_t == "Others":
    sci_tech = 0
    comm_man = 0
degree_p = col9.text_input("Degree Percentage", '91.9')
try:
    degree_p = float(degree_p)
except ValueError as e:
    col9.error("Invalid input")
col10, col11, col12 = st.beta_columns(3)
workex = col10.radio("Work Experience ", ("YES", "No"))
if workex == 'YES':
    work = 1
elif workex == "No":
    work = 0
e_test = col12.text_input("Entrance Exam Percentage", 90.2)
try:
    e_test = float(e_test)
except ValueError as e:
    col12.error("Invalid Input")
st.write("Specialization")
col13, col14, col15 = st.beta_columns(3)
Specialization = col13.radio("Course", ("Marketing and HR", "Marketing and Finances"))
if Specialization == "Marketing and HR":
    Mark_HR = 1
elif Specialization == "Marketing and Finances":
    Mark_HR = 0
mba_p = col15.text_input("MBA Percentage", 98.7)
try:
    mba_p = float(mba_p)
except ValueError as e:
    col15.error("Invalid Input")
col16, col17, col18 = st.beta_columns(3)
if col17.button("Submit"):
    predict = prediction(ssc_p, hsc_p, degree_p, e_test, mba_p, M, ssc_Central, hsc_Central, art, commerce,
                         science, comm_man, sci_tech, work, Mark_HR)
    if predict == [0]:
        st.error("less chance for placement")
    elif predict == [1]:
        st.success("have higher chance to get placement")
    else:
        st.error("Wrong input")
