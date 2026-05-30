import streamlit as st
import google.generativeai as genai

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="AI Faculty Assistant",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------
# GEMINI API CONFIG
# -------------------------------
genai.configure(api_key="AQ.Ab8RN6KPbCo6d_0gPuFbPaOe-RpYJ_Ge095f3tj0BSOCmMxgtA")

model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.big-title {
    text-align: center;
    color: #1e293b;
    font-size: 55px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #64748b;
    font-size: 20px;
    margin-bottom: 30px;
}

.stButton > button {
    background: linear-gradient(90deg,#4F46E5,#7C3AED);
    color: white;
    border-radius: 12px;
    height: 3.2em;
    width: 220px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(90deg,#4338CA,#6D28D9);
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 2px 12px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR
# -------------------------------
with st.sidebar:

    st.title("🎓 Faculty Assistant")

    st.markdown("---")

    st.success("AI Powered Teaching Assistant")

    st.markdown("""
### Features

✅ Learning Objectives

✅ Lecture Outline

✅ MCQs Generation

✅ Topic Summary

✅ Faculty Support

✅ Gemini AI Powered
""")

    st.markdown("---")

    st.info("Created using Streamlit + Gemini AI")

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<div class='big-title'>
🎓 AI Faculty Assistant
</div>

<div class='sub-title'>
Generate Learning Objectives, Lecture Plans, MCQs and Summaries using AI
</div>
""", unsafe_allow_html=True)

# -------------------------------
# INPUT
# -------------------------------
st.subheader("📚 Enter Topic")

topic = st.text_input(
    "",
    placeholder="Example: Artificial Intelligence, Data Structures, Cloud Computing"
)

# -------------------------------
# BUTTON ACTION
# -------------------------------
if st.button("🚀 Generate Content"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        prompt = f"""
Act as an expert faculty assistant.

Topic: {topic}

Generate the following:

# Learning Objectives
Provide exactly 3 learning objectives.

# Lecture Outline
Provide a lecture outline with 5 points.

# MCQs
Provide exactly 5 multiple choice questions with:
- 4 options
- Correct answer

# Summary
Provide a short summary in 5 lines.
"""

        with st.spinner("🤖 AI is preparing your content..."):

            response = model.generate_content(prompt)

        st.success("✅ Content Generated Successfully")

        st.markdown("---")

        st.markdown("<div class='result-box'>", unsafe_allow_html=True)

        st.markdown("## 📖 Generated Content")

        st.write(response.text)

        st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("© 2026 AI Faculty Assistant | Powered by Google Gemini")