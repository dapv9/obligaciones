# obligaciones
Este repositorio contiene el desarrollo de prueba tecnica, Desarrollado por David Alexander Parra Valencia.

Herramienta usada Visual Code, usando ambiente virtual
Versión de Python 3.12.1

Librerias de Python usadas y sus versiones se encuentran en el archivo "Requerimientos"

En el archivo etl-obligaciones.ipynb se realiza todo el proceso de cargue procesamiento y guardado de la información de acuerdo con los requerimientos.

Se crean dos archivos donde quedan los Dataframes necesarios para ser usados en la api:
- df_obl_tas.pkl : contiene todas las obligaciones con la tasa asociada por producto, la tasa efectiva calculada  y el valor_final.
- df_total_cliente.pkl: contiene el listado de los clientes que tienen dos o mas obligaciones con el valor total de sus obligaciones.

 En el archivo api-obligaciones.py se encuentra la api que permite poner a disposición la información de los dataframes.

 Al ejecutar el archivo api-obligaciones.py, este deja disponible la información en la ruta 127.0.0.1:5000/api/obligaciones para las obligaciones y en la 127.0.0.1:5000/api/clientes  para los clientes.

 La información que se encuentra disponible mediante la api está en formato separado por punto y coma ";" para mejor facilidad en la captura de este.

Se desarrolla tablero de powerbi para el consumo de la información que se tiene mediante la api, esta se carga ajusta y se expone mediante las diferentes graficas, tablas y filtros del reporte "Obligaciones_clientes.pbix"

Adicionalmente se realiza video con explicación del tablero y este se encuentra publicado en youtube público en el siguiente link:  https://youtu.be/uSNKMxIwwaM?si=gpdGTKZxD6UCsyIF 
 
