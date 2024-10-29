foo = ("Belajar", "Python", "di", "Duniailkom")
bar = (100, 200, 300, 400)
baz = ("Python", 200, 6.99, True)
  
print(foo)
print(bar)
print(baz)

foo = ["Belajar", "Python", "di", "Duniailkom"]
print(type(foo))
foo = ("Belajar", "Python", "di", "Duniailkom")
print(type(foo))

foo = ("Python", 200, 6.99, True, 'Duniailkom', 99j)
  
print(foo[0])
print(foo[1])
print(foo[2])
print(foo[2:5])
print(foo[:3])
print(foo[3:])
print(foo[:])

foo = ("Python", 200, 6.99, True, 'Duniailkom', 99j)
foo[0] = 'Belajar'
print(foo)