Instagram Political Comment Analysis
1. Gambaran Umum

Instagram Political Comment Analysis adalah project data analysis berbasis Python yang bertujuan menganalisis komentar negatif pada konten Instagram bertema pemerintah, kemudian mengelompokkan akun yang memberikan komentar tersebut ke dalam tiga kategori berdasarkan status akun dan indikator following terhadap akun Instagram utama Anies Rasyid Baswedan:

Pendukung Anies — akun publik yang teridentifikasi mengikuti akun Instagram utama Anies Rasyid Baswedan.
Netral / bukan pendukung teridentifikasi — akun publik yang tidak teridentifikasi mengikuti akun Instagram utama Anies.
Private — akun Instagram yang bersifat private sehingga informasi following tidak dapat diperiksa.

Tujuan akhirnya adalah memperoleh distribusi persentase ketiga kategori tersebut dari seluruh komentar negatif yang berhasil dianalisis.

Contoh:

Total komentar negatif: 1.000

Pendukung Anies      : 350 (35%)
Netral               : 450 (45%)
Private              : 200 (20%)

Hasil tersebut kemudian dapat ditampilkan dalam bentuk tabel, grafik, dan dashboard.

Catatan metodologis: mengikuti akun Anies digunakan sebagai indikator/proksi klasifikasi penelitian, bukan bukti pasti bahwa seseorang merupakan pendukung Anies. Seseorang dapat mengikuti akun publik karena berbagai alasan.

2. Latar Belakang

Media sosial menjadi salah satu tempat masyarakat menyampaikan pendapat mengenai isu sosial dan pemerintahan. Instagram, khususnya melalui kolom komentar, menyediakan sejumlah besar data teks yang dapat digunakan untuk mempelajari pola opini publik.

Namun, sekadar mengetahui bahwa suatu komentar memiliki sentimen negatif belum menjawab pertanyaan yang lebih spesifik:

Bagaimana komposisi akun yang memberikan komentar negatif jika dilihat berdasarkan indikator afiliasi yang digunakan dalam penelitian?

Project ini mencoba menjawabnya melalui kombinasi:

Data Collection
       ↓
Data Cleaning
       ↓
Sentiment Analysis
       ↓
Filter Negative Comments
       ↓
Account Classification
       ↓
Statistical Analysis
       ↓
Visualization

Dengan pendekatan tersebut, project tidak hanya melakukan sentiment analysis, tetapi menghubungkan hasil sentiment dengan informasi akun yang dapat diamati secara publik.

3. Tujuan Project
Tujuan utama

Menghasilkan analisis statistik mengenai proporsi akun yang memberikan komentar negatif pada konten Instagram bertema pemerintah, berdasarkan tiga kategori:

Pendukung Anies
Netral / tidak teridentifikasi sebagai pendukung Anies
Private
Tujuan teknis

Project juga bertujuan untuk:

mengambil dan mengelola data komentar Instagram;
melakukan preprocessing teks Bahasa Indonesia;
mendeteksi sentimen komentar;
menyaring komentar negatif;
mengklasifikasikan akun berdasarkan aturan penelitian;
menyimpan hasil analisis secara terstruktur;
menghitung jumlah dan persentase setiap kategori;
membuat visualisasi hasil;
menyediakan dashboard analisis.
4. Ruang Lingkup

Agar project tidak terlalu luas, versi pertama dibatasi sebagai berikut.

Platform

Instagram

Target konten

Konten Instagram yang memiliki hubungan dengan:

pemerintah;
kebijakan pemerintah;
tindakan pemerintah;
isu pemerintahan;
kritik terhadap pemerintah.
Target data

Komentar pada konten tersebut.

Sentiment

Versi awal hanya membutuhkan:

NEGATIVE

Komentar positif dan netral tidak menjadi bagian dari dataset akhir.

Klasifikasi akun

Hanya tiga kategori:

ANIES
NEUTRAL
PRIVATE
Tokoh pembanding

Versi awal tidak menggunakan Ganjar.

Fokus hanya pada:

Anies Rasyid Baswedan

Hal ini membuat project lebih sederhana dan metodologinya lebih mudah dikontrol.

