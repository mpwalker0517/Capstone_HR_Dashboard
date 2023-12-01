# Capstone_HR_Dashboard

The purpose of this project is to showcase the measureables of our HR team, including employee data, certification scores, call coaching stats, and quality of new hire stats. We want to be able to visualize simple items, such as how are coaches are being utilized to make sure each coach has an even amount of employees, that we maintain an equal workforce in terms of age and gender, and what departments have the largest amount of employees in order to hire effectively and position leadership in the correct places. 

We also want an "overview look" at how our employees are performing, which temas are performing the best, which certification may need to be reworked, and what the correlation is between the department, quality of new hire score and overall job performance - which could possibly indicate which departments need adjusted onboarding plans/leadership.

All stats are stored in a secure SQL database that I can not grant access to for testing the final project, but I utilized SQL to pull info from the database and utilized Python to adjust all employee names for security purposes prior to committing to Git. Each step is listed out in the Jupyter Notebook to allow for testing items. Overview of work completed below:

You can access my virtual environment (my_env) or install all requirements using ~ pip install -r requirements.txt

*Connect to virtual environment: my_env\Scripts\activate.bat


1. Created virtual environment and installed all packages utilized in jupyter, also created requirements file. You can access my virtual environment (my_env) or install all requirements using ~ pip install -r requirements.txt
2. Loaded data from Rent Manager database used to track employee data. Completed SQL request from database utilizing inner joins to gather employee information. Created three sepearate CSV files. 
	-Certification Scores (cert_pull_sql.sql, All Certs_Clean.csv)
	-Call Coaching Scores (call_pull.sql, ccall_coaching_2023_scores.csv)
	-Employee Data with Quality of New Hire Scores (qnh_pull.sql, QNH_11_17_23.csv)
3. Utilized Jupyter Notebook with Python to clean csv files
4. Used merge with Python to combine data from separate CSVs
5. Created pivot tables and other data visualizations with Python
6. Markdown cells for each step as well as comments throughout
7. Created a separate jupyter notebook (Turnover) for turnover data, utilizing this CSV for visualizations in Tableau
8. Created a third jupyter notebook (hr_dashboard_overview) to display high-level overview of visualizations from hr_dashboard_all notebook
8. Showcased data by publishing finzalized data into Tableau
	Certification data:
		-https://public.tableau.com/views/Certifications_16980767476410/CertificationStory?:language=en-US&:display_count=n&:origin=viz_share_link
	Turnover data:
		-https://public.tableau.com/views/hr_dash_tableau/EmployeeTurnoverDashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link




