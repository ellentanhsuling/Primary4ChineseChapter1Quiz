import streamlit as st
import random

def get_quiz_questions(level):
    if level == 1:
        st.write("Choose from these characters:")
        choices = ["解开", "了解", "解释", "解决"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "当我们遇到问题时，要学会自己____它。": "解决",
            "老师____了这道数学题的做法。": "解释",
            "请帮我____这个绳结。": "解开",
            "我很想____这件事情的真相。": "了解",
            "让我们一起____这个难题。": "解决",
            "他需要____这个复杂的概念。": "了解",
            "妈妈正在____给我们做饭的过程。": "解释",
            "小明试图____缠在一起的耳机线。": "解开"
        }
    elif level == 2:
        st.write("Choose from these characters:")
        choices = ["播种", "广播", "播放"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "农民在田里____庄稼。": "播种",
            "收音机正在____新闻。": "广播",
            "他正在____音乐。": "播放",
            "学校每天早上都会____通知。": "广播",
            "春天是____的季节。": "播种",
            "电视台正在____这部电影。": "播放",
            "老师在教室里____教学视频。": "播放",
            "这个电台每天____天气预报。": "广播"
        }
    elif level == 3:
        st.write("Choose from these characters:")
        choices = ["连续剧", "喜剧", "邻居", "悲剧", "居住", "剧本", "剧烈"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "这部____让我笑得很开心。": "喜剧",
            "他们是我的____，住在隔壁。": "邻居",
            "这个故事的____写得很好。": "剧本",
            "地震造成____的震动。": "剧烈",
            "我最近在看一部____。": "连续剧",
            "莎士比亚写过很多____。": "悲剧",
            "他在北京____了十年。": "居住",
            "这部____每天晚上播出。": "连续剧",
            "运动后他感到____头痛。": "剧烈",
            "这个____区环境很好。": "居住",
            "她在写一个新的____。": "剧本",
            "这是一部感人的____。": "悲剧",
            "我们和____相处得很好。": "邻居",
            "这部____的结局很精彩。": "喜剧",
            "他的心跳非常____。": "剧烈"
        }
    elif level == 4:
        st.write("Choose from these characters:")
        choices = ["收集", "集合", "第二集"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "老师要求同学们____在操场上。": "集合",
            "这部电视剧的____很精彩。": "第二集",
            "他喜欢____邮票。": "收集",
            "我们正在____资料。": "收集",
            "学生们都已经____在教室里了。": "集合"
        }
    elif level == 5:
        st.write("Choose from these characters:")
        choices = ["内外", "舞蹈", "观众", "手掌", "换衣服", "换主意", "方言", "预报", "建议", "疲倦", "情况"]
        st.write(" | ".join(choices))
        st.write("---")
        return {
            "这个剧场可以容纳上千名____。": "观众",
            "天气____说今天会下雨。": "预报",
            "她跳____的动作很优美。": "舞蹈",
            "我们要了解事情的____。": "情况",
            "他给了我一些很好的____。": "建议",
            "学习了一天后，我感到很____。": "疲倦",
            "这里的人说当地的____。": "方言",
            "运动后要记得____。": "换衣服",
            "商店____都很干净。": "内外",
            "他经常____，让人摸不着头脑。": "换主意",
            "他把钥匙放在____心。": "手掌",
            "医生正在检查病人的____。": "情况",
            "这个____很受欢迎。": "舞蹈",
            "老师____我们多做练习。": "建议",
            "请注意天气____。": "预报"
        }

def main():
    st.title("Chinese Characters Quiz")
    
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
            if st.session_state.level < 5:
                st.success(f"Perfect score! Moving to Level {st.session_state.level + 1}! 做得好！")
                if st.button("Next Level"):
                    st.session_state.level += 1
                    st.session_state.score = 0
                    st.session_state.answered = False
                    st.experimental_rerun()
            else:
                st.success("🎉 Excellent work! You've mastered all levels of Chapter 1! 太棒了！")
                st.success("Ready for more challenges? Start Chapter 2 to learn new characters! 准备好开始第二章吗？")
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
