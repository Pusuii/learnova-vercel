# Learnova — Learning Management System

Platform LMS dengan empat peran (Mahasiswa, Dosen, Admin, Super Admin) yang mengikuti ERD (21 tabel),
activity diagram tiap role, dan use-case diagram yang Anda berikan.

## Menjalankan (VS Code)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate     macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Buka http://127.0.0.1:5000. Database SQLite dan data demo dibuat otomatis di folder `instance/` pada
jalankan pertama. Untuk mengulang dari data demo bersih: `python app.py --reset`.

Variabel lingkungan opsional: `HOST`, `PORT`, `FLASK_DEBUG=1`.

## Akun demo (password semua: `Learnova123`)

| Peran | Email |
|---|---|
| Super Admin | superadmin@learnova.id |
| Admin | admin@learnova.id, admin2@learnova.id |
| Dosen | dosen@learnova.id, dosen2@learnova.id, dosen3@learnova.id (menunggu verifikasi) |
| Mahasiswa | mahasiswa@learnova.id … mahasiswa10@learnova.id; mahasiswa11@ (menunggu verifikasi); mahasiswa12@ (nonaktif) |

## Fitur utama

- **Mahasiswa**: kelas, materi (prasyarat berurutan), tugas (tenggat ditegakkan), kuis (timer, batas percobaan,
  pilihan ganda otomatis dinilai, esai menunggu dosen), absensi, progres & nilai, laporan kendala.
- **Dosen**: kelola kelas, materi, tugas & penilaian, kuis & penilaian esai, sesi absensi, laporan progres.
- **Admin**: verifikasi & kelola akun, mata kuliah, kelas & peserta, laporan kendala, monitoring aktivitas.
- **Super Admin**: akun admin, role & hak akses (17 permission), konfigurasi sistem, statistik, audit log.
- Keamanan: password pbkdf2, CSRF, batas percobaan login, whitelist & batas ukuran upload, unduhan berkas
  dengan kontrol akses, mode pemeliharaan.

## Struktur

```
app.py                 titik masuk
learnova/              paket aplikasi (blueprints/, schema.sql, seed.py, auth.py, services.py, ...)
templates/  static/    tampilan (Jinja2) dan aset (CSS, JS, logo)
tests/test_flows.py    uji alur: python -m unittest discover -s tests -v
```

## Catatan

- Dibangun dengan **Flask + SQLite (stdlib)** karena tidak memerlukan Node/npm dan mudah dijalankan di VS Code.
- Font (Bricolage Grotesque, Instrument Sans) dimuat dari Google Fonts dan butuh internet.
- Satu kolom tambahan di luar ERD: `user_reports.response` (tanggapan admin atas laporan).



## Deploy ke Vercel (preview/demo)

Project ini menyertakan `vercel.json` dan `api/index.py` sebagai entry point Flask.

1. Unggah **isi folder project ini** ke repository GitHub (pastikan `vercel.json`, `app.py`, `api/`, `learnova/`, `templates/`, dan `static/` berada di root).
2. Buka https://vercel.com/new, impor repository GitHub, lalu deploy dengan konfigurasi default.
3. Di Project Settings → Environment Variables, tambahkan `LEARNOVA_SECRET_KEY` dengan nilai acak panjang sebelum digunakan; lalu redeploy.

### Batasan penting untuk Vercel

Vercel menjalankan Python sebagai serverless function. SQLite dan file upload diarahkan ke `/tmp` agar aplikasi dapat berjalan, tetapi `/tmp` bersifat sementara dan tidak dibagikan secara andal antarinvokasi/instance. Artinya, data akun, nilai, tugas, dan unggahan **tidak dijamin tersimpan permanen**. Paket ini cocok untuk preview/demo awal, bukan penggunaan LMS produksi.

Untuk penggunaan sungguhan, migrasikan database SQLite ke PostgreSQL eksternal dan unggahan ke object storage, lalu hubungkan kredensialnya melalui Environment Variables. Jangan menyimpan rahasia di GitHub. Data demo diaktifkan secara default; atur `LEARNOVA_SEED_DEMO=0` setelah alur pembuatan akun admin produksi disiapkan.
