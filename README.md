Heart Disease Diagnostic Analysis


Project Overview
Health is real wealth, and the pandemic has highlighted the importance of being prepared for health crises. This project aims to analyze heart disease diagnostic data to better understand the factors contributing to heart disease and prepare for future health challenges.

Technologies Used
Python 3
Pandas
Seaborn
Matplotlib
Tableau



The dataset contains various attributes related to heart disease diagnostics, including:

age
sex
cp (chest pain type)
trestbps (resting blood pressure)
chol (serum cholesterol)
fbs (fasting blood sugar)
restecg (resting electrocardiographic results)
thalach (maximum heart rate achieved)
exang (exercise-induced angina)
oldpeak (ST depression induced by exercise)
slope (the slope of the peak exercise ST segment)
ca (number of major vessels colored by fluoroscopy)
thal (thalassemia)
target (1 indicates presence of heart disease, 0 indicates absence)
ETL Process
The ETL (Extract, Transform, Load) process involves:

Extracting data from the heart disease diagnostic database.
Transforming data by cleaning and preprocessing.
Loading the data into a format suitable for analysis.
Exploratory Data Analysis (EDA)
EDA is performed using Python to extract insights from the data. Key metrics and factors are identified, and meaningful relationships between attributes are visualized.







Tableau Dashboard
An interactive dashboard is created in Tableau to visualize key insights from the data.
https://public.tableau.com/views/HeartDiseaseTrendsandRiskFactorsVisualization/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Key Visualizations:
Summary Metrics (KPIs): Total number of patients, percentage with heart disease, average age.
Heart Disease Prevalence by Gender: Bar chart showing counts of heart disease by gender.
Age Distribution: Histogram showing the distribution of age.
Heart Disease Prevalence by Chest Pain Type: Bar chart showing counts of heart disease by chest pain type.
Age vs. Maximum Heart Rate Achieved: Scatter plot showing the relationship between age and maximum heart rate.
Correlation Matrix: Heatmap showing correlations between different attributes.
Cholesterol Levels by Age Group: Line chart showing average cholesterol levels by age group.
Conclusion
This project provides a comprehensive analysis of heart disease diagnostic data, highlighting key factors and relationships. The Tableau dashboard offers an interactive way to explore the data and gain insights for better health preparedness.

How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/heart-disease-diagnostic-analysis.git
cd heart-disease-diagnostic-analysis
Install dependencies:

bash
Copy code
pip install pandas seaborn matplotlib
Run the Python script for EDA:

bash
Copy code
python heart_disease_analysis.py
Open Tableau and load the CSV file for creating the dashboard.

References
Dataset Source
Pandas Documentation
Seaborn Documentation
Matplotlib Documentation
