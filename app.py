import streamlit as st

pg_home = st.Page('app_pages/home.py', title='Home', icon=':material/home:')
pg_cv = st.Page('app_pages/cv.py', title='CV', icon=':material/person_search:')

pg_ladder_score = st.Page('app_pages/zwift/ladder_score.py', title='Ladder Score', icon=':material/calculate:')
pg_power_zones = st.Page('app_pages/zwift/power_zones.py', title='Power Zones', icon=':material/signal_cellular_alt:')

pg = st.navigation({
    'Rob Griffin': [pg_home, pg_cv], 
    'Zwift':[pg_ladder_score, pg_power_zones]
    })

pg.run()
