from dotenv import load_dotenv

load_dotenv()

import streamlit as st


st.title("専門家LLMデモ: 振る舞い選択アプリ")

st.write("##### 専門家の種類を選択し、LLMの振る舞いを切り替えます。\n\n- 法律の専門家: 法律相談や法的アドバイスを提供します。\n- 医療の専門家: 健康や医療に関するアドバイスを提供します。")

# 専門家タイプの選択
expert_type = st.radio(
    "専門家の種類を選択してください。",
    ["法律の専門家", "医療の専門家"]
)

# 選択に応じたシステムメッセージ
if expert_type == "法律の専門家":
    system_message = "あなたは日本の弁護士です。民事・刑事・労働・契約など法律全般に関する相談に、専門的かつ分かりやすく、法的根拠や注意点も添えて回答してください。"
else:
    system_message = "あなたは日本の医師です。健康・病気・治療・予防・生活習慣など医療全般の相談に、専門的かつ分かりやすく、根拠や注意点も添えて回答してください。ただし診断や処方は行わず、一般的なアドバイスに留めてください。"

user_input = st.text_area("質問や相談内容を入力してください。", height=100)

if st.button("LLMに質問する"):
    st.divider()
    st.write(f"### 選択された専門家: {expert_type}")
    st.write(f"#### システムメッセージ: {system_message}")
    st.write(f"#### ユーザー入力: {user_input}")
    # ここでLLM API呼び出しを行い、system_messageとuser_inputを渡す
    # 例: response = call_llm(user_input, system_message=system_message)
    st.info("（ここにLLMの応答が表示されます）")
