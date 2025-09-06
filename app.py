from dotenv import load_dotenv

load_dotenv()

import streamlit as st



st.title("金融・キャリア: 相談アプリ")

st.write("##### 専門家の種類を選択してください。\n\n- 金融アドバイザー: お金や投資、家計管理などのアドバイスを提供します。\n- キャリアコンサルタント: 就職・転職・キャリア形成などのアドバイスを提供します。")


expert_type = st.radio(
    "専門家の種類を選択してください。",
    ["金融アドバイザー", "キャリアコンサルタント"]
)


from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def get_system_message(expert_type):
    if expert_type == "金融アドバイザー":
        return "あなたは日本の金融アドバイザーです。お金、投資、家計管理、保険など金融全般の相談に、専門的かつ分かりやすく、リスクや注意点も添えて回答してください。"
    else:
        return "あなたは日本のキャリアコンサルタントです。就職、転職、キャリア形成、職場の人間関係などキャリア全般の相談に、専門的かつ分かりやすく、アドバイスや注意点も添えて回答してください。"

def ask_llm(user_text, expert_type):
    """
    入力テキストと専門家タイプを受け取り、LLMからの回答を返す
    """
    system_message = get_system_message(expert_type)
    chat = ChatOpenAI()
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_text)
    ]
    response = chat(messages)
    return response.content


user_input = st.text_area("質問や相談内容を入力してください。", height=100)


if st.button("LLMに質問する"):
    st.divider()
    st.write(f"### 選択された専門家: {expert_type}")
    st.write(f"#### ユーザー入力: {user_input}")
    if user_input:
        with st.spinner("LLMに問い合わせ中..."):
            try:
                answer = ask_llm(user_input, expert_type)
                st.success(answer)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("質問や相談内容を入力してください。")
