import streamlit as st
import random

# 🌟 페이지 세팅
st.set_page_config(page_title="💕 두 사람의 어울림 퍼센트 💕", page_icon="💖", layout="wide")

# 🌈 CSS 꾸미기
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #FF9A9E 0%, #FAD0C4 100%);
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .title {
        font-size: 60px !important;
        color: #FF1493;
        text-align: center;
        text-shadow: 3px 3px #FFD700;
    }
    .subtitle {
        font-size: 25px;
        text-align: center;
        color: #FF69B4;
        margin-bottom: 40px;
    }
    .result-box {
        background: white;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0px 5px 30px rgba(255,105,180,0.6);
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-top: 30px;
        animation: glow 1.5s infinite alternate;
    }
    @keyframes glow {
        from { box-shadow: 0px 0px 20px #FF69B4; }
        to { box-shadow: 0px 0px 40px #FF1493; }
    }
    </style>
""", unsafe_allow_html=True)

# 🎉 타이틀
st.markdown('<div class="title">💘 두 사람의 어울림 퍼센트 💘</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">하트 뿅뿅 터지는 궁합 계산기 💕✨</div>', unsafe_allow_html=True)

# 📝 이름 입력
name1 = st.text_input("💖 첫 번째 이름을 입력하세요")
name2 = st.text_input("💖 두 번째 이름을 입력하세요")

# 🚀 버튼 클릭 시 결과
if st.button("💝 어울림 퍼센트 계산하기 💝"):
    if name1.strip() and name2.strip():
        # 랜덤 궁합 퍼센트 (항상 고정 원하면 해시 기반으로 바꿀 수도 있음)
        percent = random.randint(50, 100)

        hearts = "💖" * (percent // 10)
        st.markdown(
            f'<div class="result-box">✨ {name1} 💕 {name2} ✨<br><br>'
            f'💘 어울림 지수: <span style="color:#FF1493">{percent}%</span> 💘<br><br>{hearts}</div>',
            unsafe_allow_html=True
        )
        st.balloons()
        st.success("🌈 두 사람의 인연은 운명! 🌟")
    else:
        st.warning("⚠️ 두 사람의 이름을 모두 입력해주세요!")

