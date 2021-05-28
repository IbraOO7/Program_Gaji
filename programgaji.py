import time
import sys

class Pegawai(object):
    nama = None
    usia = None
    jabatan = None
    lembur = None
    gaji_pokok = None
    total = None

    def __init__(self,nama,usia,jabatan,lembur,gaji_pokok,total):
        self.nama = nama
        self.usia = usia
        self.jabatan = jabatan
        self.lembur = lembur
        self.gaji_pokok = gaji_pokok
        self.total = total

    def cetak(self):
        print("\n Nama Pegawai: " + self.nama  + "\n Usia: " + self.usia + "\n Jabatan: " + self.jabatan, 
              "\n Lembur: ", self.lembur, "\n Gaji Pokok: ", "Rp.{:,}".format(self.gaji_pokok) , "\n Total: ",
              "Rp.{:,}".format(self.total))
    

def awal():
    try:
        nama = input("Masukkan nama: ")
        usia = input("Masukkan usia: ")
        jabatan = input("Masukkan jabatan: ")
        lembur = int(input("Masukkan jumlah lembur: "))
        if jabatan == "Direktur":
            gaji_pokok = 15000000
            upah_lembur = 60000
            tot_lembur = int(lembur) * int(upah_lembur)
            total = int(tot_lembur) + int(gaji_pokok)
            isinya = Pegawai(nama,usia,jabatan,lembur,gaji_pokok,total)
            isinya.cetak()
            
        elif jabatan == "Manager":
            gaji_pokok = 10000000
            upah_lembur = 60000
            tot_lembur = int(lembur) * int(upah_lembur)
            total = int(tot_lembur) + int(gaji_pokok)
            isinya = Pegawai(nama,usia,jabatan,lembur,gaji_pokok,total)
            isinya.cetak()
            
        else:
            gaji_pokok = 5000000
            upah_lembur = 60000
            tot_lembur = int(lembur) * int(upah_lembur)
            total = int(tot_lembur) + int(gaji_pokok)
            isinya = Pegawai(nama,usia,jabatan,lembur,gaji_pokok,total)
            isinya.cetak()
            
    except:
        print("Ada trouble")

    finally:
        print("\n Mantap kali selamat menikmati gaji bos")
        return True

def akhir():
    while True:
        akhiri = input("Apakah anda masih ingin menggunakan program ini? ")
        if akhiri == "y" or akhiri == "ya":
            awal()
        else:
            print("Program akan dimatikan dalam waktu")
            for i in range(1,6):
                print(i)
                time.sleep(1)
            print("Ambyarrrrr")
            sys.exit()


if __name__ == '__main__':
    awal()
    akhir()

