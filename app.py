from dotenv import load_dotenv

load_dotenv()


import streamlit as st


st.title("法律・医療: 相談アプリ")

st.write("##### 専門家の種類を選択し、LLMの振る舞いを切り替えます。\n\n- 法律の専門家: 法律相談や法的アドバイスを提供します。\n- 医療の専門家: 健康や医療に関するアドバイスを提供します。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["法律の専門家", "医療の専門家"]
)

st.divider()

if selected_item == "法律の専門家":
    input_message1 = st.text_input(label="法律相談を入力してください。")

else:
    input_message2 = st.text_input(label="医療相談を入力してください。")


import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


if st.button("実行"):
    st.divider()

    if selected_item == "法律の専門家":
        if input_message1:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": input_message1}
                ]
            )
            st.write(f"法律相談の結果: {response.choices[0].message.content}")

    else:
        if input_message2:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": input_message2}
                ]
            )
            st.write(f"医療相談の結果: {response.choices[0].message.content}")

          

      