# Manual de zRadio para NVDA
## Observaciones importantes del Autor

Este complemento surge del aburrimiento y de las ganas de experimentar con NVDA.

zRadio es un complemento muy pesado, aproximadamente 120 mb una vez está instalado.

Se recomienda usar zRadio en equipos que no sean de trabajo y en equipos con un hardware aceptable.

En algunos equipos con pocos recursos puede ralentizar NVDA por lo que es recomendable desinstalar el complemento.

Como digo es un experimento y como tal hay que tenerlo, quien instale el complemento es el responsable de la ralentización que el complemento puede causar al igual que el uso que haga de dicho complemento.

El autor no se hace responsable ni del uso que se de del complemento ni de problemas que puedan aparecer.

El autor igualmente informa que las radios del complemento son todas Online por lo que el responsable de los enlaces es la página que proporciona dichos enlaces, además no se hace responsable de fallos o malos funcionamientos por la parte correspondiente a la emisión de las emisoras de radio.

Este complemento ha sido desarrollado en un ordenador con altas prestaciones por lo que no se sufre de lentitud, esta parte podre ir reescribiéndola sobre las observaciones que se me den por los distintos medios de comunicación.

Unos apuntes por si se desinstala el complemento.

El complemento solo guarda 3 archivos en el directorio zRadio que encontramos en el directorio de configuración de NVDA y son los siguientes:

* Opciones.dat

* opt_radio.dat

* fav_radios.dat

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
