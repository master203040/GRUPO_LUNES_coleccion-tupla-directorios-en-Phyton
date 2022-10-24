estuantes={"Carlos","Camila","Hervis","Alex","Estefania"}


print ("lista de estudiante desarrollo de software cesde")
print("tipo:", type (estuantes))
print("nombre del estudiante 0:",estuantes[0])
print("nombre del estudiante 1:",estuantes[1])
print("nombre del estudiante 2:",estuantes[2])
print("nombre del estudiante 3:",estuantes[3])
print("nombre del estudiante 4:",estuantes[4])


print("lista de estudiante")
for alumno in estuantes:
    print(alumno)

print("---------------------------------------")

print ("rango de los estudiantes:")
for i in range(len(estuantes)):
    print(estuantes[i])
print("---------------------------------------")

print("ciclo de los estudiantes")
i=0
while i< len(estuantes):
    print(estuantes[i])
    i=i+1
    print("-----------------------------------")