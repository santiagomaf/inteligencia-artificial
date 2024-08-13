# Inteligencia Artificial

Todo la participacion va a estar en ingles, todos los mail, material, informes, etc...\
el nombre de la profesora es Carla Viaretti- carla.viaretti@miuandes.cl (tiene proyectos con las fiscalias)\
generalmente se va a las 3:30 de la universidad\
la inteligencia artificial es explicativa, no reemplaza el trabajo de los otros. hay que ver donde esta mirando la maquina y saber donde poner los filtros.\
lo que más vamos a ver es deep learning, ese es el enfoque principal del ramo, vamos a hacer una maquina que en base al pasado predice el futuro.\
vamos a trabajar en google collab, python y tambien vamos a programar en bajo nivel.

### Big Data
Es más facil poder entrenar un modelo y más facil de masticar\
hay distintos tipos de datos, los cualitativos y cuantitativos.

### Algoritmos
Los supervisados son los datos que ya salen la respuesta y hacen un modelo predictivos, los no supervisados 

----
clase 13/8

## Regresión Logística

##### El proceso de KDD

Es el proceso no-trivial de indentificar patrones previamente desconocidos, válidos, nuevos y potencialmente útiles y comprensibles de los datos.\
- Aprendisaje supervisado: Se utiliza con conocimiento a-priori del comportamiento de un conjunto de observaciones, ejemplo las redes neuronales.
- Aprendisaje no-supervisado: no se utiliza el conocimiento a-priori del comportamiento de un conjunto de observaciones.

La clasificación y la regresión son tarea del aprendizaje supervisado que utilizan el conocimiento previo, la regresión tiene como diferencia que deja a márgen un umbrual de las distontas clases a las cuales puede predecir.\
La regresión logística utiliza coeficientes lineales que multiplican las variables que para modelar las relaciones con la variable de interes Y.\
Comenzamos con la regresion lineal que busca minimizar el error al explicar la relacion lineal. Mediante la finción de enlace logístico va a pasar de valores infinitos a valores entre 0 y 1 {0,1}.\
Lo que se busca no es buscar 0 o 1 sino el umbral que si es mayor a 0,5 es una clase y sino la otra.

El simbolo del B (beta): si el B0 es positivo y B1 tambien, el valor de esa variable aumenta o disminuye dependiendo si el valor ingresado es mayor o menor.\
Ej: a mayor ingreso mayor es la probabilidad que me den un crédito, a menor ingreso menor es la probabilidad que me den un credito.


La magnitud del beta: Si una variable esta siendo multiplicada por 0 o valor cercano a 0 esta pierde completamente su influencia sobre la probabilidad de ocurrencia del evento y es descartada.

#### Maxima verosimilitud
- Minimos cuadrados: regresión linea, requiere normalidad de las variables, entrega resultados sesgados

- Maxima Verosimilitud: no existe restricción sobre las variables, metodo complejo de usar, imposible previo a los 90'

Para llegar a la clasificación de regresión logistica tiene que llegar a 0 o 1 por eso se ocupa el umbral, los valores cercanos a 1 son 1 y los más cercanos a 0 son 0, (se toma general el 0,5).

La función logística es la función simoidal
$$
f(x) = \frac{1}{1 + e^{-x}}
$$

Con esta formula se saca la Maximum Likelihood Estimation.\
Ver pág 8 ppt en inglés.

Likelihood es un modelo paramétrico definido por sigma que es la condicion probabilistica para generar la opción correcta.

Ver todas las formulas del PPT de la profe en ingles

[El_pdf_acá](LR_AI_2024(ingles).pdf)


En la clasificación usamos Bernoulli y en la regresión usamos otra.






 