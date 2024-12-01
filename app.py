import streamlit as st
import random

def get_quiz_questions(level):
    if level == 1:
        st.write("Choose from these characters:")
        choices = ["解开 (jiě kāi)", "了解 (liǎo jiě)", "解释 (jiě shì)", "解决 (jiě jué)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "当我们遇到问题时，要学会自己____它。": "解决 (jiě jué)",
            "老师____了这道数学题的做法。": "解释 (jiě shì)",
            "请帮我____这个绳结。": "解开 (jiě kāi)",
            "我很想____这件事情的真相。": "了解 (liǎo jiě)",
            "让我们一起____这个难题。": "解决 (jiě jué)",
            "他需要____这个复杂的概念。": "了解 (liǎo jiě)",
            "妈妈正在____给我们做饭的过程。": "解释 (jiě shì)",
            "小明试图____缠在一起的耳机线。": "解开 (jiě kāi)"
        }
    elif level == 2:
        st.write("Choose from these characters:")
        choices = ["播种 (bō zhǒng)", "广播 (guǎng bō)", "播放 (bō fàng)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "农民在田里____庄稼。": "播种 (bō zhǒng)",
            "收音机正在____新闻。": "广播 (guǎng bō)",
            "他正在____音乐。": "播放 (bō fàng)",
            "学校每天早上都会____通知。": "广播 (guǎng bō)",
            "春天是____的季节。": "播种 (bō zhǒng)",
            "电视台正在____这部电影。": "播放 (bō fàng)",
            "老师在教室里____教学视频。": "播放 (bō fàng)",
            "这个电台每天____天气预报。": "广播 (guǎng bō)"
        }
    elif level == 3:
        st.write("Choose from these characters:")
        choices = ["连续剧 (lián xù jù)", "喜剧 (xǐ jù)", "邻居 (lín jū)", 
                  "悲剧 (bēi jù)", "居住 (jū zhù)", "剧本 (jù běn)", "剧烈 (jù liè)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "这部____让我笑得很开心。": "喜剧 (xǐ jù)",
            "他们是我的____，住在隔壁。": "邻居 (lín jū)",
            "这个故事的____写得很好。": "剧本 (jù běn)",
            "地震造成____的震动。": "剧烈 (jù liè)",
            "我最近在看一部____。": "连续剧 (lián xù jù)",
            "莎士比亚写过很多____。": "悲剧 (bēi jù)",
            "他在北京____了十年。": "居住 (jū zhù)"
        }
    elif level == 4:
        st.write("Choose from these characters:")
        choices = ["收集 (shōu jí)", "集合 (jí hé)", "第二集 (dì èr jí)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "老师要求同学们____在操场上。": "集合 (jí hé)",
            "这部电视剧的____很精彩。": "第二集 (dì èr jí)",
            "他喜欢____邮票。": "收集 (shōu jí)",
            "我们正在____资料。": "收集 (shōu jí)",
            "学生们都已经____在教室里了。": "集合 (jí hé)"
        }
    elif level == 5:
        st.write("Choose from these characters:")
        choices = ["内外 (nèi wài)", "舞蹈 (wǔ dǎo)", "观众 (guān zhòng)", 
                  "手掌 (shǒu zhǎng)", "换衣服 (huàn yī fu)", "建议 (jiàn yì)"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "这个剧场可以容纳上千名____。": "观众 (guān zhòng)",
            "天气____说今天会下雨。": "预报 (yù bào)",
            "她跳____的动作很优美。": "舞蹈 (wǔ dǎo)",
            "我们要了解事情的____。": "情况 (qíng kuàng)",
            "他给了我一些很好的____。": "建议 (jiàn yì)"
        }

def main():
    st.title("Chinese Characters Quiz")
    
    st.markdown("""
        <style>
        .stButton > button {
            width: 150px;
            height: 100px;
            margin: 5px;
            white-space: normal;
            word-wrap: break-word;
            font-size: 16px;
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
            choices = ["解开 (jiě kāi)", "了解 (liǎo jiě)", "解释 (jiě shì)", "解决 (jiě jué)"]
        elif st.session_state.level == 2:
            choices = ["播种 (bō zhǒng)", "广播 (guǎng bō)", "播放 (bō fàng)"]
        elif st.session_state.level == 3:
            choices = ["连续剧 (lián xù jù)", "喜剧 (xǐ jù)", "邻居 (lín jū)", 
                      "悲剧 (bēi jù)", "居住 (jū zhù)", "剧本 (jù běn)", "剧烈 (jù liè)"]
        elif st.session_state.level == 4:
            choices = ["收集 (shōu jí)", "集合 (jí hé)", "第二集 (dì èr jí)"]
        else:
            choices = ["内外 (nèi wài)", "舞蹈 (wǔ dǎo)", "观众 (guān zhòng)", 
                      "手掌 (shǒu zhǎng)", "换衣服 (huàn yī fu)", "建议 (jiàn yì)"]
        
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
            if st.session_state.level < 5:
                st.success(f"Perfect score! Moving to Level {st.session_state.level + 1}! 做得好！")
                if st.button("Next Level"):
                    st.session_state.level += 1
                    st.session_state.score = 0
                    st.session_state.answered = False
                    st.session_state.selected_answer = {}
                    st.experimental_rerun()
            else:
                st.success("🎉 Excellent work! You've mastered all levels! 太棒了！")
        
        if st.button("Try Again"):
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.selected_answer = {}
            st.experimental_rerun()

if __name__ == "__main__":
    main()