5. Definisi Kategori
A. Pendukung Anies

Akun Instagram yang:

berstatus publik;
dapat diperiksa informasi following-nya;
teridentifikasi mengikuti akun Instagram utama Anies Rasyid Baswedan.

Label internal:

anies
B. Netral / Bukan Pendukung Teridentifikasi

Akun Instagram yang:

berstatus publik;
informasi following dapat diperiksa;
tidak teridentifikasi mengikuti akun Instagram utama Anies.

Label internal:

neutral

Istilah netral di sini harus dipahami sebagai:

tidak teridentifikasi mengikuti akun Anies berdasarkan indikator yang digunakan.

Bukan berarti orang tersebut benar-benar netral secara politik.

C. Private

Akun yang:

berstatus private;
informasi following tidak dapat diperiksa.

Label:

private

Akun private tidak boleh otomatis dimasukkan ke kategori netral, karena informasi yang dibutuhkan untuk klasifikasi memang tidak tersedia.

6. Alur Sistem

Secara keseluruhan:

                    INSTAGRAM
                        │
                        ▼
               DATA COLLECTION
                        │
                        ▼
                 RAW COMMENTS
                        │
                        ▼
                DATA CLEANING
                        │
                        ▼
               SENTIMENT ANALYSIS
                        │
                ┌───────┴───────┐
                │               │
             NEGATIVE       OTHER
                │
                ▼
        FILTER NEGATIVE
                │
                ▼
        ACCOUNT INSPECTION
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
     ANIES   NEUTRAL   PRIVATE
        │       │        │
        └───────┼────────┘
                ▼
        STATISTICAL ANALYSIS
                │
                ▼
           VISUALIZATION
                │
                ▼
             DASHBOARD
7. Contoh Data

Data mentah:

username,comment_text
user01,"Pemerintah sekarang sangat mengecewakan."
user02,"Saya tidak setuju dengan kebijakan ini."
user03,"Semoga pemerintah bisa bekerja lebih baik."

Setelah sentiment analysis:

username,comment_text,sentiment
user01,"Pemerintah sekarang sangat mengecewakan.",negative
user02,"Saya tidak setuju dengan kebijakan ini.",negative
user03,"Semoga pemerintah bisa bekerja lebih baik.",neutral

Komentar non-negative kemudian dikeluarkan.

Data yang tersisa:

user01
user02

Kemudian informasi akun:

username,account_private,follows_anies
user01,false,true
user02,true,

Hasil klasifikasi:

username,sentiment,classification
user01,negative,anies
user02,negative,private
8. Rumus Persentase

Misalnya terdapat:

Total komentar negatif = 1.000

Anies   = 350
Neutral = 450
Private = 200

Maka:

Persentase Anies
= 350 / 1000 × 100
= 35%

Persentase Neutral
= 450 / 1000 × 100
= 45%

Persentase Private
= 200 / 1000 × 100
= 20%

Total:

35% + 45% + 20% = 100%
9. Arsitektur Teknologi

Untuk versi awal, stack yang digunakan:

Komponen	Teknologi
Programming language	Python
Data processing	Pandas
NLP	Transformers
Machine learning framework	PyTorch
Data storage awal	CSV
Database tahap lanjut	SQLite/PostgreSQL
Visualization	Plotly
Dashboard	Streamlit
Environment	Python venv

Struktur:

instagram-political-analysis/
│
├── data/
│   ├── raw/
│   │   └── comments.csv
│   │
│   └── processed/
│       └── comments_processed.csv
│
├── src/
│   ├── collector/
│   │   └── instagram.py
│   │
│   ├── preprocessing/
│   │   └── cleaner.py
│   │
│   ├── sentiment/
│   │   └── analyzer.py
│   │
│   ├── classification/
│   │   └── account_classifier.py
│   │
│   ├── analysis/
│   │   └── statistics.py
│   │
│   └── main.py
│
├── dashboard.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── PROJECT.md
10. Pipeline Data
Step 1 — Collection

Menghasilkan data:

post_id
post_url
comment_id
username
comment_text
timestamp
Step 2 — Cleaning

