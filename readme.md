# Manual de zRadio para NVDA
## Observaciones importantes del Autor

Este complemento surge del aburrimiento y de las ganas de experimentar con NVDA.

zRadio es un complemento muy pesado, aproximadamente 120 mb una vez está instalado.

Esto es el caso si aun usas las versiones 0.1, 0.2 y 0.3 del complemento zRadio, aunque invitamos a los usuarios de zRadio  a que descarguen la nueva versión 0.4 ya que  reduce su tamaño y mejora el rendimiento del complemento zRadio. Por favor consulta la sección  "Registro de cambios" para la versión 0.4 que se encuentra  más abajo, para más detalles.

Se recomienda usar zRadio en equipos que no sean de trabajo y en equipos con un hardware aceptable.

En algunos equipos con pocos recursos puede ralentizar NVDA por lo que es recomendable desinstalar el complemento.

Esto es el caso si aun usas las versiones 0.1, 0.2 y 0.3 del complemento zRadio, aunque invitamos a los usuarios de zRadio  a que descarguen la nueva versión 0.4 ya que  reduce su tamaño y mejora el rendimiento del complemento zRadio. Por favor consulta la sección  "Registro de cambios" para la versión 0.4 que se encuentra  más abajo, para más detalles.

Como digo es un experimento y como tal hay que tenerlo, quien instale el complemento es el responsable de la ralentización que el complemento puede causar al igual que el uso que haga de dicho complemento.

El autor no se hace responsable ni del uso que se de del complemento ni de problemas que puedan aparecer.

El autor igualmente informa que las radios del complemento son todas Online por lo que el responsable de los enlaces es la página que proporciona dichos enlaces, además no se hace responsable de fallos o malos funcionamientos por la parte correspondiente a la emisión de las emisoras de radio.

Este complemento ha sido desarrollado en un ordenador con altas prestaciones por lo que no se sufre de lentitud, esta parte podre ir reescribiéndola sobre las observaciones que se me den por los distintos medios de comunicación.

Unos apuntes por si se desinstala el complemento.

El complemento solo guarda 3 archivos en el directorio zRadio que encontramos en el directorio de configuración de NVDA y son los siguientes:

* Opciones.dat

* opt_radio.dat

* fav_radios.dat

Esto es el caso si aun usas las versiones 0.1, 0.2 y 0.3 del complemento zRadio, aunque invitamos a los usuarios de zRadio  a que descarguen la nueva versión 0.4. Al instalar  esta nueva versión se instalará  los dos nuevos archivos llamados:

* cache.dat

* radio_cache.dat

Ahora El complemento solo guardará  5 archivos en el directorio zRadio que encontramos en el directorio de configuración de NVDA si se usa esta nueva versión 0.4 del complemento zRadio.

Por favor consulta la sección  "Registro de cambios" para la versión 0.4 que se encuentra  más abajo, para más detalles.

En la versión 0.5 se sustituyen los archivos cache.dat y radio_cache.dat por cache .sqlite.

Para aquellos programadores que saben mucho, no me riñáis por el código tan burdo y tan atropellado y por no poner comentarios y hacer todo lo que no tiene que hacer un programador si quiere  ser ordenado.

Mi manera de programar esta en mi cabeza y no sabría como explicar que todo el código lo tengo en la cabeza y que va surgiendo de repente, e intentado seguir pautas las cuales siempre rompo por no serme productivas en mi manera de escribir.

Pero como digo y en mi defensa esto es fruto del aburrimiento y querer experimentar con NVDA.

## Interface de zRadio

Para abrir el complemento tendremos que dirigirnos al menú de NVDA / Herramientas y allí esta zRadio.

Igualmente podemos asignarle un gesto de entrada el cual no viene definido para abrir el complemento yendo al menú de NVDA / Preferencias / Gestos de entrada y buscar zRadio, asociado con la orden: "Muestra la ventana principal de zRadio".

Una vez abierta la interface consta de una lista en árbol que tiene 3 categorías, empezando de arriba hacia abajo nos encontramos primero con la pantalla General, la segunda Favoritos y la tercera Buscador. Cuando estemos en la lista en árbol podemos movernos por ella con las flechas arriba y abajo. Paso a resumir rápidamente las 3 categorías:

* General, en la cual tendremos las emisoras que predefinamos desde el área buscar. Esto se explicara más adelante.

* Favoritos, donde tendremos las emisoras que más escuchemos y que con anterioridad hallamos agregado.

* Buscador, en esta categoría podremos hacer ya sea una búsqueda general de radios, por países, por idioma o por etiqueta.

Bien cuando el foco este en las categoría seleccionada para activarla pulsamos la tecla TAB, y caeremos en un campo  de busqueda, ya sea  para buscar una emisora o para seleccionar una categoría en un cuadro combinado si  estamos en la categoría Buscador.

