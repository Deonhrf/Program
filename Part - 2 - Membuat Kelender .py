# Belajar membuat program untuk melihat kelender

# pertama - import packages celender
import calendar
import os




os.system('cls')
# Header Program 
print(f'{"---------------------------------" :^50}')
print(f'{"KELENDER TAHUNAN" :^50}')
print(f'{"WITH DEON HAREFA !!!" :^50}')
print(f'{"----------------------------------" :^50}')


print("\nSilahkan masukkan tahun kelender yang anda ingin lihat dibawah ini !!!")
# kedua - meminta inputan user
yy = int(input("Masukkan Tahun \t\t= "))



# Porses program
def semua_bulan(*args) :
    global yy 
    nilai = 1
    while nilai <= 13 :
        print(calendar.month(yy,nilai))
        nilai += 1
        if nilai >= 13 :
            break

    # for i in range(hasil) :
    #     print(calendar.month(yy,i))
    # return bulan


print('\n')
# Pemanggilan sifungsi semua_bulan
semua_bulan()

print('\n')
print(f'{"---------------------------------------------------" :^50}')
print(f'{"SEGENAP HATI SAYA MENGUCAPKAN " :^50}')
print(f'{"SELEMAT HARI NATAL DAN SELAMAT TAHUN BARU" :^50}')
print(f'{"TUHAN YESUS MEMBERKATI SAUDARA !!!" :^50}')
print(f'{"---------------------------------------------------" :^50}')

