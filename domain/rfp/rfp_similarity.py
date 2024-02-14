# -*- coding: utf-8 -*-

import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def get_similarity(data1, data2):
    attempts = 0
    max_attempts = 5
    while attempts < max_attempts:
        # JSON 데이터를 문자열로 변환
        data1_str = json.dumps(data1, ensure_ascii=False)
        data2_str = json.dumps(data2, ensure_ascii=False)

        # GPT에 쿼리
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user",
                        "content": f"{data1_str}\n{data2_str}\n이 두 개의 json은 rfp인데 사업의 유사도를 백분율로 알려줘, 그리고 두 개의 json에서 공통된 키워드 3개를 뽑아줘. 너가 답변할 때 각종 설명들은 다 빼고 형식만 출력해줘. 형식은 유사도: 키워드: 유사도는 한 번만 출력해줘."
                    }
                ]
            )
            answer = response.choices[0].message.content
            if "유사도:" in answer and "키워드:" in answer:
                similarity_str = answer.split("유사도: ")[1].split("%")[0]
                similarity = int(similarity_str)
                lines = answer.strip().split("\n")
                keywords = [line.split("키워드: ")[1].strip().split(", ") for line in lines if "키워드: " in line][0]
                return similarity, keywords
            else:
                raise ValueError("유사도, 키워드 추출 실패")
        except (IndexError, ValueError) as e:
            print(f"Attempt {attempts + 1} failed: {e}")
            attempts += 1

    error_message = "최대 쿼리 횟수 초과"
    print(error_message)
    return 0, []