from caso_D import caso_D
from caso_L import caso_L
from graficar3d import ver_reticulado_3d

print("Caso Pre-Optimización:")

ret_D = caso_D()
ret_L = caso_L()

ver_reticulado_3d(ret_D, 
	axis_Equal=False, 
	opciones_barras={
	"ver_numeros_de_barras": False
	}, 
    llamar_show=True,
    zoom=280.,
    deshabilitar_ejes=True)


#Peso propio
ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
f_D = ret_D.recuperar_fuerzas()

#Carga Viva
ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
f_L = ret_L.recuperar_fuerzas()

#Combinaciones de carga
f_1 = 1.4*f_D           #Combinacion 1
f_2 = 1.2*f_D + 1.6*f_L #Combinacion 2

# Calcular factores 
FU_caso1 = ret_D.recuperar_factores_de_utilizacion(f_1)
FU_caso2 = ret_D.recuperar_factores_de_utilizacion(f_2)


import matplotlib.pyplot as plt

ver_reticulado_3d(ret_D,
    axis_Equal=False,
    opciones_nodos = {
        "usar_posicion_deformada": False,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 1: 1.4 D ")
plt.show()



ver_reticulado_3d(ret_D,
    axis_Equal=False,  
    opciones_nodos = {
        "usar_posicion_deformada": False,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 1: 1.2 D + 1.6 L")
plt.show()




ver_reticulado_3d(ret_D,
    axis_Equal=False,  
    opciones_nodos = {
        "usar_posicion_deformada": False,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso 1: 1.4 D ")
plt.show()



ver_reticulado_3d(ret_D,
    axis_Equal=False, 
    opciones_nodos = {
        "usar_posicion_deformada": False,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso 2: 1.2 D + 1.6 L")
plt.show()


peso = ret_D.calcular_peso_total()

print(f"peso total = {peso}")

# Para obtener las deformaciones del caso pre-optimización:
    
nodos = 11
for a in range(nodos):
    print(f" nodo {a}: {ret_D.obtener_desplazamiento_nodal(a)*100}")



#------ OPTIMIZACION -------#

print("CASO OPTIMIZADO:")

ret_opt_D = caso_D()
ret_opt_L = caso_L()


# PESO PROPIO
ret_opt_D.ensamblar_sistema()
ret_opt_D.resolver_sistema()
f_opt_D = ret_opt_D.recuperar_fuerzas()

# CARGA VIVA
ret_opt_L.ensamblar_sistema()
ret_opt_L.resolver_sistema()
f_opt_L = ret_opt_L.recuperar_fuerzas()


# REDISEÑAR 
barras_a_rediseñar = [2, 28, 4, 23, 29]
barras = ret_opt_D.obtener_barras()
for i in barras_a_rediseñar:
    barras[i].rediseñar(f_opt_D[i], ret_opt_D)

ret_opt_D.ensamblar_sistema()
ret_opt_D.resolver_sistema()
f_opt_D = ret_opt_D.recuperar_fuerzas()

'''
# RETICULADO
ver_reticulado_3d(ret_opt_D, 
    axis_Equal=False, 
    opciones_barras={
    "ver_numeros_de_barras": False
    }, 
    llamar_show=True,
    zoom=280.,
    deshabilitar_ejes=True)
plt.title(" Reticulado Optimizado ")
plt.show()
'''

#COMBIS CARGAS
f_opt1 = 1.4*f_opt_D               #Combinacion 1
f_opt2 = 1.2*f_opt_D + 1.6*f_opt_L #Combinacion 2

# FU
FU_opt1 = ret_opt_D.recuperar_factores_de_utilizacion(f_opt1)
FU_opt2 = ret_opt_D.recuperar_factores_de_utilizacion(f_opt2)


import matplotlib.pyplot as plt

ver_reticulado_3d(ret_opt_D,
    axis_Equal=False,
    opciones_nodos = {
        "usar_posicion_deformada": False,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_opt1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Optimizado: - Tensiones en caso 1: 1.4 D ")
plt.show()



ver_reticulado_3d(ret_opt_D,
    axis_Equal=False,  
    opciones_nodos = {
        "usar_posicion_deformada": False,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_opt2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title(f"Optimizado - Tensiones en caso 1: 1.2 D + 1.6 L")
plt.show()




ver_reticulado_3d(ret_opt_D,
    axis_Equal=False,  
    opciones_nodos = {
        "usar_posicion_deformada": False,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_opt1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU Optimizado - caso 1: 1.4 D ")
plt.show()



ver_reticulado_3d(ret_opt_D,
    axis_Equal=False, 
    opciones_nodos = {
        "usar_posicion_deformada": False,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_opt2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU Optimizado - caso 2: 1.2 D + 1.6 L")
plt.show()


peso = ret_opt_D.calcular_peso_total()

print(f"peso total al optimizar = {peso}")

# Para obtener las deformaciones del caso optimizado:
    
nodos = 11
for a in range(nodos):
    print(f" nodo {a}: {ret_opt_D.obtener_desplazamiento_nodal(a)*100}")

