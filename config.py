PROMPT_CALCULADORA = """
Resuelve el ejercicio de teoria actuarial de los seguros patrimoniales(argentina),
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
        "nombre": "resuelve el siguiente ejercicio de ART(argentina)",
        "ejemplo":  """(RESUMEN ART - GUÍA PARA EJERCICIOS
PARTE I: PRESTACIONES Y COTIZACIÓN
1. Conceptos Base
Hojas
Concepto	Definición
Accidente de trabajo	Acontecimiento súbito y violento por el hecho u ocasión del trabajo o en el trayecto (sin interrupciones ajenas al trabajo).
Enfermedad profesional	Las incluidas en el listado del PEN o determinadas por la Comisión Médica Central.
ILT	Incapacidad Laboral Temporaria (hasta 2 años desde la 1ª manifestación).
ILP	Incapacidad Laboral Permanente. 5 situaciones: Leve, Grave, Total, Gran Invalidez, Muerte.
2. Fórmulas Base
plain
IBD = Total remuneraciones sujetas a aporte últimos 12 meses ajustadas por RIPTE / Días corridos trabajados
IBM = IBD × 30,4
ILT = IBD × (1 + % Contribución Patronal) × (Días caídos – 10)
3. Indemnizaciones ILP (In Situ / Enfermedad Profesional = ×1,20)
Hojas
Situación	%	Indemnización de Pago Único (I)	Adicional Pago Único (II)	Compensación (III)
Leve	0% < % < 50%	Máx{53 × IBM × % × 65/x ; M₁ × %}	20% de (I)	—
Grave	50% ≤ % < 66%	Máx{53 × IBM × % × 65/x ; M₁ × %}	20% de (I)	M₂
Total	% ≥ 66%	Máx{53 × IBM × 65/x ; M₁}	Máx{20% de (I); M₃}	M₃
Gran Invalidez	% ≥ 66% + necesita tercero	Igual que Total	Igual que Total	Igual que Total + Prestación mensual
Muerte	—	Máx{53 × IBM × 65/x ; M₁}	Máx{20% de (I); M₃}	M₄
Parámetros fijos (ajustar por RIPTE/ISIPA según corresponda):
M₁ = 180.000 (base enero 2010)
M₂ = 80.000
M₃ = 70.000 (para adicional) / 100.000 (compensación total/GI)
M₄ = 120.000 (compensación muerte)
x = edad del trabajador a la 1ª manifestación invalidante
Prestación mensual GI = 2.000 ajustados por ISIPA
Ajustes:
RIPTE = RIPTE mes anterior al pago / RIPTE enero 2010
ISIPA = ISIPA mes anterior al pago / ISIPA noviembre 2009
4. Cotización
Hojas
Concepto	Fórmula
Prima Pura (PU)	Costo Medio × Frecuencia = E(S)
Prima de Tarifa (PT)	PP / (1 – % Gastos – % Utilidad)
Premio	PT × (1 + Impuestos)
Tope gastos	20% de PT (comercialización máx 5% dentro de ese 20%)
Componentes de la PP agregada:
plain
PP = PP_PE + PP_ILT + PP_Leve + PP_Grave + PP_Total + PP_GI + PP_Muerte
PARTE II: RESERVAS TÉCNICAS
1. SLAP (Siniestros Liquidados a Pagar)
Monto que la aseguradora debe pagar, valuado al cierre del ejercicio.
2. IBNR (Siniestros Ocurridos No Reportados)
14% de las primas emitidas netas de cancelación de los últimos 4 trimestres.
3. Prestaciones en Especies (PE)
a) Caso a caso
Base: Siniestros denunciados últimos 2 años antes del cierre.
% ≤ 50% (leves):
Sin alta médica, O
Con alta médica en el trimestre del cálculo y pendientes de pago total/parcial.
% > 50% (graves):
Sin alta médica, O
Con alta médica + continuidad de prestaciones o pendientes de pago.
Costos mínimos por caso (ajustados trimestralmente desde oct-2019 por Tasa de Actualización de Pasivos, capitalización simple diaria).
plain
Rva Caso a caso = Σ (Reservas caso a caso – Pagos)
Si da negativo → 0
b) Global
plain
Rva Global = 1% × Promedio masa salarial últimos 6 meses
Reserva PE Total
plain
Rva PE = Máx { Caso a caso ; Global }
4. ILT (Incapacidad Laboral Temporaria)
a) Caso a caso
Base: Siniestros denunciados últimos 24 meses antes del cierre.
Casos con extensión de ILT cuya prestación dineraria está pendiente (total o parcial).
A1: Con fecha real de alta médica
plain
Rva(A1) = [Días caídos reales a/c ART / (fecha alta – F1º manif. inv. – 10)] × Remuneración ajustada – Pagos
Si negativo → 0
A2: Sin alta médica
plain
Rva(A2) = [(fecha valuación – F1º manif. inv. – 10) × Rem. ajustada] + [(DC estimados – DC reales) × R] – Pagos
La segunda parte no puede dar negativo. Si negativo total → 0.
b) Global
plain
Rva Global = 1% × Promedio masa salarial últimos 6 meses
Reserva ILT Total
plain
Rva ILT = Máx { A1 + A2 ; Global }
5. SPL (Siniestros con Prestaciones Laborales) – Casos D y E
Fórmulas Biométricas Base
Hojas
Símbolo	Fórmula	Significado
ₙqₓ	[l(x) – l(x+n)] / l(x)	Prob. de muerte entre x y x+n
ₙEₓ	D(x+n) / D(x)	Factor de descuento actuarial
ₙAₓ	[M(x) – M(x+n)] / D(x)	Seguro de vida temporal
ₙaₓ	[N(x) – N(x+n)] / D(x)	Renta temporal
Parámetros comunes:
Q = 88% (factor de ajuste)
p (Leve) = 16% GAM 1971 (Caso D) / 12% GAM 1971 (Caso E)
p (Grave) = 56% GAM 1971 (Caso D) / 57% GAM 1971 (Caso E)
Tabla de mortalidad: MI 1985
📌 CASO D: Siniestros del 26/10/2012 al 04/03/2017
Hojas
Contingencia	Fórmula de Reserva
Muerte	Vᵐ init(T) = Máx{IBM × 65/x × 53 ; M₁} + M₄ – Pagos
Vᵐ in situ/EP = 1,2 × Vᵐ init(T) – Pagos
Leve	ILPPD(T) = Máx{53 × IBM × 65/x × p ; M₁ × p}
Rva init = Q × [(1 – q(x;0;1)) × ILPPD + q(x;0;1) × Vᵐ init] – Pagos
V in situ/EP = Q × [(1 – q(x;0;1)) × ILPPD × 1,2 + q(x;0;1) × Vᵐ in situ/EP] – Pagos
Grave	ILPPD(T) = Máx{53 × IBM × 65/x × p ; M₁ × p}
V init = Q × [E(x+r, x+z) × (M₂ + ILPPD) + q(x+r, x+r, x+z) × Vᵐ init] – Pagos
V in situ/EP = Q × [E(x+r, x+z) × (M₂ + ILPPD) × 1,2 + q(...) × Vᵐ in situ/EP] – Pagos
Total	ILPTD = Máx{53 × IBM × 65/x ; M₁}
V total init = Q × [E(x+r, x+z) × (M₃ + ILPTD) + q(...) × Vᵐ init] – Pagos
V total in situ/EP = Q × [E(x+r, x+z) × (M₃ + ILPTD) × 1,2 + q(...) × Vᵐ in situ/EP total] – Pagos
Gran Invalidez	V GI init = V total init + 2.000 × (ISIPAₜ / ISIPAₙₒᵥ₀₉) × 12 × a(x+r+t, x+z+t, w, 12) – Pagos
V GI in situ/EP = V total in situ/EP + 2.000 × (ISIPAₜ / ISIPAₙₒᵥ₀₉) × 12 × a(...) – Pagos
r = años transcurridos desde 1ª manifestación hasta fecha de valuación o fin ILT (r = 0; 1)
z = r + 1 (z = 1; 2). Si fecha fin ILT es incierta: z=1 si no superó la anualidad, z=2 si superó.
t = años transcurridos desde inicio de ILP provisoria hasta fecha de valuación.
📌 CASO E: Siniestros desde 05/03/2017 en adelante
Hojas
Contingencia	Fórmula de Reserva
Muerte	Vᵐ init = Máx{IBM_ley27348 × 65/x × 53 ; M₁} + M₄ – Pagos
Vᵐ in situ/EP = Vᵐ init × 1,2 – Pagos
Leve	ILPPD = Máx{IBM_ley27348 × p × 53 × 65/x ; M₁ × p} ; p = 12%
V init = Q × [E(x+r, x+z) × ILPPD + A(x+r, x+r, x+z) × Vᵐ init] – Pagos
V in situ/EP = Q × [E(x+r, x+z) × ILPPD × 1,2 + A(...) × Vᵐ in situ/EP] – Pagos
Grave	ILPPD = Máx{IBM_ley27348 × p × 53 × 65/x ; M₁ × p} ; p = 57%
V init = Q × [E(x+r, x+z) × (M₂ + ILPPD) + A(...) × Vᵐ init] – Pagos
V in situ/EP = Q × [E(x+r, x+z) × (M₂ + ILPPD) × 1,2 + A(...) × Vᵐ in situ/EP] – Pagos
Total	ILPTD = Máx{IBM_ley27348 × 53 × 65/x ; M₁}
V total init = Q × [E(x+r, x+z) × (M₃ + ILPTD) + A(...) × Vᵐ init] – Pagos
V total in situ/EP = Q × [E(x+r, x+z) × (M₃ + ILPTD) × 1,2 + A(...) × Vᵐ in situ/EP total] – Pagos
Gran Invalidez	V GI init = V total init + 2.000 × (ISIPAₜ / ISIPAₙₒᵥ₀₉) × 12 × a(x+r+t, x+z+t, w, 12) – Pagos
V GI in situ/EP = V total in situ/EP + 2.000 × (ISIPAₜ / ISIPAₙₒᵥ₀₉) × 12 × a(...) – Pagos
Diferencia clave Caso E vs D: Usa IBM_ley27348, porcentajes de p distintos (12% leve, 57% grave), y reemplaza q por A (seguro de vida) en las fórmulas de Leve, Grave y Total.
6. Juicios
Hojas
Tipo	Reserva
Con sentencia (definitiva o 1ª instancia)	Rva = [Monto sentencia + Gastos/Honorarios (30% sentencia) – Pagos] actualizado por tasa pasiva
Sin sentencia (demandas)	Rva = [Importe que se hubiera visto obligada a pagar la ART + 30% gastos/honorarios – Pagos] actualizado por tasa pasiva
Mediación	Promedio valor de mediación últimos 12 meses
Reserva Total Juicios	Rva Juicio = Máx{Pasivo Global ; A + B} + C
Siempre: si da negativo → 0
🎯 CHECKLIST PARA RESOLVER EJERCICIOS
Identificar la fecha del siniestro → ¿Caso D o Caso E?
Clasificar la contingencia → Leve, Grave, Total, GI, Muerte
Verificar si es In Situ o EP → Si sí, aplicar factor 1,20 donde corresponda
Calcular IBM / IBD con RIPTE si es necesario
Determinar edad x a la 1ª manifestación invalidante
Aplicar Máx{} entre fórmula actuarial y monto fijo (M₁, M₂, M₃, M₄)
Reservas: ¿SLAP? ¿IBNR? ¿PE (caso a caso vs global)? ¿ILT (A1, A2 vs global)? ¿SPL? ¿Juicios?
Verificar siempre: Si la reserva da negativa → 0""",
    },
"3": {
        "nombre": "Resuelve teniendo en cuenta la siguiente teoria para el razonamiento y procedimiento",
        "ejemplo": 
            """ Resumen Tarificación — Fórmulas y Razonamiento para el Parcial

