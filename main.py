import streamlit as st
import random

# 🌟 페이지 세팅
st.set_page_config(page_title="MBTI 진로 추천 🎭", page_icon="🌈", layout="wide")

# 🌈 CSS로 쌈뽕하게 꾸미기
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .title {
        font-size: 50px !important;
        color: #FF1493;
        text-align: center;
        text-shadow: 2px 2px #FFD700;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #FF69B4;
        margin-bottom: 30px;
    }
    .job-box {
        background: white;
        padding: 25px;
        border-radius: 25px;
        box-shadow: 0px 5px 20px rgba(255,105,180,0.6);
        text-align: center;
        font-size: 25px;
        margin-top: 20px;
        animation: glow 2s infinite alternate;
    }
    @keyframes glow {
        from { box-shadow: 0px 0px 15px #FF69B4; }
        to { box-shadow: 0px 0px 25px #FFD700; }
    }
    </style>
""", unsafe_allow_html=True)

# 🎉 타이틀
st.markdown('<div class="title">✨ MBTI 진로 추천 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🌈 나의 성격 유형에 맞는 찰떡 직업 찾기 💼🚀</div>', unsafe_allow_html=True)

# 📌 MBTI 리스트
mbti_list = [
    "ISTJ 🧑‍💼", "ISFJ 🤗", "INFJ 🌌", "INTJ 🧠",
    "ISTP 🛠️", "ISFP 🎨", "INFP ✨", "INTP 📚",
    "ESTP 🎉", "ESFP 🎭", "ENFP 🌈", "ENTP ⚡",
    "ESTJ 📊", "ESFJ 💕", "ENFJ 🌟", "ENTJ 🏆"
]

# 🧩 추천 직업 데이터
job_recommendations = {
    "ISTJ 🧑‍💼": "📊 공무원, 회계사, 군인 🏛️🪖",
    "ISFJ 🤗": "🤲 간호사, 교사, 사회복지사 🏥📚",
    "INFJ 🌌": "🌌 심리상담가, 작가, 연구원 🧘‍♀️📖🔬",
    "INTJ 🧠": "🧠 데이터 과학자, 전략가, 연구개발자 💻📊",
    "ISTP 🛠️": "⚙️ 엔지니어, 파일럿, 탐험가 🛠️✈️",
    "ISFP 🎨": "🎨 디자이너, 예술가, 음악가 🎶🎨",
    "INFP ✨": "✨ 작가, 상담사, 인권운동가 📖💬✊",
    "INTP 📚": "📚 교수, 프로그래머, 철학자 🖥️📚",
    "ESTP 🎉": "🎉 기업가, 운동선수, 배우 🏃‍♂️🎬",
    "ESFP 🎭": "🎭 가수, 방송인, 이벤트 기획자 🎤🎪",
    "ENFP 🌈": "🌈 마케터, 크리에이터, 여행작가 🌍📸",
    "ENTP ⚡": "⚡ 벤처사업가, 발명가, 토론가 🚀🧩",
    "ESTJ 📊": "📊 경영자, 판사, 장교 👩‍⚖️📈",
    "ESFJ 💕": "💕 교사, 간호사, 상담가 🏫❤️",
    "ENFJ 🌟": "🌟 리더, 교육자, 사회운동가 🌟📚",
    "ENTJ 🏆": "🏆 CEO, 정치가, 전략가 🏛️🚀"
}

# 🎯 MBTI 선택
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택해주세요!", mbti_list)

# 🚀 결과 출력
if selected_mbti:
    st.markdown(f'<div class="job-box">🌟 {selected_mbti} 에게 어울리는 직업은?<br><br>{job_recommendations[selected_mbti]}</div>', unsafe_allow_html=True)
    st.balloons()
    st.success("✨ 당신의 미래는 무궁무진합니다! ✨")
    st.markdown("🔥 더 큰 꿈을 향해 달려가 보세요! 🚀🌍")

    # 랜덤 보너스 직업 추천 🎁
    if st.button("🎁 보너스 랜덤 직업 추천 받기!"):
        random_job = random.choice(list(job_recommendations.values()))
        st.info(f"🌈 깜짝 추천! 당신이 도전해볼 수도 있는 직업은 👉 {random_job}")
