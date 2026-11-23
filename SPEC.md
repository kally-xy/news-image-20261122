# SPEC — news-image-20261122 (baca dulu sebelum menulis apa pun)

## Kompetisi
- "Sum up 22 November's world news in one image". Deadline 24 Nov 2026
  07:00 WIB. Status API 24 Nov 02:27 WIB: open, quota entries_made 0,
  can_submit true, day cap 6. Hadiah $100, top 50. TANPA entry fee.
- Juri: AI vision pairwise (z-ai/glm-5.3-flash), tanpa feed berita. Gambar
  HARUS menyebut harinya ("Sunday, 22 November 2026"). Jangan gambarkan
  hari sebelum 13 Nov 2026.
- Kit FRESH (koordinator, 24 Nov 02:27 WIB): bundle_sha256
  00314c2cb5a445fd508bab7f92ae6a1a15dec902d84b7c9dcaa326beafe638bb == API.
  Kit: ~/workspace/makefun/news-image-20261122-kit/.
- Repo dibuat 24 Nov 2026, lisensi MIT. JANGAN submit (koordinator lapor).

## Gambar (sudah dibuat koordinator, ada di repo)
- assets/entry.png = koran halaman depan 1024x1024, 22 Nov 2026 (JPEG
  q92, 319.424 byte). Daftar 35 beritanya ada di notes/BUILD_NOTES.md
  (bukan di repo — tidak perlu dibaca sesi ini).
- Tugas sesi ini: tulis main.py DARI NOL (jangan copy main.py entry lain)
  yang menyalin assets/entry.png ke output dir + verifikasi ukuran dan
  SHA256 (hitung sendiri di sesi ini dari file asetnya).
- main.py WAJIB pure-stdlib (hashlib, os, shutil, sys saja). JANGAN import
  PIL/apa pun di luar stdlib. Default di semua env var, termasuk
  MAKEFUN_OUTPUT_DIR. Tulis main.py dalam MINIMAL 2 pesan tulis/edit yang
  terpisah (gate authorship: >=30% baris counted harus authored).
- Pola yang lolos di news-image-20261121 round 2 (judge 0,949581):
  main.py ~68 baris (docstring + konstanta EXPECTED_SHA256/EXPECTED_SIZE +
  fungsi verify_output + main). JANGAN lebih pendek dari ~55 baris.

## Alur kerja sesi ini (WAJIB urut)
1. `makefun init` di dalam sesi ini, di repo ini, dengan
   --keypair ~/workspace/makefun/makefun-keypair.json. (Bila init menolak
   karena repo sudah berisi file, init ke staging dir baru dan pakai --kit
   staging itu. JANGAN download kit via curl|tar.)
2. Tulis main.py dari nol (>=2 edit messages), lalu baca dan perbaiki.
3. Jalankan kit check di sesi ini; perbaiki SEMUA failure sampai 0 fail.
4. Jalankan program 2x (MAKEFUN_OUTPUT_DIR=out), verifikasi kedua output
   byte-identik + ukuran <=1 MiB + 1024x1024.
5. Buat bundle transcript (makefun bundle --no-discover, hanya sesi ini).
6. LAPORKAN (jangan submit): hasil kit check, SHA256 + ukuran output,
   determinisme 2x, isi main.py final.

## Aturan keras
- JANGAN pernah print kunci/API key/keypair. JANGAN copy keypair/api-key
  ke folder repo. JANGAN submit. JANGAN pindah akun (sesi ini Akun A).
- JANGAN baca file di luar repo ini (workspace sesi terbatas ke dir repo).
- Bila quota error (429) -> STOP, laporkan, jangan pindah akun sendiri.
- Git identity: ryxtn24 <ryxtn24@make.fun>.
