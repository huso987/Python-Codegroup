# 1️⃣ Python tabanlı bir image seç
FROM python:3.11-slim

# 2️⃣ Çalışma dizini oluştur
WORKDIR /app

# 3️⃣ Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ Uygulama dosyasını kopyala
COPY app.py .

# 5️⃣ Hugging Face modelleri için cache dizini (opsiyonel ama tavsiye)
ENV TRANSFORMERS_CACHE=/app/cache
ENV HF_HOME=/app/cache

# 6️⃣ Kodları kaydedeceğimiz klasör (host ile mount edilebilir)
RUN mkdir -p leetcode_solutions

# 7️⃣ Port aç (opsiyonel, Flask ekleyeceksen)
EXPOSE 5000

# 8️⃣ Uygulamayı çalıştır
CMD ["python", "app.py"]
