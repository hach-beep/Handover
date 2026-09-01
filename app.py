import streamlit as st
import time

# --- THE FACE OF HANDOVERHERO ---
st.set_page_config(page_title="HandoverHero", page_icon="🏥")

st.title("🏥 HandoverHero AI")
st.subheader("Autonomous Nursing Handoff Assistant")

# Sidebar for Nurse Info
st.sidebar.header("Nurse Profile")
nurse_name = st.sidebar.text_input("Nurse Name", "Nurse Khalid")
shift = st.sidebar.selectbox("Current Shift", ["Day (7A-7P)", "Night (7P-7A)"])

# 1. THE INPUT
st.write("### 📤 Step 1: Upload Handoff Data")
uploaded_file = st.file_uploader("Upload a photo of your 'Brain' or a voice memo", type=['jpg', 'png', 'pdf', 'mp3'])

if uploaded_file is not None:
    st.success("File Received! HandoverHero is analyzing...")
    
    with st.spinner('Applying Nurse Logic...'):
        time.sleep(2) # Simulating AI thinking
        
    # 2. THE OUTPUT (The SBAR Report)
    st.write("### 📄 Step 2: Structured SBAR Report")
    
    # We will show the 'Betty White' data as our demo
    st.error("🚨 CRITICAL ALERT: Renal function declining (Creatinine 0.89 -> 2.0)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**S: Situation**\n99yo F, Full Code. Admitted for Acute Respiratory Failure.")
        st.info("**B: Background**\nHx of COPD, Asthma, Stage 3 CKD. Intubated 12/2.")
    with col2:
        st.info("**A: Assessment**\nSedated (RASS -2). ACVC Vent mode. Drips: Propofol/Fentanyl.")
        st.info("**R: Recommendation**\nMonitor UO closely. Renal consult pending.")

    # 3. THE CHAT FEATURE
    st.write("---")
    st.write("### 💬 Step 3: Ask HandoverHero a Question")
    user_question = st.text_input("Ask about labs, meds, or trends...")
    if user_question:
        st.write(f"**HandoverHero:** Based on the report, the patient was last medicated with Fentanyl at 50mcg/hr. No bowel movements were noted this shift.")