## UNIDAD 6: TARIFICACIÓN (RATEMAKING)

### Idea central
**Precio = Costo + Beneficio**
**Prima = Siniestros + LAE + Gastos de Suscripción + Ganancia + Margen de Seguridad**

Objetivos esenciales: cubrir siniestros y gastos esperados, prever contingencias, promover control de siniestralidad (bonus-malus), satisfacer al regulador (tarifas adecuadas, no excesivas, no discriminatorias).

---

### Fórmulas "madre"

**Prima Pura:**
PP = Frecuencia × Intensidad

**Prima de Tarifa:**
PT = [PP × (1+LAE) + Gastos Fijos] / [1 − %GV − %MgUt − %MgSeg]

**Tasa de Seguro** (cuando piden variación de tasa, NO prima):
Tasa = [%Siniestralidad con ALAE × (1+%ULAE) + %GF] / [1 − %GV − %MgUt − %MgSeg]

ΔTasa = Tasa − 1

%Siniestralidad = Siniestros Ultimate con Tendencia / Prima Ganada on level con Tendencia

**Regla clave para elegir fórmula:**
- Si piden TASA o VARIACIÓN DE TASA → usás % Siniestralidad (ratio).
- Si piden PRIMA o VALOR $ → usás Prima Pura y la fórmula de Prima de Tarifa, y para gastos fijos se usa el método basado en exposición (nunca el de razón siniestral para esto).

