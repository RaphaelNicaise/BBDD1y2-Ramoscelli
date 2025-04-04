# **Ejercicio: PROGRAMAS DE RADIO**

## **<u>Esquema</u>**
`
PROGRAMA<radio, año, programa, conductor, gerente, frecuencia_radio>
`

### *Restricciones:*
1. Una radio se transmite por una única frecuencia (frecuencia_radio) en un año
determinado, y puede cambiarla en años diferentes.
2. Cada radio tiene un único gerente por año, pero el mismo gerente puede repetirse en la 
misma radio en diferentes años. Y la misma persona puede ser gerente de diferentes 
radios durante el mismo año.
3. Un mismo programa puede transmitirse por varias radios y en diferentes años.
4. Un programa transmitido en una radio en un año determinado tiene un solo conductor

## <u>Dependencias Funcionales</u>

Considerando las restricciones y el esquema, podemos determinar las siguientes dependencias funcionales:</br>
**1. `radio`, `año` -> `frecuencia_radio`:** Una radio solo puede tener una una frecuencia en un determinado año.</br>
**2. `radio`, `año` -> `gerente`:** Una radio solo puede tener un gerente en un año determinado </br>
**3. `radio`, `año` -> `frecuencia_radio`, `gerente`:** Una radio solo puede tener una frecuencia de radio y un solo gerente en un año determinado.  </br>
**4. `radio`, `año`, `programa` -> `conductor`:** Una radio solo puede tener un conductor en un programa y año determinado.

## <u>Claves candidatas</u>

Podemos ver que `<radio, año, programa>` juntos identifican de manera unica cada registro ya que: 
- `radio` y `año` identifican una frecuencia y un gerente
- `programa` en combinacion con `radio` y `año` permiten identificar un conductor unico para ese programa.
**Clave Candidata:** (`radio, año, programa`)

## <u>Diseño en Tercera Forma Normal</u> *(3FN)*

**TABLAS**
- **<u>PROGRAMA</u>**

    *ATRIBUTOS* </br>
    `<radio, año, programa, conductor>`
    
    *CLAVE PRIMARIA COMPUESTA* </br>
    `(radio, año, programa)` </br>

    *CLAVES FORANEAS* </br> 
    `radio` con referencia a RADIO.radio  </br> 
    `año` con referencia a RADIO.año  </br> 
    `programa` con referencia a PROGRAMA_RADIO.programa </br> </br>

- **RADIO**

    *ATRIBUTOS* </br>
    `<radio, año, frecuencia_radio, gerente>`

    *CLAVE PRIMARIA COMPUESTA* </br>
    `(radio, año)` </br> </br>

- **PROGRAMA_RADIO**

    *ATRIBUTOS* </br>
    `<programa>` </br>

    *CLAVE PRIMARIA* </br>
    `programa` </br>

## <u>Justificacion de Claves Primarias</u>
En la tabla **PROGRAMA**, elegimos como clave primaria compuesta a `(radio, año, programa)` ya que un programa puede transmitirse en varias radios y diferentes años, de esta forma un conductor depende de esa combinacion para que no haya duplicados. </br>
En la tabla **RADIO**, elegimos como clave primaria compuesta `(radio, año)` ya que es imposible que haya dos radios distintas con los mismos datos para un mismo año. </br>
En la tabla **PROGRAMA_RADIO** usamos a su unico atributo `programa` como clave primaria, con esta tabla lo que hacemos es almacenar los datos de las tablas **RADIO** y **PROGRAMA**