# streamlit에 쓸 파일
# ml은 colab
import streamlit as st

st.title("MachineLearning")
st.header("주식 예측 프로그램")
companys = st.text_input

st.write(companys)