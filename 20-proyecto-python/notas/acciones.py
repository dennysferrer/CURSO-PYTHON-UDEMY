from notas import nota as modelo

class AccionesNotas:

    def crearNotas(self, usuario):
        titulo = input("\nEscribe el titulo de la nota: ")
        description = input("\nEscribe la descripción de la nota: ")
        nota = modelo.Nota(usuario[0], titulo, description)
        guardar = nota.guardar()

        if (guardar[0]>=1):
            print("Nota guardada perfectamente")
            print(f"{guardar[1].titulo}: {guardar[1].description}")
        else:
            print("Error al guardar la nota ...")

    def mostrarNotas(self, usuario):
        nota = modelo.Nota(usuario[0],'','')
        listadoNotas = nota.listar()
        print(f"\nLISTADO DE NOTAS DE {usuario[1]}")
        for nota in listadoNotas:
            print(f"""
            Nota_id {nota[0]}: 
            Título: {nota[2]}
            Descripción: {nota[3]}
            Fecha: {nota[4]}
            """)

    def eliminarNotas(self, usuario):
        self.mostrarNotas(usuario)
        titulo = input("\n Cual nota deseas eliminar: ")
        nota = modelo.Nota(usuario[0], titulo, '')
        notaEliminada = nota.eliminar(titulo)
        print(f"\n {usuario[1]} haz eliminado la nota {notaEliminada[1].titulo}")