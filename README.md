# Expresiones Regulares en Regex


Coincidencias Basicas 

-   . &nbsp; Cualquier Caracter, excepto nueva linea
- \d &nbsp;  Cualquier Digitos (0-9)
- \D &nbsp;  No es un Digito (0-9)
- \w &nbsp;  Caracter de Palabra (a-z, A-Z, 0-9, _)
- \W &nbsp;  No es un Caracter de Palabra.
- \s &nbsp;  Espacios de cualquier tipo. (espacio, tab, nueva linea)
- \S &nbsp;  No es un Espacio, Tab o nueva linea.

Limites
- \b  &nbsp;  Limite de Palabra
- \B  &nbsp;  No es un Limite de Palabra
- ^   &nbsp;  Inicio de una cadena de texto
- $   &nbsp;  Final de una cadena de texto

Cuantificadores:
- '*  &nbsp;     0 o Más
- '+  &nbsp;     1 o Más
- ?   &nbsp;     0 o Uno
- {3} &nbsp;     Numero Exacto
- {3,4} &nbsp;   Rango de Numeros (Minimo, Maximo)

Conjuntos de Caracteres
- []       Caracteres dentro de los brackets
- [^ ]     Caracteres que NO ESTAN dentro de los brackets

Grupos
- ( )      Grupo
- |        Uno u otro
