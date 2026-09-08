# 1. Instalasi Data

batas_nilai = (65,100)
nilai_masuk = []
lulus = []
remedi = []

# 2. perulangan input nilai dan berhenti input

print("masukkan nilai ujian mahasiswa satu per satu.")
print("ketik 'selesai' untuk mengakhiri input nilai.")

while True:
    input_nilai = input("masukkan nilai ujian mahasiswa (atau 'selesai'/'hapus'): ")

    if input_nilai.lower() == "selesai":
        if len(nilai_masuk) == 0:
            print("tidak ada nilai, harus ada minimal 5 nilai")
            continue
        else:
            break

    # 3. menghapus input nilai
    if input_nilai.lower() == "hapus":
        if len(nilai_masuk) == 0:
            print("belum ada nilai untuk dihapus.\n")
            continue
        print("nilai saat ini:", nilai_masuk)
        nilai_hapus = input("masukkan nilai yang ingin dihapus: ")
        try:
            nilai_hapus = int(nilai_hapus)
            if nilai_hapus in nilai_masuk:
                nilai_masuk.remove(nilai_hapus)
                if nilai_hapus in lulus:
                    lulus.remove(nilai_hapus)
                elif nilai_hapus in remedi:
                    remedi.remove(nilai_hapus)
                print(f"nilai {nilai_hapus} berhasil dihapus.\n")
            else:
                print("nilai tidak ditemukan dalam data.\n")
        except ValueError:
            print("input tidak valid.\n")
        continue

    # 4. pengelompokan nilai
    try:
        nilai = int(input_nilai)
        if nilai < 0 or nilai > batas_nilai[1]:
            print(f"nilai harus antara 0 - {batas_nilai[1]}!\n")
            continue

        nilai_masuk.append(nilai)
        if nilai >= batas_nilai[0]:
            lulus.append(nilai)
            print(f"nilai {nilai} -> LULUS\n")
        else:
            remedi.append(nilai)
            print(f"nilai {nilai} -> REMEDI\n")
    except ValueError:
        print("input tidak valid! Masukkan angka, 'hapus', atau 'selesai'.\n")

# 5. tampilkan nilai 
print("\n 'HASIL AKHIR'")
print("seluruh nilai masuk", nilai_masuk)
print("nilai ujian lulus", lulus)
print("nilai remedi", remedi)
