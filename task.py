# TUGAS HAL 36 ppt pertemuan 6 (Network Security)
    # Bob : p = 9433, g = 2884, x = 162
    # Alice: mengirimkan pesan 123 (k=139)
    # Tentukan:
    # a. Public dan private key yang dimiliki Bob
    # b. Chipertext yang dikirimkan Alice
    # c. Proses Deksripsi oleh Bob

# pembangkitan kunci (oleh Bob)
print("========== pembangkitan kunci oleh Bob ==========")
p = 9433
g = 2884
x = 162

y = (g**x) % p

print("kunci publik (y=",y,",g=",g,",p=",p,")")
print("kunci privat (x=",x,",p=",p,")")
print("\t")

# Enkripsi oleh ALice
print('=========== Enkripsi oleh Alice ============')
# pesan: 123
m = 123
k = 139

a = (g**k) % p
b = ((y**k)*m) % p

print('chiperteks yg dihasilkan: (', a, ",",b,")")
# Alice mengirim chipertext ke Bob
print("\t")

# Dekripsi oleh Bob
print("========== Dekripsi oleh Bob ==========")
pangkat = p-1-x
aPangkatxMin1 = (a**pangkat) % p
    # print("pangkat", aPangkatxMin1)
dekripsi = (b*aPangkatxMin1) % p

print('hasil dekripsi: ',dekripsi)

