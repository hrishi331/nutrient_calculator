import streamlit as st
import numpy as np
import time

st.title('NUTRIENT CACULATOR')

st.header("INSERT VALUES")

l = st.multiselect(
    label="Select your fertilizers",
    options=['Micro','Calcium Nitrate','Magnecium Sulphate','NPK 19:19:19','NPK 0:52:34','DAP'],
    placeholder='Choose',
    label_visibility='visible'
)


vals = []
for i in l:
    v = st.number_input(f"Enter percentage for {i} ")
    vals.append(v)
st.write(f"Remaining percentage : {100 - np.sum(vals)}")



sol_lits = st.number_input("Enter desired liters of solution")
concentration = st.number_input('Enter desired concentration in PPM ')



fert_dict = dict(zip(l,vals))

vals_factor = []

factor = concentration/1000

new_vals = []
for i in vals:
    f = (i/100)*factor*sol_lits
    new_vals.append(f)

result = dict(zip(l,new_vals))



if st.button('CALCULATE'):
    # Initiate progress bar
    progress_bar = st.progress(0)

    # Update the progress bar over time
    for i in range(100):
        time.sleep(0.05)  # Simulate a task by sleeping for a short time
        progress_bar.progress(i + 1)  # Update progress bar

    # Display a completion message
    st.success("Task Completed!")

    st.header('RESULTS')
    st.write(f"""
    To make **{sol_lits} liters** of **{concentration} PPM** solution with above ratios,
    mix following amounts of fertlizers :
    """)
    for i in result.items():
        st.write(f"**{i[0]}** : {round(i[1],2)} gms")





