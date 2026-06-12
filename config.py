PROMPT_CALCULADORA = """
Resuelve,
REGLAS DE FORMATO:
- Escribe en lineas, cada linea tiene MAXIMO 16 caracteres contando espacios.
- NO uses tildes ni acentos: escribi "a" no "a con tilde", "u" no "u con tilde".
- NO uses caracteres especiales: solo letras sin acento, numeros y: + - * / = ( ) [ ] ^ . , _
- En vez de x (multiplicacion) usa: *, en vez de simbolo sigma usa: sigma, en vez de % usa pct.
- Usa 2 decimales como maximo.
- Usa abreviaciones: E[X], Var, PP, Ptarifa, Ded, sin, tend, fact, etc.
- NO uses palabras largas en lo posible.
- no expliques el procedimiendo, excepto en "Sigue la resolucion del ejercicio con explicaciones breves" , "Tema libre con explicacion breve", "Teorico"
- No hagas espacio entre lineas ni uases separadores entre lineas
"""
 
TEMAS = {
    "1": {
        "nombre": "Sigue la resolucion del ejercicio",
        "ejemplo": ""
    },
    "2": {
        "nombre": "Sigue la resolucion del ejercicio con explicaciones breves",
        "ejemplo": ""
    },
    "3": {
        "nombre": "Resuelve el ejercicio con menor numero",
        "ejemplo": (
            "si ves dos ejercicios y uno dice ejercicio 2 y otro ejercicio 4 resluelve el 2"
        )
    },
    "4": {
        "nombre": "Teorico",
        "ejemplo": (
          "a continuacion te paso el teorico que vimos en clase: 1. ¿Por qué los GLM son útiles en Predictive Analytics?
          Los GLM permiten construir tarifas segmentadas según las características del asegurado o del riesgo a suscribir. Sus principales ventajas son:
          Resultados fáciles de presentar y explicar (son fundamentales para "vender" un proyecto de tarifas basadas en scoring frente a la gerencia comercial).
          Son modelos multiplicativos: la frecuencia o el costo medio se obtienen multiplicando un valor base por una serie de factores (relatividades), lo cual es sencillo de entender y comunicar.
          Aprovechan toda la información de la base, permitiendo estimar valores incluso para combinaciones con muestra muy pequeña o nula (gracias a que el modelo "rellena" esas combinaciones usando la información del resto de las variables).
          Utilizan una cantidad reducida de parámetros comparado con tablas de tarifas tradicionales con miles de celdas.
          Aplicaciones en seguros de personas: Accidentes Personales, Asistencia al Viajero, Accidentes de Trabajo, Seguros de Salud (no solo riesgos patrimoniales/automotores).
          2. Supuestos y componentes de los GLM
          Los Modelos Lineales Clásicos (MLC) (regresión lineal tradicional) requieren tres supuestos restrictivos:
          Normalidad de la variable respuesta.
          Varianza constante (homocedasticidad).
          Aditividad de los efectos.
          Los GLM generalizan al MLC removiendo estos supuestos:
          La variable respuesta puede pertenecer a cualquier distribución de la familia exponencial (Normal, Poisson, Gamma, Binomial, Tweedie, etc.), no solo a la Normal.
          La varianza NO es constante: cambia según la media (relación media-varianza específica de cada distribución).
          Se mantiene un predictor lineal (combinación lineal de las variables explicativas y sus coeficientes Beta), pero éste se conecta con la media de la variable respuesta a través de una función de enlace (link function), lo que permite relaciones no aditivas (por ejemplo, multiplicativas si el enlace es logarítmico).
          Componentes de un GLM
          Componente aleatorio: distribución de la familia exponencial de la variable respuesta (Y).
          Componente sistemático (predictor lineal): combinación lineal de las variables explicativas (X·Beta).
          Función de enlace (link function): relaciona la media esperada de Y con el predictor lineal.
          3. Output típico de un GLM — Conceptos clave
          Beta (β): coeficiente estimado para cada nivel de cada variable. Indica el efecto de esa categoría sobre el predictor lineal.
          Exp(B) o "Relatividad" (e^β): es el factor multiplicativo que se aplica sobre la base. Es la forma "traducida" del Beta a un lenguaje comercial/tarifario.
          Ejemplo: si para "40 años" el Exp(B) = 0,819, significa que a los 40 años se es 18,1% menos riesgoso que la categoría base (21 años).
          Ejemplo: Buenos Aires con Exp(B)=1,221 implica ser 22,1% más riesgosa que Santa Fe (categoría base).
          Universitario (Exp(B)=0,756) implica 24,4% menos riesgo que Secundario (base).
          Categoría Base (nivel de referencia): la categoría de cada variable que tiene Beta = 0 y por lo tanto Exp(B) = 1. Todas las demás categorías se comparan (relativizan) contra ella.
          Error Estándar: mide la precisión de la estimación del Beta.
          Chi-cuadrado de Wald y Significatividad (Sig.): prueban si el coeficiente Beta es estadísticamente distinto de 0 (es decir, si la categoría es significativamente diferente de la base). Si Sig. > 0,05 (umbral habitual), la categoría no es significativamente distinta de la base.
          Expuestos y Siniestros: tamaño de la muestra detrás de cada categoría (relevante para evaluar la confiabilidad de la estimación).
          Escala: parámetro de dispersión del modelo (relevante en modelos Gamma/Tweedie)
          Cómo se calcula una estimación (cotización)
          La frecuencia o costo medio estimado se obtiene multiplicando:
          Valor Base (Exp del Intercepto) × Exp(B) de cada variable relevante para ese riesgo
          Ejemplo del webinar: para un Camión, Zona 2, fabricación Nacional, 7 años de antigüedad, conductor de 41 años → se multiplican las relatividades correspondientes de cada variable y se obtiene la frecuencia estimada (2,0696%).
          4. Modelos GLM típicos en la actividad aseguradora
          4.1 Poisson — Frecuencia de siniestros
          Modelo multiplicativo estándar para modelar cantidad de siniestros / frecuencias.
          Propiedad clave: es invariante respecto a la unidad de tiempo. Medir frecuencias mensuales o anuales no cambia el resultado relativo del modelo (es decir, da el mismo resultado proporcional).
          4.2 Gamma — Costo Medio (severidad)
          Modelo multiplicativo estándar para modelar intensidad o costo medio de los siniestros.
          Su forma general la hace apropiada para modelar montos de siniestros.
          Propiedad clave: es invariante respecto de la unidad monetaria. Trabajar en pesos o en miles de pesos no afecta el resultado final del cálculo (relatividades).
          4.3 Logit / Logístico — Retención de carteras
          Modelo típico para analizar retención de clientes (variable respuesta binaria: renovó / no renovó).
          Usa una función de enlace Logit con término de error de distribución Binomial.
          La transformación Logit da resultados acotados entre 0 y 1 (probabilidades), independientemente de la magnitud de las variables explicativas.
          Importante: en este modelo, el Exp(B) no tiene el significado habitual de "relatividad" multiplicativa simple como en Poisson/Gamma — es un odds ratio (razón de probabilidades).
          4.4 Tweedie — Prima Pura
          Distribución típica para modelar directamente la Prima Pura (PP = Frecuencia × Costo Medio).
          Características de la distribución Tweedie:
          Masa de probabilidad en cero (pólizas sin siniestros).
          Rango continuo de valores positivos (pólizas con siniestros).
          Permite modelar en un solo paso lo que normalmente requeriría dos modelos separados (Frecuencia y Severidad).
          5. Construcción de Modelos GLM
          5.1 Elementos a tener en cuenta
          Volumen de datos: hay que equilibrar la experiencia histórica/tamaño de la base, la frecuencia siniestral del riesgo, y el grado de segmentación deseado.
          Es habitual combinar información de varios años y agrupar localidades para dar estabilidad al modelo, asumiendo consistencia en ese agrupamiento.
          Definición de variables explicativas y sus niveles base.
          Interacciones: analizar potenciales relaciones entre variables predictoras mediante análisis bivariados previos.
          Correlaciones (Near Aliasing): estudiar si existen correlaciones entre los expuestos de distintas variables.
          Coberturas: las variables predictoras no siempre explican igual la variable respuesta en distintas coberturas (se suele modelar por cobertura).
          5.2 Análisis previo de las bases
          Detectar registros con valores ilógicos, negativos, faltantes o nulos en bases de exposición y/o siniestros.
          Controlar el cruce de bases (siniestros sin su correspondiente grupo de expuestos).
          Definir el tratamiento de siniestros en cero y de valores extraordinarios (outliers).
          Realizar análisis univariados y bivariados previos a correr el GLM.
          5.3 Near Aliasing (cuasi-colinealidad)
          Ocurre cuando ciertas combinaciones de categorías de dos o más variables están correlacionadas (muy pocos o muchos casos en combinaciones específicas), generando relatividades distorsivas para esas combinaciones particulares.
          Ejemplo del webinar: si la frecuencia de "Camión, Zona 1" se estima multiplicando relatividades obtenidas de forma independiente (10% base × relatividad de Camión × relatividad de Zona 1), se puede llegar a un resultado claramente erróneo (ej. 4,72% o 27,78%) porque esa combinación específica no está bien representada en la muestra usada para estimar cada relatividad por separado.
          Conclusión: hay que detectar estas combinaciones "alias" y tratarlas especialmente (no confiar ciegamente en el producto de relatividades marginales).
          6. Elección inicial de variables y validación posterior
          La elección inicial está limitada por la disponibilidad y calidad de los datos.
          Se debe usar la lógica del riesgo y considerar la factibilidad legal y comercial.
          Es necesario consensuar con otras áreas de la compañía la propuesta de variables.
          Proceso de validación técnica
          Métodos de selección: Forward, Backward y Stepwise.
          Validar el poder explicativo de las variables.
          Diferenciación entre categorías: verificar que existan diferencias reales entre los niveles de cada variable.
          Criterios para decidir si el efecto de una variable es "sistemático"
          Pruebas de bondad de ajuste con y sin la variable (comparación de modelos).
          Nivel de significatividad de las variables:
          Tipo I: apropiado cuando hay un orden a priori para introducir los predictores.
          Tipo III: de aplicación más general (no depende del orden de entrada).
          Consistencia en el tiempo de las relatividades.
          Sentido común (validación de negocio).
          7. Manejo de Variables Multinivel
          Problema: variables con muchas categorías suelen tener categorías no significativas (sin evidencia estadística de diferencia respecto a la base) o con valores distorsivos (poca muestra).
          Alternativas de tratamiento (sin modelo jerárquico)
          Agrupamiento: unir categorías similares en una sola.
          Suavizado: técnicas de smoothing para moderar valores extremos.
          Eliminación: quitar la categoría o no usar la variable.
          A veces es recomendable usar modelos jerárquicos (otras veces no).
          Agrupamiento entre categorías significativas — Test del Coeficiente de Variación
          Se utiliza un test informal basado en el Coeficiente de Variación (CV) para decidir si conviene agrupar categorías que, aunque significativas individualmente, presentan relatividades cercanas entre sí.
          El CV es una medida de dispersión relativa que ayuda a determinar si las diferencias entre categorías son lo suficientemente grandes como para justificar mantenerlas separadas.
          8. Utilización de Interacciones
          Una interacción ocurre cuando el efecto de una variable cambia según el nivel/categoría de otra variable.
          Ejemplo del webinar: en general los hombres son 10% más riesgosos que las mujeres, pero en el rango de edad 50-55 años esa diferencia se reduce a solo 3%.
          Tipos de especificación
          Interacción marginal: A + B + A*B (se mantienen los efectos principales más el término de interacción).
          Interacción completa: A*B (solo el término combinado).
          Ambas especificaciones llevan a las mismas estimaciones finales, pero difieren los tests estadísticos y la cantidad de parámetros del modelo.
          Cuándo usar interacciones
          Tienen más sentido práctico entre variables con pocas categorías.
          Conviene buscar interacciones puntuales (los efectos más fuertes) en lugar de evaluar todas las combinaciones posibles de variables multinivel.
          Usarlas cuando existan interacciones reales y el contexto comercial permita aplicarlas.
          Interacciones con la variable "tiempo" son útiles para detectar efectos distorsivos pasados producidos por una suscripción particular (cambios de política de suscripción en el tiempo).
          9. Análisis de la variable "Tiempo", IBNR e IBNER
          Análisis general de la variable período
          Al analizar la variable período pueden aparecer comportamientos crecientes, decrecientes u oscilantes.
          Hay que evaluar si esto es coherente con otros análisis disponibles.
          Se debe elegir un período específico como referencia para la corrección del intercepto (es decir, a qué nivel de tarifa "anclar" el modelo).
          El último período suele tener un comportamiento atípico (no sigue la tendencia, por estar incompleto).
          Es fundamental incluir la proyección a futuro de la tendencia en la tarifa final.
          IBNR e IBNER
          IBNR (Incurred But Not Reported) e IBNER (Incurred But Not Enough Reported): siniestros ocurridos pero no reportados (o no completamente desarrollados/valuados) a la fecha de corte.
          Para evitar su efecto distorsivo, una opción es "retirarse en el tiempo" (no usar los períodos más recientes), pero esto:
          Reduce la muestra disponible.
          Hace perder la posibilidad de observar comportamientos recientes.
          Trabajar solo con casos cerrados también es un error: distorsiona tanto las frecuencias como los costos medios, y no compensa correctamente el IBNR/IBNER.
          Solución recomendada: incluir en la variable de compensación (offset) el factor de desarrollo correspondiente a cada período, de modo de "corregir" la inmadurez de los datos recientes sin descartarlos.
          Comparación: variable "tiempo" sin vs. con factores de desarrollo en el offset
          Sin factores de desarrollo: las relatividades de los períodos más recientes muestran una tendencia ascendente artificial (por la inmadurez/IBNR de esos períodos).
          Con factores de desarrollo incluidos en el offset: la tendencia temporal se corrige, mostrando el comportamiento "real" de la siniestralidad a través del tiempo.
          Punto clave: al corregir la variable tiempo mediante el offset, las relatividades de las demás variables permanecen prácticamente iguales — el ajuste del offset aísla y corrige específicamente el efecto de desarrollo/IBNR sin distorsionar el resto del modelo.
          10. Análisis de relatividades a través del tiempo
          Es recomendable hacer análisis temporales de cada variable para detectar cambios de comportamiento y evitar que un promedio histórico distorsione la tarifa.
          Estos análisis pueden ser:
          Univariados (análisis simple de la evolución de cada categoría en el tiempo), o
          GLMs segmentados corriendo el modelo en sub-períodos más cortos.
          El objetivo es evitar que las curvas/relatividades anuales "absorban" cambios que en realidad corresponden a otras variables (confusión de efectos).
          Relatividades consistentes a través del tiempo: indican que la variable tiene un efecto estable y confiable → se puede usar tal cual.
          Relatividades NO consistentes a través del tiempo: indican inestabilidad → requieren mayor análisis, posible suavizado, o revisión de la inclusión de la variable.
          11. Modelos de Costo Medio: UM vs. Porcentaje de la Suma Asegurada (S.A.)
          Los costos medios pueden modelarse de dos formas:
          En Unidades Monetarias (U.M.): la Prima Pura en U.M. se obtiene multiplicando el CM (en UM) por la Frecuencia.
          Como porcentaje de la S.A.: la Prima Pura (en % de S.A.) se obtiene multiplicando el CM (en %) por la Frecuencia.
          Práctica habitual: calcular la PP en U.M. y luego convertirla a porcentaje de una S.A. promedio.
          Ventajas/desventajas de modelar en UM
          Adecuado si el CM es estable en UM dentro de cada rango de S.A.
          En contextos inflacionarios, requiere actualización permanente.
          La S.A. (o gama del vehículo) adquiere mucha mayor relevancia como variable explicativa.
          Las relatividades del GLM no se actualizan con la frecuencia deseable (problema de mercado).
          Mayores inconvenientes al proyectar el costo medio a futuro.
          Ventajas/desventajas de modelar como % de la S.A.
          Adecuado si el CM es estable en porcentaje dentro de cada rango de S.A.
          Mejor estrategia frente a la inflación.
          Las relatividades igual deben revisarse periódicamente.
          Problema: las sumas aseguradas no siempre están bien disponibles (infraseguro, actualizaciones poco frecuentes, cláusulas de ajuste automático, seguros a valor de reposición sin S.A. explícita).
          Menor riesgo al proyectar el costo medio a futuro.
          Aspectos a considerar antes de decidir
          Dentro de cada rango de S.A., ¿los siniestros son más estables como % de la S.A. o como monto en UM?
          Agilidad de la aseguradora para actualizar valores.
          Calidad de los datos de Suma Asegurada (fijada por el asegurado, implícita, sin ajustes, etc.).
          Niveles de inflación y estabilidad del tipo de cambio.
          Existencia de índices propios de costos (mano de obra/honorarios médicos, repuestos/medicamentos, tipo de cambio) que pueden evolucionar distinto del índice general.
          Antiselección
          Riesgo de antiselección: si se modela en UM cuando en realidad el siniestro se comporta como un porcentaje constante de la S.A., o viceversa (modelar en % cuando el siniestro es constante en UM), se generan errores de tarifa que el asegurado/mercado puede explotar (eligiendo sumas aseguradas que minimicen su costo relativo), generando antiselección.
          12. Tarificación de productos con franquicias (deducibles)
          Contexto general
          En algunos mercados las coberturas de Todo Riesgo sin franquicia son habituales → se puede adaptar esa base para construir tarifas con distintas franquicias, homogeneizando monedas o trabajando con porcentajes sobre la S.A. o límite de indemnización.
          En otros mercados, las coberturas sin franquicia tienen baja participación → los daños parciales se ofrecen mayormente con franquicia, con:
          Variedad de franquicias (distintos valores).
          Pocos expuestos y siniestros por cada nivel de franquicia.
          Distorsión inflacionaria en franquicias fijas en UM.
          Necesidad de homogeneizar la información entre las distintas franquicias para aprovecharla al máximo.
          Pasos típicos en un GLM con franquicias
          Utilizar solo información de coberturas con menores franquicias al modelar frecuencia/costo medio (para no perder información por exclusión de siniestros menores).
          Desindexar las franquicias (en UM) a valores comercializables y unificar la información a moneda del momento del análisis.
          Alternativamente, utilizar valores porcentuales respecto de las S.A.
          Correr los GLM y analizar la lógica de las variables.
          Importante: las relatividades NO se mantienen iguales entre las distintas franquicias (cada nivel de franquicia tiene su propia estructura de relatividades).
          Distribución de siniestros TRSF (Todo Riesgo Sin Franquicia)
          Al introducir una franquicia, ciertos siniestros (los de monto menor a la franquicia) se eliminan, lo que:
          Reduce la frecuencia (menos siniestros indemnizables).
          Modifica (recalcula) el Costo Medio del siniestro (se recalcula descontando el tramo cubierto por la franquicia).
          Franquicias en UM vs. en % de la S.A.
          Franquicias en UM: obligan a que la S.A. y/o gama del vehículo sean muy relevantes como variables de segmentación. Con el paso del tiempo, las franquicias fijas pierden poder adquisitivo; si no se ajustan, las frecuencias y costos medios reales serán mayores a los modelados.
          Franquicia como % de la S.A.: con el tiempo también puede distorsionarse (requiere análisis periódicos). Requiere buena calidad de datos de S.A.; si hay infraseguro, se distorsionan los resultados.
          Comparación de resultados finales
          Buscar coherencia técnica y comercial entre las distintas franquicias.
          Decidir si conviene fijar valores mínimos y máximos según política de la aseguradora y los valores extremos que arrojen los distintos GLMs.
          Al comparar relatividades entre franquicias por zona/categoría, se busca verificar si la lógica se repite consistentemente; si una relatividad "baja" de forma inesperada en alguna franquicia, hay que entender por qué (podría ser muestra pequeña → considerar unificar comportamiento).
          13. Variables de Respuesta Binaria — Regresión Logística (Distribución Logística)
          Para retención de clientes (variable: Renovó / No Renovó), el modelo típico usa función de enlace Logit con error Binomial → modelo logístico.
          La función Logit transforma cualquier valor del predictor lineal a un resultado entre 0 y 1 (probabilidad), independientemente de la magnitud de las variables explicativas.
          Otras funciones de enlace para respuesta binaria
          Probit: también simétrica como la Logit, pero converge más rápido a 0 y a 1 (colas más "cortas").
          Log-log: asimétrica.
          Interpretación del output
          En regresión logística, Exp(B) es un odds ratio, por lo que no tiene el significado habitual de "relatividad" multiplicativa de Poisson/Gamma sobre una frecuencia o costo medio — se interpreta como la razón de probabilidades (odds) de un evento entre una categoría y la base.
          Para obtener la probabilidad estimada de un caso particular (ej. probabilidad de renovación), se combinan los Betas relevantes a través de la función logística (transformación inversa del Logit), no mediante simple multiplicación de relatividades. En el ejemplo del webinar, la probabilidad estimada de renovación para un caso particular fue 83,14%.
          14. Restricciones sobre la tarifa teórica y uso del Offset
          Concepto de Offset
          El offset es un término que se incluye en el modelo con coeficiente fijo (no estimado), funcionando como un ajuste conocido a priori sobre el predictor lineal — permite "forzar" o compensar efectos sin que el GLM los estime libremente.
          Restricciones sin uso del offset — Limitaciones a la tarifa teórica
          Ejemplos de restricciones externas (de mercado o regulatorias):
          Mercado: no es bien recibido diferenciar tarifas por género.
          Regulación: no se permiten descuentos por alarma vehicular.
          Efecto de no incluir una variable restringida:
          Si no hay correlación entre los expuestos de la variable restringida y el resto, al no incluirla solo se modifica el intercepto para compensar globalmente lo que no se puede diferenciar en el precio.
          Si existen correlaciones (ej. entre vehículos con alarma y ciertas localidades), las relatividades de las variables correlacionadas se distorsionan para compensar el efecto: aumentan los Betas de las categorías con más vehículos sin alarma, y disminuyen los de las restantes. Es decir, las relatividades "buscan compensar" la limitación, generando una distorsión indirecta.
          Uso del offset en reemplazo de una variable no incluida
          Caso de uso típico — subsidios cruzados entre localidades:
          Correr primero un GLM sin restricciones y observar las relatividades reales de cada localidad.
          Para lograr el subsidio cruzado deseado (ej. que localidades con mejor poder adquisitivo subsidien a otras), se incluye en el offset el LN (logaritmo natural) de cada una de las relatividades deseadas por localidad, y se corre el GLM sin esa variable como explicativa.
          Consecuencia: las variables correlacionadas y el intercepto sufren modificaciones al tratar de compensar el efecto impuesto por el offset.
          Ejemplo del webinar: la relatividad de "sin alarma" baja para compensar parcialmente el sobrecosto que se le cobra de más a Buenos Aires (por el subsidio impuesto vía offset).
          Otros ejemplos de aplicación de restricciones / offset
          Suavizar el impacto de incluir variables nuevas que penalizan fuertemente a ciertas categorías de riesgo.
          Combinar relatividades de experiencia externa (de mercado) con relatividades propias de la cartera.
          Subyace una hipótesis sobre la distribución de la cartera, su deterioro, seguimiento y corrección a lo largo del tiempo.
          15. Otros aspectos generales de los modelos GLM
          Agrupando coberturas con GLM
          Para productos "enlatados" (multirriesgo, ej. combinado familiar / multirriesgo hogar), se puede llegar a una tarifa global mediante el siguiente procedimiento:
          Calcular frecuencia y costo medio de cada cobertura.
          Obtener la Prima Pura de cada cobertura.
          Sumar las PP de todas las coberturas y agregar (si corresponde) valores fijos por póliza.
          Correr un GLM sobre las primas resultantes y expresar la tarifa final en UM o como porcentaje de la S.A. principal.
          Análisis del impacto de la nueva tarifa en la cartera vigente
          Para comparar el resultado del GLM contra la tarifa actual, se puede analizar:
          Los resultados variable por variable (impacto individual).
          El efecto global combinado de todas las modificaciones simultáneas.
          Gráfico de Impactos
          Muestra el número de expuestos de la cartera vigente que experimentarían alzas o bajas en sus primas si se implementa la nueva tarifa.
          Permite distinguir entre:
          Negocios actualmente rentables.
          Negocios actualmente NO rentables.
          El gráfico de impactos puede segmentarse por categorías de una variable particular (ej. por localidad), lo que permite identificar qué categorías son rentables y cuáles no, considerando el efecto combinado de todas las variables y las nuevas relatividades.
          Aplicación práctica: si una gran proporción de expuestos de ciertas zonas (ej. "Resto Sur" y "Buenos Aires") experimentaría fuertes alzas, esto permite repensar el suavizado de ciertas variables para atenuar el impacto del cambio de tarifa, o aplicarlo en dos o más etapas (implementación gradual)."
          )
    },
    "5": {
        "nombre": "Tema libre con explicacion breve",
        "ejemplo": ""
    },
    "6": {
        "nombre": "Tema libre",
        "ejemplo": ""
    }
}
