class ViewMahasiswa:
    @staticmethod
    def tampilkan_list(data_mahasiswa):
        print("=== List Data Mahasiswa ===")
        if not data_mahasiswa:
            print("Tidak ada data.")
        else:
            for mhs in data_mahasiswa:
                print(mhs)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("=== Detail Mahasiswa ===")
            print(mahasiswa)
        else:
            print("Data tidak ditemukan.")
