print("Lütfen iki Değer Giriniz")
a=int(input("a:"))
b=int(input("b:"))

print("Değiştirilmeden Önceki Değer:\n a: {} b:{}\n".format(a,b))
a,b=b,a

print("Değiştirildikten Sonraki Değer:\n a:{} b:{}\n".format(a,b))