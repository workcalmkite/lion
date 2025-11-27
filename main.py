import streamlit as st
import time
import random

from games.rock_paper_scissors import rock_paper_scissors
from games.clicker import clicker_game
from games.quiz import quiz_game
from games.number_guess import number_guess_game
from games.timing_stop import timing_stop
from games.minesweeper_mini import minesweeper_mini
from games.word_shuffle import word_shuffle
from games.dice_battle import dice_battle
from games.memory_card import memory_card
from games.updown import updown_game
from games.fast_math import fast_math
from games.typing_game import typing_game

st.set_page_config(
    page_title="🎮 10분마다 새로 태어나는 게임",
    page_icon="🎲",
    layout="centered"
)

GAME_LIST = [
    ("가위바위보", rock_paper_scissors),
    ("클리커 게임", clicker_game),
    ("퀴즈 게임", quiz_game),
    ("숫자 맞추기", number_guess_game),
    ("타이밍 스탑", timing_stop),
    ("미니 지뢰찾기", minesweeper_mini),
    ("단어 섞기", word_shuffle),
    ("주사위 배틀", dice_battle),
    ("메모리 카드", memory_card),
    ("업다운 게임", updown_game),
    ("빠른 사칙연산", fast_math),
    ("타자 연습", typing_game)
]

REFRESH_INTERVAL = 10 * 60


def get_current_game():
    slot = int(time.time() // REFRESH_INTERVAL)
    random.seed(slot)
    return random.choice(GAME_LIST)


def main():
    st.title("🎮 10분마다 새로운 게임이 생성되는 공간")

    game_name, game_func = get_current_game()

    now = time.time()
    seconds_left = REFRESH_INTERVAL - (now % REFRESH_INTERVAL)
    minutes = int(seconds_left // 60)
    seconds = int(seconds_left % 60)

    st.markdown(
        f"""
        <div style="padding:20px;border-radius:12px;background:#1f2937;color:white;">
            <h2>🎲 현재 게임: {game_name}</h2>
            <p>다음 게임까지 남은 시간: <b>{minutes}분 {seconds}초</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(1 - seconds_left / REFRESH_INTERVAL)

    st.divider()
    st.subheader("🕹 게임 공간")

    game_func()


if __name__ == "__main__":
    main()
