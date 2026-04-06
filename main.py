from bank import Bank
from utils import input_string, input_angka, input_hp, input_rekening

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