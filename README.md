# UrbanPulse-ETL-CSI
Urban Pulse is a data project that builds an ETL pipeline in Python + MySQL and a Power BI dashboard to track a City Stress Index (CSI). It combines weather, air quality, and traffic into one score, making urban livability easy to monitor and analyze.
The idea is simple: cities are stressful, and many factors like weather, traffic, and air quality contribute to that stress. But instead of looking at them separately, I wanted to create a single score that tells how stressful or livable a city feels at any given time. That’s where the City Stress Index (CSI) comes in.

The backbone of the project is an ETL pipeline. I wrote Python scripts that can extract raw data (like weather, air quality, and traffic data), clean it, and then load it into a MySQL database. Once the data is structured, I calculate the CSI by combining these factors into one score between 0 and 100. A lower score means the city is under a lot of stress (bad air, bad traffic, bad weather), and a higher score means conditions are better.

After that, I used Power BI to make everything easy to understand. The dashboard shows trends of CSI over time, compares different factors side by side, and highlights the latest CSI so you instantly know how the city is doing.

What makes this project exciting for me is that it feels close to a real-world application. Cities and governments actually use similar systems to monitor livability, so this project is like a mini version of that. It’s not just about writing code — it’s about solving a real problem in a way people can see and understand.

I’ve uploaded everything to this repository, including my ETL code, SQL schema, and Power BI dashboard, so anyone can explore it, improve it, or even adapt it for another city.