Una vez que hayas escrito lo que deseas encontrar  pulsa el botón Buscar. También se puede pulsar la tecla Intro después  de haber introducido una búsqueda en dicho campo. Por lo tanto, esta  acción vendría a ser la misma que si hubieramos pulsado el botón Buscar.

Si tabulamos encontraremos  el listado de emisoras. Cuando estemos en la lista podemos movernos por ella con las flechas,  Una vez sobre el nombre de las emisora,y pulsando la tecla aplicaciones o shift+f10 para mostrar las opciones disponibles para la radio.

Si volvemos a tabular y no tenemos nada en reproducción caeremos en una barra de volumen que por defecto la primera vez esta al 50%, si estamos reproduciendo algo caeremos en los botones que controlan la reproducción.

En el control de volumen podemos usar las flechas tanto izquierda o derecha como arriba y abajo tanto para subir como para bajar el volumen. Paso a resumir rápidamente los botones:

* Detener, que parara toda la reproducción.

* Recargar, que recargara la emisora que estaba sonando. Esto es útil por si se pierde el buffer y no queremos buscar de nuevo la emisora.

* Silenciar, este botón cambiara su nombre cuando lo usemos a Quitar Silencio y viceversa durante la reproducción.

Si tabulamos otra vez caeremos en una barra de botones en la cual ahora solo esta salir, pero próximamente tendrá más opciones.

## Pantalla General

En esta pantalla lo primero que caeremos es en un campo de búsqueda donde podremos poner lo que queramos buscar. Decir de este campo que es indiferente si ponemos mayúsculas o minúsculas y que nos devolverá el resultado que contenga lo que hayamos escrito.

Por ejemplo si ponemos onda nos devolverá todas las emisoras que contengan esa palabra, cuidado si ponemos solo la letra o nos devolverá todas las emisoras que contengan la letra o, esto puede causar un retardo en la búsqueda de resultados si estamos en una lista muy grande de emisoras y hay muchas que contengan la letra o.

Si tabulamos tendremos el botón Buscar el cual si lo pulsamos empezara la búsqueda y dicho botón cambiara su nombre a Limpiar. Para volver a tener el listado de emisoras tendremos que pulsar el botón limpiar.

Nota: También se puede pulsar la tecla Intro después  de haber introducido una búsqueda en dicho campo. Por lo tanto, esta  acción vendría a ser la misma que si hubieramos pulsado el botón Buscar.

Si volvemos a tabular tendremos un Listado de emisoras o el resultado de la búsqueda dependiendo de lo que hubiésemos echo en el cuadro de búsqueda.

## Pantalla Favoritos

En esta pantalla podremos agregar aquellas emisoras que deseemos tener a mano rápidamente, decir que podremos agregar todas las que deseemos incluso duplicando nombres.

El área de trabajo es exactamente igual que la pantalla General por lo que no la volveré a describir.

Comentar que por el listado tanto de emisoras como de resultados de una búsqueda podemos movernos rápidamente pulsando una letra, lo que nos llevara si hay a la primera emisora que tenga esa letra en el principio de su nombre.

En la interfaz de zRadio para la nueva versión 0.3 acabo de agregar nuevas características tales como:

* Ordenar las emisoras en favoritos.

* Añadir, editar y borrar emisoras en Favoritos.

* Ahora tienes la posibilidad de lanzar específicamente  5 emisoras rápidas mediante un gesto de entrada asociado con cada orden llamada "Reproducir emisora rápidamente y seguido de una numeración del 1 al 5" desde el diálogo Gestos de entrada de NVDA y buscar zRadio.

Por favor consulta la sección  "Registro de cambios" para la versión 0.3 que se encuentra  más abajo, para obtener detalles sobre el uso de las nuevas características.

## Pantalla Buscador

En esta pantalla se diferencia de las anteriores en que lo primero que nos encontraremos es un cuadro combinado el cual contiene distintas categorías donde buscar.

En la primera categoría, Búsqueda general de radios podremos buscar en todo el catalogo de radios.

Podremos también buscar por países, por idioma o por etiqueta. En el caso de una búsqueda por etiqueta:

Bien si buscamos Rock nos dará todas las etiquetas con dicha clasificación.

Bien en cualquiera de las categorías anteriores podremos buscar, pero solo en la categoría General podremos reproducir directamente desde esa categoría al igual que agregar a favoritos y copiar la URL de la emisora.

En el resto de categorías solo podremos añadir lo que elijamos a la pantalla General y en dicha pantalla General explorarlo.

## Relacionado con teclas, gestos y menús contextuales

En cada lista de resultados ya sea de emisoras  o de una búsqueda podremos lanzar un menú contextual para interactuar con lo que tengamos seleccionado.

