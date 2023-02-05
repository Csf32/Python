
notas = {
    
    "Caique": 9.1,
    "Eliana": 9.0,
    "Vera": 9.2
}
print(notas)
print()

print(notas["Caique"])
print()

print(notas.keys())
print()

print(notas.values())
print()

print("Gilberto" in notas)
print("Vera" in notas)
print()

del notas["Caique"]
print(notas)
print()


notas["Antonio"] = 10.0
print(notas)
print()

print(notas.get("Geraldo", "Não encontrado!"))
print()

print(type(notas))
