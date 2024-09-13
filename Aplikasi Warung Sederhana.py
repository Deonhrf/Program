# return adalha nilai kembali

import os






os.system('cls')
pil_makanan = ['indomie','telur','pop mie'] # list makanan
pil_minuman = ['susu','ale-ale','fanta'] # list minumna

def warung () :
    print(f'================================')
    print(f'SELAMAT DATANG DI WARUNG RIZKY')
    print(f'{'Jln. Ampera Poncol No. 19':^30}')
    print(f'================================')
    print(f'1. Belanja  \n2. Keluar')




def makanan(pil_makanan) :
    print('\n\n')
    print(f'--------------------------------')
    print(f'Pilihan Makanan ada dibawah ini ')
    print(f'--------------------------------')
    print('+---------------------------------------+')
    print('| KODE |    Makanan    |       Harga    |')
    print('+---------------------------------------+')
    print('| 0010 |     Indomie   |   Rp. 3,000    |')
    print('| 0011 |     Kerupuk   |   Rp. 5,000    |')
    print('| 0012 |      Telur    |   Rp. 2,500    |')
    print('+---------------------------------------+')

    #for indkes, pil_nama in enumerate(pil_makanan) :
     #   print(f'{indkes + 1}. {pil_nama}')
        


def minuman(pil_minuman) :
    print('\n\n')
    print(f'--------------------------------')
    print(f'Pilihan Minuman ada dibawah ini ')
    print(f'--------------------------------')
    print('+---------------------------------------+')
    print('| KODE |    Minuman    |       Harga    |')
    print('+---------------------------------------+')
    print('|  1   |  Air Mineral  |   Rp. 3,000    |')
    print('|  2   |     Susu      |   Rp. 4,000    |')
    print('|  3   |    Sprite     |   Rp. 7,000    |')
    print('+---------------------------------------+')
    #for indkes, pil_nama2 in enumerate(pil_minuman) :
     #   print(f'{indkes + 1}. {pil_nama2}')



# isi program bagian depan
def isi_program():
    #while True :
        # pembuka program
        pilihan = int(input('Pilihan anda = ')) 
        if pilihan ==  1 :
            #print('\nWARUNG RIZKY !!!')
            while True :
                minuman(pil_minuman)
                print('\n(*) Silahkan masukkan belanjaan anda didalm keranjang berdasarkan kode barang !!!')
                keranjang_minuman = int((input('Kode barang \t= ')))
                keranjang_minuman2 = int( (input('Jumlah barang \t= ')))
                if keranjang_minuman == 1:
                    hasil0001 = (3000*keranjang_minuman2)
                    print('--------------------------------------------')
                    print(f'{'Air Mineral'}\t{keranjang_minuman2}\t{hasil0001}')
                    print('--------------------------------------------')
                elif keranjang_minuman == 2:
                    hasil0001 = (4000*keranjang_minuman2)
                    print('--------------------------------------------')
                    print(f'{'Susu'}\t{keranjang_minuman2}\t{hasil0001}')
                    print('--------------------------------------------')
                elif keranjang_minuman == 1:
                    hasil0001 = (7000*keranjang_minuman2)
                    print('--------------------------------------------')
                    print(f'{'Sprite'}\t{keranjang_minuman2}\t{hasil0001}')
                    print('--------------------------------------------')
                print('Apakah anda ingin belanja minuman yang lain !!!')
                print('1. Yes \n2. Keluar dan Bayar')
                jawaban = int(input('Silahkan Masukkan Pilihan Anda = '))
                print('\n')

                    
        elif pilihan == 2 :
            #print('\nWARUNG RIZKY !!!')
            makanan(pil_makanan)
        else : 
            print(f'Data yang dimasukkan salah')
        # berhenti = input('Apakah anda ingin mengulangi program ini !!! (y/n) ? \nPilihan anda = ')
        # if berhenti == 'n' :
        #     break
        # else :
        #     print('Data yang anda masukkan salah ')
        #     print('Program selesai !!!')
        #     break
        

    

# program selesai (break)
def penutup ():
    print(f'\n\n---------------------------------------')
    print('TERIMA KASIH TELAH BERBELANJA DISINI')
    print('SAMPAI JUMPA LAGI')
    print('UMAHH')
    print(f'---------------------------------------')


# bagian dalam program

    

# inti program dibawah ini 

warung()
pil_1 = int(input('Pilihan Anda = '))
if pil_1 == 1 : 
    print('\nSilahkan Mau belanja apa !!!')
    print('1. Minuman \n2. Makanan')
    isi_program()
    

#def pembuka() :
