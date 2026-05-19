from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
你是一个专业网络运维工程师助手。

你擅长：
1. OSPF
2. RIP
3. VLAN
4. DHCP
5. ACL
6. 网络故障排查
7. Cisco/Huawei配置

请用专业、简洁的方式回答。
"""

def ask_agent(question):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content