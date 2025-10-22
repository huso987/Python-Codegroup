import requests
import json
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# 1️⃣ Hugging Face modelini hazırla
# Bu örnek CodeLlama veya CodeGen tarzı modeli kullanabilir
MODEL_NAME = "Salesforce/codegen-350M-mono"  # Hugging Face modeli
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

code_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# 2️⃣ LeetCode sorularını çek
def fetch_all_problems():
    url = "https://leetcode.com/api/problems/all/"
    resp = requests.get(url, headers={"User-Agent": "python-requests/2.x"})
    resp.raise_for_status()
    data = resp.json()
    pairs = data.get("stat_status_pairs", [])
    problems = []
    for p in pairs:
        stat = p.get("stat", {})
        problem = {
            "id": stat.get("question_id"),
            "title": stat.get("question__title"),
            "slug": stat.get("question__title_slug"),
            "difficulty": ("Easy" if p.get("difficulty", {}).get("level")==1 else
                           "Medium" if p.get("difficulty", {}).get("level")==2 else
                           "Hard" if p.get("difficulty", {}).get("level")==3 else None),
        }
        problems.append(problem)
    return problems

# 3️⃣ Kodları kaydedeceğimiz klasör
SAVE_DIR = "leetcode_solutions"
os.makedirs(SAVE_DIR, exist_ok=True)

# 4️⃣ Soruları al, modelden çözüm al ve .py dosyası oluştur
def solve_and_save(problems, limit=5):
    """
    problems: LeetCode'dan çekilen problem listesi
    limit: kaç soruyu işlemek istediğini belirler
    """
    for i, problem in enumerate(problems[:limit], 1):
        prompt = f"# Solve the LeetCode problem: {problem['title']}\n# Difficulty: {problem['difficulty']}\n\n"
        prompt += "def solution():\n    "
        
        # Modelden kod üret
        result = code_pipeline(prompt, max_length=200, do_sample=True, temperature=0.2)[0]['generated_text']
        
        # Koddan sadece function kısmını al
        code = result.split("def solution():")[1].strip() if "def solution():" in result else result
        
        # Dosya adı oluştur
        filename = f"{SAVE_DIR}/{problem['slug']}.py"
        with open(filename, "w") as f:
            f.write("def solution():\n")
            # indent düzelt
            for line in code.splitlines():
                f.write("    " + line.strip() + "\n")
        
        print(f"{i}. {problem['title']} — Kod {filename} olarak kaydedildi ✅")

# 5️⃣ Main
if __name__ == "__main__":
    problems = fetch_all_problems()
    print(f"Toplam {len(problems)} problem çekildi")
    solve_and_save(problems, limit=5)  # Buradaki limiti artırabilirsin
