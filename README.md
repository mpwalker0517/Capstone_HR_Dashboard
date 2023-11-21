# Capstone_HR_Dashboard

The purpose of this project is to showcase the measureables of our HR team, including employee data, certification scores, call coaching stats, and quality of new hire stats. We want to be able to visualize simple items, such as how are coaches are being utilized to make sure each coach has an even amount of employees, that we maintain an equal workforce in terms of age and gender, and what departments have the largest amount of employees in order to hire effectively and position leadership in the correct places. 

We also want an "overview look" at how our employees are performing, which temas are performing the best, which certification may need to be reworked, and what the correlation is between the department, quality of new hire score and overall job performance - which could possibly indicate which departments need adjusted onboarding plans.

All stats are stored in a secure SQL database that I can not grant access to for testing the final project, but I utilized SQL to pull info from the database and utilized Python to adjust all employee names for security purposes prior to committing to Git. Each step is listed out in the Jupyter Notebook to allow for testing items. Overview of work completed below:

You can access my virtual environment (my_env) or install all requirements using ~ pip install -r requirements.txt


1. Created virtual environment and installed all packages utilized in jupyter. You can access my virtual environment (my_env) or install all requirements using ~ pip install -r requirements.txt
2. Loaded data from Rent Manager database used to track employee data. Completed SQL request from database utilizing inner joins to gather employee information. Created three sepearate CSV files. 
	-Certification Scores (cert_pull_sql.sql, All_Certs.csv)
	-Call Coaching Scores (call_pull.sql, call_coaching_2023.csv)
	-Employee Data with Quality of New Hire Scores (employee_pull.sql, QNH_11_17.csv)
3. Utilized Jupyter Notebook with Python to clean csv files and complete visualizations
	-Markdown cells for each step as well as comments throughout
4. Showcased data by publishing finzalized CSV into Tableau
		-https://public.tableau.com/views/Certifications_16980767476410/CertificationStory?:language=en-US&:display_count=n&:origin=viz_share_link




