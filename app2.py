import streamlit as st
import random

def get_quiz_questions(level):
    if level == 1:
        st.write("Choose from these characters:")
        choices = ["不怕 (bú pà)", "词语 (cí yǔ)", "表示 (biǎo shì)", 
                  "苹果 (píng guǒ)", "暖暖 (nuǎn nuǎn)", "外套 (wài tào)", 
                  "帽子 (mào zi)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "天气冷了，我穿上____。": "外套 (wài tào)",
            "冬天戴上____可以保暖。": "帽子 (mào zi)",
            "他____黑暗的环境。": "不怕 (bú pà)",
            "这个____的意思是什么？": "词语 (cí yǔ)",
            "他点头____同意。": "表示 (biǎo shì)",
            "这个____又大又红。": "苹果 (píng guǒ)",
            "阳光____地照在身上。": "暖暖 (nuǎn nuǎn)"
        }
    elif level == 2:
        st.write("Choose from these characters:")
        choices = ["急急忙忙 (jí jí máng máng)", "鼓起 (gǔ qǐ)", "靠 (kào)", 
                  "挤 (jǐ)", "姑姑 (gū gu)", "递给 (dì gěi)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "他____地跑出门。": "急急忙忙 (jí jí máng máng)",
            "小明____勇气说话。": "鼓起 (gǔ qǐ)",
            "请不要____着墙。": "靠 (kào)",
            "公交车上很____。": "挤 (jǐ)",
            "____买了礼物给我。": "姑姑 (gū gu)",
            "他____我一本书。": "递给 (dì gěi)"
        }
    elif level == 3:
        st.write("Choose from these characters:")
        choices = ["灵机一动 (líng jī yí dòng)", "鱼丸 (yú wán)", 
                  "倾盆大雨 (qīng pén dà yǔ)", "不怕 (bú pà)", 
                  "递给 (dì gěi)", "姑姑 (gū gu)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "他____想到了好主意。": "灵机一动 (líng jī yí dòng)",
            "这个____很好吃。": "鱼丸 (yú wán)",
            "外面下着____。": "倾盆大雨 (qīng pén dà yǔ)",
            "我们____困难。": "不怕 (bú pà)",
            "请____我那本书。": "递给 (dì gěi)",
            "我和____去公园。": "姑姑 (gū gu)"
        }

def main():
    st.title("Chinese Characters Quiz - Chapter 2")
    
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
            # Get choices based on current level
            if st.session_state.level == 1:
                choices = ["不怕 (bú pà)", "词语 (cí yǔ)", "表示 (biǎo shì)", 
                          "苹果 (píng guǒ)", "暖暖 (nuǎn nuǎn)", "外套 (wài tào)", 
                          "帽子 (mào zi)"]
            elif st.session_state.level == 2:
                choices = ["急急忙忙 (jí jí máng máng)", "鼓起 (gǔ qǐ)", "靠 (kào)", 
                          "挤 (jǐ)", "姑姑 (gū gu)", "递给 (dì gěi)"]
            else:
                choices = ["灵机一动 (líng jī yí dòng)", "鱼丸 (yú wán)", 
                          "倾盆大雨 (qīng pén dà yǔ)", "不怕 (bú pà)", 
                          "递给 (dì gěi)", "姑姑 (gū gu)"]
            
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
