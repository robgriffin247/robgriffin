
key_skills = [
    {'category':'Programming', 'skills':['Python', 'SQL', 'R', 'SAS']},
    {'category':'Technologies', 'skills':['Dagster', 'Snowflake', 'DBT', 'DLT', 'Streamlit', 'PowerBI', 'Shiny', 'Git', 'AI']},
    {'category':'Methods', 'skills':['ETL/ELT', 'Data Visualisation', 'Statistical Analysis']},
    {'category':'Soft Skills', 'skills':['Presentation', 'Scientific Writing', 'Leadership']},
    ]

for i in key_skills:
    print(i['category'])
    print(', '.join([f'<pre>{j}</pre>' for j in i['skills']]))