import streamlit as st
import time
import random

# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="암호를 풀어라",
    page_icon="🧩",
    layout="centered"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top, #24283b, #0b0d14 70%);
    color: white;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    color: #8be9fd;
    text-shadow: 0 0 15px #00d9ff;
}

.subtitle {
    text-align: center;
    color: #aaa;
    margin-bottom: 25px;
}

.panel {
    background: rgba(20, 23, 35, 0.95);
    border: 2px solid #3b4260;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}

.story {
    background: #111522;
    border-left: 5px solid #8be9fd;
    padding: 18px;
    border-radius: 5px;
    line-height: 1.8;
}

.timer {
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    color: #ff6b6b;
    margin: 10px;
}

.success {
    background: #102c1c;
    border: 2px solid #40d47e;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
}

.failure {
    background: #321313;
    border: 2px solid #ff5555;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
}

.puzzle-title {
    font-size: 25px;
    font-weight: bold;
    color: #f1fa8c;
}

.code-box {
    background: #080a10;
    border: 2px solid #555;
    padding: 20px;
    text-align: center;
    font-size: 35px;
    letter-spacing: 10px;
    border-radius: 8px;
}

.stButton > button {
    width: 100%;
    min-height: 45px;
    background: #20263a;
    color: white;
    border: 1px solid #566080;
    border-radius: 8px;
}

.stButton > button:hover {
    background: #343d5c;
    border-color: #8be9fd;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 게임 초기화
# =========================================================

def new_game():

    st.session_state.started = True

    st.session_state.start_time = time.time()

    # 퍼즐 1
    st.session_state.puzzle1 = False

    # 퍼즐 2
    st.session_state.sequence = []
    st.session_state.sequence_answer = [2, 4, 1, 3]
    st.session_state.puzzle2 = False

    # 퍼즐 3
    st.session_state.puzzle3 = False

    # 최종 암호
    st.session_state.final_code = False

    st.session_state.game_clear = False
    st.session_state.game_over = False


if "started" not in st.session_state:
    st.session_state.started = False


# =========================================================
# 시작 화면
# =========================================================

if not st.session_state.started:

    st.markdown(
        '<div class="title">🧩 암호를 풀어라</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">3분 안에 모든 퍼즐을 해결하라</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="story">

    당신은 정체불명의 방에서 눈을 떴다.

    <br><br>

    방 중앙에는 잠긴 금고가 있다.

    <br>

    금고에는 다음과 같은 문장이 적혀 있다.

    <br><br>

    <b>"세 개의 퍼즐을 풀면 문이 열린다."</b>

    <br><br>

    제한시간은 단 3분.

    <br><br>

    과연 탈출할 수 있을까?

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("▶ 게임 시작"):

        new_game()

        st.rerun()

    st.stop()


# =========================================================
# 성공 화면
# =========================================================

if st.session_state.game_clear:

    st.markdown("""
    <div class="success">

    <h1>🎉 탈출 성공!</h1>

    <p>
    모든 퍼즐을 해결하고 금고를 열었다.
    </p>

    <h2>🔓 문이 열렸다.</h2>

    <p>
    당신은 무사히 방을 빠져나왔다.
    </p>

    <br>

    <b>THE END</b>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("🔄 다시 플레이"):

        new_game()

        st.rerun()

    st.stop()


# =========================================================
# 시간 계산
# =========================================================

elapsed = int(time.time() - st.session_state.start_time)

remaining = max(0, 180 - elapsed)

minutes = remaining // 60
seconds = remaining % 60

st.markdown(
    f'<div class="timer">⏱️ {minutes:02d}:{seconds:02d}</div>',
    unsafe_allow_html=True
)


# =========================================================
# 시간 초과
# =========================================================

if remaining <= 0:

    st.markdown("""
    <div class="failure">

    <h1>💀 시간 초과</h1>

    <p>
    금고의 경고음이 울렸다.
    </p>

    <p>
    모든 장치가 잠겼다.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 다시 시작"):

        new_game()

        st.rerun()

    st.stop()


# =========================================================
# 제목
# =========================================================

st.markdown(
    '<div class="title">🧩 암호를 풀어라</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">SECURITY ROOM</div>',
    unsafe_allow_html=True
)


# =========================================================
# 진행 상황
# =========================================================

solved = sum([
    st.session_state.puzzle1,
    st.session_state.puzzle2,
    st.session_state.puzzle3
])

st.progress(
    solved / 3,
    text=f"퍼즐 진행도 {solved} / 3"
)


# =========================================================
# 퍼즐 1
# =========================================================

st.markdown("""
<div class="panel">

<div class="puzzle-title">
🔢 퍼즐 1 — 숫자의 규칙
</div>

<br>

다음 숫자의 규칙을 찾아 마지막 숫자를 입력하세요.

<br><br>

<b>
2 → 4 → 8 → 16 → ?
</b>

<br><br>

힌트: 같은 규칙으로 계속 증가합니다.

</div>
""", unsafe_allow_html=True)

if not st.session_state.puzzle1:

    answer1 = st.number_input(
        "정답",
        min_value=0,
        max_value=999,
        step=1,
        key="answer1"
    )

    if st.button("퍼즐 1 확인"):

        if answer1 == 32:

            st.session_state.puzzle1 = True

            st.success("정답! 32입니다.")

            st.rerun()

        else:

            st.error("틀렸습니다. 숫자의 변화 규칙을 다시 생각해보세요.")

else:

    st.success("✅ 퍼즐 1 해결 완료")


# =========================================================
# 퍼즐 2
# =========================================================

st.divider()

st.markdown("""
<div class="panel">

<div class="puzzle-title">
🔘 퍼즐 2 — 버튼의 순서
</div>

<br>

다음 순서대로 버튼을 눌러야 합니다.

<br><br>

<b>
2 → 4 → 1 → 3
</b>

<br>

현재 입력:

</div>
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="code-box">
    {" ".join(map(str, st.session_state.sequence))}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

if not st.session_state.puzzle2:

    cols = st.columns(4)

    for i in range(1, 5):

        with cols[i - 1]:

            if st.button(str(i), key=f"button_{i}"):

                current = st.session_state.sequence

                expected = st.session_state.sequence_answer[
                    len(current)
                ]

                if i == expected:

                    current.append(i)

                    if len(current) == 4:

                        st.session_state.puzzle2 = True

                    st.rerun()

                else:

                    st.session_state.sequence = []

                    st.error(
                        "❌ 틀린 버튼입니다. 순서가 초기화되었습니다."
                    )

                    st.rerun()

else:

    st.success("✅ 퍼즐 2 해결 완료")


# =========================================================
# 퍼즐 3
# =========================================================

st.divider()

st.markdown("""
<div class="panel">

<div class="puzzle-title">
🧠 퍼즐 3 — 논리 문제
</div>

<br>

방에는 세 개의 상자가 있다.

<br>

🔴 빨간 상자<br>
🔵 파란 상자<br>
🟢 초록 상자

<br><br>

단 하나의 상자에 열쇠가 들어 있다.

<br>

벽에는 다음 문장이 적혀 있다.

<br>

<b>
"열쇠는 빨간색이 아니다."
<br>
"열쇠는 초록색에 있다."
</b>

<br><br>

두 문장 중 <b>오직 하나만 참</b>이라면,
열쇠가 들어 있는 상자는?

</div>
""", unsafe_allow_html=True)


if not st.session_state.puzzle3:

    answer3 = st.radio(
        "정답을 선택하세요.",
        [
            "🔴 빨간 상자",
            "🔵 파란 상자",
            "🟢 초록 상자"
        ],
        key="answer3"
    )

    if st.button("퍼즐 3 확인"):

        # 초록:
        # "열쇠는 빨간색이 아니다" = True
        # "열쇠는 초록색이다" = True
        # → 둘 다 참이므로 조건 불만족
        #
        # 빨강:
        # 첫 문장 False
        # 두 번째 False
        #
        # 파랑:
        # 첫 문장 True
        # 두 번째 False
        # → 정확히 하나만 참

        if answer3 == "🔵 파란 상자":

            st.session_state.puzzle3 = True

            st.success("정답! 파란 상자입니다.")

            st.rerun()

        else:

            st.error(
                "조건을 다시 확인해보세요. "
                "두 문장 중 정확히 하나만 참이어야 합니다."
            )

else:

    st.success("✅ 퍼즐 3 해결 완료")


# =========================================================
# 최종 금고
# =========================================================

st.divider()

st.markdown("""
<div class="panel">

<div class="puzzle-title">
🔐 최종 금고
</div>

<br>

세 개의 퍼즐을 모두 해결하면
최종 비밀번호를 입력할 수 있습니다.

<br><br>

<b>
퍼즐 1 → 32<br>
퍼즐 2 → 2413<br>
퍼즐 3 → 파란색
</b>

<br><br>

금고에는 다음 문장이 적혀 있다.

<br>

<b>
"숫자를 순서대로 이어 붙여라."
</b>

</div>
""", unsafe_allow_html=True)


if not (
    st.session_state.puzzle1
    and st.session_state.puzzle2
    and st.session_state.puzzle3
):

    st.info(
        "🔒 아직 금고가 잠겨 있습니다. "
        "먼저 세 개의 퍼즐을 모두 해결하세요."
    )

else:

    st.success("🔓 모든 퍼즐을 해결했습니다!")

    final_code = st.text_input(
        "최종 비밀번호 6자리를 입력하세요.",
        max_chars=6,
        placeholder="예: 322413",
        key="final_code_input"
    )

    if st.button("🔓 금고 열기"):

        if final_code == "322413":

            st.session_state.game_clear = True

            st.rerun()

        else:

            st.error(
                "❌ 비밀번호가 틀렸습니다."
            )


# =========================================================
# 힌트
# =========================================================

st.divider()

with st.expander("💡 힌트 보기"):

    st.write("**퍼즐 1:** 숫자가 어떻게 변하는지 확인하세요.")

    st.write(
        "**퍼즐 2:** 화면에 표시된 순서 "
        "`2 → 4 → 1 → 3`을 그대로 입력하세요."
    )

    st.write(
        "**퍼즐 3:** 두 문장 중 정확히 하나만 참이어야 합니다."
    )

    st.write(
        "**최종 암호:** 퍼즐 1과 퍼즐 2의 숫자를 이어 붙입니다."
    )


# =========================================================
# 다시 시작
# =========================================================

st.divider()

if st.button("🔄 게임 초기화"):

    new_game()

    st.rerun()


# =========================================================
# 자동 시간 갱신
# =========================================================

time.sleep(1)

st.rerun()
