# Proyecto 2 - Diseño Estructural Optimo - MCIOC
Grupo 4 
- Verónica Guzmán
- Alejandro Bello
- Crescente Perez
<br>
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
 
## Informe 
 
* Escoja 5 barras interesantes del reticulado (identificadas por sus nodos) y manualmente realice el rediseño, buscando minimizar el peso de la barra y cumplir con F.U. < 1.0, pero cerca a 1.0 comparando con los resultados de su programa. 
<br>

* Explique en detalle su función de rediseño de cada barra. Si existen supuestos importantes, declarelos ahora. <br>
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

* Mostrar los nuevos factores de utilización, fuerzas en las barras y deformada para cada combinación de carga. Para esto, Graficando todo lo pedido y explicando sus criterios de rediseño. 
<br>

* ¿Cual es el desplazamiento vertical máximo en los nodos del tablero del reticulado antes y después de los cambios?
<br>

* Comente respecto de la nueva distribución de FU del reticulado y el peso del mismo. ¿Que cambios globales se pueden hacer para mejorar aún más el costo (peso del acero) del mismo? 
<br>
