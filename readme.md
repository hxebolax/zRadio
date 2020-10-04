# Manual de zRadio para NVDA
## Observaciones importantes del Autor

Este complemento surge del aburrimiento y de las ganas de experimentar con NVDA.

zRadio es un complemento muy pesado, aproximadamente 120 mb una vez está instalado.

Se recomienda usar zRadio en equipos que no sean de trabajo y en equipos con un hardware aceptable.

En algunos equipos con pocos recursos puede ralentizar NVDA por lo que es recomendable desinstalar el complemento.

Como digo es un experimento y como tal hay que tenerlo, quien instale el complemento es el responsable de la ralentización que el complemento puede causar al igual que el uso que haga de dicho complemento.

El autor no se hace responsable ni del uso que se de del complemento ni de problemas que puedan aparecer.

El autor igualmente informa que las radios del complemento son todas Online por lo que el responsable de los enlaces es la pagina que proporciona dichos enlaces, no haciéndome responsable de fallos o malos funcionamientos por la parte correspondiente a la emisión de las emisoras de radio.

Este complemento ha sido desarrollado en un ordenador con altas prestaciones por lo que no se sufre de lentitud, esta parte podre ir reescribiéndola sobre las observaciones que se me den por los distintos medios de comunicación.

Unos apuntes por si se desinstala el complemento.

El complemento solo graba en el disco del usuario 3 archivos que no se encuentran dentro del directorio del complemento.

Dichos archivos se encuentran en el directorio de NVDA de configuración y son los siguientes:

* Opciones.dat

* opt_radio.dat

* fav_radios.dat

Bien estos 3 archivos contienen configuración interna del complemento que no pueden ir en el directorio del complemento por que en ocasiones si está abierta la lectura de dichos archivos y actualizamos el complemento puede dar error. Por lo tanto estos 3 archivos si decidimos desinstalar el complemento podemos borrarlos.

De momento el código no esta en Github pero junto al email que mando a la lista de NVDA en Español adjuntare también un enlace a mi nube personal donde comparto dodo el código.

Este complemento tengo que limpiarlo todavía mucho, prepararlo para poder ser traducido, optimizar el código y bueno seguir añadiéndole cosas que tengo en la cabeza.

Para aquellos programadores que saben mucho, no me riñáis por el código tan burdo y tan atropellado y por no poner comentarios y hacer todo lo que no tiene que hacer un programador si quiere  ser ordenado.

Mi manera de programar esta en mi cabeza y no sabría como explicar que todo el código lo tengo en la cabeza y que va surgiendo de repente, e intentado seguir pautas las cuales siempre rompo por no serme productivas en mi manera de escribir.

Pero como digo y en mi defensa esto es fruto del aburrimiento y querer experimentar con NVDA.

## Interface de zRadio

Para abrir el complemento tendremos que dirigirnos al menú de NVDA / Herramientas y allí esta zRadio.

Igualmente podemos asignarle un gesto el cual no viene definido para abrir la aplicación en Preferencias / Gestos de entrada y buscar zRadio.

Una vez abierta la interface consta de una lista que tiene 3 categorías:

* General, en la cual tendremos las emisoras que predefinamos desde el área buscar. Esto se explicara más adelante.

* Favoritos, donde tendremos las emisoras que más escuchemos y que con anterioridad hallamos agregado.

* Buscador, en esta pestaña podremos hacer búsquedas generales, por país, por lenguaje o por etiquetas.

Si tabulamos de esta lista anterior caeremos a continuación en otra área donde tendremos para buscar y una lista con las emisoras o todo lo correspondiente a las radios.

Si volvemos a tabular y no tenemos nada en reproducción caeremos en una barra de volumen que por defecto la primera vez esta al 50%, si estamos reproduciendo algo caeremos en los botones que controlan la reproducción.

* Detener, que parara toda la reproducción.

* Recargar, que recargara la emisora que estaba sonando. Esto es útil por si se pierde el buffer y no queremos buscar de nuevo la emisora.

* Silenciar, este botón cambiara silenciando o quitando el silencio de la reproducción.

Si tabulamos otra vez caeremos en una barra de botones en la cual ahora solo esta salir, pero próximamente tendrá más opciones.

## Pantalla General

En esta pantalla lo primero que caeremos es en un campo de búsqueda donde podremos poner lo que queramos buscar. Decir de este campo que es indiferente si ponemos mayúsculas o minúsculas y que nos devolverá el resultado que contenga lo que hayamos escrito.

Por ejemplo si ponemos onda nos devolverá todas las emisoras que contengan esa palabra, cuidado si ponemos solo la letra a nos devolverá todas las emisoras que contengan la letra a, esto puede causar un retardo en la búsqueda de resultados si estamos en una lista muy grande de emisoras y hay muchas que contengan la letra a.

