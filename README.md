# Proyecto 2 - Diseño Estructural Optimo - MCIOC
Grupo 4 
- Verónica Guzmán => encargada de pasar a 3D y las funciones de barra.py
- Alejandro Bello => deformaciones + informe
- Crescente Perez => encargado de los archivos caso_D.py caso_L.py
<br>

# E4 - Análisis y diseño automático de un reticulado 3D
## Output ejemplo_4_casos_de_analisis.py
### Reticulado
 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Output/Figura_Reticulado.png) 
 <br>
### Caso 1,4D
 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Output/Caso_1%2C4D.png) 
 <br>
##### FU
 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Output/FU_1%2C4D.png) 
 <br>
### Caso 1,2D + 1,6L
 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Output/Caso_1%2C2D1%2C6L.png) 
 <br>
#### FU
 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Output/FU_1%2C2D1%2C6L.png) 
 <br>
### Peso Total
 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Output/Pesos.png) 
 <br>
 
 <br>
 
# Informe 
 
#### Escoja 5 barras interesantes del reticulado (identificadas por sus nodos) y manualmente realice el rediseño, buscando minimizar el peso de la barra y cumplir con F.U. < 1.0, pero cerca a 1.0 comparando con los resultados de su programa.<br>
Barras a rediseñar y sus respectivos R,t con el FU obtenido al optimizar =>  
   - [2 (nodos 2-3)] ->  R, t : [ 0.01, 0.001] -> FU: C1(0.01), C2(0.18)
   - [28 (nodos 4-5)] -> R, t : [ 0.04, 0.001] -> FU: C1(0.17), C2(0.44)
   - [4 (nodos 9-10)] ->  R, t : [ 0.01 0.001] -> FU: C1(0.01), C2(0.18)
   - [23 (nodos 2-5)] -> R, t : [ 0.01, 0.002] -> FU: C1(0.00), C2(0.01)
   - [29 (nodos 5-6)] -> R, t : [ 0.04. 0.001] -> FU: C1(0.17), C2(0.44)
<br>
Llegando a un peso total del reticulado de: 

 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Optimizado/Pesos.png) 
<br>

#### Explique en detalle su función de rediseño de cada barra. Si existen supuestos importantes, declarelos ahora. <br>
Segun lo que se nos fue explicado en clases, la idea de la función de rediseñar era encontrar valores optimos y logicos tanto para el radio R y el espesor t con el fin de que su F.U fuera lo más cercano a 1.
Partimos creando dos listas (tipo arange) tanto para R como para t donde cada valor maximo dependia de lo que dispuesto en el enunciado, que el radio era 8cm y el espesor 5mm valores que fueron considerados como los maximos. Luego con las listas creadas se buscó la forma de crear distintas combinaciones y buscando en internet llegamos que itertools servia para crear una lista con todas las combinaciones posibles para valores de R y t.
Por cada combinacion se fue calculando el Area, Inercia, Radio de giro y las que cumplieran la condición:
<br>
<img src="https://latex.codecogs.com/gif.latex?%5Csqrt%7B%5Cfrac%7BL%7D%7BRadio%20de%20giro%7D%7D%5Cleq%20300" /> 
<br>
las combinaciones que cumplian la condicion anterior se fueron guardando en otra lista llamada cumple.
Luego por cada combinacion en cumple, se debia verificar que el valor de FU < 1. Se divieron en los casos < 0 (es decir los negativos que se encuentran en compresión) ya que dependen de:
<br>
<img src="https://latex.codecogs.com/gif.latex?min%28%5Cfrac%7BArea%7D%7B%5Csigma%20y%7D%3B%20%5Cpi%20%5E%7B2%7D%5Cfrac%7BEI%7D%7BL%5E%7B2%7D%7D%29" />
<br>
mientras que los casos > 0 (es decir los positivos que se encuentran en tracción) solo se debe considerar el caso de:
<br>
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BArea%7D%7B%5Csigma%20y%7D" />
<br>
Como se dijo anteriormente, se tenia que cumplir la condicion de:
<br>
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cleft%20%5C%7C%20Fu%20%5Cright%20%5C%7C%7D%7B%5Cphi%20Fn%7D%5Cleq%201" />
<br>
las que cumplian se fueron guardando en una lista llamada cumple_fu, la que estaba compuesta por el valor del radio, espesor y fu.
Luego para optimizar se necesitaba el valor más cercano a 1, por lo que se creó un codigo que recorria la lista cumple_fu y buscaba el valor maximo de fu para guardarlo junto con su respectivo radio y espesor en otra lista.
Finalmente al self.R y self.t se le asignaron los valores encontrados anteriormente para el FU más cercano a 1.
<br>
<br>

