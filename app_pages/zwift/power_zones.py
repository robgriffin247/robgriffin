import streamlit as st
import polars as pl

col1, col2, col3 = st.columns([4,4,2])

with col3:
    units = st.selectbox('weight_units', label_visibility='hidden', options=['kg', 'lbs'])
with col2:
    weight = st.slider('Weight', min_value=1, max_value=441 if units=='lbs' else 200, value=179 if units=='lbs' else 81)
    kg = weight / 2.2046 if units=='lbs' else weight
with col1:
    ftp = st.slider('FTP', min_value=1, max_value=500, value=318)


zones = [
        {'number':1,
         'zone':'Active Recovery', 
         'bounds':'<55', 
         'watts': '<{:.0f}'.format(ftp*0.55), 
         'wkg': '<{:.2f}'.format(ftp*0.55/kg)},

        {'number':2,
         'zone':'Endurance',  
         'bounds':'55 - 75', 
         'watts': '{:.0f} - {:.0f}'.format(ftp*0.55, ftp*0.75), 
         'wkg': '{:.2f} - {:.2f}'.format(ftp*0.55/kg, ftp*0.75/kg)},

        {'number':3,
         'zone':'Tempo', 
         'bounds':'75 - 90', 
         'watts': '{:.0f} - {:.0f}'.format(ftp*0.75, ftp*0.90), 
         'wkg': '{:.2f} - {:.2f}'.format(ftp*0.75/kg, ftp*0.90/kg)},

        {'number':4,
         'zone':'Lactate Threshold',  
         'bounds':'90 - 105', 
         'watts': '{:.0f} - {:.0f}'.format(ftp*0.90, ftp*1.05), 
         'wkg': '{:.2f} - {:.2f}'.format(ftp*0.90/kg, ftp*1.05/kg)},

        {'number':5, 
         'zone':'VO2 Max', 
         'bounds':'105 - 120', 
         'watts': '{:.0f} - {:.0f}'.format(ftp*1.05, ftp*1.20), 
         'wkg': '{:.2f} - {:.2f}'.format(ftp*1.05/kg, ftp*1.20/kg)},

        {'number':6, 
         'zone':'Anaerobic Capacity', 
         'bounds':'120 - 150', 
         'watts': '{:.0f} - {:.0f}'.format(ftp*1.20, ftp*1.50), 
         'wkg': '{:.2f} - {:.2f}'.format(ftp*1.20/kg, ftp*1.50/kg)},

        {'number':7, 
         'zone':'Neuromuscular Power', 
         'bounds':'>150', 
         'watts': '>{:.0f}'.format(ftp*1.50), 
         'wkg': '>{:.2f}'.format(ftp*1.50/kg)},
]

df = pl.DataFrame(zones)

st.divider()

st.dataframe(df,
             use_container_width=True,
             column_config={
                 'number':st.column_config.TextColumn('#', width='small'),
                 'zone':st.column_config.TextColumn('Zone'),
                 'bounds':st.column_config.TextColumn('% FTP'),
                 'watts':st.column_config.TextColumn('Watts'),
                 'wkg':st.column_config.TextColumn('W/kg'),
             })

st.divider()

st.markdown('''
**About**
            
This calculator is based on Coggan Power Zones which divide power into 
seven ranges based on the typical physiological effects. Briefly:
            
- *Active Recovery* causes no significant physiological adaptations (but it's nice to be on the bike)
- *Endurance* riding improves the bodies energy efficiency, ability to delay and recover from fatigue, and converts explosive muscle fibers to endurance-friendly ones, for efforts over several hours
- *Tempo* riding builds stamina, increases energy storage, raises your ability to sustain higher effort for longer, and strengthens heart and lungs, for efforts up to a couple of hours
- *Lactate Threshold* training enables you to work harder for longer without tiring quickly, for efforts of around 20-30 minutes
- *VO2 Max* training increases both aerobic and anaerobic capacity, preparing you to tackle short, intense efforts of 2-5 minutes and recover quickly
- *Anaerobic Capacity* training builds explosive power, sprinting ability, and tolerance for intense efforts of up to 2 minutes through muscle growth and improved energy stores
- *Neuromuscular Power* training raises peak power, enhances sprinting strength, and develops fast-twitch muscles for all-out very short efforts

Read more [here](https://www.trainingpeaks.com/blog/power-training-levels/)
''')