medida = float(input("Uma distancia em metros"))
km = medida / 1000
hm = medida / 100
dc = medida / 10
dcm = medida * 10
cm = medida * 100
mm = medida * 1000
print("A medida de {:.0f}m corresponde a {:.1f}km e {:.0f} hm a {:.0f} dc  {:.0f}metros {}dcm {:.0f}cm e {:.0f}mm".format(medida, km, hm, dc, medida,dcm, cm, mm))

