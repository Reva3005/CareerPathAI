# CareerPath AI Assistant

## Deskripsi Project

CareerPath AI Assistant adalah aplikasi sederhana berbasis konsep Retrieval-Augmented Generation (RAG) yang membantu mahasiswa, fresh graduate, dan pencari kerja memperoleh informasi karier berdasarkan dokumen yang tersedia dalam knowledge base.

## Target User

* Mahasiswa tingkat akhir
* Fresh Graduate
* Pencari kerja

## Permasalahan yang Diselesaikan

Banyak pengguna mengalami kesulitan dalam menentukan jalur karier dan memahami skill yang harus dipelajari untuk mencapai karier tertentu. Aplikasi ini membantu memberikan informasi karier berdasarkan dokumen yang tersedia.

## Knowledge Base

Project ini menggunakan tiga dokumen sebagai sumber informasi:

* frontend.txt
* backend.txt
* data_analyst.txt

## Fitur

* Pencarian dokumen berdasarkan pertanyaan pengguna
* Menampilkan retrieved context
* Memberikan jawaban berdasarkan dokumen yang ditemukan
* Menampilkan sumber dokumen (citation)

## Struktur Project

CareerPathAI/

├── frontend.txt

├── backend.txt

├── data_analyst.txt

├── app.py

└── README.md

## Cara Menjalankan

1. Pastikan Python sudah terinstall.
2. Buka terminal pada folder project.
3. Jalankan perintah:

python app.py

4. Masukkan pertanyaan yang berkaitan dengan Frontend Developer, Backend Developer, atau Data Analyst.

## Contoh Pertanyaan

* Bagaimana cara menjadi Frontend Developer?
* Apa skill yang dibutuhkan Data Analyst?
* Apa roadmap Backend Developer?
* Apa yang harus dipelajari untuk menjadi Web Developer?

## Workflow Sistem

User Question

↓

Retrieval

↓

Retrieved Context

↓

AI Answer

↓

Source Citation

## Evaluasi

* Dokumen ditemukan sesuai pertanyaan
* Jawaban dihasilkan berdasarkan dokumen
* Sumber dokumen ditampilkan
* Mengurangi kemungkinan hallucination karena jawaban berasal dari knowledge base

## Teknologi yang Digunakan

* Python
* Text File Knowledge Base
* Retrieval-Based Search
* Basic RAG Concept

## Penulis

Nama: Reva Indita
Mata Kuliah: Artificial Intelligence
Project: CareerPath AI Assistant