Membersihkan:

URL;
mention;
hashtag;
emoji;
karakter berulang;
whitespace;
komentar kosong;
duplikasi.

Contoh:

"PEMERINTAH INI BURUK BANGET!!! 😡😡 https://..."

menjadi:

"pemerintah ini buruk banget"
Step 3 — Sentiment Analysis

Model NLP memproses:

"pemerintah ini buruk banget"

menjadi:

sentiment = negative
confidence = 0.94

Confidence sebaiknya tetap disimpan sehingga nantinya kita bisa melakukan evaluasi atau menentukan threshold.

Step 4 — Filtering

Hanya:

sentiment == negative

yang diteruskan.

Step 5 — Account Classification

Untuk setiap akun negatif:

PRIVATE?
│
├── YA → PRIVATE
│
└── TIDAK
      │
      ▼
Following Anies?
      │
      ├── YA → ANIES
      │
      └── TIDAK → NEUTRAL
Step 6 — Aggregation

Menghasilkan:

category
count
percentage
Step 7 — Visualization

Dashboard dapat menampilkan:

Total komentar
Komentar negatif
Anies
Neutral
Private

serta grafik:

pie chart komposisi;
bar chart jumlah akun;
distribusi berdasarkan postingan;
distribusi berdasarkan tanggal jika timestamp tersedia.
11. Contoh Dashboard

Dashboard nantinya bisa memiliki:

┌───────────────────────────────────────────┐
│ Instagram Political Comment Analysis      │
├────────────┬────────────┬─────────────────┤
│ Comments   │ Negative   │ Anies           │
│ 10,245     │ 3,821      │ 1,247           │
├────────────┴────────────┴─────────────────┤
│                                           │
│       Composition of Negative Comments    │
│                                           │
│              [ PIE CHART ]                │
│                                           │
├───────────────────────────────────────────┤
│ Anies       32.63%                        │
│ Neutral     48.21%                        │
│ Private     19.16%                        │
└───────────────────────────────────────────┘
12. Dataset yang Sebaiknya Disimpan

Untuk setiap komentar, idealnya data internal memiliki:

comment_id
post_id
post_url
username_hash
comment_text
comment_timestamp

sentiment
sentiment_score

account_private
follows_anies

classification

Contoh:

comment_id: 829102
post_id: 712938
username_hash: a81f...
comment_text: "Kebijakan ini benar-benar buruk"

sentiment: negative
sentiment_score: 0.93

account_private: false
follows_anies: true

classification: anies

Untuk hasil penelitian/publikasi, hindari mempublikasikan username atau informasi identitas pengguna.

13. Evaluasi Sentiment Model

Ini bagian yang penting kalau project ini nantinya mau dianggap sebagai project data science yang serius.

Jangan hanya mengatakan:

“Model menghasilkan 90% komentar negatif.”

Kita harus menguji apakah model memang cukup baik.

Buat dataset validasi manual, misalnya:

500 komentar

kemudian diberi label manusia:

negative
neutral
positive

Model dibandingkan dengan label tersebut.

Metrik:

Accuracy
Precision
Recall
F1-score
Confusion Matrix

Dengan begitu kita bisa mengetahui apakah model terlalu sering menganggap komentar sebagai negatif.

14. Tantangan NLP Bahasa Indonesia

Komentar Instagram biasanya tidak menggunakan Bahasa Indonesia formal.

Contohnya:

"pemerintah goblok bgt dah"
"yg beginian aja gk becus"
"anjir makin kacau"
"fix gagal total"

Model harus menghadapi:

slang;
singkatan;
typo;
bahasa campuran;
emoji;
sarkasme;
konteks;
kata kasar;
bahasa daerah.

Sarkasme akan menjadi salah satu masalah terbesar.

Contoh:

“Wah hebat sekali pemerintah kita 😂”

Secara literal positif, tetapi konteksnya bisa berupa kritik.

Karena itu model sentiment tidak boleh dianggap sempurna.

15. Tantangan Klasifikasi Akun

Ini juga sangat penting.

Indikator:

Following Anies = TRUE

