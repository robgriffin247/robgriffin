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