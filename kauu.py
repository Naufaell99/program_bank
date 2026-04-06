from datetime import datetime

# ==========================
# VALIDASI INPUT
# ==========================
def input_string(pesan):
    while True:
        data = input(pesan)
        if data.replace(" ", "").isalpha():
            return data
        else:
            print("❌ Hanya huruf!")

def input_angka(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            return nilai
        except ValueError:
            print("❌ Harus angka!")

def input_hp(pesan):
    while True:
        hp = input(pesan)
        if hp.isdigit():
            return hp
        else:
            print("❌ No HP harus angka!")

def input_rekening(pesan):
    while True:
        rek = input(pesan)
        if rek.isdigit():
            return rek
        else:
            print("❌ No rekening harus angka!")

# ==========================
# CLASS NASABAH
# ==========================
class Nasabah:
    counter = 1

    def __init__(self, nama, alamat, no_hp, password):
        self.id_nasabah = Nasabah.counter
        Nasabah.counter += 1
        self.nama = nama
        self.alamat = alamat
        self.no_hp = no_hp
        self.password = password

# ==========================
# CLASS TRANSAKSI
# ==========================
class Transaksi:
    def __init__(self, jenis, jumlah):
        self.jenis = jenis
        self.jumlah = jumlah
        self.tanggal = datetime.now()

    def tampilkan(self):
        print(f"{self.jenis} | Rp {self.jumlah} | {self.tanggal.strftime('%d-%m-%Y %H:%M:%S')}")

# ==========================
# CLASS REKENING
# ==========================
class Rekening:
    counter = 1001

    def __init__(self, nasabah, saldo_awal=0):
        self.no_rekening = str(Rekening.counter)
        Rekening.counter += 1
        self.__saldo = saldo_awal if saldo_awal >= 0 else 0
        self.nasabah = nasabah
        self.transaksi_list = []

    def setor(self, jumlah):
        if jumlah <= 0:
            print("❌ Jumlah harus > 0")
            return
        self.__saldo += jumlah
        self.transaksi_list.append(Transaksi("Setor", jumlah))
        print("✅ Setor berhasil")

    def tarik(self, jumlah):
        if jumlah <= 0:
            print("❌ Jumlah harus > 0")
            return
        if jumlah > self.__saldo:
            print("❌ Saldo tidak cukup")
            return
        self.__saldo -= jumlah
        self.transaksi_list.append(Transaksi("Tarik", jumlah))
        print("✅ Penarikan berhasil")

    def transfer(self, rek_tujuan, jumlah, password_input):
        if password_input != self.nasabah.password:
            print("❌ Password salah!")
            return

        if rek_tujuan == self:
            print("❌ Tidak bisa transfer ke rekening sendiri")
            return

        if jumlah <= 0:
            print("❌ Jumlah harus > 0")
            return

        if jumlah > self.__saldo:
            print("❌ Saldo tidak cukup")
            return

        self.__saldo -= jumlah
        rek_tujuan._Rekening__saldo += jumlah

        self.transaksi_list.append(Transaksi("Transfer Keluar", jumlah))
        rek_tujuan.transaksi_list.append(Transaksi("Transfer Masuk", jumlah))

        print("✅ Transfer berhasil")

    def cek_saldo(self):
        print(f"💰 Saldo: Rp {self.__saldo}")

    def riwayat(self):
        if not self.transaksi_list:
            print("Belum ada transaksi")
        else:
            for t in self.transaksi_list:
                t.tampilkan()

# ==========================
# CLASS BANK
# ==========================
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

    # 🔑 LOGIN PAKAI NO REKENING
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

# ==========================
# MAIN PROGRAM
# ==========================
def main():
    bank = Bank()
    bank.load_data()

    while True:
        print("\n=== SISTEM BANK ===")
        print("1. Daftar")
        print("2. Login")
        print("3. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            nama = input_string("Nama: ")
            alamat = input("Alamat: ")
            hp = input_hp("No HP: ")
            password = input("Password: ")
            saldo = input_angka("Saldo Awal: ")

            bank.daftar(nama, alamat, hp, password, saldo)

        elif pilih == "2":
            kesempatan = 3
            user = None

            while kesempatan > 0:
                no_rek = input_rekening("No Rekening: ")
                password = input("Password: ")

                user = bank.login(no_rek, password)

                if user:
                    break
                else:
                    kesempatan -= 1
                    print(f"❌ Login gagal! Sisa: {kesempatan}")

            if not user:
                continue

            print(f"✅ Selamat datang {user.nama}")
            rek = bank.get_rekening(user)

            while True:
                print("\n=== MENU ===")
                print("1. Cek Saldo")
                print("2. Setor")
                print("3. Tarik")
                print("4. Transfer")
                print("5. Riwayat")
                print("6. Logout")

                m = input("Pilih: ")

                if m == "1":
                    rek.cek_saldo()

                elif m == "2":
                    rek.setor(input_angka("Jumlah: "))
                    bank.simpan_data()

                elif m == "3":
                    rek.tarik(input_angka("Jumlah: "))
                    bank.simpan_data()

                elif m == "4":
                    bank.tampilkan_rekening(user)

                    tujuan = input_rekening("No Rekening Tujuan: ")
                    r_tujuan = bank.cari_rek(tujuan)

                    if r_tujuan:
                        jumlah = input_angka("Jumlah: ")
                        pw = input("Password: ")

                        rek.transfer(r_tujuan, jumlah, pw)
                        bank.simpan_data()
                    else:
                        print("❌ Rekening tidak ditemukan")

                elif m == "5":
                    rek.riwayat()

                elif m == "6":
                    break

                else:
                    print("❌ Menu salah")

        elif pilih == "3":
            print("Terima kasih 👋")
            break

        else:
            print("❌ Pilihan salah")

if __name__ == "__main__":
    main()