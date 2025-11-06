
# Serambi Cafe (Flask + HTML + CSS)

Proyek contoh website cafe sederhana menggunakan Flask.

## Cara Menjalankan
1. Pastikan Python 3.9+ terpasang.
2. (Opsional) Buat virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install dependency:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan server:
   ```bash
   python app.py
   ```
5. Akses di browser: http://127.0.0.1:5000

## Struktur Folder
```
cafe_flask/
├─ app.py
├─ requirements.txt
├─ README.md
├─ templates/
│  ├─ base.html
│  ├─ home.html
│  ├─ menu.html
│  ├─ about.html
│  └─ contact.html
└─ static/
   └─ style.css
```
