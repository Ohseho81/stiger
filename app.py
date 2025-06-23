import streamlit as st
from analyzer import analyze_video
from report import generate_report

st.set_page_config(page_title="AllThatBasketball AI", layout="centered")
st.title("AllThatBasketball 리포트 생성기")

uploaded_file = st.file_uploader("운동 영상을 업로드하세요", type=["mp4", "mov", "avi"])

if uploaded_file:
    with st.spinner("분석 중입니다..."):
        results = analyze_video(uploaded_file.name)
        report_image = generate_report(results)
        st.image(report_image, caption="AI 분석 리포트")
