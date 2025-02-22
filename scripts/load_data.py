import json
import os
from datasets import load_dataset

# 데이터 저장 경로 설정
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)  # 폴더가 없으면 생성

# KLUE-NLI 데이터셋 로드
dataset = load_dataset("klue", "nli")

# JSON 파일로 저장하는 함수
def save_json(dataset, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=4)

# 파일 저장
save_json(dataset["train"].to_dict(), os.path.join(data_dir, "klue_nli_train.json"))
save_json(dataset["validation"].to_dict(), os.path.join(data_dir, "klue_nli_validation.json"))

print("✅ KLUE-NLI 데이터셋 저장 완료! `data/` 폴더를 확인하세요.")
