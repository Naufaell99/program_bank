from datetime import datetime

class Transaksi:
    def __init__(self, jenis, jumlah):
        self.jenis = jenis
        self.jumlah = jumlah
        self.tanggal = datetime.now()

    def tampilkan(self):
        print(f"{self.jenis} | Rp {self.jumlah} | {self.tanggal.strftime('%d-%m-%Y %H:%M:%S')}")