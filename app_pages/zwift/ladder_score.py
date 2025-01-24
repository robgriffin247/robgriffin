import streamlit as st

col1, col2 = st.columns([3,7])

with col1:
    n_riders = st.number_input('Total Number of Riders', value=10, min_value=1, max_value=10)
with col2:
    positions = st.multiselect('Positions', options=[i+1 for i in range(0,n_riders)])

total = 0

for position in positions:
    total += 11-position

max_points = 0

for position in range(1,n_riders+1):
    max_points += 11-position

st.code(f"{'Win :D' if total>(max_points-total) else 'Loss :(' if total<(max_points-total) else 'Draw :/'}")
st.code(f"Scored {total} of {max_points} points")

st.divider()

st.markdown('''
**About**
            
The Club Ladder is a racing format and league in Zwift. 
Races feature two teams, of up to 5 riders each, going head-to-head. 
Points are awarded as 10 for 1st, 9 for 2nd ... 1 for 10th. 
The team with the most points wins. 
I built this tool to allow a quick input of rider positions during races to
make it easier to judge the situation on the road and help guide strategy.
            ''')