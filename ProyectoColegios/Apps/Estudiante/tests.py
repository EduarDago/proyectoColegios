from django.test import TestCase
from Apps.Estudiante.models import Estudiante
from Apps.Estudiante.views import cargarTareasdeEstudiante
from Apps.Tarea.models import Tarea
from Apps.Curso.models import Curso
from Apps.Grupo.models import Grupo
from Apps.Grado.models import Grado
from Apps.Tema.models import Tema
from Apps.MateriaGrado.models import MateriaGrado
from Apps.Profesor.models import Profesor

from django.contrib.auth.models import User
# Create your tests here.
class Estudiante_ViewsTest(TestCase):


    def test_cargarTareasEstudiante(self):

        grado=Grado(idGrado="1")
        matgrado1=MateriaGrado(idMateriaGrado="1", nombreMateria="Matematicas", foraneaGrado_id="1")
        matgrado2=MateriaGrado(idMateriaGrado="2", nombreMateria="Biologia", foraneaGrado_id="1")
        grupo=Grupo(idGrupo="1",foraneaGrado="1")
        grupo2=Grupo(idGrupo="2",foraneaGrado="1")


        usuarios=[]
        profesores=[]
        estudiantes=[]
        for i in range(1,10):
            usuarios.append(User(id=i,password=i,last_login='2018-12-05 00:00:00.000000',is_superuser=0,username='L'+i,
                                 first_name="L"+i,last_name="L"+i,email="L"+i,is_staff=0,is_active=0,date_joined='2018-12-05 00:00:00.000000'))

            if i%2==0:
                profesores.append(Profesor(cedula=1*i,profesion="Licenciado"+i,telefono=i,codigoprofesor=i,usuario_id=usuarios[i].id))
            else:
                estudiantes.append(Estudiante(usuario=usuarios[i].id,codigo=i+"",sexo="M"),edad=i,direccion=i+"",email=i,foraneaGrupo=grupo.idGrupo)


        curso1 = Curso(idCurso="1", foraneaProfesor=profesores[0].codigoprofesor,foraneaMateriaGrado=matgrado1.idMateriaGrado,foraneaGrupo=grupo.idGrupo)
        #curso2 = Curso(idCurso="2", foraneaProfesor=profesores[1].codigoprofesor,foraneaMateriaGrado=matgrado1.idMateriaGrado,foraneaGrupo=grupo.idGrupo)
        curso3 = Curso(idCurso="3", foraneaProfesor=profesores[1].codigoprofesor,foraneaMateriaGrado=matgrado2.idMateriaGrado,foraneaGrupo=grupo2.idGrupo)



        tema1=Tema(idTema="1",nombreTema="Desigualdades",descripcionTema="fekmmvke",foraneaMateriaGrado=matgrado1.idMateriaGrado)
        tema2 = Tema(idTema="2", nombreTema="Ecuaciones", descripcionTema="fekmmvke",
                     foraneaMateriaGrado=matgrado1.idMateriaGrado)
        tema3 = Tema(idTema="3", nombreTema="Celula", descripcionTema="fekmmvke",
                     foraneaMateriaGrado=matgrado2.idMateriaGrado)

        tareas=[]
        t1=Tarea(idTarea="1",tituloTarea="Taller desigualdades 1",descripcionTarea="Resuelva",fechaLimite='2018-12-05 00:00:00.000000',
                 logrosTarea="erbb",foraneaCurso=curso1.idCurso,foraneTema=tema1.idTema)
        t2 = Tarea(idTarea="2", tituloTarea="Taller celula", descripcionTarea="Resuelva",
                   fechaLimite='2018-12-05 00:00:00.000000',
                   logrosTarea="erbb", foraneaCurso=curso3.idCurso, foraneTema=tema3.idTema)
        t3=Tarea(idTarea="3", tituloTarea="Taller ecuaciones", descripcionTarea="Resuelva",
                   fechaLimite='2018-12-05 00:00:00.000000',
                   logrosTarea="erbb", foraneaCurso=curso1.idCurso, foraneTema=tema2.idTema)
        tareas.append(t1)
        tareas.append(t2)
        tareas.append(t3)

        estudiantes[0].tareasEstudiante.add(t1)
        estudiantes[0].tareasEstudiante.add(t2)
        estudiantes[0].tareasEstudiante.add(t3)

        #self.assertIs(future_question.was_published_recently(), True)

        self.assertEqual(cargarTareasdeEstudiante("0"),tareas)