Dicho menú lo lanzaremos bien con la tecla aplicaciones o con Shift+F10 en aquellos ordenadores que no dispongan de la tecla aplicaciones.

En la pantalla General podremos interactuar con lo siguiente ya sea en el listado de emisoras o de una búsqueda:

* Reproducir, nos reproducirá la emisora.

* Agregar a favoritos, nos agregara la emisora a la pantalla Favoritos.

* Copiar URL, nos copiara la URL de la emisora al portapapeles pudiendo abrirla en un navegador web o compartirla.

En la pantalla Favoritos podremos interactuar con lo siguiente:

Listado de emisoras:

* Reproducir, reproduciremos la emisora seleccionada.

* Quitar de favoritos, eliminaremos la emisora de favoritos.

* Copiar URL, copiaremos la URL de la emisora al portapapeles.

Listado de una búsqueda:

* Reproducir, reproduciremos la emisora.

* Copiar URL, copiaremos al portapapeles la URL de la emisora.

En la pantalla Buscador  podremos interactuar con lo siguiente:

Después de haber hecho la búsqueda utilizando la categoría Búsqueda general de radios:

En el listado de resultados de una búsqueda general:

* Reproducir

* Agregar a favoritos

* Copiar URL

Ya explicados con anterioridad.

En las categorías Búsqueda por países, Búsqueda por idioma y Búsqueda por etiqueta solo podremos usar tanto en el listado de emisoras como en el listado de una búsqueda lo siguiente:

* Poner por defecto en General, si elegimos esto en la pantalla General tendremos las emisoras que correspondan a lo que hallamos elegido.

Si nos fijamos estas 3 categorías tienen un número el cual corresponden a cuantas emisoras tienen dicha selección.

Decir que a veces si elegimos una por ejemplo que tiene 9 emisoras y cuando vamos a la pantalla General solo cargan 8 es porque la que falta no esta bien el enlace.

### Teclas rápidas:

Realmente cada botón tiene su tecla rápida por lo que al estar explicados con anterioridad no voy a ponerlas, nuestro NVDA nos dará los atajos cuando caigamos en ellos.

Pero si hay una combinación que no aparece y es solo para cuando la ventana de zRadio esta enfocada y abierta.

* Alt +V, esta combinación de teclas nos llevara rápidamente a la barra de volumen para que podamos interactuar con ella con las teclas de flechas.

Decir también que podremos salir de la ventana de zRadio ya sea con el botón salir, con Alt+F4 o con Escape.

### Gestos de entrada

En el menú de NVDA / Preferencias / Gestos de entrada / zRadio podremos asignar un gesto de entrada es decir combinaciones de teclas a  las siguientes órdenes que se encuentran más abajo para poder interactuar desde cualquier lugar inclusive con su ventana utilizando zRadio.

Acordaros que la combinación de teclas no este asignada para otra función o no se solape con alguna de las aplicaciones que usamos.

Por defecto zRadio viene sin asignar ninguna tecla dejando al usuario a su gusto esta configuración.

Decir igualmente que estas teclas servirán tanto con zRadio abierta la ventana como si la tenemos cerrada.

zRadio proporciona las siguientes órdenes para que el usuario pueda añadir un gesto de entrada:

* Bajar volumen

* Detener reproducción

* Muestra la ventana principal de zRadio

* Poner y quitar silencio

* Recargar reproducción

* Saber emisora en reproducción

* Subir volumen

## Traductores y colaboradores:

* Francés: Rémy Ruiz
* Portugués: Ângelo Miguel Abrantes
* Inglés: slanovani
* Italiano: Simone Dal Maso
* Árabe: Wafiq Taher
# Registro de cambios.
## Versión 0.5.

* Agregado nuevo manejo de cache.

Ahora se usa la cache predefinida de la librería en vez de la creada para aligerar la carga.

Al usar la cache predefinida la carga del complemento es muchísimo más rápida. Puede que alguna vez por conexión al servidor se nos ralentice pero ahora el 95% de veces el complemento debe de cargar como si fuese un complemento más sin demorar a nuestro NVDA.


## Versión 0.4a.
* Agregados idiomas Italiano y Árabe
## Versión 0.4.
* Optimizado el código reduciendo su tamaño a más de la mitad.

Se ha optimizado el código para que ahora la instalación sea un 60% más reducida. Esto afecta a que el rendimiento es mejor.

* Agregado un pequeño cache que ayuda a acelerar el inicio del complemento.

A veces una minoría de arranques, el lector de pantalla NVDA puede llegar a tardar un poco en arrancar, esto es problema de la comunicación del complemento con el servidor.

Antes en la versión 0.3 siempre tardaba mucho en arrancar, con el cache que puse en el complemento eso ahora pasara muy pocas veces.

