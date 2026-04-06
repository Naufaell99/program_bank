from nasabah import Nasabah
from rekening import Rekening

class Bank:
    def __init__(self):
        self.daftar_nasabah = []
        self.daftar_rekening = []

    def simpan_data(self):
        with open("data_bank.txt", "w") as f:
            for r in self.daftar_rekening:
                f.write(f"{r.nasabah.id_nasabah}|{r.nasabah.nama}|{r.nasabah.alamat}|{r.nasabah.no_hp}|{r.nasabah.password}|{r.no_rekening}|{r._Rekening__saldo}\n")

    def load_data(self):
        try:
            with open("data_bank.txt", "r") as f:
                for line in f:
                    data = line.strip().split("|")

                    nasabah = Nasabah(data[1], data[2], data[3], data[4])
                    nasabah.id_nasabah = int(data[0])

                    rekening = Rekening(nasabah, float(data[6]))
                    rekening.no_rekening = data[5]

                    self.daftar_nasabah.append(nasabah)
                    self.daftar_rekening.append(rekening)

            if self.daftar_nasabah:
                Nasabah.counter = max(n.id_nasabah for n in self.daftar_nasabah) + 1
                Rekening.counter = max(int(r.no_rekening) for r in self.daftar_rekening) + 1

        except FileNotFoundError:
            pass

    def daftar(self, nama, alamat, no_hp, password, saldo):
        for n in self.daftar_nasabah:
            if n.no_hp == no_hp:
                print("❌ No HP sudah terdaftar")
                return

        nasabah = Nasabah(nama, alamat, no_hp, password)
        rekening = Rekening(nasabah, saldo)

        self.daftar_nasabah.append(nasabah)
        self.daftar_rekening.append(rekening)

        self.simpan_data()

        print("\n✅ BERHASIL DAFTAR")
        print(f"ID Anda     : {nasabah.id_nasabah}")
        print(f"No Rekening : {rekening.no_rekening}")

    def login(self, no_rek, password):
        for r in self.daftar_rekening:
            if r.no_rekening == no_rek and r.nasabah.password == password:
                return r.nasabah
        return None

    def get_rekening(self, nasabah):
        for r in self.daftar_rekening:
            if r.nasabah == nasabah:
                return r

    def cari_rek(self, no_rek):
        for r in self.daftar_rekening:
            if r.no_rekening == no_rek:
                return r
        return None

    def tampilkan_rekening(self, current_user):
        print("\n=== DAFTAR REKENING TUJUAN ===")
        for r in self.daftar_rekening:
            if r.nasabah != current_user:
                print(f"{r.no_rekening} | {r.nasabah.nama}")