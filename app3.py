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
            "老师，____辛苦了。": "您 (nín)"
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
            "兄弟不要____。": "吵架 (chǎo jià)"
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
            "他____打游戏。": "迷上了 (mí shàng le)"
        }

def main():
    st.title("Chinese Characters Quiz - Chapter 3")
    
    if 'level' not in st.session_state:
        st.session_state.level = 1
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answered' not in st.session_state:
        st.session_state.answered = False
        
    st.subheader(f"Level {st.session_state.level}")
    st.write("Select the correct character for each sentence!")
    
    questions = get_quiz_questions(st.session_state.level)
    
    with st.form(f"quiz_form_level_{st.session_state.level}"):
        user_answers = {}
        for question, correct_answer in questions.items():
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
            
            user_answer = st.radio(
                question,
                choices,
                key=f"{question}_{st.session_state.level}"
            )
            user_answers[question] = user_answer
        
        submit_button = st.form_submit_button("Check Answers")
        
        if submit_button:
            score = 0
            for question, user_answer in user_answers.items():
                if user_answer == questions[question]:
                    score += 1
                    st.success(f"✓ {question} - Correct!")
                else:
                    st.error(f"✗ {question} - Your answer: {user_answer} | Correct answer: {questions[question]}")
            
            st.session_state.score = score
            st.session_state.answered = True
    
    if st.session_state.answered:
        st.write(f"Your score: {st.session_state.score}/{len(questions)}")
        
        if st.session_state.score == len(questions):
            st.balloons()
            if st.session_state.level < 3:
                st.success(f"Perfect score! Moving to Level {st.session_state.level + 1}! 做得好！")
                if st.button("Next Level"):
                    st.session_state.level += 1
                    st.session_state.score = 0
                    st.session_state.answered = False
                    st.experimental_rerun()
            else:
                st.success("🎉 Excellent work! You've mastered all levels of Chapter 3! 太棒了！")
                st.success("Ready for more challenges? Start Chapter 4 to learn new characters! 准备好开始第四章吗？")
        elif st.session_state.score >= len(questions)/2:
            st.success("Good effort! Keep practicing! 继续加油！")
        else:
            st.info("Keep practicing! You'll get better! 继续学习！")
        
        if st.button("Try Again"):
            st.session_state.score = 0
            st.session_state.answered = False
            st.experimental_rerun()

if __name__ == "__main__":
    main()
