import streamlit as st
import random

def get_quiz_questions(level):
    if level == 1:
        st.write("Choose from these characters:")
        choices = ["不怕", "词语", "表示", "苹果", "暖暖", "外套", "帽子"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "天气冷了，我穿上____。": "外套",
            "冬天戴上____可以保暖。": "帽子",
            "他____黑暗的环境。": "不怕",
            "这个____的意思是什么？": "词语",
            "他点头____同意。": "表示",
            "这个____又大又红。": "苹果",
            "阳光____地照在身上。": "暖暖",
            "妈妈给我买了新____。": "帽子",
            "这件____很保暖。": "外套",
            "老师教我们新的____。": "词语"
        }
    elif level == 2:
        st.write("Choose from these characters:")
        choices = ["急急忙忙", "鼓起", "靠", "挤", "姑姑", "递给"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "他____地跑出门。": "急急忙忙",
            "小明____勇气说话。": "鼓起",
            "请不要____着墙。": "靠",
            "公交车上很____。": "挤",
            "____买了礼物给我。": "姑姑",
            "他____我一本书。": "递给",
            "妹妹____我吃的。": "递给",
            "我的____住在北京。": "姑姑",
            "他____完成作业。": "急急忙忙",
            "人太多，很____。": "挤"
        }
    elif level == 3:
        st.write("Choose from these characters:")
        choices = ["灵机一动", "鱼丸", "倾盆大雨", "不怕", "递给", "姑姑"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "他____想到了好主意。": "灵机一动",
            "这个____很好吃。": "鱼丸",
            "外面下着____。": "倾盆大雨",
            "我们____困难。": "不怕",
            "请____我那本书。": "递给",
            "我和____去公园。": "姑姑",
            "他____做出了决定。": "灵机一动",
            "汤里的____很新鲜。": "鱼丸",
            "昨天下了一场____。": "倾盆大雨",
            "小朋友们____黑暗。": "不怕"
        }

def main():
    st.title("Chinese Characters Quiz - Chapter 2")
    
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
                st.success("🎉 Excellent work! You've mastered all levels of Chapter 2! 太棒了！")
                st.success("Ready for more challenges? Start Chapter 3 to learn new characters! 准备好开始第三章吗？")
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