Bien el archivo cache.dat se actualiza cada vez que reiniciemos NVDA ya que es el que contiene el contador de las veces que tiene que llevar el número de arranques y cuando llega a 5 a la sexta vez el archivo radio_cache.dat también se actualizara.

Los archivos cache.dat y radio_cache.dat se guardan en el directorio zRadio que encontramos en el directorio de configuración de NVDA.

* Se tradujo los diccionarios de los países para que cuando seleccionemos el idioma de NVDA "Predeterminado para el usuario" bajo  la categoría "General" del cuadro de diálogo "Opciones de NVDA", ya sea el idioma  "Francés, fr", "Portugués (Portugal, Brasil), pt_PT / pt_BR" o "Inglés en", que actualmente son los tres idiomas soportados por el complemento zRadio, además del idioma español, los nombres de los países se muestren correctamente en el caso de una búsqueda por países.

De forma predeterminada zRadio está configurado para utilizar l idioma "Español, es", pero si has  elegido "Predeterminado para el usuario"  y tu idioma aún no está traducido tendrás siempre la interfaz del complemento en español.

* Se agrego traducción al Portugués (Portugal / Brasil) y al Inglés.

## Versión 0.3.

* Agregado el poder ordenar las emisoras en favoritos.

Esta nueva opción es solo para Favoritos y podremos mover la emisora que tenga el foco hacia arriba o abajo con Alt + Flecha arriba o abajo.

Al llegar tanto a la parte superior como a la inferior de la lista se reproducirá un sonido para avisarnos que estamos en el principio o final de la lista.

El sonido es diferente para identificar bien donde estamos.

* Agregada la posibilidad de añadir, editar y borrar emisoras en Favoritos.

Cuando estemos en la categoría Favoritos se mostrara un nuevo botón llamado Acción con la tecla de acceso directo Alt + a.

Este botón solo aparecerá cuando estemos en la categoría Favoritos.

Podremos llamar al botón desde cualquier parte de la interface y consta de un menú que se desplegara con las siguientes opciones:

* Nueva emisora: Nos abrirá un dialogo para introducir una emisora personal.

* Editar emisora: Editara la emisora que tenga el foco en Favoritos.

* Quitar de favoritos: Borrara la emisora que tenga el foco. Esto no es reversible.

El cuadro de dialogo tanto para Nueva emisora como para Editar emisora, es el mismo para las dos opciones.

Dicho cuadro consta de dos campos de edición, para el nombre de la emisora y para la dirección URL de la emisora.

Estos campos son obligatorios y no pueden quedar en blanco.

En la lista de Favoritos se pueden tener emisoras con el mismo nombre, pero se recomienda tener diferenciados los nombres para nuestra mejor comprensión.

Tenemos también dos botones, Aceptar y Cancelar. 

Si aceptamos se guardaran los cambios dependiendo de lo que estemos haciendo ya sea Nueva emisora o Editar emisora.

Si cancelamos se perderán todos los datos y no se guardara nada.

Además podemos cerrar el dialogo presionando Alt + F4 o Escape en estas dos acciones se perderá lo que tengamos echo.

* Agregada la posibilidad de emisoras rápidas.

Esta nueva opción nos permitirá empezar la reproducción de una emisora rápidamente.

Bien ahora podremos tener 5 emisoras rápidas, dichas emisoras serán las que tengamos puestas en Favoritos en las 5 primeras posiciones.

Para esta nueva opción se agregaron 5 nuevos Gestos de entrada que tendremos que configurar yendo al menú de NVDA / Preferencias / Gestos de entrada... / zRadio.

Bien los nuevos gestos se llaman Reproducir emisora rápidamente y seguido de una numeración del 1 al 5.

Bien cada gesto que configuremos corresponderá a la emisora que tengamos en favoritos.

Si configuramos Reproducir emisora rápidamente 1 y en Favoritos tenemos Radio de pruebas, cuando pulsemos en cualquier parte ya sea con la ventana abierta de zRadio o con la ventana cerrada la combinación de teclas que hayamos asignado a esta órden empezara a reproducir dicha emisora.

Esto es válido para las 5 emisoras primeras de Favoritos siempre y cuando hayamos asignado un gesto de entrada para cada favorito. Esta opción junto con la anterior documentada de poder ordenar las emisoras se complementan para poder tener 5 emisoras preferidas de rápido acceso.

## Versión 0.2.

* Agregado idioma Francés.

* Corregida documentación.

* Solucionado el retardo en Buscador / Búsqueda por etiqueta.

Ahora ya no se colgara la interface. Se ha reestructurado dicho área quitando los resultados por defecto y mostrando solo cuando se busque.

* Se agrego la posibilidad de pulsar Intro en los campos de búsqueda.

* Corregidos errores del código.

## Versión 0.1.

* Versión inicial.