from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        Grupo.grado = "grado 12"

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista = None):
        if lista == None:
            lista = []

    def __str__(self):
        return "grupo de estudiantes: " + self._grupo
         pass

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
