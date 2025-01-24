import streamlit as st


# Data 
summary ='''
#### Rob Griffin, PhD

##### Data Engineer / Analytics Engineer
'''

profile = '''
Passionate about enabling data-driven decision making, Rob is a programmer with experience in 
data processing, visualisation and analysis. A background in research and training as a scientist 
provides a great understanding of how to interpret and communicate data effectively and accurately.
Thrives with problem solving, learning new skills/techniques and strives to make valuable contributions.
'''

key_skills = [
    {'category':'Coding', 'skills':['Python', 'SQL', 'R', 'SAS', 'HTML', 'CSS', 'Markdown',]},
    {'category':'Technologies', 'skills':['Dagster', 'Snowflake', 'DBT', 'DLT', 'Streamlit', 'PowerBI', 'Shiny', 'Git', 'AI']},
    {'category':'Methods', 'skills':['ETL/ELT', 'Data Visualisation', 'Statistical Analysis']},
    {'category':'Soft Skills', 'skills':['Presentation', 'Scientific Writing', 'Leadership']},
    ]

assignments = [
    {'primary':False, 'role':'Data Engineer', 'employer':'Göteborgs Hamn', 'period':'May 2024 → Present', 'highlight':True, 'description':'Part of a team developing a data platform that collects, prepares and serves production-ready data to end-users across the business, using a data stack including Dagster, DBT and Snowflake. Provide support in educating and assisting end-users using Power BI as an analytics/business intelligence tool, enabling them to combine our data products with their domain-knowledge to ceate insights with genuine value to the client.'},
    {'primary':False, 'role':'Analytics Engineer', 'employer':'Volvo Cars (VCC)', 'period':'Dec 2023 → Present', 'highlight':True, 'description':'Primarily developing dashboards and applications in Power BI that extract and transform raw data into visualistions to produce visuals that assist project and test management. Additional focus on improving data practices and the suitability of data (experimental design).'},
    {'primary':True, 'role':'Data Engineer (Consultant)', 'employer':'Knowit Solutions CoCreate', 'period':'Oct 2023 → Present', 'highlight':False, 'description':'Working with a number of clients to develop data platforms, delivering production-ready data fit for use by project managers and decision makers. Educating and advising clients on data practices, data interpretation and business intelligence tools.'},
    {'primary':True, 'role':'Statistical Programmer', 'employer':'AstraZeneca', 'period':'Sep 2020 → Sep 2023', 'highlight':True, 'description':'Production of deliverables (tables, figures, datasets) for use in regulatory applications for drug approval using SAS. Secondary role exploring and testing the viability of using R in place of SAS in pharmecutical applications. Working with distributed teams of colleagues in the US, UK, Sweden, Poland and India.'},
    {'primary':True, 'role':'Visiting Academic', 'employer':'University of Queensland', 'period':'Jan 2019 → Aug 2020', 'highlight':False, 'description':'Working on the evolution of sex-biased genes and cuticular hydrocarbons, using fruit-flies as a model system. Development and application of advanced statistical methods allowing the analysis of evolutionary potential (evolvability and autonomy) in the context of sex differences in multi-dimensional space.'},
    {'primary':True, 'role':'Postdoctoral Research Fellow', 'employer':'Uppsala University', 'period':'Sep 2018 → Sep 2020', 'highlight':False, 'description':'Research on the evolution of sexual dimorphism with funded through a highly-competitive program from the Swedish Research Council (Vetenskapsrådet), including a secondment to an overseas research group (see above). Being invited to speak at the *Swedish Collegium for Advanced Studies* was a major highlight.'},
    {'primary':True, 'role':'Postdoctoral Researcher', 'employer':'University of Turku', 'period':'Mar 2016 → Sep 2018', 'highlight':False, 'description':'Working on the ecology and evolution of sex differences in modern human populations, using contemporary records from the Finnish church, combining demographic data with climate, nutrition and other data sources. This research demonstrated that changing patterns of sex differences in human lifespan - increasingly more female-biased in modern societies - can be explained by improved environmental conditions during childhood.'},
    {'primary':True, 'role':'Doctoral Candidate', 'employer':'Uppsala University', 'period':'Sep 2011 → Sep 2015', 'highlight':True, 'description':'''PhD on the Evolutionary Quantitative Genetics of Sex Differences. This role involved leading the design and implementation of ambitious and robust experiments, application of advanced multivariate statistical analysis, and communication of research through scientific writing and presentations at large international conferences. This led to a successful career in academia with postdocs in Finland, Sweden and Australia &mdash; links to [doctoral thesis](https://www.diva-portal.org/smash/record.jsf?pid=diva2%3A842941&dswid=5725) and [publications](https://scholar.google.com/citations?user=w0uVTwIAAAAJ&hl=en).'''},
    ]

education = [
    {'primary':True, 'title':'Biology, specialising in Evolutionary Genetics', 'qualification':'PhD', 'provider':'Uppsala University', 'period':'2011 → 2015'},
    {'primary':True, 'title':'Evolutionary and Behvaioural Ecology', 'qualification':'MSc', 'provider':'University of Exeter', 'period':'2010 → 2011'},
    {'primary':True, 'title':'Conservation Biology and Ecology', 'qualification':'BSc', 'provider':'University of Exeter', 'period':'2007 → 2010'},
]



# Layout
st.html('''
<style>
        img { border-radius: 0.5em !important; }
</style>
        ''')

# - Top Block
col1, col2 = st.columns([2,8])

with col1:
    st.image('images/rob_griffin.jpg', use_container_width=False, width=180)

with col2:
    st.markdown(summary)


# - Tabs
tab_overview, tab_employment,  tab_education, = st.tabs(['Overview', 'Employment', 'Education', ])

with tab_overview:

    st.write('')

    st.info(profile)
        
    st.divider()

    st.markdown('###### Key Skills')

    for i in key_skills:
        st.html(f'''<p style="margin: 0 auto; padding:0 auto 0.6em auto; line-height: 1.2em;">{i['category'] + ''.join([f'<code style="font-family: inherit; background-color: #99999930; padding: 0.2em 0.4em; margin: 0 0 0 0.5em; border-radius: 0.5em;">{j}</code>' for j in i['skills']])}</p>''')

    st.divider()

    st.markdown('###### Selected Assignments')

    for assignment in assignments:
        if assignment['highlight']:
            st.info(f'''
                    **{assignment['role']}** 
                    
                    {assignment['employer']}, {assignment['period']}

                    {assignment['description']}
                    ''')

with tab_employment:
   
    #st.dataframe([assignment for assignment in assignments if assignment['primary']], 
    #             use_container_width=True,
    #             column_order=('role','employer', 'period'),
    #             column_config={
    #                 'role':st.column_config.TextColumn('Title', width='medium'),
    #                 'employer':st.column_config.TextColumn('Employer', width='medium'),
    #                 'period':st.column_config.TextColumn('Period', width='medium'),
    #             })

    st.write('')

    content = st.container()
    detailed_view = st.toggle('Detailed View', value=False)

    with content:
        for assignment in assignments:
            if assignment['primary']:
                st.info(f'''
                    **{assignment['role']}**
                    
                    {assignment['employer']}, {assignment['period']}

                    {assignment['description'] if detailed_view else ''}
                    ''')

    
    st.divider()
    
    st.markdown('*Does not include numerous part-time positions prior to and during university including management and leadership roles in hospitality and retail, and voluntary roles in research.*')


with tab_education:

    st.write('')

    for course in education:
        if course['primary']:
            st.info(f'''
                    **{course['qualification']} &mdash; {course['title']}** 
                    
                    {course['provider']} ({course['period']})

                    ''')



