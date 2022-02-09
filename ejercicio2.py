#Calcular y Mostrar la serie Fibonacci hasta el 100. (cada número es la suma de los dos precedentes, comenzando por 0 y 1).

var a=0
var b=1
 

si valor 'c'<=100 repetir{
     c = a+b
     a = b
     b = c    
}
imprimir serie


-------------

var 'SegIngr' = ingresar cantidad en segundos

'Minutos' = Cociente de 'SegIngr' dividido por 60
var 'Segundos'= Cociente de 'Minutos'
mostrar 'Minutos' + 'Segundos'

-------------

elegir tipo de valor a introducir "pies" o "pulgadas"

introducir valor

var 'DisIngr' = valor introducido por usuario

'si' usuario eligio 'pulgadas'{
    var 'PulgadasEnCM' = 'DisIngr' multiplicada por 2.54
    imprimir 'PulgadasEnCM'
}

'si' usuario eligio 'pies'{
    var 'PiesEnCM' = 'DisIngr' multiplicada por 30.48
    imprimir 'PiesEnCM'
}

-----------------
var 'ValorHora' = 1200
var 'CantHoras' = Ingresar cantidad de horas trabajadas
var'Sueldo' = 'CantHoras' multiplicado por 'ValorHora'

-------

var 'GradosCelsius' = Ingresar cantidad de Grados
var 'GradosFarenheit' = 'GradosCelsius' *1.8 +32

---------------
var 'Velocidad' = ingrese valor
var 'Tiempo'= Ingrese valor
var 'Distancia' = 'Velocidad'*'Tiempo'
---------------
Inicio
var 'Nota1' = Ingrese Valor
var 'Nota2' = Ingrese Valor
var 'Nota3' = Ingrese Valor
var 'Nota4' = Ingrese Valor
var 'Nota5' = Ingrese Valor
var 'Nota6' = Ingrese Valor
var 'Nota7' = Ingrese Valor
var 'Promedio' = (('Nota1'+'Nota2'+'Nota3'+'Nota4'+'Nota5'+'Nota6'+'Nota7') / 7 )
Mostrar 'Promedio'
Fin
---------------
Inicio
var 'Inversion' = Ingrese valor en Pesos
var 'InteresAnual' = Ingrese valor en Porcentaje
var 'NumeroDeAnios' = Ingrese valor en Anios
var 'CapitalObtenido' = (('Inversion' + 'InteresAnual') * 'NumeroDeAnios') 
Mostrar 'CapitalObtenido'
Fin
---------

--------
Inicio
var 'Payaso' = 112
var 'munieca' = 75
var 'CantPayasos' = Ingrese Valor
var 'CantMuniecas' = Ingrese Valor

var 'PaqueteTotal' = ('Payaso' * 'CantPayasos') + ('munieca' * 'CantMuniecas')
Monstar 'PaqueteTotal'
Fin