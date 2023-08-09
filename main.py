import streamlit as st

st.title("Do an yeu thich")

appetizer = ["Cheese Bread", "Onion Soup", "Ceasar Salad", "Garlic Bread", "Spring roll"]
main = ["Pizza", "Burger", "Steak", "Chicken", "Mousaka", "Paella"]
dessert = ["Cheese Cake", "Cupcake", "Tiramisu", "Panna Cotta", "Triffle"]

with st.form("Thuc don yeu thich"):
  options1 = st.multiselect("Mon khai vi ua thich:", appetizer)
  options2 = st.multiselect("Mon chinh ua thich:", main)
  options3 = st.multiselect("Mon trang mieng ua thich:", dessert)
  submitted = st.form_submit_button("Submit")

if submitted:
  st.write("Cac lua chon cua ban la:")
  st.write("**1. Mon khai vi:**")
  if len(options1)==0:
    st.write("Ban chua chon mon khai vi!")
  else:
    for i in range(len(options1)):
      st.write(options1[i])

  st.write("**2. Mon chinh:**")
  if len(options2)==0:
    st.write("Ban chua chon mon chinh!")
  else:
    for i in range(len(options2)):
      st.write(options2[i])

  st.write("**3. Mon trang mieng:**")
  if len(options3)==0:
    st.write("Ban chua chon mon trang mieng!")
  else:
    for i in range(len(options3)):
      st.write(options3[i])