---

### 1. PRIMA — Camino: Histórica → On Level → On Level con Tendencia

#### A) PRIMA ON LEVEL (llevar a tasas actuales)

**a) Método de Prolongación de la Exposición** (exacto pero costoso)
Prima histórica = (Suma asegurada × factores + GF) × N° expuestos
Prima on level = Prima histórica × (1+Tasa)
Prima on level total = Prima on level × Expuestos ganados

**b) Método del Paralelogramo** (rápido, promedio ponderado — pierde exactitud)

Pasos:
1. Calcular índices acumulados (cada cambio multiplica al anterior).
2. Dibujar el cuadrado del año (CY) y trazar líneas según el tipo de cambio:
   - Diagonal → cambio por motivos de suscripción (afecta pólizas nuevas progresivamente).
   - Vertical → cambio por ley/normativa (afecta TODAS las pólizas vigentes desde esa fecha).
3. Calcular superficies (ponderadores). El CY completo = 1 (área total del cuadrado).
   - Triángulo = (base × altura) / 2
   - Paralelogramo = base × altura
   - Trapezoide = ½ × (base1+base2) × altura
   - La última superficie sale por diferencia: 1 − (resto de superficies)
4. Asignar a cada superficie el índice acumulado vigente en ese tramo.
5. Aplicar:

Factor on level = Último Índice Acumulado / Σ(Superficie_i × Índice_i)

Prima on level = Prima histórica × Factor on level

**Tip:** el numerador (último factor) NO cambia con el año analizado; el denominador SÍ.
Base = vigencia de la póliza durante ese año (tiempo dentro del CY). Altura = % de prima ganada en ese año.

---

#### B) PRIMA ON LEVEL CON TENDENCIA

Prima on level con tendencia = Prima on level × (1+Tendencia)^n

"n" = tiempo entre fecha promedio del período histórico y fecha promedio del período proyectado.

**a) Método a UN PASO**
Depende de 3 cosas: prima ganada vs emitida, año calendario vs suscripción, vigencia de póliza.

- Prima GANADA (histórico): me proyecto hacia atrás el plazo completo de la póliza (caso extremo: póliza que se emitió justo antes y empieza a ganar 1 día en el período). Promedio entre el extremo hacia atrás y el fin del período.
- Prima EMITIDA (histórico): NO me corro hacia atrás, promedio directo del período indicado.
- Período proyectado: SIEMPRE el promedio del período donde regirá la nueva tasa.

Ejemplos (pólizas, CY2011 → CY2013):
- Prima ganada, anual → n = 2,5 años
- Prima ganada, semestral → n = 2,25 años
- Prima emitida, anual → n = 2 años

**b) Método a DOS PASOS** (el más usado — cuando la tendencia cambia en el tiempo)

Paso I — Factor de tendencia actual de prima (trae la prima histórica a "hoy"):
Factor tendencia actual = Última prima emitida promedio on level / Prima ganada promedio on level

- Numerador debe ser promedio (si no, dividir por expuestos).
- Si el numerador es prima histórica (no on level), aplicar paralelogramo primero.

Paso II — Proyectar desde "hoy" al futuro:
Factor tendencia total = Factor tendencia actual × (1+Tendencia)^n

- "n" va desde la fecha promedio del último trimestre usado en el Paso I hasta la fecha promedio del período proyectado.

---

### 2. SINIESTROS

Objetivo: estimar el costo final de siniestros para el período en que regirán las nuevas tasas.

Pasos:
1. Ultimate (IBNR / factores de desarrollo) — sobre siniestros abiertos/inmaduros.
2. Sacar siniestros extraordinarios/catastróficos y tratarlos aparte (provisión de largo plazo).
3. Calcular "n" = desde fecha promedio de accidente del período histórico (AY) hasta fecha promedio de accidente del próximo período efectivo (pensando el escenario más extremo: póliza suscripta el último día de vigencia de la nueva tasa).
4. Aplicar tendencia:

Siniestros Ultimate con Tendencia = Ultimate × (1+Tendencia)^n

Tendencia siniestral = Frecuencia × Intensidad (si no es dato).

---

### 3. GASTOS DE SINIESTROS (LAE)

- ALAE (asignados): atribuibles a un siniestro específico (ej: honorarios legales).
- ULAE (no asignados): no atribuibles a un siniestro puntual (ej: sueldos del depto. de siniestros).

%ULAE = ULAE / (Siniestros pagados + ALAE)

- Sacar atípicos/catastróficos del promedio histórico, usar el % promedio "limpio".
- Aplicar el % a (Siniestros pagados + ALAE) proyectados.

**Con recupero/salvataje (Paso II bis):**
ratio de recupero = recupero / pagados
ratio con ultimate = ratio de recupero × FDA

Siniestro Neto Ultimate con Tendencia = (ratio con ultimate × siniestro con tendencia) combinado con el siniestro con tendencia → es el numerador del % siniestralidad.

---

