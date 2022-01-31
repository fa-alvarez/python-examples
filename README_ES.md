# python_examples
El objetivo de este repositorio es contener algunos ejemplos básicos de
código python.  Todos los ejemplos están basados en código del curso
de Crash Course on Python de Google disponible en el sitio de Coursera
al día de hoy.


## Conditionals

### color_translator.py
La función color_translator recibe el nombre de un color y luego imprime su
valor hexadecimal.  Actualmente, solo soporta los tres colores primarios
aditivos (rojo, verde, azul), por lo que devuelve "unknown" (desconocido) para todos los
demás colores.

### exam_grade.py
Los estudiantes de una clase reciben sus calificaciones como Aprobado/Reprobado. Las notas de 60 o más (de 100) significan "Pass" (Aprobado). Las notas menores, "Fail" (Reprobado).  Además, las notas por sobre 95 (no incluido) son calificadas como "Top Score" (Puntuación Máxima).  Esta función recibe la nota y devuelve la correspondiente calificación.

### format_address.py
La función format_address separa partes de una cadena de dirección en nuevas cadenas: house_number y street_name, y devuelve: "house number X on
street named Y" (número de casa X en la calle de nombre Y).  El formato de la cadena de entrada es: número de casa numérico, seguido por el nombre de calle el cual puede contener números, pero nunca por sí mismos, y podría ser varias palabras de largo.  Por ejemplo, "123 Main Street", "1001 1st Ave", o "55 North Center Drive".  

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
La función count_letters cuenta la frecuencia de las letras en una cadena de entrada.  Solo se cuentan las letras, no los espacios en blanco, ni los números, ni las puntuaciones.  Las mayúsculas se consideran igual que las minúsculas.  Por ejemplo, count_letters("This is a sentence.") debería devolver
{'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

### email_list.py
La función email_list recibe un diccionario, el cual contiene nombres de dominio como claves y una lista de usuarios como valores.  Devuelve una lista que contiene direcciones email completas (e.j. diana.prince@gmail.com).

### groups_per_user.py
La función groups_per_user recibe un diccionario, el cual contiene nombres de grupo con la lista de usuarios.  Los usuarios pueden pertenecer a múltiples grupos.  Devuelve un diccionario con los usuarios como claves y una lista de sus grupos como valores.


## Functions

### convert_distance.py
La función convert_distance convierte millas en kilómetros (km).

### order_numbers.py
La función order_numbers compara dos números y los devuelve en orden creciente.