tidak sama dengan:

Pendukung Anies = TRUE

Maka dalam laporan, lebih tepat menggunakan istilah:

“Akun yang teridentifikasi mengikuti akun Anies”

daripada:

“Pendukung Anies”

Jika tetap menggunakan label Pendukung Anies, definisinya harus dijelaskan secara eksplisit sebagai label operasional/proksi penelitian.

16. Privasi

Project harus menghindari pengumpulan data yang tidak diperlukan.

Data yang dibutuhkan:

Komentar
Status akun public/private
Indikator following

Tidak perlu:

Email
Nomor HP
Alamat
DM
Data pribadi non-publik

Dan data pengguna sebaiknya dianonimkan dalam dataset analisis.

17. Batasan Project

Project ini tidak bertujuan menentukan pilihan politik seseorang secara pasti.

Hasilnya hanya menunjukkan:

distribusi komentar negatif berdasarkan indikator klasifikasi yang telah ditentukan.

Contoh:

35% → akun yang mengikuti Anies
45% → akun publik yang tidak mengikuti Anies
20% → akun private

Hasil tersebut tidak boleh ditafsirkan sebagai:

“35% komentator negatif adalah pendukung Anies.”

Kesimpulan yang lebih tepat:

“35% komentar negatif berasal dari akun yang teridentifikasi mengikuti akun Anies berdasarkan kriteria penelitian.”

18. Tahapan Pengembangan

Aku akan membagi project menjadi beberapa fase.

Phase 1 — Prototype
CSV
 ↓
Cleaning
 ↓
Sentiment
 ↓
Filter negative
 ↓
Classification
 ↓
Percentage

Status: sedang kita kerjakan.

Phase 2 — Model Evaluation
Dataset manual
 ↓
Testing model
 ↓
Accuracy
Precision
Recall
F1
Phase 3 — Data Collection

Menentukan metode pengambilan data Instagram yang sesuai dengan akses dan aturan platform.

Ini sengaja kita pisahkan dari NLP supaya pipeline bisa tetap dipakai meskipun metode pengumpulan datanya berubah.

Phase 4 — Database

Migrasi:

CSV
 ↓
SQLite

atau kalau dataset sudah besar:

PostgreSQL
Phase 5 — Automated Pipeline
Collect
 ↓
Clean
 ↓
Sentiment
 ↓
Classification
 ↓
Store

bisa dijalankan secara otomatis.

Phase 6 — Dashboard

Menggunakan:

Streamlit
+
Plotly
Phase 7 — Analysis

Dashboard akhirnya dapat menjawab:

Berapa jumlah komentar negatif?

Berapa persen yang berasal dari akun yang mengikuti Anies?

Berapa persen akun publik yang tidak mengikuti Anies?

Berapa persen akun private?

Bagaimana distribusinya berdasarkan postingan?

Bagaimana distribusinya berdasarkan waktu?

19. Versi Singkat Project

Kalau harus dijelaskan ke dosen dalam beberapa kalimat:

Instagram Political Comment Analysis merupakan project analisis data dan NLP yang memproses komentar pada konten Instagram bertema pemerintah. Sistem terlebih dahulu melakukan analisis sentimen untuk mengidentifikasi komentar negatif. Komentar negatif kemudian dikaitkan dengan klasifikasi akun berdasarkan status private/public dan indikator apakah akun tersebut mengikuti akun Instagram utama Anies Rasyid Baswedan. Hasil akhirnya berupa jumlah dan persentase tiga kategori, yaitu akun yang teridentifikasi mengikuti Anies, akun publik yang tidak teridentifikasi mengikuti Anies, dan akun private.

Jadi inti project kita sekarang sudah jelas:

        INSTAGRAM
            ↓
       KOMENTAR
            ↓
    SENTIMENT ANALYSIS
            ↓
       NEGATIVE ONLY
            ↓
     ACCOUNT CHECKING
            ↓
    ┌───────┼────────┐
    ↓       ↓        ↓
  ANIES   NEUTRAL  PRIVATE
    └───────┼────────┘
            ↓
       PERCENTAGE
            ↓
        DASHBOARD
