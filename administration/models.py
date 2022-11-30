from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born_date = models.DateField()

    class Meta:
        abstract = True

class Classroom(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.TimeField()

    class Meta():
        db_table = 'classroom'

    def __str__(self):
        return self.name + " - " + self.start_time.strftime("%H:%M")

class Student(Person):
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    grade_lab = models.FloatField(default=0.0)
    grade_exam = models.FloatField(default=0.0)
    grade_final = models.FloatField(default=0.0)

    class Meta():
        db_table = 'student'

class StudentProxy(Student):
    class Meta():
        ordering = ['id']
        proxy = True
    
    def average(self):
        return self.grade_exam * 0.1 + self.grade_lab * 0.6 + self.grade_final * 0.3

class Teacher(Person):
    salary = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)

    class Meta():
        db_table = 'teacher'

class TeacherProxy(Teacher):
    class Meta():
        proxy = True

    def get_bonus(self):
        return self.salary + self.rating * 100



''' TAREA '''
# Evaluacion
class Quiz(models.Model):
    hour = models.TimeField()
    date = models.DateField()
    course = models.CharField(max_length=30)
    tester = models.CharField(max_length=50)

    class Meta():
        abstract = True

# Examen final
class FinalExam(Quiz):
    duration = models.IntegerField() # numero de minutos
    number_of_questions = models.IntegerField()
    final_grade = models.IntegerField()

class FinalExamProxy(FinalExam):
    class Meta():
        proxy = True

    def score_per_question(self):
        return self.number_of_questions / self.final_grade

# Proyecto
class Project(Quiz):
    project_title = models.CharField(max_length=100)
    number_of_groups = models.IntegerField()

class ProjectProxy(Project):
    class Meta():
        ordering = ['project_title']
        proxy = True

    def __str__(self) -> str:
        return self.project_title + ' - ' + str(self.number_of_groups)
