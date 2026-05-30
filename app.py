import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(
    page_title="AI Faculty Assistant",
    page_icon="🎓",
    layout="wide"
)

# Gemini API Key from Streamlit Secrets
genai.configure(api_key=st.secrets["AQ.Ab8RN6KPbCo6d_0gPuFbPaOe-RpYJ_Ge095f3tj0BSOCmMxgtA"])

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Custom CSS
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #eef2ff, #f8fafc);
}

.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #1e3a8a;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #475569;
    margin-bottom: 30px;
}

.feature-box {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom: 10px;
}

.result-box {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🎓 Faculty Assistant")

    st.success("AI Powered Teaching Assistant")

    st.markdown("### Features")
    st.markdown("""
    ✅ Learning Objectives

    ✅ Lecture Outline

    ✅ MCQs Generation

    ✅ Topic Summary

    ✅ Faculty Support

    ✅ Gemini AI Powered
    """)

    st.info("Created using Streamlit + Gemini AI")

# Main Header
st.markdown(
    "<div class='title'>🎓 AI Faculty Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Generate Learning Objectives, Lecture Plans, MCQs and Summaries using AI</div>",
    unsafe_allow_html=True
)

# Topic Input
st.markdown("## 📚 Enter Topic")

topic = st.text_input(
    "",
    placeholder="Example: Data Structures, Machine Learning, DBMS..."
)

# Generate Button
if st.button("🚀 Generate Content"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        prompt = f"""
        Act as an expert faculty assistant.

        Topic: {topic}

        Generate the following:

        ## Learning Objectives
        Provide exactly 3 learning objectives.

        ## Lecture Outline
        Provide a lecture outline with 5 points.

        ## MCQs
        Provide exactly 5 multiple choice questions with 4 options and the correct answer.

        ## Summary
        Provide a short summary in 5 lines.
        """

        with st.spinner("Generating content..."):

            response = model.generate_content(prompt)

            st.markdown("## 📖 Generated Content")

            st.markdown(
                f"<div class='result-box'>{response.text}</div>",
                unsafe_allow_html=True
            )