### 4. GASTOS DE SUSCRIPCIÓN

Tipos de gasto y base de cálculo:
- Comisión y Brokerage → Prima Emitida
- Gastos de Adquisición → Prima Emitida
- Impuestos → Prima Emitida
- Gastos Generales → Prima Ganada

- Gastos Fijos: igual importe sin importar el tamaño de la prima.
- Gastos Variables: varían directamente con la prima.

**a) Método de Gastos Variables** (supone que TODO es variable)
%GV = Monto de Gastos / Prima Emitida → promedio
Crítica: asume que no hay gastos fijos (irreal).

**b) Método basado en la Prima** (reconoce fijos y variables)
Ratio de Gastos = Monto de Gastos / Prima Emitida → promedio
Ratio Gs Fijos = Ratio de Gastos × %Gastos Fijos
Ratio Gs Variables = Ratio de Gastos × %Gastos Variables
Crítica: asume que la composición fijo/variable y la prima promedio se mantienen igual en el futuro; problema si hay diferencias regionales.

**c) Método basado en la Exposición** (usar cuando piden PRIMA / valor $, no tasa)
Monto Gs Fijos = Monto de Gastos × %Gastos Fijos
Gs Fijo por expuesto = Monto Gs Fijos / Expuestos Ganados → promedio
Gastos Variables = Monto de Gastos − Monto Gs Fijos
%Gs Variables = Gastos Variables / Prima Emitida → promedio

**Regla:** si el ejercicio pide TASA o ΔTASA → métodos a) o b).
Si pide PRIMA (valor $) → método c) (gastos fijos $ por expuesto van directo a la fórmula de Prima de Tarifa).

---

### 5. MARGEN DE UTILIDAD (MgUt)

Total Utilidad = Ingresos por Inversión + Utilidad por Suscripción
Utilidad Suscripción = Prima − Siniestros − LAE − Otros Gastos

Ingresos por inversión: (1) inversión de capital propio, (2) "float" entre cobro de prima y pago de siniestros (mayor en negocios de cola larga).

---

### 6. MARGEN DE SEGURIDAD (MgSeg)

Recargo por la incertidumbre de trabajar con estimaciones. A mayor cantidad/calidad de información histórica → menor margen.

---

## UNIDAD 7: TARIFICACIÓN CON SEGMENTACIÓN

### Idea central
Se segmenta cuando el comportamiento siniestral no es homogéneo dentro de un mismo ramo. Cada segmento debe ser homogéneo internamente y heterogéneo respecto a otros.

Metodología:
1. Tomar el ramo.
2. Definir criterio de segmentación.
3. Dividir en subgrupos.
4. Tarifar el subgrupo BASE (mayor cantidad de expuestos = mayor credibilidad).
5. Calcular relatividades del resto de subgrupos respecto a la base.

**Razonamiento del ejemplo "Compañía A vs B" (no segmentar):**
La compañía que NO segmenta cobra una tarifa promedio a todos. En la renovación, los riesgos buenos (L) se van a la compañía que sí segmenta (porque ahí pagan menos), y los riesgos malos (H) llegan a la que no segmenta (porque ahí pagan menos que su costo real). Resultado: la compañía sin segmentación termina con déficit (antiselección / selección adversa), mientras la que segmenta queda en equilibrio (déficit/superávit = 0 siempre).

---

### Criterios de Segmentación
1. Estadísticos: costo esperado distinto entre grupos, homogéneo dentro del grupo, muestra grande y estable.
2. Operativos: objetivo (no ambiguo), bajo costo de implementación, verificable (no manipulable).
3. Sociales: asequible (info accesible), causal (que explique el riesgo, sin dañar imagen — ej. sexo), controlable, cuidado con datos privados.
4. Legales: no puede violar la normativa vigente.

---

### Relatividades

**a) Método de Razón Siniestral** (cuando la tarifa se calcula como TASA, dato principal = % Siniestralidad / Loss Ratio):
Relatividad indicada_i = Relatividad existente_i × (Loss Ratio_i / Loss Ratio_base)

**b) Método de Costo Siniestral** (cuando la tarifa se calcula como PRIMA, dato principal = monto esperado de siniestros):
Relatividad indicada_i = Relatividad existente_i × (Costo siniestral_i / Costo siniestral_base)
Costo Siniestral = Prima Pura × Expuestos

El grupo BASE se tarifa con sus propios datos (como si no hubiese segmentación). El resto = tarifa base × relatividad indicada del subgrupo.

---

### Factor Off-Balance / Factor de Compensación

Cuando se ajustan primas por restricciones técnicas/comerciales (ej: tope de precio en un ramo), puede generarse un desbalance entre lo recaudado y lo necesario.

FoB = Σ(Uer_i × Nueva Relatividad_i) / Σ(Uer_i × Relatividad Actual_i)

Factor de Compensación = 1/FoB = Relatividad Actual / Nueva Relatividad

donde Uer = Unidades expuestas a riesgo.

**Razonamiento práctico (ejemplo auto/camión):**
1. Calcular recaudación técnica necesaria = Σ (precio técnico × expuestos).
2. Si por motivos comerciales se topea un ramo (ej: camión a $130 en vez de $140), plantear la ecuación:
   Recaudación necesaria = (precio topeado × exp_topeado) + (x × exp_otro)
3. Despejar x → ese es el nuevo precio del otro ramo.
4. El % de incremento sobre el precio técnico original de ese ramo = factor de compensación.
(Solo es posible si hay margen suficiente en el ramo "compensador"; si no, queda déficit.)

---

## CHECKLIST RÁPIDO PARA RESOLVER UN EJERCICIO

1. ¿Piden TASA/ΔTASA o PRIMA ($)? → define qué fórmula madre y qué método de gastos usar.
2. Prima: histórica → ¿on level? (paralelogramo: dibujar cuadro, índices acumulados, superficies, factor on level) → ¿con tendencia? (definir "n": ganada vs emitida, 1 paso vs 2 pasos).
3. Siniestros: ultimate (IBNR) → sacar catastróficos → tendencia con "n" (AY histórico → fecha promedio del próximo período efectivo).
4. Gastos: clasificar fijos/variables, elegir método según se pida tasa o prima.
5. Armar % Siniestralidad o Prima de Tarifa con todos los componentes.
6. Si hay segmentación: definir base, calcular relatividades (razón siniestral o costo siniestral según corresponda), verificar si hace falta factor off-balance/compensación.
""",
    },
    "4": {
        "nombre": "Teorico",
        "ejemplo": """a continuacion te paso el teorico que vimos en clase: 1. Por que los GLM son utiles en Predictive Analytics?

