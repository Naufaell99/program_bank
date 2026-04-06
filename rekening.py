from transaksi import Transaksi

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