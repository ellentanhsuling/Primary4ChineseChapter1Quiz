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
            "阳光____地照在身上。": "暖暖 (nuǎn nuǎn)",
            "妈妈给我买了新____。": "帽子 (mào zi)",
            "这件____很保暖。": "外套 (wài tào)",
            "老师教我们新的____。": "词语 (cí yǔ)"
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
            "他____我一本书。": "递给 (dì gěi)",
            "妹妹____我吃的。": "递给 (dì gěi)",
            "我的____住在北京。": "姑姑 (gū gu)",
            "他____完成作业。": "急急忙忙 (jí jí máng máng)",
            "人太多，很____。": "挤 (jǐ)"
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
            "我和____去公园。": "姑姑 (gū gu)",
            "他____做出了决定。": "灵机一动 (líng jī yí dòng)",
            "汤里的____很新鲜。": "鱼丸 (yú wán)",
            "昨天下了一场____。": "倾盆大雨 (qīng pén dà yǔ)",
            "小朋友们____黑暗。": "不怕 (bú pà)"
        }

def main():
    st.title("Chinese Characters Quiz - Chapter 2")
    
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
                st.success("🎉 Excellent work! You've mastered all levels of Chapter 2! 太棒了！")
                st.success("Ready for more challenges? Start Chapter 3 to learn new characters! 准备好开始第三章吗？")
        
        if st.button("Try Again"):
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.selected_answer = {}
            st.experimental_rerun()

if __name__ == "__main__":
    main()
