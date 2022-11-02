
# pembangkitan kunci (oleh Alice)
print("========== pembangkitan kunci oleh Alice ==========")
p = 2357
g = 2
x = 1751

y = (g**x) % p

print("kunci publik (y=",y,",g=",g,",p=",p,")")
print("kunci privat (x=",x,",p=",p,")")
print("\t")

# Enkripsi oleh Bob
print('=========== Enkripsi oleh Bob ============')
# pesan : 2035
m = 2035
k = 1520

a = (g**k) % p
b = ((y**k)*m) % p

print('chiperteks yg dihasilkan: (', a, ",",b,")")
# Bob mengirim chipertext ke Alice
print("\t")

# Dekripsi oleh Alice
print("========== Dekripsi oleh Alice ==========")
pangkat = p-1-x
aPangkatxMin1 = (a**pangkat) % p
    # print("pangkat", aPangkatxMin1)
dekripsi = (b*aPangkatxMin1) % p

print('hasil dekripsi: ',dekripsi)

