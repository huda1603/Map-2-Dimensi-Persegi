def posisi_p(maplist):
    indeks_p_awal = 0
    urutan_p_awal = 0
    urutan_p_akhir = 0
    indeks_p_akhir = 0
    for i in range(len(maplist)):
        if "Y" in maplist[i]:
            indeks_p_awal = maplist[i].find("Y")
            urutan_p_awal = i
        if "Z" in maplist[i]:
            indeks_p_akhir = maplist[i].find("Z")
            urutan_p_akhir = i
    return indeks_p_awal, urutan_p_awal, indeks_p_akhir, urutan_p_akhir

def proses_map(i_p_awal, u_p_awal, i_p_akhir, u_p_akhir):
    ket_horizontal = ""
    ket_vertikal = ""
    horizontal = 0
    vertikal = 0
    hasil = 0
    negatif_x = False
    negatif_y = False
    
    if i_p_awal < i_p_akhir:
        horizontal = i_p_akhir - i_p_awal
    else:
        negatif_x = True
        horizontal = i_p_awal - i_p_akhir
    
    if u_p_awal < u_p_akhir:
        vertikal = u_p_akhir - u_p_awal
    else:
        negatif_y = True
        vertikal = u_p_awal - u_p_akhir
                              
    hasil = horizontal + vertikal
    if negatif_x:
        if horizontal > 0:
            ket_horizontal = " Langkah Ke Kiri"
    else:
        if horizontal > 0:
            ket_horizontal = " Langkah Ke Kanan"
    if negatif_y:
        if vertikal > 0:
            ket_vertikal = " Langkah Ke Atas"
    else:
        if vertikal > 0:
            ket_vertikal = " Langkah Ke Bawah"
    return hasil, horizontal, vertikal, ket_horizontal, ket_vertikal

if __name__ == "__main__":
    hurufchar = "qwertuiopasdfghjklcvbnm09876544321@#$_&-+()/?!;:'*."
    Program = True
    while Program:
        print("==============================")
        print("**ATURAN**\nMisalnya Apabila Membuat Map 3 Baris Maka Kolomnya Harus 3 Kolom Juga\nUntuk Titik X Adalah Background Mapnya\nUntuk Titik Y Adalah Titik Mulainya\nDan Titik Z Adalah Titik Tujuannya")
        print("==============================")
        print("**INPUT**")
        while True:
            try:
                map = input("Masukkan Map Berbentuk Persegi Dengan Titik X Y Z nya: ")
                for i in map:
                    if i in hurufchar:
                        print("Error: Titik Map Tidak Valid")
                        raise ValueError
                if "x" not in map and "X" not in map:
                    print("Error: Titik X Tidak Ditemukan")
                    raise ValueError
                if "y" not in map and "Y" not in map:
                    print("Error: Titik Y Tidak Ditemukan")
                    raise ValueError
                if "z" not in map and "Z" not in map:
                    print("Error: Titik Z Tidak Ditemukan")
                    raise ValueError
                map = map.replace("x", "X").replace("y", "Y").replace("z", "Z")
                maplist = map.split(",")
                baris = len(maplist)
                for i in maplist:
                    kolom = len(i)
                    if baris != kolom:
                        print("Error: Map Yang Kamu Masukkan Tidak Berbentuk Persegi")
                        raise ValueError
            except:
                pass
            else:
                break
        i_p_awal, u_p_awal, i_p_akhir, u_p_akhir = posisi_p(maplist)
        hasil, horizontal, vertikal,ket_horizontal, ket_vertikal = proses_map(i_p_awal, u_p_awal, i_p_akhir, u_p_akhir)
        print("==============================")
        print("**OUTPUT**")
        if horizontal > 0 and vertikal > 0:
            print("Total " + str(hasil) + " Langkah\n" + str(horizontal) + ket_horizontal + "\n" + str(vertikal) + ket_vertikal)
        elif horizontal > 0:
            print("Total " + str(hasil) + " Langkah\n" + str(horizontal) + ket_horizontal)
        elif vertikal > 0:
            print("Total " + str(hasil) + " Langkah\n" + str(vertikal) + ket_vertikal)
        print("==============================")
        
        while True:
            try:
                loop = input("Ulangi?(y/t): ")
                if loop != "y" and loop != "t":
                    raise ValueError
            except:
                print("Error: Inputan Tidak Valid")
            else:
                if loop == "t":
                    print("Terima Kasih Telah Menggunakan Program Ini")
                    Program = False
                break