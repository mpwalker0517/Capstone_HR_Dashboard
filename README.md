# Capstone_HR_Dashboard

The purpose of this Dashboard is to showcase the measureables of our team, including certification scores, call coaching stats, and quality of new hire stats. All statistics are stored in a secure SQL database that I can not grant access to for testing the final project, but I utilized SQL to pull info from the database and created Excel files from those queries to utilize in Tableau. Also will utilize Python to make adjustments to Excel files for security purposes. 


-Certification scores 
	1. Completed SQL request from database utilizing inner joins to gather employee name, certification, scores, and dates.
		-cert_pull_sql.sql
	2. Utilized python to split Score and Date column
		-Split_columns.py
	3. Utilized python to generate random names for security purposes and overwrite first column
		-name_update.py
	4. Showcase certification pass rate/dashboard by pulling completed CSV into Tableau
		-https://public.tableau.com/views/Certifications_16980767476410/CertificationStory?:language=en-US&:display_count=n&:origin=viz_share_link

-Certification scores from PDC - API access. Utilize SQL. 
	-Push scores to PDC from Excel sheet with API (weekly)
	-Create weekly report for managers to receive certification scores

-Quality of New Hire dashboard
	-Pull metrics from PDC db (SQL)
	-Create Tableau dashboard

-Coach dashboard
	1. Completed SQL request from database utilizing intter joins to gather employee name, queue, call coaching score, and date 
	-How many employees, departments, last check in, offers in progress
	-Pull metrics from PDC db (SQL)
	-Pull data from Offers in Progress sheet


-Call stats
	-Call coaching google sheet (collect who's upcoming, checklist?)
	-Stats by quarter

