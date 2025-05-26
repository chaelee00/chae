import streamlit as st
import pandas as pd
import plotly.express as px

# 구글 드라이브 CSV 주소
CSV_URL = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    return pd.read_csv(CSV_URL)

df = load_data()

st.title("📊 산점도 시각화 앱")

st.subheader("데이터 미리보기")
st.dataframe(df.head())

st.subheader("수치형 열만 선택 (산점도용)")
# 수치형 열만 추출
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

# 산점도 축 선택
x_col = st.selectbox("X축", numeric_cols)
y_col = st.selectbox("Y축", numeric_cols)

# 산점도 그리기
fig = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col} 산점도")
st.plotly_chart(fig)
