import clases

persona = clases.Persona()

persona.setNombre("Dennys")
persona.setApellido("Ferrer")
persona.setEdad(34)
persona.setAltura(1.8)

print(persona.hablar())

informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellido("Fernandez")
informatico.setEdad(44)
informatico.setAltura(1.9)

print(informatico.programar())

informatico2 = clases.Tecnico()
print(informatico2.getLenguajes())