#### Mostrar los nuevos factores de utilización, fuerzas en las barras y deformada para cada combinación de carga. Para esto, Graficando todo lo pedido y explicando sus criterios de rediseño. 
<br>

##### Caso 1,4D
 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Optimizado/Caso_1%2C4D.png) 
 <br>
 
###### FU
 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Optimizado/Fu_1%2C4D.png) 
 <br>
 
##### Caso 1,2D + 1,6L
 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Optimizado/Caso_1%2C2D%2B1%2C6L.png) 
 <br>
 
###### FU
 ![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Optimizado/Fu_1%2C2D%2B1%2C6L.png) 
 <br>

#### ¿Cual es el desplazamiento vertical máximo en los nodos del tablero del reticulado antes y después de los cambios? <br>
Si se observan los datos que se obtuvieron para la deformación de los nodos del reticulado (Incluido los del tablero), se puede observar lo siguiente, tanto para el caso pre-optimización, y ya optimizado: 
1) Caso Pre-Optimización 

![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Desplazamientos/Deformacion_2.jpg) 
<br>
En este caso, se observan las deformaciones en todos los ejes, tanto x,y,z ---> Que se forman a través de (x,y,z).
Si vemos específicamente el caso de las deformaciones verticales nodales del tablero (Nodos = 0,1,2,3,7,8,9,10), se puede observar que la mayor deformación se encuentra en 4 de los nodos anteriormente mencionados. Específicamente, el nodo 1,2,8,9 ; Donde los dos primeros tienen deformación positiva según los ejes tomados, mientras que los otros dos nodos, poseen deformación negativa. "AMBOS POSEEN IGUAL DEFORMACIÓN ABSOLUTA".
2) Caso Optimizado

![alt text](https://github.com/vjguzman/P2-E4-MCIOC/blob/main/Desplazamientos/Deformacion_1.jpg) 
<br>
Al igual que lo anterior, analizando la deformación para el eje Y (Vertical), se observa que la mayor existe en el nodo 2, tomando el valor de 0,0007. Luego de esta, la siguen los mismos nodos mencionados anteriormente, tomando el siguiente orden ---> Nodo 2 ; Nodo 9 ; Nodo 1 ; Nodo 8. 

Como método general, es muy claro, que a simple vista, se tendrán las mayores deformaciones donde no existe un apoyo directo en la estructura, pues es en el centro del vano (O cercano a él), donde existirá una deformación mucho más clara, que en los ejes laterales de la estructura, como lo puede ser un puente, viaducto, etc. A su vez, es importante notar, que la unidad de medida utilizada para la deformación es en metros, por lo cual, la deformación en la estructura es mínima. 

#### Comente respecto de la nueva distribución de FU del reticulado y el peso del mismo. ¿Que cambios globales se pueden hacer para mejorar aún más el costo (peso del acero) del mismo? <br>
Como se puede ver en las gráficas obtenidas, las nuevas distribuciones de FU, al ser optimizadas, presentan mayores cargas en las barras superiores horizontales, en ambas combinaciones de carga, pero el peso total bajó significativamente de 24197.43 kg a 20032.14 kg, o sea que disminuyo un 17% de su peso total.
Para mejorar aún mas el costo se podría disminuir aún mas los diámetros de las barras ya optimizadas o disminuir los diámetros de las barras que no reciben cargas ni tienen deformaciones como lo son las barras entre los nodos 0-7 y 3-10.