Los GLM permiten construir tarifas segmentadas segun las caracteristicas del asegurado o del riesgo a suscribir. Sus principales ventajas son:

Resultados faciles de presentar y explicar (son fundamentales para 'vender' un proyecto de tarifas basadas en scoring frente a la gerencia comercial).
Son modelos multiplicativos: la frecuencia o el costo medio se obtienen multiplicando un valor base por una serie de factores (relatividades), lo cual es sencillo de entender y comunicar.
Aprovechan toda la informacion de la base, permitiendo estimar valores incluso para combinaciones con muestra muy pequena o nula (gracias a que el modelo 'rellena' esas combinaciones usando la informacion del resto de las variables).
Utilizan una cantidad reducida de parametros comparado con tablas de tarifas tradicionales con miles de celdas.

Aplicaciones en seguros de personas: Accidentes Personales, Asistencia al Viajero, Accidentes de Trabajo, Seguros de Salud (no solo riesgos patrimoniales/automotores).

2. Supuestos y componentes de los GLM

Los Modelos Lineales Clasicos (MLC) (regresion lineal tradicional) requieren tres supuestos restrictivos:

Normalidad de la variable respuesta.
Varianza constante (homocedasticidad).
Aditividad de los efectos.

Los GLM generalizan al MLC removiendo estos supuestos:

La variable respuesta puede pertenecer a cualquier distribucion de la familia exponencial (Normal, Poisson, Gamma, Binomial, Tweedie, etc.), no solo a la Normal.
La varianza NO es constante: cambia segun la media (relacion media-varianza especifica de cada distribucion).
Se mantiene un predictor lineal (combinacion lineal de las variables explicativas y sus coeficientes Beta), pero este se conecta con la media de la variable respuesta a traves de una funcion de enlace (link function), lo que permite relaciones no aditivas (por ejemplo, multiplicativas si el enlace es logaritmico).

Componentes de un GLM

Componente aleatorio: distribucion de la familia exponencial de la variable respuesta (Y).
Componente sistematico (predictor lineal): combinacion lineal de las variables explicativas (X*Beta).
Funcion de enlace (link function): relaciona la media esperada de Y con el predictor lineal.

3. Output tipico de un GLM - Conceptos clave

Beta (b): coeficiente estimado para cada nivel de cada variable. Indica el efecto de esa categoria sobre el predictor lineal.
Exp(B) o 'Relatividad' (e^b): es el factor multiplicativo que se aplica sobre la base. Es la forma 'traducida' del Beta a un lenguaje comercial/tarifario.

Ejemplo: si para '40 anos' el Exp(B) = 0.819, significa que a los 40 anos se es 18.1pct menos riesgoso que la categoria base (21 anos).
Ejemplo: Buenos Aires con Exp(B)=1.221 implica ser 22.1pct mas riesgosa que Santa Fe (categoria base).
Universitario (Exp(B)=0.756) implica 24.4pct menos riesgo que Secundario (base).

Categoria Base (nivel de referencia): la categoria de cada variable que tiene Beta = 0 y por lo tanto Exp(B) = 1. Todas las demas categorias se comparan (relativizan) contra ella.
Error Estandar: mide la precision de la estimacion del Beta.
Chi-cuadrado de Wald y Significatividad (Sig.): prueban si el coeficiente Beta es estadisticamente distinto de 0 (es decir, si la categoria es significativamente diferente de la base). Si Sig. > 0.05 (umbral habitual), la categoria no es significativamente distinta de la base.
Expuestos y Siniestros: tamano de la muestra detras de cada categoria (relevante para evaluar la confiabilidad de la estimacion).
Escala: parametro de dispersion del modelo (relevante en modelos Gamma/Tweedie).

Como se calcula una estimacion (cotizacion)

La frecuencia o costo medio estimado se obtiene multiplicando:

Valor Base (Exp del Intercepto) * Exp(B) de cada variable relevante para ese riesgo

Ejemplo del webinar: para un Camion, Zona 2, fabricacion Nacional, 7 anos de antiguedad, conductor de 41 anos -> se multiplican las relatividades correspondientes de cada variable y se obtiene la frecuencia estimada (2.0696pct).

4. Modelos GLM tipicos en la actividad aseguradora

4.1 Poisson - Frecuencia de siniestros

Modelo multiplicativo estandar para modelar cantidad de siniestros / frecuencias.
Propiedad clave: es invariante respecto a la unidad de tiempo. Medir frecuencias mensuales o anuales no cambia el resultado relativo del modelo (es decir, da el mismo resultado proporcional).

4.2 Gamma - Costo Medio (severidad)

Modelo multiplicativo estandar para modelar intensidad o costo medio de los siniestros.
Su forma general la hace apropiada para modelar montos de siniestros.
Propiedad clave: es invariante respecto de la unidad monetaria. Trabajar en pesos o en miles de pesos no afecta el resultado final del calculo (relatividades).

4.3 Logit / Logistico - Retencion de carteras

Modelo tipico para analizar retencion de clientes (variable respuesta binaria: renovo / no renovo).
Usa una funcion de enlace Logit con termino de error de distribucion Binomial.
La transformacion Logit da resultados acotados entre 0 y 1 (probabilidades), independientemente de la magnitud de las variables explicativas.
Importante: en este modelo, el Exp(B) no tiene el significado habitual de 'relatividad' multiplicativa simple como en Poisson/Gamma - es un odds ratio (razon de probabilidades).

4.4 Tweedie - Prima Pura

Distribucion tipica para modelar directamente la Prima Pura (PP = Frecuencia * Costo Medio).
Caracteristicas de la distribucion Tweedie:

