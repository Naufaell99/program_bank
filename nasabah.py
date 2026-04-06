class Nasabah:
    counter = 1

    def __init__(self, nama, alamat, no_hp, password):
        self.id_nasabah = Nasabah.counter
        Nasabah.counter += 1
        self.nama = nama
        self.alamat = alamat
        self.no_hp = no_hp
        self.password = password