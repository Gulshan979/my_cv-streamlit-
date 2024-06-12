import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
lottie_coding_url = "https://assets9.lottiefiles.com/packages/lf20_J2zX5w.json"  # Example Lottie URL
lottie_welcome_url = "https://assets10.lottiefiles.com/packages/lf20_5g4lb1kv.json"
lottie_coding = load_lottieurl(lottie_coding_url)
lottie_welcome = load_lottieurl(lottie_welcome_url)

# CSS for background and styling
st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(90deg, #74ebd5 0%, #ACB6E5 100%);
        color: #333333;
    }
    .title {
        font-size:50px;
        color: #4CAF50;
        text-align: center;
    }
    .subtitle {
        font-size:30px;
        color: #008CBA;
        text-align: center;
    }
    .content {
        font-size:20px;
        color: #333333;
    }
    .academic-table {
        margin: 0 auto;
        border: 1px solid #ddd;
        border-collapse: collapse;
        width: 80%;
        background-color: #ffffff;
    }
    .academic-table th, .academic-table td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    .academic-table th {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">Gulshan Kumar</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Data Scientist / Data Analyst / ML Engineer / PowerBI Developer</div>', unsafe_allow_html=True)

# Add welcome animation
if lottie_welcome:
    st_lottie(lottie_welcome, height=300, key="welcome")

# Contact Information
st.markdown('**Email:** gulshankumaransh979@gmail.com')
st.markdown('**GitHub:** [Gulshan979](https://github.com/Gulshan979)')
st.markdown('**LinkedIn:** [Gulshan Kumar](https://www.linkedin.com/in/gulshan-kumar-5936bb182)')
st.markdown('**Phone:** +91-7019782758')

# Academics
st.markdown('## Academics')
st.markdown("""
<table class="academic-table">
  <tr>
    <th>Degree</th>
    <th>Institution</th>
    <th>Year</th>
    <th>CGPA/Marks</th>
  </tr>
  <tr>
    <td>M. Tech (Food Process Engineering)</td>
    <td>Indian Institute of Technology, Kharagpur</td>
    <td>2023</td>
    <td>CGPA: 8.93</td>
  </tr>
  <tr>
    <td>B. Tech (Agricultural Engineering)</td>
    <td>ANGRAU, AP</td>
    <td>2021</td>
    <td>CGPA: 7.67</td>
  </tr>
  <tr>
    <td>Intermediate Examination (BSEB)</td>
    <td>R.B.S College, Hajipur (Bihar)</td>
    <td>2016</td>
    <td>Marks: 70.20%</td>
  </tr>
  <tr>
    <td>Secondary School Examination (CBSE)</td>
    <td>ST. Paul’s High School, Hajipur (Bihar)</td>
    <td>2014</td>
    <td>CGPA: 9.4</td>
  </tr>
</table>
""", unsafe_allow_html=True)

# Work Experience
st.markdown('## Work Experience')
st.markdown("""
**Data Scientist**, Shape My Skills Pvt Ltd, Noida (May’23- Mar’24)
- Developed and implemented machine learning algorithms to personalize learning experiences for thousands of students, resulting in a 20% increase in user engagement.
- Designed predictive models to identify at-risk students, enabling early interventions and improving retention rates by 15%.
- Created and maintained data by performing ETL operations for processing large-scale educational data, enhancing the efficiency of data management by 30%.
- Analyzed user interaction data to uncover insights that informed the redesign of the platform, leading to a 25% increase in user activity.
- Built and maintained dashboards and reports to track KPIs such as student performance, lead conversion rate, trainers record, and student engagement metrics.
- Provided knowledge sessions to various students and working professionals.

**Data Science Intern**, GlobalCert Pte. Ltd., Singapore (Jan’22-Mar’22)
- Time Series Forecasting for Store Item Demand.
- Predicted 3 months of sales for 50 different items in 10 different stores from past 5-year sales data using time series techniques.
- Analyzed Trend, Seasonality, and Noise by decomposing Time Series into their Components.
- Plotted PACF and ACF to determine the best parameters p, d, and q.
- Checked Stationarity Using ADF-test (p=0.036) and Stationarized Time Series by Differencing (d).
- Utilized SMAPE (27%) and MAPE (33%) metrics in AR, MA, ARMA, ARIMA (6,1,1), and SARIMA (6,1,0) time series models.
""")

# Projects
st.markdown('## Projects')
st.markdown("""
**Loan Approval Prediction**, IIT KGP (Aug’21 – Dec’21)
- Predicted the home loan approval for customers based on customer segmentation for a finance company.
- Performed EDA, analyzed various independent features, and log-transformed the features to normalize them.
- Data split into test-train (75:25), model trained on Logistic Regression, Decision Tree, and Random Forest.
- Achieved accuracies of 77%, 72%, and 74%, with best accuracy of 81% for logistic regression after hyperparameter tuning.

**Plant Leaf Disease Detection Using Image Processing and Machine Learning**, IIT KGP (Jan’22 – Apr’22)
- Evaluated four classification models for identifying diseases and providing remedies for diseases in Elephant foot yam and Potato plant leaves.
- Dataset: Yam - 1175 RGB images of three categories, Potato - 1515 RGB images of three classes.
- Features extracted from images to create a dataset, split into training, testing, and validation sets.
- Random Forest achieved highest accuracy at 95%, SVM at 80%, Decision Tree comparable to Random Forest, CNN achieved 97%.

**Dashboard of Stock Market Price Analysis of IOCL for last 5 years using PowerBI and SQL** (May’23-June’23)
- Customized data in SQL and integrated it into PowerBI to perform ETL operations for transforming data.
- Parameters: open price, close price, high price, low price of stock for every single day for 5 years.
- Applied DAX formulas for finding Day Name, Day number, Week Name, Week number, Quarter, and Year.
- Analysis: Found stock price values were higher on Mondays, in July, in the second quarter, and were good until 2019, after which they decreased.
""")

# Skills and Certifications
st.markdown('## Skills and Certifications')
st.markdown("""
**Technical Skills**: Python, Statistics, Machine Learning, Deep Learning, NLP, MySQL, Tableau, PowerBI, Performance Management, MS Office

**Tools & Libraries**: TensorFlow, Keras, nltk, Sklearn, Seaborn, Matplotlib, NumPy, pandas, spacy

**Soft Skills**: Team Management, Adaptability, Problem Solving, Analytical Thinking, Decision-Making Capabilities

**Certifications**:
- Programming For Everybody (Getting started with Python) (Coursera)
- Data Science with Python (Henry Harvin Education)
- Machine Learning (Great Learning)
- Excel skills for Business (Coursera)
- SQL for Data Science (Coursera)
""")

# Positions of Responsibility
st.markdown('## Positions of Responsibility')
st.markdown("""
- **Student Representative**, ANGRAU – Acted as the voice of B. Tech students at the student-teacher council (June’18 – July’21)
- **NSS Volunteer**, ANGRAU – 240+ hours of regular service & leading the special camp in Poondla village (A.P) (July’17 - Feb’20)
- **Class Representative**, IIT KGP (Aug’21- May’23)
- **Senior Core Team Member of Organizing Committee**, Prakriti 2022 (Food Fest), IIT Kharagpur
    - Interviewed 200+ candidates from different institutions for the selection of campus Ambassadors throughout India.
    - Reviewed potential Sponsors and acquired funding of 95000 for the program from 2 major sponsors.
""")



# Achievements and Extracurricular Activities
st.markdown('## Achievements and Extracurricular Activities')
st.markdown("""
- **Data Science Virtual Hackathon Datathon (CoinedOne Technologies)** – 1st Runner up of the 7-day virtual hackathon Datathon by CoinedOne Technologies
- **Golden Badges in Hacker Rank (SQL)**
- **Secured AIR 67 in GATE** – Agricultural Engineering 2021
- **1st rank in exhibition held in college**
- **1st rank in essay competition held on World Food Day**
- **Received certificate of merit for all India essay competition** organized by the United Nations Information Centre for India and Bhutan
""")

# Footer
st.markdown('<div class="subtitle">Thank you for visiting my CV website!</div>', unsafe_allow_html=True)

# Add some animations or interactive elements if needed
st.balloons()


