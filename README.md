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
  - Positif(mendukung gerakan cancel culture): 55%
  - Negatif(tidak mendukung gerakan cancel culture): 45%


  <img width="590" height="390" alt="image" src="https://github.com/user-attachments/assets/f777c63a-c640-423b-8053-2d2dcb4e9f5b" />

  ## Contoh Data Sentimen

Berikut adalah contoh tweet dari masing-masing kategori sentimen:

### Sentimen Positif
@g****n16
Untuk entertainment industri yang lebih baik menurut gue bagus-bagus aja sih cancel culture ini. 
Jadi artis tuh kan tujuan aslinya emang harus nunjukin bakat di bidang seni dan juga tanggung jawabnya besar karena dikenal publik.

### Sentimen Negatif
@s****w
Dan orang-orang melakukan cancel culture hanya ikut-ikutan dari satu opini saja. 
Itu jelas nggak baik banget, menumpahkan lewat ketikan yang jahat-jahat malah memperburuk keadaan. 
Semuanya punya alasan. Belajarlah mendengar, belajar menahan jempol, belajar menilai dari berbagai sudut.


Berikut wordcloud dari dataset tweet terkait cancel culture.

### Wordcloud Sentimen Negatif
<img width="944" height="663" alt="image" src="https://github.com/user-attachments/assets/f2543a8f-4e5d-4a60-b773-1ce24efd3475" />

### Wordcloud Sentimen Positif
<img width="944" height="663" alt="image" src="https://github.com/user-attachments/assets/42651e74-26d0-42a4-b584-f8b2b85d6dc8" />

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

<img width="1021" height="424" alt="image" src="https://github.com/user-attachments/assets/8cb87349-4a9b-4b4f-af65-a4a76d9f7c18" />

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
