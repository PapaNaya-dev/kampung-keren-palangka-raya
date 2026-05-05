# WebGIS Kampung Keren

## DOKUMEN PERSYARATAN PRODUK WEBGIS KAMPUNG KEREN

### DESKRIPSI PRODUK
WebGIS ini merupakan platform pemetaan interaktif untuk Lomba Penataan Wilayah Kampung Keren. Pemerintah Kota Palangka Raya menyelenggarakan kegiatan ini. Anda bisa mengakses situs ini secara bebas. Platform ini menampilkan batas wilayah peserta lomba dan informasi pendukung secara transparan.

### TUJUAN
1. Menyediakan platform visual penataan wilayah untuk publik.
2. Menampilkan profil area dan dokumentasi kondisi lapangan secara interaktif.
3. Mendukung transparansi data penataan wilayah untuk dewan juri dan masyarakat.

### PENGGUNA SASARAN
- Masyarakat umum
- Dewan juri lomba
- Perangkat daerah dan instansi terkait

### FITUR UTAMA
1. **Peta Interaktif Leaflet**: Menggunakan Leaflet JS, ringan dan responsif.
2. **Polygon Wilayah Lomba**: Batas wilayah berwarna-warni untuk identitas area.
3. **Jendela Informasi Atribut (Popup)**:
   - Profil Daerah: Nama wilayah, luas, jumlah penduduk.
   - Fokus Permasalahan: Titik banjir, penumpukan sampah.
   - Foto Dokumentasi: Galeri foto kondisi terkini.
   - Data Pendukung: Rencana solusi dan potensi lokal.
4. **Logo Instansi Mengambang**: Logo dinas semi-transparan di area tengah antarmuka.

### DESAIN ANTARMUKA
- Modern, santai, namun tetap formal (pemerintah).
- Huruf tegas, warna bersih, tata letak minimalis.
- Responsif (Mobile & Desktop).

### ALUR KERJA
1. Buka WebGIS.
2. Muat peta dasar & polygon.
3. Logo mengambang terlihat.
4. Interaksi peta (pan/zoom).
5. Klik polygon -> Muncul popup informasi.