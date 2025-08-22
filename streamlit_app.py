
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="에겐-테토 유형 진단")

# 에겐/테토 유형별 특징 설명
EGEN_DESCRIPTION = """
**당신은 '에겐(Estrogen)' 유형입니다!**

감수성이 풍부하고 공감 능력이 뛰어난 당신은 주변 사람들을 편안하게 만드는 따뜻한 마음을 가졌습니다. [1, 7, 10] 갈등을 피하고 조화로운 관계를 중요하게 생각하며, 타인의 감정을 섬세하게 살피는 배려심이 깊습니다. [9]

**주요 특징:**
- **관계 중심적:** 사람들과 깊이 있는 관계를 맺는 것을 중요하게 생각합니다. [9]
- **뛰어난 공감 능력:** 다른 사람의 감정을 잘 이해하고 위로를 잘 건넵니다. [10]
- **섬세함과 배려:** 말과 행동이 다정하고, 상대방을 먼저 생각하는 경향이 있습니다. [8]
- **조화 추구:** 갈등 상황을 불편해하며, 평화로운 해결을 선호합니다.
"""

TETO_DESCRIPTION = """
**당신은 '테토(Testosterone)' 유형입니다!**

독립적이고 자기 주장이 뚜렷한 당신은 논리적이고 목표 지향적인 성향을 가지고 있습니다. [2, 5] 문제 상황이 발생했을 때 감정보다는 이성적인 판단으로 해결책을 찾는 것을 선호합니다. [3]

**주요 특징:**
- **독립성과 자기주도성:** 혼자서도 일을 잘 처리하며, 자신의 신념과 기준이 명확합니다. [4]
- **논리적 사고:** 감정적인 호소보다는 명확한 사실과 논리에 더 끌립니다. [3]
- **목표 지향적:** 한번 목표를 설정하면 강한 추진력으로 밀고 나갑니다. [7]
- **솔직한 표현:** 감정을 숨기지 않고 직선적으로 표현하는 경향이 있습니다. [4]
"""

# 진단 문항
questions = [
    "나는 문제 해결 시 논리적 분석보다 사람들의 감정을 먼저 고려하는 편이다.",
    "상대방과 갈등이 생겼을 때, 관계가 불편해지는 것이 싫어 내 의견을 잠시 접어둘 때가 많다.",
    "친구의 고민을 들어줄 때, 해결책을 제시하기보다 주로 감정적인 위로와 공감을 표현한다.",
    "나는 계획을 세우고 목표를 달성하는 과정에서 성취감을 느낀다.",
    "주변 사람들은 나를 '다정하다', '따뜻하다'고 평가하는 경우가 많다.",
    "어떤 일을 결정할 때, 다른 사람의 의견을 듣는 것보다 나의 기준과 원칙을 따르는 것이 더 중요하다.",
    "나는 감정 표현이 풍부하다는 말을 자주 듣는다.",
    "결과가 불확실하더라도, 도전적인 목표에 끌리는 경향이 있다.",
    "나는 단체 활동에서 리더 역할을 맡는 것을 즐긴다.",
    "나는 다른 사람의 미묘한 감정 변화를 빠르게 알아차리는 편이다."
]

# 앱 제목 및 소제목
st.title("나는 에겐일까, 테토일까?")
st.subheader("간단한 테스트로 자신이 에겐인지 테토인지 알아보자!")
st.write("---")

# 세션 상태 초기화
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
    st.session_state.scores = {'egen': 0, 'teto': 0}
    st.session_state.answers = [None] * len(questions)

# 라디오 버튼 문항 표시
for i, question in enumerate(questions):
    st.session_state.answers[i] = st.radio(
        f"**질문 {i+1}.** {question}",
        ('그렇다', '아니다'),
        key=f'q{i}',
        horizontal=True
    )

st.write("---")

# 제출 버튼
if st.button("결과 확인하기"):
    st.session_state.submitted = True
    
    # 점수 계산
    egen_score = 0
    teto_score = 0
    
    # '그렇다'를 선택했을 때 각 유형의 점수를 올리는 문항 인덱스
    egen_questions_indices = [0, 1, 2, 4, 6, 9]
    teto_questions_indices = [3, 5, 7, 8]
    
    for i, answer in enumerate(st.session_state.answers):
        if answer == '그렇다':
            if i in egen_questions_indices:
                egen_score += 1
            elif i in teto_questions_indices:
                teto_score += 1
        else: # '아니다'를 선택했을 때
            if i in egen_questions_indices:
                teto_score += 1
            elif i in teto_questions_indices:
                egen_score += 1
                
    st.session_state.scores = {'egen': egen_score, 'teto': teto_score}

# 결과 출력
if st.session_state.submitted:
    st.write("## 📜 당신의 유형 진단 결과는...")

    egen_score = st.session_state.scores['egen']
    teto_score = st.session_state.scores['teto']
    
    st.info(f"에겐 점수: **{egen_score}점** / 테토 점수: **{teto_score}점**")

    if egen_score >= teto_score:
        st.success(EGEN_DESCRIPTION)
    else:
        st.warning(TETO_DESCRIPTION)
        
    st.markdown("<br><p style='text-align: center; color: grey;'>이 테스트는 재미를 위해 만들어졌으며, 과학적 근거는 없습니다.</p>", unsafe_allow_html=True)