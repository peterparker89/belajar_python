#bangunruang.py (module)
import math
def volumeTabung(r,tinggi_tabung):
    v_Tabung=math.pi*r*r*tinggi_tabung
    return v_Tabung
def volumeKerucut(r,tinggi_kerucut):
    v_Kerucut=1/3*math.pi*r*r*tinggi_kerucut
    return v_Kerucut
def volumeBalok(panjang,lebar,tinggi_balok):
    v_Balok=panjang*lebar*tinggi_balok
    return v_Balok
def volumePrisma(panjang,lebar,tinggi_prisma):
    v_Prisma=1/2*panjang*lebar*tinggi_prisma
    return v_Prisma
