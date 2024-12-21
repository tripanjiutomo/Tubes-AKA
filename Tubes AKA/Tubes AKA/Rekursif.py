class Tugas:
    def __init__(self, nama, tenggat, prioritas):
        self.nama = nama
        self.tenggat = tenggat
        self.prioritas = prioritas

    def __repr__(self):
        return f"{{nama: {self.nama}, tenggat: {self.tenggat}, prioritas: {self.prioritas}}}"

def jadwalkan_rekursif(tugas_tugas):
    if not tugas_tugas:
        return []

    tugas_prioritas_tertinggi = min(tugas_tugas, key=lambda tugas: tugas.prioritas)
    tugas_tersisa = [tugas for tugas in tugas_tugas if tugas != tugas_prioritas_tertinggi]

    return [tugas_prioritas_tertinggi] + jadwalkan_rekursif(tugas_tersisa)

def main():
    daftar_tugas = []
    while True:
        try:
            nama = input("Masukkan nama tugas (atau ketik 'selesai' untuk berhenti): ")
            if nama.lower() == 'selesai':
                break
            tenggat = int(input("Masukkan tenggat waktu (hari): "))
            prioritas = int(input("Masukkan prioritas (1-10, 1 prioritas tertinggi): "))
            daftar_tugas.append(Tugas(nama, tenggat, prioritas))
        except ValueError:
            print("Input tidak valid. Masukkan angka untuk tenggat dan prioritas.")

    tugas_terjadwal = jadwalkan_rekursif(daftar_tugas)
    print("\nJadwal Tugas (Rekursif):", tugas_terjadwal)

if __name__ == "__main__":
    main()