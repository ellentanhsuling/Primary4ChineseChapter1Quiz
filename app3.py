import streamlit as st
import random

def get_quiz_questions(level):
    if level == 1:
        st.write("Choose from these characters:")
        choices = ["碗", "云吞面", "警察", "模型", "补习", "最近", "您"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "这____汤很好喝。": "碗",
            "我最喜欢吃____。": "云吞面",
            "____叔叔在指挥交通。": "警察",
            "他做的飞机____很精致。": "模型",
            "放学后我要去____。": "补习",
            "____天气变冷了。": "最近",
            "老师，____辛苦了。": "您",
            "妈妈买了新的____。": "碗",
            "____工作很辛苦。": "警察",
            "我____在学画画。": "最近"
        }
    elif level == 2:
        st.write("Choose from these characters:")
        choices = ["尊敬", "长辈", "发脾气", "批评", "舍不得", "吵架"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "我们要____老师。": "尊敬",
            "要听____的话。": "长辈",
            "不要随便____。": "发脾气",
            "老师____了我。": "批评",
            "他____离开家。": "舍不得",
            "兄弟不要____。": "吵架",
            "爸爸在____我。": "批评",
            "弟弟又在____。": "发脾气",
            "我很____这本书。": "舍不得",
            "要____父母。": "尊敬"
        }
    elif level == 3:
        st.write("Choose from these characters:")
        choices = ["叫醒", "睁开", "泪水", "落", "后悔", "说谎", "偷", "迷上了"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "妈妈早上____我。": "叫醒",
            "他____眼睛看着我。": "睁开",
            "____从眼中流出。": "泪水",
            "树叶____在地上。": "落",
            "我很____没听话。": "后悔",
            "不要____。": "说谎",
            "小偷____了东西。": "偷",
            "他____打游戏。": "迷上了",
            "我____做错事。": "后悔",
            "叶子慢慢地____。": "落"
        }

def main():
    st.title("Chinese Characters Quiz - Chapter 3")
    
    # Initialize session state
    if 'level' not in st.session_state:
        st.session_state.level = 1
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answered' not in st.session_state:
        st.session_state.answered = False
        
    # Display current level
    st.subheader(f"Level {st.session_state.level}")
    st.write("Fill in the blanks with the correct characters!")
    
    # Get questions for current level
    questions = get_quiz_questions(st.session_state.level)
    
    # Create form for quiz
    with st.form(f"quiz_form_level_{st.session_state.level}"):
        user_answers = {}
        for question, correct_answer in questions.items():
            user_answer = st.text_input(question, key=f"{question}_{st.session_state.level}")
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