Si tabulamos tendremos el botón Buscar el cual si damos empezara la búsqueda y dicho botón cambiara su nombre a Limpiar. Para volver a tener la lista original tendremos que pulsar el botón limpiar.

Si volvemos a tabular tendremos una lista con las emisoras originales o con la búsqueda dependiendo de lo que hubiésemos echo en el cuadro de búsqueda.

## Pantalla favoritos

En esta pantalla podremos agregar aquellas emisoras que deseemos tener a mano rápidamente, decir que podremos agregar todas las que deseemos incluso duplicando nombres.

El área de trabajo es exactamente igual que la pantalla general por lo que no la volveré a describir.

Comentar que por la lista tanto original como de resultados de una búsqueda podemos movernos rápidamente pulsando una letra, lo que nos llevara si hay a la primera emisora que tenga esa letra en el principio de su nombre.

## Pantalla buscador

En esta pantalla se diferencia de las anteriores en que lo primero que nos encontraremos es un cuadro combinado el cual contiene distintas categorías donde buscar.

En la primera categoría podremos buscar en todo el catalogo de radios.

Podremos también buscar por País, idioma o por etiqueta. En esta ultima etiquetas tranquilos si cuando la elegís tarda en cargar ya que tiene que cargar muchas etiquetas.

Bien en cualquiera de las categorías anteriores podremos buscar, pero solo en la general podremos reproducir directamente desde esa categoría al igual que guardar en favoritos y copiar la url de la emisora.

En el resto de categorías solo podremos añadir lo que elijamos a la pantalla general y en dicha pantalla general explorarlo.

## Relacionado con teclas, gestos y menús contextuales

En cada lista de resultados ya sea la original o de una búsqueda podremos sacar un menú contextual para interactuar con lo que tengamos seleccionado.

Dicho menú lo sacaremos bien con la tecla aplicaciones o con Shift+F10 en aquellos ordenadores que no dispongan de la tecla aplicaciones.

En la pantalla general podremos interactuar con lo siguiente ya sea en la lista original o de búsqueda:

* Reproducir, nos reproducirá la emisora.

* Agregar a favoritos, nos agregara la emisora a la pantalla favoritos.

* Copiar URL, nos copiara la url de la emisora al portapapeles pudiendo abrirla en un navegador web o compartirla.

En la pantalla favoritos podremos interactuar con lo siguiente:

Lista original:

* Reproducir, reproduciremos la emisora seleccionada.

* Quitar de favoritos, eliminaremos la emisora de favoritos.

* Copiar URL, copiaremos la url de la emisora al portapapeles.

Lista búsqueda:

* Reproducir, reproduciremos la emisora.

* Copiar URL, copiaremos al portapapeles la emisora.

En la pantalla búsqueda podremos interactuar con lo siguiente:

categoría general:

* Reproducir

* Agregar a favoritos

* Copiar URL

Ya explicados con anterioridad.

En las categorías búsqueda por países, búsqueda por idioma y búsqueda por etiqueta solo podremos usar tanto en la lista original como en una lista de búsqueda lo siguiente:

* Poner por defecto en General, si elegimos esto en la pantalla general tendremos las emisoras que correspondan a lo que hallamos elegido.

Si nos fijamos estas 3 categorías tienen un número el cual corresponden a cuantas emisoras tienen dicha selección.

Decir que a veces si elegimos una por ejemplo que tiene 9 emisoras y cuando vamos a general solo cargan 8 es que la que falta no esta bien el enlace.

### Teclas rápidas:

Realmente cada botón tiene su tecla rápida por lo que al estar explicados con anterioridad no voy a ponerlas, nuestro NVDA nos dará los atajos cuando caigamos en ellos.

Pero si hay una combinación que no aparece y es solo para cuando la ventana de zRadio esta enfocada y abierta.

* Alt +V, esta combinación de teclas nos llevara rápidamente a la barra de volumen para que podamos interactuar con ella.

Decir también que podremos salir de la ventana de zRadio ya sea con el botón salir, con Alt+F4 o con Escape.

### Gestos de entrada

En Preferencias / Gestos de entrada / zRadio podremos asignar las siguientes combinaciones de teclas para poder interactuar desde cualquier parte y ventana con zRadio.

Acordaros que la combinación de teclas no este asignada para otra función o no se solape con alguna de las aplicaciones que usamos.

Por defecto zRadio viene sin asignar ninguna tecla dejando al usuario a su gusto esta configuración.

Decir igualmente que estas teclas servirán tanto con zRadio abierta la ventana como si la tenemos cerrada.

Gestos que el usuario puede modificar:

* Bajar volumen

* Detener reproducción

* Muestra la ventana principal de zRadio

* Poner y quitar silencio

* Recargar reproducción

* Saber emisora en reproducción

* Subir volumen
