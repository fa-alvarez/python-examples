# python-examples
Este repositorio contiene algunos ejemplos básicos de código en python.  Todos los ejemplos están basados en código del curso de Crash Course on Python de Google disponible en el sitio de Coursera al día de hoy.


## Conditionals

### color_translator.py
La función color_translator recibe el nombre de un color y luego imprime su valor hexadecimal.  Actualmente, solo soporta los tres colores primarios aditivos (rojo, verde, azul), por lo que devuelve "unknown" (desconocido) para todos los demás colores.

### exam_grade.py
Los estudiantes de una clase reciben sus calificaciones como Aprobado/Reprobado. Las notas de 60 o más (de 100) significan "Pass" (Aprobado). Las notas menores, "Fail" (Reprobado).  Además, las notas por sobre 95 (no incluido) son calificadas como "Top Score" (Puntuación Máxima).  Esta función recibe la nota y devuelve la correspondiente calificación.

### format_address.py
La función format_address separa partes de una cadena de dirección en nuevas cadenas: house_number y street_name, y devuelve: "house number X on street named Y" (número de casa X en la calle de nombre Y).  El formato de la cadena de entrada es: número de casa numérico, seguido por el nombre de calle el cual puede contener números, pero nunca por sí mismos, y podría ser varias palabras de largo.  Por ejemplo, "123 Main Street", "1001 1st Ave", o "55 North Center Drive".  

### format_name.py
Esta función recibe los parámetros first_name (primer_nombre) y last_name (apellido) y luego devuelve una cadena apropiadamente formateada.

### fractional_part.py
La función fractional_part divide el numerador por el denominador y devuelve la parte fraccional (un número entre 0 y 1).

### longest_word.py
La función longest_word se usa para comparar 3 palabras.  Devuelve la palabra con mayor número de caracteres (y la primera en la lista cuando tienen la misma longitud).

### number_group.py
La función number_group devuelve "Positive" si el número recibido es positivo, "Negative" si es negativo y "Zero" si es 0.


## Dictionaries

### add_prices.py
La función add_prices devuelve el precio total de todos los comestibles en el diccionario.

### combine_guests.py
Taylor y Rory están organizando una fiesta.  Enviaron invitaciones y cada uno guardó las respuestas en diccionarios con los nombres de sus amigos y cuántos invitados cada uno traería.  Cada diccionario es una lista parcial, pero la lista de Rory tiene información más actualizada sobre el número de invitados.  Esta función combina ambos diccionarios en uno, con cada amigo listado una sola vez, y el número de invitados del diccionario de Rory tomando precedencia en caso de que el nombre esté incluido en ambos diccionarios.  Luego, la función imprime el diccionario resultante.