Masa de probabilidad en cero (polizas sin siniestros).
Rango continuo de valores positivos (polizas con siniestros).

Permite modelar en un solo paso lo que normalmente requeriria dos modelos separados (Frecuencia y Severidad).

5. Construccion de Modelos GLM

5.1 Elementos a tener en cuenta

Volumen de datos: hay que equilibrar la experiencia historica/tamano de la base, la frecuencia siniestral del riesgo, y el grado de segmentacion deseado.
Es habitual combinar informacion de varios anos y agrupar localidades para dar estabilidad al modelo, asumiendo consistencia en ese agrupamiento.
Definicion de variables explicativas y sus niveles base.
Interacciones: analizar potenciales relaciones entre variables predictoras mediante analisis bivariados previos.
Correlaciones (Near Aliasing): estudiar si existen correlaciones entre los expuestos de distintas variables.
Coberturas: las variables predictoras no siempre explican igual la variable respuesta en distintas coberturas (se suele modelar por cobertura).

5.2 Analisis previo de las bases

Detectar registros con valores ilogicos, negativos, faltantes o nulos en bases de exposicion y/o siniestros.
Controlar el cruce de bases (siniestros sin su correspondiente grupo de expuestos).
Definir el tratamiento de siniestros en cero y de valores extraordinarios (outliers).
Realizar analisis univariados y bivariados previos a correr el GLM.

5.3 Near Aliasing (cuasi-colinealidad)

Ocurre cuando ciertas combinaciones de categorias de dos o mas variables estan correlacionadas (muy pocos o muchos casos en combinaciones especificas), generando relatividades distorsivas para esas combinaciones particulares.
Ejemplo del webinar: si la frecuencia de 'Camion, Zona 1' se estima multiplicando relatividades obtenidas de forma independiente (10pct base * relatividad de Camion * relatividad de Zona 1), se puede llegar a un resultado claramente erroneo (ej. 4.72pct o 27.78pct) porque esa combinacion especifica no esta bien representada en la muestra usada para estimar cada relatividad por separado.
Conclusion: hay que detectar estas combinaciones 'alias' y tratarlas especialmente (no confiar ciegamente en el producto de relatividades marginales).

6. Eleccion inicial de variables y validacion posterior

La eleccion inicial esta limitada por la disponibilidad y calidad de los datos.
Se debe usar la logica del riesgo y considerar la factibilidad legal y comercial.
Es necesario consensuar con otras areas de la compania la propuesta de variables.

Proceso de validacion tecnica

Metodos de seleccion: Forward, Backward y Stepwise.
Validar el poder explicativo de las variables.
Diferenciacion entre categorias: verificar que existan diferencias reales entre los niveles de cada variable.

Criterios para decidir si el efecto de una variable es 'sistematico'

Pruebas de bondad de ajuste con y sin la variable (comparacion de modelos).
Nivel de significatividad de las variables:

Tipo I: apropiado cuando hay un orden a priori para introducir los predictores.
Tipo III: de aplicacion mas general (no depende del orden de entrada).

Consistencia en el tiempo de las relatividades.
Sentido comun (validacion de negocio).

7. Manejo de Variables Multinivel

Problema: variables con muchas categorias suelen tener categorias no significativas (sin evidencia estadistica de diferencia respecto a la base) o con valores distorsivos (poca muestra).

Alternativas de tratamiento (sin modelo jerarquico)

Agrupamiento: unir categorias similares en una sola.
Suavizado: tecnicas de smoothing para moderar valores extremos.
Eliminacion: quitar la categoria o no usar la variable.

A veces es recomendable usar modelos jerarquicos (otras veces no).

Agrupamiento entre categorias significativas - Test del Coeficiente de Variacion

Se utiliza un test informal basado en el Coeficiente de Variacion (CV) para decidir si conviene agrupar categorias que, aunque significativas individualmente, presentan relatividades cercanas entre si.
El CV es una medida de dispersion relativa que ayuda a determinar si las diferencias entre categorias son lo suficientemente grandes como para justificar mantenerlas separadas.

8. Utilizacion de Interacciones

Una interaccion ocurre cuando el efecto de una variable cambia segun el nivel/categoria de otra variable.
Ejemplo del webinar: en general los hombres son 10pct mas riesgosos que las mujeres, pero en el rango de edad 50-55 anos esa diferencia se reduce a solo 3pct.

Tipos de especificacion

Interaccion marginal: A + B + A*B (se mantienen los efectos principales mas el termino de interaccion).
Interaccion completa: A*B (solo el termino combinado).
Ambas especificaciones llevan a las mismas estimaciones finales, pero difieren los tests estadisticos y la cantidad de parametros del modelo.

Cuando usar interacciones

Tienen mas sentido practico entre variables con pocas categorias.
Conviene buscar interacciones puntuales (los efectos mas fuertes) en lugar de evaluar todas las combinaciones posibles de variables multinivel.
Usarlas cuando existan interacciones reales y el contexto comercial permita aplicarlas.
Interacciones con la variable 'tiempo' son utiles para detectar efectos distorsivos pasados producidos por una suscripcion particular (cambios de politica de suscripcion en el tiempo).

9. Analisis de la variable 'Tiempo', IBNR e IBNER

Analisis general de la variable periodo

Al analizar la variable periodo pueden aparecer comportamientos crecientes, decrecientes u oscilantes.
Hay que evaluar si esto es coherente con otros analisis disponibles.
Se debe elegir un periodo especifico como referencia para la correccion del intercepto (es decir, a que nivel de tarifa 'anclar' el modelo).
El ultimo periodo suele tener un comportamiento atipico (no sigue la tendencia, por estar incompleto).
Es fundamental incluir la proyeccion a futuro de la tendencia en la tarifa final.

IBNR e IBNER

IBNR (Incurred But Not Reported) e IBNER (Incurred But Not Enough Reported): siniestros ocurridos pero no reportados (o no completamente desarrollados/valuados) a la fecha de corte.
Para evitar su efecto distorsivo, una opcion es 'retirarse en el tiempo' (no usar los periodos mas recientes), pero esto:

