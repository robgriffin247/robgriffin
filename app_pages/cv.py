import streamlit as st


# Data 
summary ='''
#### Rob Griffin, PhD

##### Data Engineer / Analytics Engineer
'''

profile = '''
Passionate about enabling data-driven decision making, Rob is a programmer with experience in 
data processing, visualisation and analysis. A background research and training as a scientist 
provides a great understanding of how to interpret and communicate data effectively and accurately.
Thrives with problem solving, learning new skills/techniques and strives to make valuable contributions.
'''

key_skils = [
    {'category':'Programming', 'skills':['Python', 'SQL', 'R', 'SAS']},
    {'category':'Technologies', 'skills':['Dagster', 'Snowflake', 'DBT', 'DLT', 'Streamlit', 'PowerBI', 'Shiny', 'Git', 'AI']},
    {'category':'Methods', 'skills':['ETL/ELT', 'Data Visualisation', 'Statistical Analysis']},
    {'category':'Soft Skills', 'skills':['Presentation', 'Scientific Writing', 'Leadership']},
    ]

employment = [
    {'role':'Data Engineer, Consultant', 'employer':'Knowit Solutions CoCreate', 'period':'Oct 2023 → Present'},
    {'role':'Statistical Programmer', 'employer':'AstraZeneca', 'period':'Sep 2020 → Sep 2023'},
    {'role':'Visiting Academic', 'employer':'University of Queensland', 'period':'Jan 2019 → Aug 2020'},
    {'role':'Postdoctoral Research Fellow', 'employer':'Uppsala University', 'period':'Sep 2018 → Sep 2020'},
    {'role':'Postdoctoral Researcher', 'employer':'University of Turku', 'period':'Mar 2016 → Sep 2018'},
    {'role':'Doctoral Candidate', 'employer':'Uppsala University', 'period':'Sep 2011 → Sep 2015'},
    ]



# Layout
# - Top Block
col1, col2 = st.columns([2,8])

with col1:
    st.image('images/rob_griffin.jpg', use_container_width=False, width=180)

with col2:
    st.markdown(summary)
                    
st.markdown(profile)
st.dataframe(key_skils, 
             use_container_width=True,
             column_config={
                 'category':st.column_config.TextColumn('Category'),
                 'skills':st.column_config.ListColumn('Skills'),
             })


# - Tabs
tab1, tab2, tab3 = st.tabs(['Experience', 'Education', 'Other'])

with tab1:
    st.markdown('''
                ###### Employment
                ''')
    
    st.dataframe(employment, 
                 use_container_width=True,
                 column_config={
                     'role':st.column_config.TextColumn('Title', width='medium'),
                     'employer':st.column_config.TextColumn('Employer', width='medium'),
                     'period':st.column_config.TextColumn('Period', width='medium'),
                 })

    st.markdown('*Does not include numerous part-time roles including management and supervision roles in hospitality and retail*')
