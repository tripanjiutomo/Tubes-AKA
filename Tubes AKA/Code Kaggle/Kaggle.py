from prettytable import PrettyTable
import matplotlib.pyplot as plt
import time
import random

# Program untuk mensimulasikan penjadwalan tugas kuliah 
# berdasarkan prioritas dengan membandingkan algoritma 
# rekursif dan iteratif.
# Anggota: 
# TRI PANJI UTOMO (2311102213) 
# Hendwi Saputra (2311102218)

class Tugas:
    def __init__(self, nama, tenggat, prioritas):
        self.nama = nama
        self.tenggat = tenggat
        self.prioritas = prioritas

    def __repr__(self):
        return f"{{nama: {self.nama}, tenggat: {self.tenggat}, prioritas: {self.prioritas}}}"

# Fungsi rekursif untuk menjadwalkan tugas
def jadwalkan_rekursif(tugas_tugas):
    if not tugas_tugas:
        return []

    tugas_prioritas_tertinggi = min(tugas_tugas, key=lambda tugas: tugas.prioritas)
    tugas_tersisa = [tugas for tugas in tugas_tugas if tugas != tugas_prioritas_tertinggi]

    return [tugas_prioritas_tertinggi] + jadwalkan_rekursif(tugas_tersisa)

# Fungsi iteratif untuk menjadwalkan tugas
def jadwalkan_iteratif(tugas_tugas):
    tugas_terjadwal = []
    salinan_tugas = tugas_tugas.copy()

    while salinan_tugas:
        tugas_prioritas_tertinggi = min(salinan_tugas, key=lambda tugas: tugas.prioritas)
        tugas_terjadwal.append(tugas_prioritas_tertinggi)
        salinan_tugas.remove(tugas_prioritas_tertinggi)

    return tugas_terjadwal

# Fungsi untuk menampilkan tabel eksekusi
def tampilkan_tabel_eksekusi(jumlah_tugas, waktu_rekursif, waktu_iteratif):
    tabel = PrettyTable(["Jumlah Tugas", "Rekursif (s)", "Iteratif (s)"])
    for n, waktu_rekursif, waktu_iteratif in zip(jumlah_tugas, waktu_rekursif, waktu_iteratif):
        tabel.add_row([n, f"{waktu_rekursif:.6e}", f"{waktu_iteratif:.6e}"])
    print(tabel)

# Fungsi untuk memperbarui dan menampilkan grafik
def perbarui_grafik(jumlah_tugas, waktu_rekursif, waktu_iteratif):
    plt.figure(figsize=(8, 6))
    plt.plot(jumlah_tugas, waktu_rekursif, label="Rekursif", marker='o')
    plt.plot(jumlah_tugas, waktu_iteratif, label="Iteratif", marker='o')
    plt.xlabel("Jumlah Tugas (n)")
    plt.ylabel("Waktu Eksekusi (detik)")
    plt.title("Perbandingan Waktu Eksekusi: Rekursif vs Iteratif")
    plt.legend()
    plt.grid(True)
    plt.show()

# Program utama
def main():
    jumlah_tugas_list = []
    waktu_rekursif_list = []
    waktu_iteratif_list = []

    while True:
        try:
            n = int(input("Masukkan jumlah tugas (atau ketik -1 untuk keluar): "))
            if n == -1:
                print("Program selesai. Terima kasih!")
                break
            if n < 0:
                print("Masukkan jumlah tugas yang positif!")
                continue

            # Generate tugas secara acak
            daftar_tugas = [
                Tugas(f"Tugas {i+1}", random.randint(1, 30), random.randint(1, 10))
                for i in range(n)
            ]

            # Ukur waktu eksekusi algoritma rekursif
            waktu_awal = time.time()
            jadwalkan_rekursif(daftar_tugas)
            waktu_rekursif = time.time() - waktu_awal
            waktu_rekursif_list.append(waktu_rekursif)

            # Ukur waktu eksekusi algoritma iteratif
            waktu_awal = time.time()
            jadwalkan_iteratif(daftar_tugas)
            waktu_iteratif = time.time() - waktu_awal
            waktu_iteratif_list.append(waktu_iteratif)

            jumlah_tugas_list.append(n)

            # Cetak tabel eksekusi
            tampilkan_tabel_eksekusi(jumlah_tugas_list, waktu_rekursif_list, waktu_iteratif_list)

            # Update dan tampilkan grafik
            perbarui_grafik(jumlah_tugas_list, waktu_rekursif_list, waktu_iteratif_list)

        except ValueError:
            print("Masukkan jumlah tugas yang valid!")

if __name__ == "__main__":
    main()