Reduce la muestra disponible.
Hace perder la posibilidad de observar comportamientos recientes.

Trabajar solo con casos cerrados tambien es un error: distorsiona tanto las frecuencias como los costos medios, y no compensa correctamente el IBNR/IBNER.
Solucion recomendada: incluir en la variable de compensacion (offset) el factor de desarrollo correspondiente a cada periodo, de modo de 'corregir' la inmadurez de los datos recientes sin descartarlos.

Comparacion: variable 'tiempo' sin vs. con factores de desarrollo en el offset

Sin factores de desarrollo: las relatividades de los periodos mas recientes muestran una tendencia ascendente artificial (por la inmadurez/IBNR de esos periodos).
Con factores de desarrollo incluidos en el offset: la tendencia temporal se corrige, mostrando el comportamiento 'real' de la siniestralidad a traves del tiempo.
Punto clave: al corregir la variable tiempo mediante el offset, las relatividades de las demas variables permanecen practicamente iguales - el ajuste del offset aisla y corrige especificamente el efecto de desarrollo/IBNR sin distorsionar el resto del modelo.

10. Analisis de relatividades a traves del tiempo

Es recomendable hacer analisis temporales de cada variable para detectar cambios de comportamiento y evitar que un promedio historico distorsione la tarifa.
Estos analisis pueden ser:

Univariados (analisis simple de la evolucion de cada categoria en el tiempo), o
GLMs segmentados corriendo el modelo en sub-periodos mas cortos.

El objetivo es evitar que las curvas/relatividades anuales 'absorban' cambios que en realidad corresponden a otras variables (confusion de efectos).
Relatividades consistentes a traves del tiempo: indican que la variable tiene un efecto estable y confiable -> se puede usar tal cual.
Relatividades NO consistentes a traves del tiempo: indican inestabilidad -> requieren mayor analisis, posible suavizado, o revision de la inclusion de la variable.

11. Modelos de Costo Medio: UM vs. Porcentaje de la Suma Asegurada (S.A.)

Los costos medios pueden modelarse de dos formas:

En Unidades Monetarias (U.M.): la Prima Pura en U.M. se obtiene multiplicando el CM (en UM) por la Frecuencia.
Como porcentaje de la S.A.: la Prima Pura (en pct de S.A.) se obtiene multiplicando el CM (en pct) por la Frecuencia.
Practica habitual: calcular la PP en U.M. y luego convertirla a porcentaje de una S.A. promedio.

Ventajas/desventajas de modelar en UM

Adecuado si el CM es estable en UM dentro de cada rango de S.A.
En contextos inflacionarios, requiere actualizacion permanente.
La S.A. (o gama del vehiculo) adquiere mucha mayor relevancia como variable explicativa.
Las relatividades del GLM no se actualizan con la frecuencia deseable (problema de mercado).
Mayores inconvenientes al proyectar el costo medio a futuro.

Ventajas/desventajas de modelar como pct de la S.A.

Adecuado si el CM es estable en porcentaje dentro de cada rango de S.A.
Mejor estrategia frente a la inflacion.
Las relatividades igual deben revisarse periodicamente.
Problema: las sumas aseguradas no siempre estan bien disponibles (infraseguro, actualizaciones poco frecuentes, clausulas de ajuste automatico, seguros a valor de reposicion sin S.A. explicita).
Menor riesgo al proyectar el costo medio a futuro.

Aspectos a considerar antes de decidir

Dentro de cada rango de S.A., los siniestros son mas estables como pct de la S.A. o como monto en UM?
Agilidad de la aseguradora para actualizar valores.
Calidad de los datos de Suma Asegurada (fijada por el asegurado, implicita, sin ajustes, etc.).
Niveles de inflacion y estabilidad del tipo de cambio.
Existencia de indices propios de costos (mano de obra/honorarios medicos, repuestos/medicamentos, tipo de cambio) que pueden evolucionar distinto del indice general.

Antiseleccion

Riesgo de antiseleccion: si se modela en UM cuando en realidad el siniestro se comporta como un porcentaje constante de la S.A., o viceversa (modelar en pct cuando el siniestro es constante en UM), se generan errores de tarifa que el asegurado/mercado puede explotar (eligiendo sumas aseguradas que minimicen su costo relativo), generando antiseleccion.

12. Tarificacion de productos con franquicias (deducibles)

Contexto general

En algunos mercados las coberturas de Todo Riesgo sin franquicia son habituales -> se puede adaptar esa base para construir tarifas con distintas franquicias, homogeneizando monedas o trabajando con porcentajes sobre la S.A. o limite de indemnizacion.
En otros mercados, las coberturas sin franquicia tienen baja participacion -> los danos parciales se ofrecen mayormente con franquicia, con:

Variedad de franquicias (distintos valores).
Pocos expuestos y siniestros por cada nivel de franquicia.
Distorsion inflacionaria en franquicias fijas en UM.
Necesidad de homogeneizar la informacion entre las distintas franquicias para aprovecharla al maximo.

Pasos tipicos en un GLM con franquicias

Utilizar solo informacion de coberturas con menores franquicias al modelar frecuencia/costo medio (para no perder informacion por exclusion de siniestros menores).
Desindexar las franquicias (en UM) a valores comercializables y unificar la informacion a moneda del momento del analisis.
Alternativamente, utilizar valores porcentuales respecto de las S.A.
Correr los GLM y analizar la logica de las variables.
Importante: las relatividades NO se mantienen iguales entre las distintas franquicias (cada nivel de franquicia tiene su propia estructura de relatividades).

Distribucion de siniestros TRSF (Todo Riesgo Sin Franquicia)

Al introducir una franquicia, ciertos siniestros (los de monto menor a la franquicia) se eliminan, lo que:

Reduce la frecuencia (menos siniestros indemnizables).
Modifica (recalcula) el Costo Medio del siniestro (se recalcula descontando el tramo cubierto por la franquicia).

Franquicias en UM vs. en pct de la S.A.

