import streamlit as st

# 1. Page Configuration Settings
st.set_page_config(
    page_title="Grade Converter", 
    page_icon="🎓", 
    layout="centered"
)

# 2. Injecting the Colorful Gradient Background
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"], .main {
        background: linear-gradient(135deg, #e0f2fe 0%, #dcfce7 50%, #fef9c3 100%) !important;
        background-attachment: fixed !important;
    }
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    .results-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 25px;
        border-radius: 12px;
        border: 1px solid rgba(0, 0, 0, 0.05);
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Main Interface Header
st.title("🎓 Mark to Letter Grade Converter")
st.write("Enter your profile information below to calculate your final letter grade.")
st.write("---")

# 4. Initialize State Tracking Variables
if "show_results" not in st.session_state:
    st.session_state.show_results = False

# Callback function to handle the fields clearing routine accurately
def clear_all_fields():
    # Directly wipe the interactive input widget keys
    st.session_state["mark_input"] = 0.0
    st.session_state["name_input_field"] = ""
    # Hide the evaluation results display block
    st.session_state.show_results = False

# 5. Native Input Fields with Explicit Keys
mark = st.number_input(
    label="Enter your mark (0 - 100):",
    min_value=0.0,
    max_value=100.0,
    step=1.0,
    format="%.2f",
    key="mark_input"
)

name_input = st.text_input(
    label="Student Name (Optional):", 
    placeholder="Enter your name...",
    key="name_input_field"
)

# 6. Action Control Grid System Layout
col_sub, col_clr = st.columns(2)

with col_sub:
    if st.button("Calculate Grade", type="primary", use_container_width=True):
        st.session_state.show_results = True

with col_clr:
    # We pass the custom callback function directly into the native on_click routine
    st.button("Clear Fields", type="secondary", use_container_width=True, on_click=clear_all_fields)

st.write("---")

# 7. Processing Actions & Output Generation
if st.session_state.show_results:
    if 0 <= mark <= 100:
        # Scale range boundaries configuration parameters
        thresholds = [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "E")]
        grade = next((g for t, g in thresholds if mark >= t), "E")

        # The feedback dictionary containing your custom motivational messages
        feedback_dictionary = {
            "A": "Fantastic job {name}! You set the bar high—keep maintaining this brilliant consistency!",
            "B": "Great work {name}! You are so close to the top tier. Keep pushing, you have absolutely got this!",
            "C": "Solid effort {name}! You are almost there—stay consistent and watch your progress soar!",
            "D": "Never give up {name}! Every mistake is a stepping stone to growth. Keep trying your best!",
            "E": "Do not be discouraged {name}! Your current score does not define your future. Keep your head up and start fresh!"
        }

        # Setup display fallbacks for blank naming slots
        display_name = name_input.strip() if name_input and name_input.strip() else "Student"
        personalized_remark = feedback_dictionary.get(grade, "").format(name=display_name)

        # Output Results Container Card UI
        st.markdown('<div class="results-card">', unsafe_allow_html=True)
        st.subheader("📊 Evaluation Results")
        st.write(f"Entered Mark: **{mark:.2f}**")
        st.write(f"Calculated Grade: **{grade}**")
        st.write(" ") 
        
        # Large and Bold text using a native subheader markdown tag
        st.markdown(f"### **Remark: {personalized_remark}**")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Error: Please enter a mark between 0 and 100.")
