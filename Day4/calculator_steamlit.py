import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Custom Styled Calculator", layout="centered")

# 2. Initialize State Management
if 'display' not in st.session_state:
    st.session_state.display = '0'
if 'operation' not in st.session_state:
    st.session_state.operation = ''
if 'calc_theme' not in st.session_state:
    st.session_state.calc_theme = 'Pink Gradient'

# 3. Dynamic Injection of Themes & Layout Enhancements
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #5a189a 0%, #7b2cbf 50%, #9d4edd 100%);
        min-height: 100vh;
    }
    
    /* Base wrapper matching your design matrix dimensions */
    .calculator-frame {
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        max-width: 320px;
        margin: 20px auto;
        background: #f5f5f5;
    }
    
    /* Display Layout Configurations */
    .screen-container {
        padding: 25px 20px;
        text-align: right;
        min-height: 110px;
    }
    
    .screen-op {
        font-size: 14px;
        min-height: 20px;
        margin-bottom: 5px;
    }
    
    .screen-res {
        font-size: 36px;
        font-weight: bold;
        word-wrap: break-word;
    }

    /* Core Streamlit Native Button Styling Extensions */
    div.stButton > button {
        border: none !important;
        border-radius: 8px !important;
        padding: 18px 0px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        cursor: pointer;
        transition: all 0.2s !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    div.stButton > button:hover {
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Theme Styles Injector
if st.session_state.calc_theme == 'Pink Gradient':
    st.markdown("""
    <style>
        .screen-container { background: linear-gradient(135deg, #f8a5c2 0%, #f5c6d6 100%); }
        .screen-op { color: #666; }
        .screen-res { color: #333; }
        div.stButton > button { background-color: #ffffff !important; color: #333 !important; }
        div.op-btn div.stButton > button { background-color: #f8a5c2 !important; color: #333 !important; }
        div.eq-btn div.stButton > button { background-color: #7b2d8e !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        .screen-container { background: #3d3d3d; }
        .screen-op { color: #aaa; }
        .screen-res { color: #fff; }
        div.stButton > button { background-color: #ffffff !important; color: #333 !important; }
        div.op-btn div.stButton > button { background-color: #4a4a4a !important; color: white !important; }
        div.eq-btn div.stButton > button { background-color: #4a4a4a !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. Backend Logic Operations Engine
def handle_click(btn):
    if btn == 'C':
        st.session_state.display = '0'
        st.session_state.operation = ''
    elif btn == 'CE':
        if len(st.session_state.display) > 1 and st.session_state.display not in ['Error', 'Error (Div by 0)']:
            st.session_state.display = st.session_state.display[:-1]
        else:
            st.session_state.display = '0'
    elif btn == '=':
        try:
            # FIX: Remove formatting commas before sending string to eval engine
            expr = st.session_state.display.replace(',', '').replace('×', '*').replace('÷', '/')
            st.session_state.operation = st.session_state.display
            
            val = eval(expr)
            # Remove trailing .0 from whole floats safely
            if isinstance(val, float) and val.is_integer():
                st.session_state.display = f"{int(val):,}"
            else:
                st.session_state.display = f"{val:,}" if isinstance(val, int) else f"{val:.6g}"
        except ZeroDivisionError:
            st.session_state.display = 'Error (Div by 0)'
        except Exception:
            st.session_state.display = 'Error'
    else:
        # Overwrite current initializations or handle character append actions
        if st.session_state.display in ['0', 'Error', 'Error (Div by 0)']:
            if btn in ['÷', '×', '-', '+', '%']:
                st.session_state.display = '0' + btn
            else:
                st.session_state.display = btn
        else:
            st.session_state.display += btn

# 5. Core Interface Construction
st.title("🧮 Custom Dashboard Calculator")
st.session_state.calc_theme = st.selectbox("Choose Visual Skin Style Theme:", ["Pink Gradient", "Dark Shadow"])

# Generate Unified View Interface container wrapper
st.markdown(f"""
<div class="calculator-frame">
    <div class="screen-container">
        <div class="screen-op">{st.session_state.operation if st.session_state.operation else "&nbsp;"}</div>
        <div class="screen-res">{st.session_state.display}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 2D Grid Layout Logic Mapping Matrix Array
buttons = [
    ['C', '÷', '×', 'CE'],
    ['7', '8', '9', '-'],
    ['4', '5', '6', '+'],
    ['1', '2', '3', '='],
    ['%', '0', '.', '']
]

# Grid Column Structure Matrix Render Loop block
with st.container():
    for r_idx, row in enumerate(buttons):
        cols = st.columns(4)
        for c_idx, btn_label in enumerate(row):
            if btn_label: # Only render columns that are populated
                with cols[c_idx]:
                    # Determine visual wrapper class grouping for operational theme styles mapping
                    if btn_label in ['÷', '×', '-', '+', 'C', 'CE']:
                        class_wrap = "op-btn"
                    elif btn_label == '=':
                        class_wrap = "eq-btn"
                    else:
                        class_wrap = "num-btn"
                    
                    st.markdown(f'<div class="{class_wrap}">', unsafe_allow_html=True)
                    st.button(
                        label=btn_label, 
                        key=f"btn_{btn_label}_{r_idx}_{c_idx}", 
                        on_click=handle_click, 
                        args=(btn_label,),
                        use_container_width=True
                    )
                    st.markdown('</div>', unsafe_allow_html=True)
