# tugas-akhir-Analisis Sentimen opini cancelCulture di media sosial X
![Poster TA_Hazna Hamida Saputri_1301220094](https://github.com/user-attachments/assets/7183e288-64d7-40ff-bf3a-b2d463afa59e)

Proyek ini merupakan implementasi Tugas Akhir S1 Informatika Telkom University berjudul:

**Analisis Sentimen Masyarakat Media Sosial X terhadap Gerakan Cancel Culture di Indonesia Menggunakan IndoBERT**  
*Hazna Hamida Saputri — 1301220094*  
*Telkom University, 2025*

---

## Latar Belakang

Cancel culture di media sosial X memicu banyak opini publik yang teksnya bersifat informal, ambigu, dan tidak baku. Metode NLP klasik sering tidak akurat dalam menilai sentimen jenis ini. IndoBERT dipilih karena kemampuannya memahami konteks dua arah dalam bahasa Indonesia informal.

---

## Tujuan Penelitian

- Menganalisis sentimen masyarakat terhadap gerakan cancel culture di media sosial X menggunakan model IndoBERT.
- Mengevaluasi kinerja IndoBERT dan membandingkannya dengan metode klasifikasi berbasis SVM + TF-IDF.

---

## Dataset

- 29.000 tweet terkumpul
- 7.217 tweet dilabeli manual oleh 3 annotator
- Distribusi:
  - Positif: 55%
  - Negatif: 45%

Atribut data antara lain: `full_text`, `created_at`, `favorite_count`, `retweet_count`, dll.

---

## Metodologi

1. Scraping data dari X  
2. Cleaning teks (URL, mention, hashtag, emoji)  
3. Normalisasi karakter dan huruf  
4. Tokenisasi WordPiece  
5. Fine-tuning IndoBERT  
6. Evaluasi (Accuracy, Precision, Recall, F1-score)  
7. Perbandingan dengan SVM + TF-IDF  

---

## Model IndoBERT

Model dasar: indobenchmark/indobert-base-p1


Parameter utama:

- Learning rate: 1e-5  
- Batch size: 16  
- Epoch: 3  
- Warmup: 0.1  
- Weight decay: 0.01  

---

## Hasil Evaluasi

### IndoBERT
- Akurasi: 83%
- F1-score Negatif: 0.85
- F1-score Positif: 0.81

### SVM + TF-IDF
- Akurasi: 79%
- Performa lebih rendah pada teks informal

---

## Download Saved Models

Model tidak dapat diupload ke GitHub karena ukurannya >100MB.  
Unduh melalui Google Drive:

**https://drive.google.com/drive/folders/1drwVbnQX7Lu5jy7idVZe9rEIgLffQUOM?usp=sharing**

Struktur folder yang diperlukan:
saved_models/
indobert/
config.json
pytorch_model.bin
tokenizer_config.json
vocab.txt

---

## Cara Menjalankan

Install dependencies: pip install -r requirements.txt
Jalankan aplikasi: streamlit run app.py
Atau inferensi manual: python inference_utils.py

## Acknowledgment

- Bunyamin, M.Kom — Pembimbing I  
- Hasmawati, S.Kom., M.Kom — Pembimbing II  
- Fakultas Informatika, Telkom University
