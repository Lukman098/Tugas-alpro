# Lampu          = 5 w
# Tv             = 75 w
# Kipas angin    = 40 w
# Harga per kwh  = 1.500
# Durasi         = 15 Jam
# Per_kwh        = 1000

biayaperkwh = 1500

#input watt
wattlampu = int(input("masukkan watt lampu = "))
wattkipas = int(input("masukkan watt kipas = "))
watttv = int(input("masukkan watt tv = "))
durasi = int(input("masukkan durasi penggunaan = "))

#hitung kwh
kwhlampu = wattlampu*durasi/1000
kwhkipas = wattkipas*durasi/1000
kwhtv = watttv*durasi/1000
print("Hasil kwh lampu = ", kwhlampu)
print("Hasil kwh kipas = ", kwhkipas)
print("Hasil kwh tv = ", kwhtv)
print("Total seluruh kwh", kwhlampu + kwhkipas + kwhtv)

#hitung biaya per hari
hari = kwhlampu + kwhkipas + kwhtv * biayaperkwh
print("Biaya perharin = ", hari)

#hitung biaya per bulan
bulan = hari*30
print("Biaya perbulan = ", bulan)