Franquicias en UM: obligan a que la S.A. y/o gama del vehiculo sean muy relevantes como variables de segmentacion. Con el paso del tiempo, las franquicias fijas pierden poder adquisitivo; si no se ajustan, las frecuencias y costos medios reales seran mayores a los modelados.
Franquicia como pct de la S.A.: con el tiempo tambien puede distorsionarse (requiere analisis periodicos). Requiere buena calidad de datos de S.A.; si hay infraseguro, se distorsionan los resultados.

Comparacion de resultados finales

Buscar coherencia tecnica y comercial entre las distintas franquicias.
Decidir si conviene fijar valores minimos y maximos segun politica de la aseguradora y los valores extremos que arrojen los distintos GLMs.
Al comparar relatividades entre franquicias por zona/categoria, se busca verificar si la logica se repite consistentemente; si una relatividad 'baja' de forma inesperada en alguna franquicia, hay que entender por que (podria ser muestra pequena -> considerar unificar comportamiento).

13. Variables de Respuesta Binaria - Regresion Logistica (Distribucion Logistica)

Para retencion de clientes (variable: Renovo / No Renovo), el modelo tipico usa funcion de enlace Logit con error Binomial -> modelo logistico.
La funcion Logit transforma cualquier valor del predictor lineal a un resultado entre 0 y 1 (probabilidad), independientemente de la magnitud de las variables explicativas.

Otras funciones de enlace para respuesta binaria

Probit: tambien simetrica como la Logit, pero converge mas rapido a 0 y a 1 (colas mas 'cortas').
Log-log: asimetrica.

Interpretacion del output

En regresion logistica, Exp(B) es un odds ratio, por lo que no tiene el significado habitual de 'relatividad' multiplicativa de Poisson/Gamma sobre una frecuencia o costo medio - se interpreta como la razon de probabilidades (odds) de un evento entre una categoria y la base.
Para obtener la probabilidad estimada de un caso particular (ej. probabilidad de renovacion), se combinan los Betas relevantes a traves de la funcion logistica (transformacion inversa del Logit), no mediante simple multiplicacion de relatividades. En el ejemplo del webinar, la probabilidad estimada de renovacion para un caso particular fue 83.14pct.

14. Restricciones sobre la tarifa teorica y uso del Offset

Concepto de Offset

El offset es un termino que se incluye en el modelo con coeficiente fijo (no estimado), funcionando como un ajuste conocido a priori sobre el predictor lineal - permite 'forzar' o compensar efectos sin que el GLM los estime libremente.

Restricciones sin uso del offset - Limitaciones a la tarifa teorica

Ejemplos de restricciones externas (de mercado o regulatorias):

Mercado: no es bien recibido diferenciar tarifas por genero.
Regulacion: no se permiten descuentos por alarma vehicular.

Efecto de no incluir una variable restringida:

Si no hay correlacion entre los expuestos de la variable restringida y el resto, al no incluirla solo se modifica el intercepto para compensar globalmente lo que no se puede diferenciar en el precio.
Si existen correlaciones (ej. entre vehiculos con alarma y ciertas localidades), las relatividades de las variables correlacionadas se distorsionan para compensar el efecto: aumentan los Betas de las categorias con mas vehiculos sin alarma, y disminuyen los de las restantes. Es decir, las relatividades 'buscan compensar' la limitacion, generando una distorsion indirecta.

Uso del offset en reemplazo de una variable no incluida

Caso de uso tipico - subsidios cruzados entre localidades:

Correr primero un GLM sin restricciones y observar las relatividades reales de cada localidad.
Para lograr el subsidio cruzado deseado (ej. que localidades con mejor poder adquisitivo subsidien a otras), se incluye en el offset el LN (logaritmo natural) de cada una de las relatividades deseadas por localidad, y se corre el GLM sin esa variable como explicativa.
Consecuencia: las variables correlacionadas y el intercepto sufren modificaciones al tratar de compensar el efecto impuesto por el offset.

Ejemplo del webinar: la relatividad de 'sin alarma' baja para compensar parcialmente el sobrecosto que se le cobra de mas a Buenos Aires (por el subsidio impuesto via offset).

Otros ejemplos de aplicacion de restricciones / offset

Suavizar el impacto de incluir variables nuevas que penalizan fuertemente a ciertas categorias de riesgo.
Combinar relatividades de experiencia externa (de mercado) con relatividades propias de la cartera.
Subyace una hipotesis sobre la distribucion de la cartera, su deterioro, seguimiento y correccion a lo largo del tiempo.

15. Otros aspectos generales de los modelos GLM

Agrupando coberturas con GLM

Para productos 'enlatados' (multirriesgo, ej. combinado familiar / multirriesgo hogar), se puede llegar a una tarifa global mediante el siguiente procedimiento:

Calcular frecuencia y costo medio de cada cobertura.
Obtener la Prima Pura de cada cobertura.
Sumar las PP de todas las coberturas y agregar (si corresponde) valores fijos por poliza.
Correr un GLM sobre las primas resultantes y expresar la tarifa final en UM o como porcentaje de la S.A. principal.

Analisis del impacto de la nueva tarifa en la cartera vigente

Para comparar el resultado del GLM contra la tarifa actual, se puede analizar:

Los resultados variable por variable (impacto individual).
El efecto global combinado de todas las modificaciones simultaneas.

Grafico de Impactos

Muestra el numero de expuestos de la cartera vigente que experimentarian alzas o bajas en sus primas si se implementa la nueva tarifa.
Permite distinguir entre:

Negocios actualmente rentables.
Negocios actualmente NO rentables.

El grafico de impactos puede segmentarse por categorias de una variable particular (ej. por localidad), lo que permite identificar que categorias son rentables y cuales no, considerando el efecto combinado de todas las variables y las nuevas relatividades.
Aplicacion practica: si una gran proporcion de expuestos de ciertas zonas (ej. 'Resto Sur' y 'Buenos Aires') experimentaria fuertes alzas, esto permite repensar el suavizado de ciertas variables para atenuar el impacto del cambio de tarifa, o aplicarlo en dos o mas etapas (implementacion gradual).""",
    },
    "5": {
        "nombre": "Tema libre con explicacion breve",
        "ejemplo": ""
    },
    "6": {
        "nombre": "Resuelve",
        "ejemplo": ""
    }
}
