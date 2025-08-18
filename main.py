import streamlit as st

# 🌟 웹앱 기본 세팅
st.set_page_config(page_title="MBTI 진로 추천 🎭", page_icon="🌟", layout="centered")

# 🌈 타이틀
st.title("✨ MBTI 기반 진로 추천 사이트 ✨")
st.markdown("당신의 MBTI에 맞는 **최고의 직업**을 찾아드릴게요! 💼🌍🚀")

# 🎨 스타일 강조
st.markdown("""
    <style>
    .stSelectbox label {
        font-size: 20px;
        font-weight: bold;
        color: #FF69B4;
    }
    .stTitle, h1, h2, h3 {
        text-align: center;
        color: #FF1493;
    }
    </style>
""", unsafe_allow_html=True)

# 📌 MBTI 리스트
mbti_list = [
    "ISTJ 🧑‍💼", "ISFJ 🤗", "INFJ 🌌", "INTJ 🧠",
    "ISTP 🛠️", "ISFP 🎨", "INFP ✨", "INTP 📚",
    "ESTP 🎉", "ESFP 🎭", "ENFP 🌈", "ENTP ⚡",
    "ESTJ 📊", "ESFJ 💕", "ENFJ 🌟", "ENTJ 🏆"
]

# 🧩 추천 직업 데이터
job_recommendations = {
    "ISTJ 🧑‍💼": "공무원, 회계사, 군인 🏛️🪖",
    "ISFJ 🤗": "간호사, 교사, 사회복지사 🏥📚",
    "INFJ 🌌": "심리상담가, 작가, 연구원 🧘‍♀️📖🔬",
    "INTJ 🧠": "데이터 과학자, 전략가, 연구개발자 💻📊",
    "ISTP 🛠️": "엔지니어, 파일럿, 탐험가 🛠️✈️",
    "ISFP 🎨": "디자이너, 예술가, 음악가 🎶🎨",
    "INFP ✨": "작가, 상담사, 인권운동가 📖💬✊",
    "INTP 📚": "교수, 프로그래머, 철학자 🖥️📚",
    "ESTP 🎉": "기업가, 운동선수, 배우 🏃‍♂️🎬",
    "ESFP 🎭": "가수, 방송인, 이벤트 기획자 🎤🎪",
    "ENFP 🌈": "마케터, 크리에이터, 여행작가 🌍📸",
    "ENTP ⚡": "벤처사업가, 발명가, 토론가 🚀🧩",
    "ESTJ 📊": "경영자, 판사, 장교 👩‍⚖️📈",
    "ESFJ 💕": "교사, 간호사, 상담가 🏫❤️",
    "ENFJ 🌟": "리더, 교육자, 사회운동가 🌟📚",
    "ENTJ 🏆": "CEO, 정치가, 전략가 🏆🏛️"
}

# 🎯 MBTI 선택
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택해주세요!", mbti_list)

# 🚀 결과 출력
if selected_mbti:
    st.subheader(f"🌟 {selected_mbti} 에게 어울리는 직업은?")
    st.success(job_recommendations[selected_mbti])

    st.balloons()  # 🎈 화려한 효과!
    st.markdown("🔥 당신의 미래는 무궁무진해요! 🔥")

