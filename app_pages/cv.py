import streamlit as st

col1, col2 = st.columns([2,8])

with col1:
    st.image('images/rob_griffin.jpg', use_container_width=True)

with col2:
    st.markdown('''
                #### Rob Griffin, PhD
                                
                ##### Data Engineer / Analytics Engineer
                                
                Knowit Solutions CoCreate, Göteborg
                ''')
                    
st.markdown('''
            Passionate about enabling data-driven decision making, Rob is a programmer with experience in 
            data processing, visualisation and analysis. A background research and training as a scientist 
            provides a great understanding of how to interpret and communicate data effectively and accurately.
            Thrives with problem solving, learning new skills/techniques and strives to make valuable contributions.
            ''')

tab1, tab2, tab3 = st.tabs(['Experience', 'Education', 'Other'])

with tab1:
    st.markdown('''
                ###### Employment
                ''')
    
    
    employment = [
        {'role':'Data Engineer', 'employer':'🇸🇪 Knowit Solutions CoCreate', 'period':'Sep 2023 → Present'},
        {'role':'Statistical Programmer', 'employer':'🇸🇪 AstraZeneca', 'period':'Sep 2020 → Sep 2023'},
        {'role':'Visiting Academic', 'employer':'🇦🇺 University of Queensland', 'period':'Jan 2019 → Aug 2020'},
        {'role':'Postdoctoral Research Fellow', 'employer':'🇸🇪 Uppsala University', 'period':'Sep 2018 → Sep 2020'},
        {'role':'Postdoctoral Researcher', 'employer':'🇫🇮 University of Turku', 'period':'Mar 2016 → Sep 2018'},
        {'role':'Doctoral Candidate', 'employer':'🇸🇪 Uppsala University', 'period':'Sep 2011 → Sep 2015'},
    ]

    st.dataframe(employment)

