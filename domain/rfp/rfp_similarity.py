# -*- coding: utf-8 -*-

import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def get_similarity(data1, data2):

    # JSON 데이터를 문자열로 변환
    data1_str = json.dumps(data1, ensure_ascii=False)
    data2_str = json.dumps(data2, ensure_ascii=False)

    # GPT에 쿼리
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"""{data1_str}\n{data2_str}\n이 
                두 개의 json은 rfp인데 사업의 유사도를 백분율로 알려줘, 
                그리고 두 개의 json에서 공통된 키워드 3개를 뽑아줘. 
                너가 답변할 때 각종 설명들은 다 빼고 형식만 출력해줘. 
                형식은 유사도: 키워드: 유사도는 한 번만 출력해줘."""
            }
        ]
    )

    # 응답 파싱
    answer = response.choices[0].message.content
    similarity = int(answer.split("유사도: ")[1].split("%")[0])
    lines = answer.strip().split("\n")
    keywords = [line.split("키워드: ")[1].strip().split(", ") for line in lines if "키워드: " in line]
    return similarity, keywords