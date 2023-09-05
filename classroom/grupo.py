from classroom.asignatura import Asignatura

class Grupo:
    
    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas= [], estudiantes = []):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        Grupo.grado = "Grado 12"

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista = None):
        if lista == None:
            lista = []

        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return "grupo de estudiantes: " + self._grupo
        

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
