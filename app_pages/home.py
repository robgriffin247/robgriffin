import streamlit as st

# Data
summary ='''
#### Rob Griffin, PhD

##### Data Engineer / Analytics Engineer
'''

main_body = '''
This site has been created to host and showcase a number of smaller web-apps &mdash; 
apps where a stand-alone app would be overkill &mdash; while larger apps have dedicated deployments.
These smaller apps have largely been created as a way to practice coding, try new 
technologies or test new ideas &mdash; even this site was partly to test making multipage apps in Streamlit.       

I am both a data nerd and keen cyclist &mdash; spending a lot of time riding and racing on the virtual roads 
of Zwift &mdash; so a lot of my projects combine these two worlds. Check out some of my larger projects below
and smaller apps in the navigation menu (← over there!)'''

projects = [
    {'display':False, 'title':'RouteViewer', 'link':'https://routeviewer.streamlit.app', 'description':'A platform providing race notes for routes on Zwift, built on a database of road descriptions and route landmarks that combine to create consistent notes for the various routes that pass through the same roads.'},
    {'display':True, 'title':'ZwiftRacing.App Demo', 'link':'[https://github.com/robgriffin247/zrapp_demo]', 'description':'A demonstration of using Python, DuckDB, DLT and Streamlit to extract, transform and visualise data from ZwiftRacing.app.'},
    {'display':False, 'title':'', 'link':'', 'description':''}
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

st.divider()

st.markdown(main_body)

st.divider()

for project in projects:
    if project['display']:
        st.info(f'''[{project['title']}]({project['link']}) &mdash; {project['description']}''' )
