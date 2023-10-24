# Chile War Bot

Un proyecto realizado como aprendizaje de Python, inspirado por las versiones internacionales muy populares durante el año 2021.

Este programa es un simulador de guerra entre provincias, un programa que simula batallas y alianzas entre diferentes comunas o municipios. El funcionamiento es muy sencillo, siendo definida por una lista de listas, cuyo primer elemento es la provincia seleccionada y el resto sus vecinas. A medida de que se produzcan
conquistas o alianzas, se adquieren las comunidades vecinas y se elimina el perdedor.


El objetivo es determinar cuál de estas comunas prevalecerá al final de la simulación. El criterio de victoria es una mezcla entre azar y el factor población
El programa continuará ejecutándose mientras queden comunas/municipios en pie. 

# Turnos:

### Acciones de Batalla:

Cuando no se permiten alianzas o en una ventana donde se lanza una moneda que resulta en 0, se produce una batalla. El resultado de la batalla se determina mediante la función battle().

### Acciones de Alianza:

Cuando se permite una alianza o se lanza una moneda que resulta en 1, se produce una alianza entre comunas/municipios. El resultado de la alianza se determina mediante la función alliance().

### Continuar la Simulación:

Después de cada acción de batalla o alianza, se pausará la simulación y se te pedirá que presiones la tecla Enter para continuar.

### Fin de la Simulación:

La simulación continuará hasta que solo quede una comuna/municipio en pie. Cuando esto ocurra, se mostrará la pantalla final con el resultado.

### Guardar Resultados:

Durante la simulación, se guardan los resultados de cada batalla o alianza. Estos resultados pueden ser consultados posteriormente.

# Ventanas de Turnos:

Durante ciertos turnos específicos, las alianzas entre comunas/municipios son permitidas. Estos turnos se determinan por el número de comunas/municipios restantes. Las ventanas de turnos se definen de la siguiente manera:

Ventana 1: 2 a 5 comunas/municipios restantes.
Ventana 2: 10 a 14 comunas/municipios restantes.
Ventana 3: 25 a 29 comunas/municipios restantes.
Ventana 4: 52 a 56 comunas/municipios restantes.

Durante estos turnos, existe un 50% de probabilidad de que se genere una alianza.

# Notas Importantes:
1. Este proyecto fue realizado durante 2021 y tiene una lógica y uso de librerías bastante pobre y distinta a la que utilizaría hoy en día. Aún así, me sorprende gratamente el hecho de que la wea aun corra.
  
2. Dado que la simulación se basa en la lógica de batallas y alianzas semi aleatorias, los resultados varian en cada ejecución.

# Mejoras futuras:
Si existen interesados que quieran implementar este bot en una red social, te invito a contactarme para que podamos desarrollar mejoras y nuevas caracteristicas, por ejemplo, 
generando automaticamente las graficas utilizando GeoPandas, generación de lore mediante un LLM, la integración a la API de dicha red, entre otras nuevas caracteristicas.




