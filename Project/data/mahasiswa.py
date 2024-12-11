class Mahasiswa:
    def __init__(self, nim, nama, prodi):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Prodi: {self.prodi}"


class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)
        return "Data berhasil ditambahkan!"

    def hapus_data(self, nim):
        for mhs in self.data:
            if mhs.nim == nim:
                self.data.remove(mhs)
                return "Data berhasil dihapus!"
        return "Data tidak ditemukan."

    def ubah_data(self, nim, nama_baru=None, prodi_baru=None):
        for mhs in self.data:
            if mhs.nim == nim:
                if nama_baru:
                    mhs.nama = nama_baru
                if prodi_baru:
                    mhs.prodi = prodi_baru
                return "Data berhasil diubah!"
        return "Data tidak ditemukan."

    def cari_data(self, nim):
        for mhs in self.data:
            if mhs.nim == nim:
                return mhs
        return None
