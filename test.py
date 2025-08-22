
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 가상의 혈액형별 헌혈 참여율 데이터 (실제 통계 기반 예시)
# -----------------------------
blood_donation_data = {
    "혈액형": ["A형", "B형", "O형", "AB형"],
    "헌혈 참여율(%)": [34, 25, 32, 9]
}
df = pd.DataFrame(blood_donation_data)

# -----------------------------
# Streamlit 앱 설정
# -----------------------------
st.set_page_config(page_title="혈액형별 헌혈 참여율", page_icon="🩸", layout="centered")

# CSS로 디자인 강화 (깔끔 + 포인트 레드)
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
        }
        h1 {
            color: #d90429;
            text-align: center;
            font-size: 45px !important;
            font-weight: bold;
        }
        h2 {
            color: #d90429;
            font-size: 30px !important;
            margin-top: 20px;
        }
        .result-box {
            text-align: center;
            border: 3px solid #d90429;
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            background-color: #fff5f5;
        }
        .highlight {
            color: #d90429;
            font-size: 26px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 메인 제목
# -----------------------------
st.markdown("<h1>🩸 혈액형별 헌혈 참여율 분석</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center;'>당신의 혈액형, 나이, 지역 정보를 입력하면 실제 헌혈 통계와 비교해 드립니다.</p>", unsafe_allow_html=True)

# -----------------------------
# 사용자 입력
# -----------------------------
st.markdown("<h2>👤 사용자 정보 입력</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("나이 입력", min_value=10, max_value=100, value=20, step=1)
with col2:
    region = st.text_input("지역 입력 (예: 광주광역시, 서울특별시)")

blood_type = st.selectbox("혈액형 선택", ["A형", "B형", "O형", "AB형"])

# -----------------------------
# 결과 분석
# -----------------------------
st.markdown("<h2>📊 결과 분석</h2>", unsafe_allow_html=True)

user_rate = df.loc[df["혈액형"] == blood_type, "헌혈 참여율(%)"].values[0]

# 결과 박스 (깔끔 + 간지)
st.markdown(f"""
    <div class="result-box">
        <p>나이: <b>{age}세</b></p>
        <p>지역: <b>{region}</b></p>
        <p>혈액형: <b style='color:#d90429; font-size:22px;'>{blood_type}</b></p>
        <p class="highlight">➡ {blood_type}의 헌혈 참여율은 {user_rate}% 입니다!</p>
    </div>
""", unsafe_allow_html=True)

# -----------------------------
# 그래프
# -----------------------------
st.markdown("<h2>📈 혈액형별 헌혈 참여율 비교</h2>", unsafe_allow_html=True)

fig, ax = plt.subplots()
ax.bar(df["혈액형"], df["헌혈 참여율(%)"], color="#f28b82")
ax.set_xlabel("혈액형")
ax.set_ylabel("헌혈 참여율(%)")
ax.set_title("혈액형별 헌혈 참여율")

highlight = df.loc[df["혈액형"] == blood_type, "헌혈 참여율(%)"].values[0]
ax.bar(blood_type, highlight, color="#d90429")

st.pyplot(fig)

# -----------------------------
# 추가 안내
# -----------------------------
st.info("💡 참고: 실제 헌혈 참여율은 대한적십자사 혈액관리본부 통계를 기반으로 하며, 본 앱은 교육용으로 단순화한 데이터를 사용했습니다.")
# -----------------------------
# 헌혈 장점 및 사용 과정 안내
# -----------------------------
st.markdown("<h2 style='color:red;'>🩸 헌혈을 하면 좋은 점</h2>", unsafe_allow_html=True)
st.write("""
- 다른 사람의 생명을 살릴 수 있습니다.  
- 혈액 검사를 통해 자신의 건강 상태를 확인할 수 있습니다.  
- 헌혈 후 제공되는 간단한 검사 결과로 **빈혈, 간 기능 이상** 등을 조기에 알 수 있습니다.  
- 정기적으로 헌혈을 하면 **혈액 순환이 촉진**되어 건강 유지에 도움이 될 수 있습니다.
""")

st.markdown("<h2 style='color:red;'>🩸 헌혈된 혈액은 이렇게 사용됩니다</h2>", unsafe_allow_html=True)
st.write("""
1. **채혈** – 헌혈자의 혈액은 안전하게 채취됩니다.  
2. **검사** – 감염병(간염, HIV 등) 여부를 철저히 검사합니다.  
3. **성분 분리** – 혈액은 **적혈구, 혈장, 혈소판**으로 분리되어 각각 필요한 환자에게 전달됩니다.  
4. **환자 치료에 사용** –  
   - 수혈이 필요한 **교통사고 환자**  
   - **수술 환자**  
   - **백혈병·혈액암 환자** 등에게 큰 도움이 됩니다.  
5. 헌혈 한 번으로 **최대 3명의 생명을 구할 수 있습니다.**
""")

st.success("💡 당신의 작은 참여가 누군가에겐 큰 희망이 됩니다!")