### count_letters.py
La función count_letters cuenta la frecuencia de las letras en una cadena de entrada.  Solo se cuentan las letras, no los espacios en blanco, ni los números, ni las puntuaciones.  Las mayúsculas se consideran igual que las minúsculas.  Por ejemplo, count_letters("This is a sentence.") debería devolver {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

### email_list.py
La función email_list recibe un diccionario, el cual contiene nombres de dominio como claves y una lista de usuarios como valores.  Devuelve una lista que contiene direcciones email completas (e.j. diana.prince@gmail.com).

### groups_per_user.py
La función groups_per_user recibe un diccionario, el cual contiene nombres de grupo con la lista de usuarios.  Los usuarios pueden pertenecer a múltiples grupos.  Devuelve un diccionario con los usuarios como claves y una lista de sus grupos como valores.

### wardrobe.py
En Python, un diccionario solo puede contener un valor único para una clave dada.  Para solucionar esto, el valor único puede ser una lista conteniendo múltiples valores.  Este código tiene un diccionario llamado "wardrobe" (guardaropa) con artículos de ropa y sus colores.


## Functions

### convert_distance.py
La función convert_distance convierte millas en kilómetros (km).

### order_numbers.py
La función order_numbers compara dos números y los devuelve en orden creciente.


## Lists

### combine_lists.py
Un profesor con dos asistentes, Jamie y Drew, necesita una lista de estudiantes asistentes en el orden en que llegaron a la sala de clases.  Drew fue el primero en anotar quienes llegaron y luego Jamie tomó su lugar.  Después de clases, cada uno ingresó sus listas en el computador y se las envió por correo al profesor, quien necesita combinar ambas listas en el orden de llegada de cada estudiante.  Jamie avisó al profesor por correo que su lista está en orden inverso.  La función combine_lists combina ambas listas en una de la siguiente forma: el contenido de la lista de Drew, seguido de la lista de Jamie en orden inverso, para obtener una lista exacta de la llegada de los estudiantes.

### file_size.py
La función file_size recibe una tupla para almacenar información sobre un archivo: su nombre, su tipo y su tamaño en bytes.  Devuelve el tamaño en kilobytes (un kilobyte es 1024 bytes) con hasta dos decimales.

### filenames.py
Dada una lista de nombres de archivo, este código renombra todos los archivos con extensión hhp a la extensión h.

### octal_to_string.py
Los permisos de un archivo en un sistema Linux se dividen en tres conjuntos de tres permisos: lectura, escritura y ejecución para el propietario, grupo y otros.  Cada uno de los tres valores puede ser expresado como un número octal sumando cada permiso, con 4 correspondiendo a lectura, 2 a escritura y 1 a ejecución.  O puede ser escrito con una cadena usando las letras r (lectura), w (escritura) y x (ejecución) o - cuando no hay permiso otorgado.

Por ejemplo:

640 es lectura/escritura para el propietario, lectura para el grupo y sin permisos para otros; convertido en cadena sería: "rw-r-----"
755 es lectura/escritura/ejecución para el propietario, y lectura/ejecución para el grupo y otros; convertido en cadena sería: "rwxr-xr-x"

La función octal_to_string convierte un permiso en formato octal en su formato en cadena.

### odd_numbers.py
La función odd_numbers devuelve una lista de números impares entre 1 y n, incluido este último.

### pig_latin.py
La función pig_latin convierte texto en latin porcino: una simple transformación de texto que modifica cada palabra moviendo el primer caracter al final y agregando "ay" al final.  Por ejemplo, python termina como ythonpay.

### squares.py
La función squares usa una comprensión de listas para crear una lista de números cuadrados (n\*n).  Recibe las variables *start* y *end*, y devuelve una lista de cuadrados de números consecutivos entre *start* y *end*, ambos incluidos.  Por ejemplo, squares(2, 3) debería retornar [4, 9]


## Loops

### counter.py
La función counter realiza una cuenta regresiva desde *start* hasta *stop* cuando *start* es mayor que *stop*, y una cuenta progresiva desde *start* hasta *stop* en caso contrario.

### digits.py
La función digits devuelve la cantidad de dígitos que tiene un número.  Por ejemplo: 25 tiene 2 dígitos y 144 tiene 3 dígitos.

### even_numbers.py
La función even_numbers devuelve una cadena de todos los números positivos divisibles por 2 separados por espacio, hasta e incluyendo el máximo que se le entrega a la función.  Por ejemplo, even_numbers(6) devuelve “2 4 6”.

### factorial.py
La función factorial devuelve el producto de un entero y todos los enteros bajo él.  Por ejemplo, el factorial de cuatro (4!) es igual a 1\*2\*3\*4=24.

### multiplication_table.py
Esta función imprime una tabla de multiplicación (donde cada número es el resultado de multiplicar el primer número de su fila por el primer número de su columna).

### show_letters.py
La función show_letters imprime cada letra de una palabra en una línea separada.

### square.py
La función sum_squares devuelve la suma de todos los cuadrados de los números entre 0 y x (no incluido).


## OOP (Programación Orientada a Objetos)

#### animal.py
Un ejemplo de herencia que hace hablar a los animales.

### city.py
La clase City tiene los siguientes atributos: nombre, país (donde se ubica la ciudad), elevación (medida en metros), y población (aproximada, de acuerdo a recientes estadísticas).  La función max_elevation_city devuelve el nombre de la ciudad y su país (separados por coma), cuando se comparan 3 instancias definidas para una población mínima específica.  Por ejemplo, llamar a la función para una población mínima de 1 millón: max_elevation_city(1000000) debería devolver "Sofia, Bulgaria".

### clothing1.py
En este ejemplo tenemos una clase base llamada Clothing.  Una segunda clase, llamada Shirt, hereda métodos desde la clase Clothing.

### clothing2.py
Este código muestra el actual inventario de ropa por material.  Primero, agrega 6 camisas de algodón seguido de 4 pantalones deportivos de algodón.  Finalmente, imprime el resultado.

### dog.py
La clase Dog contiene un método que devuelve siete por el año ingresado (un año humano es aproximadamente 7 años de perro).

### elevator.py
Este código define una clase Elevator.  El ascensor tiene un piso actual.  También tiene un piso mínimo y un piso máximo a los cuales puede ir.  El ascensor recorre a través de los pisos solicitados.

### flower.py
Este código imprime un poema.

### fruit.py
Este es un ejemplo muy básico de herencia.

### furniture.py
Tenemos dos muebles: una mesa de madera café y un sofá de cuero rojo.  La función describe_furniture puede dar formato a una oración que describe estas piezas como sigue: "This piece of furniture is made of {color} {material}" ("Este mueble está hecho de {color} {material}").

### zoo.py
Este código muestra cuántos tipos de animales hay en una cierta categoría de un zoológico.


## Recursion

### is_power_of.py
Esta función devuelve si un número es potencia de una determinada base.  Nota: se asume que la base es un número positivo.

### sum_positive_numbers.py
La función sum_positive_numbers devuelve la suma de todos los números positivos entre el número n recibido y 1.  Por ejemplo, cuando n es 3 devuelve 1+2+3=6, y cuando n es 5 devuelve 1+2+3+4+5=15.


## String

### convert_distance.py
La función convert_distance devuelve la frase "X miles equals Y km", con Y teniendo solo un lugar decimal.  Por ejemplo, convert_distance(12) devuelve "12 miles equals 19.2 km".

### double_word.py
La función double_word devuelve la misma palabra repetida dos veces, seguido por la longitud de la nueva palabra repetida.  Por ejemplo, double_word("hello") devuelve "hellohello10".

### ex_format_method1.py
Este es un ejemplo del método format() usando un string.

### ex_format_method2.py
Este es otro ejemplo del método format() usando un string.

### ex_index.py
Este ejemplo muestra cómo encontrar la posición de "x" en "supercalifragilisticexpialidocious" usando el método index.

### first_and_last.py
Esta función devuelve True (Verdadero) si la primera letra de una cadena es igual a su última letra, y False (Falso) si son diferentes.  Una cadena vacía devuelve True.
