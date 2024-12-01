import streamlit as st
import random

def get_quiz_questions(level):
    if level == 1:
        st.write("Choose from these characters:")
        choices = ["碗 (wǎn)", "云吞面 (yún tun miàn)", "警察 (jǐng chá)", 
                  "模型 (mó xíng)", "补习 (bǔ xí)", "最近 (zuì jìn)", "您 (nín)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "这____汤很好喝。": "碗 (wǎn)",
            "我最喜欢吃____。": "云吞面 (yún tun miàn)",
            "____叔叔在指挥交通。": "警察 (jǐng chá)",
            "他做的飞机____很精致。": "模型 (mó xíng)",
            "放学后我要去____。": "补习 (bǔ xí)",
            "____天气变冷了。": "最近 (zuì jìn)",
            "老师，____辛苦了。": "您 (nín)",
            "妈妈买了新的____。": "碗 (wǎn)",
            "____工作很辛苦。": "警察 (jǐng chá)",
            "我____在学画画。": "最近 (zuì jìn)"
        }
    elif level == 2:
        st.write("Choose from these characters:")
        choices = ["尊敬 (zūn jìng)", "长辈 (zhǎng bèi)", "发脾气 (fā pí qi)", 
                  "批评 (pī píng)", "舍不得 (shě bu de)", "吵架 (chǎo jià)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "我们要____老师。": "尊敬 (zūn jìng)",
            "要听____的话。": "长辈 (zhǎng bèi)",
            "不要随便____。": "发脾气 (fā pí qi)",
            "老师____了我。": "批评 (pī píng)",
            "他____离开家。": "舍不得 (shě bu de)",
            "兄弟不要____。": "吵架 (chǎo jià)",
            "爸爸在____我。": "批评 (pī píng)",
            "弟弟又在____。": "发脾气 (fā pí qi)",
            "我很____这本书。": "舍不得 (shě bu de)",
            "要____父母。": "尊敬 (zūn jìng)"
        }
    elif level == 3:
        st.write("Choose from these characters:")
        choices = ["叫醒 (jiào xǐng)", "睁开 (zhēng kāi)", "泪水 (lèi shuǐ)", 
                  "落 (luò)", "后悔 (hòu huǐ)", "说谎 (shuō huǎng)", 
                  "偷 (tōu)", "迷上了 (mí shàng le)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "妈妈早上____我。": "叫醒 (jiào xǐng)",
            "他____眼睛看着我。": "睁开 (zhēng kāi)",
            "____从眼中流出。": "泪水 (lèi shuǐ)",
            "树叶____在地上。": "落 (luò)",
            "我很____没听话。": "后悔 (hòu huǐ)",
            "不要____。": "说谎 (shuō huǎng)",
            "小偷____了东西。": "偷 (tōu)",
            "他____打游戏。": "迷上了 (mí shàng le)",
            "我____做错事。": "后悔 (hòu huǐ)",
            "叶子慢慢地____。": "落 (luò)"
        }

def main():
    st.title("Chinese Characters Quiz - Chapter 3")
    
    st.markdown("""
        <style>
        .stButton > button {
            width: 120px;
            height: 80px;
            margin: 3px;
            white-space: normal;
            word-wrap: break-word;
            font-size: 14px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    if 'level' not in st.session_state:
        st.session_state.level = 1
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answered' not in st.session_state:
        st.session_state.answered = False
    if 'selected_answer' not in st.session_state:
        st.session_state.selected_answer = {}
        
    st.subheader(f"Level {st.session_state.level}")
    st.write("Click the correct character for each sentence!")
    
    questions = get_quiz_questions(st.session_state.level)
    
    for question, correct_answer in questions.items():
        st.write(question)
        
        if st.session_state.level == 1:
            choices = ["碗 (wǎn)", "云吞面 (yún tun miàn)", "警察 (jǐng chá)", 
                      "模型 (mó xíng)", "补习 (bǔ xí)", "最近 (zuì jìn)", "您 (nín)"]
        elif st.session_state.level == 2:
            choices = ["尊敬 (zūn jìng)", "长辈 (zhǎng bèi)", "发脾气 (fā pí qi)", 
                      "批评 (pī píng)", "舍不得 (shě bu de)", "吵架 (chǎo jià)"]
        else:
            choices = ["叫醒 (jiào xǐng)", "睁开 (zhēng kāi)", "泪水 (lèi shuǐ)", 
                      "落 (luò)", "后悔 (hòu huǐ)", "说谎 (shuō huǎng)", 
                      "偷 (tōu)", "迷上了 (mí shàng le)"]
        
        cols = st.columns(len(choices))
        for idx, choice in enumerate(choices):
            with cols[idx]:
                if st.button(choice, key=f"{question}_{choice}"):
                    st.session_state.selected_answer[question] = choice
        
        if question in st.session_state.selected_answer:
            st.write(f"Selected: {st.session_state.selected_answer[question]}")
        
        st.write("---")
    
    if st.button("Check Answers"):
        score = 0
        for question, correct_answer in questions.items():
            if question in st.session_state.selected_answer:
                if st.session_state.selected_answer[question] == correct_answer:
                    score += 1
                    st.success(f"✓ {question} - Correct!")
                else:
                    st.error(f"✗ {question} - Your answer: {st.session_state.selected_answer[question]} | Correct answer: {correct_answer}")
        
        st.session_state.score = score
        st.session_state.answered = True
        
        st.write(f"Your score: {score}/{len(questions)}")
        
        if score == len(questions):
            st.balloons()
            if st.session_state.level < 3:
                st.success(f"Perfect score! Moving to Level {st.session_state.level + 1}! 做得好！")
                if st.button("Next Level"):
                    st.session_state.level += 1
                    st.session_state.score = 0
                    st.session_state.answered = False
                    st.session_state.selected_answer = {}
                    st.experimental_rerun()
            else:
                st.success("🎉 Excellent work! You've mastered all levels of Chapter 3! 太棒了！")
                st.success("Ready for more challenges? Start Chapter 4 to learn new characters! 准备好开始第四章吗？")
        
        if st.button("Try Again"):
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.selected_answer = {}
            st.experimental_rerun()

if __name__ == "__main__":
    main()
