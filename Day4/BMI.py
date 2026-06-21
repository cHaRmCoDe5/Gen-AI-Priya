import streamlit as st

# Page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="🧍", layout="centered")

st.title("🧍 BMI Calculator")
st.write("Calculate your Body Mass Index")

# Input fields
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)

with col2:
    height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)

# Calculate BMI
if st.button("Calculate BMI", type="primary"):
    if height > 0:
        bmi = weight / (height ** 2)
        
        # Display result
        st.success(f"Your BMI is: **{bmi:.2f}**")
        
        # BMI Category
        if bmi < 18.5:
            st.error("**Underweight**")
        elif bmi < 25:
            st.success("**Normal weight**")
        elif bmi < 30:
            st.warning("**Overweight**")
        else:
            st.error("**Obese**")
        
        # Health info
        st.info("""
        BMI Categories:
        - Underweight: < 18.5  
        - Normal weight: 18.5 – 24.9  
        - Overweight: 25 – 29.9  
        - Obese: ≥ 30
        """)
    else:
        st.error("Height cannot be zero!")

# Footer
st.caption("Made with ❤️ using Streamlit")