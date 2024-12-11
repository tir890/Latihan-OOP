from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

data_manager = DataMahasiswa()

def menu():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Ubah Data")
        print("4. Cari Data")
        print("5. Tampilkan Semua Data")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, prodi = InputForm.input_data()
            mahasiswa = Mahasiswa(nim, nama, prodi)
            print(data_manager.tambah_data(mahasiswa))
        elif pilihan == "2":
            nim = input("Masukkan NIM yang akan dihapus: ")
            print(data_manager.hapus_data(nim))
        elif pilihan == "3":
            nim = input("Masukkan NIM yang akan diubah: ")
            nama_baru = input("Masukkan Nama Baru (kosongkan jika tidak diubah): ")
            prodi_baru = input("Masukkan Prodi Baru (kosongkan jika tidak diubah): ")
            print(data_manager.ubah_data(nim, nama_baru or None, prodi_baru or None))
        elif pilihan == "4":
            nim = input("Masukkan NIM: ")
            mahasiswa = data_manager.cari_data(nim)
            ViewMahasiswa.tampilkan_detail(mahasiswa)
        elif pilihan == "5":
            ViewMahasiswa.tampilkan_list(data_manager.data)
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    menu()
