## Tarea
## Modificando Campos 
1 - Añadir el id del profesor a la tabla salón para relacionar a un profesor con un salón.✅

2 - Añadir el salario del profesor al modelo.✅

## Creando nuevos modelos
1 - Cree un modelo Evaluacion la cual será una clase padre, esta deberá tener los siguientes atributos. Recuerde que esta debe ser abstract.

- Hora y fecha
- Curso: máximo 30 caracteres
- Evaluador: máximo 50 caracteres

2 - Cree un modelo Examen_Final el cual herede de Evaluacion, y añade los siguiente atributos.

- Atributos
    - Duración del examen: minutos como cantidad entera
    - Número de preguntas: entero
    - Puntaje total: entero

- Métodos
    - Puntaje * pregunta: debe retornar la división del número de preguntas entre el puntaje total.

3 - Cree un modelo Proyecto el cual herede de Evaluacion y añada los siguientes campos.

- Tema del proyecto: máximo 100 caracteres
- Número de grupos

4 - Del modelo Proyecto crea un modelo proxy, el cual ordena los registros por el tema del proyecto.
