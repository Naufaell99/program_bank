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