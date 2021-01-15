# Manuel de zRadio pour NVDA
## Observations importantes de l'auteur

Cette extension provient de l'ennui et le désir d'expérimenter avec NVDA.

zRadio est une extension très lourde, d'environ 120 Mo une fois installée.

C'est le cas si vous utilisez toujours des versions 0.1, 0.2 et 0.3 de l'extension zRadio, bien que nous invitons les utilisateurs de zRadio à télécharger la nouvelle version 0.4 puisqu'il réduit sa taille et améliore la performance de l'extension zRadio. Veuillez consulter la section "Journal des changements" pour la version 0.4 ci-dessous, pour plus de détails.

zRadio est recommandé sur les ordinateurs qui ne sont pas de travail et sur les ordinateurs avec un matériel acceptable.

Sur certains ordinateurs avec peu de ressources peuvent ralentir NVDA il est donc conseillé de désinstaller l'extension.

C'est le cas si vous utilisez toujours des versions 0.1, 0.2 et 0.3 de l'extension zRadio, bien que nous invitons les utilisateurs de zRadio à télécharger la nouvelle version 0.4 puisqu'il réduit sa taille et améliore la performance de l'extension zRadio. Veuillez consulter la section "Journal des changements" pour la version 0.4 ci-dessous, pour plus de détails.

Comme je le dis ceci est une expérience et en tant que telle doit l'être, qui installe est responsable du ralentissement que l'extension peut provoquer de même que  de l'utilisation qui est faite de cette extension.

L'auteur n'est pas responsable ni de l'utilisation de l'extension ou des problèmes qui peuvent survenir.

L'auteur signale également que toutes les radios de l'extension sont en ligne donc le responsable des liens est la page qui fournit lesdits liens, en plus il ne se fait pas responsable des erreurs ou des dysfonctionnements de la partie correspondante à la diffusion   de les stations de radio.

Cette extension a été développée dans un ordinateur de haute performance de sorte qu'il ne souffre pas de lenteur, cette partie je serai en mesure de  la réécrire  sur les observations que je prends à travers des différents  moyens de communication.

Quelques notes si l'extension est désinstallée.

L'extension uniquement enregistre 3 fichiers dans le répertoire zRadio que nous trouvons dans le répertoire de configuration NVDA et sont les suivants:

* Opciones.dat

* opt_radio.dat

* fav_radios.dat

C'est le cas si vous utilisez toujours des versions 0.1, 0.2 et 0.3 de l'extension zRadio, bien que nous invitons les utilisateurs de zRadio à télécharger la nouvelle version 0.4. Lors de l'installation de cette nouvelle version, les deux nouveaux fichiers seront installés:

* cache.dat

* radio_cache.dat

Maintenant, l'extension  uniquement enregistrera 5 fichiers dans le répertoire zRadio que nous trouvons dans le répertoire de configuration NVDA si cette nouvelle version 0.4 de l'extension zRadio est utilisée.

Veuillez consulter la section "Journal des changements" pour la version 0.4 ci-dessous, pour plus de détails.

Pour les programmeurs qui savent beaucoup, ne me disputez pas pour le code  tant grossier et tant précipité et de ne pas mettre de commentaires et faire tout ce qui ne doit  pas faire un programmeur si souhaite  être ordonné.

Ma façon de programmer est dans ma tête et je ne sais pas comment expliquer tout le code que j'ai dans ma tête et qui émerge soudain, et j'ai essayé de suivre les directives lesquelles  toujours je brise parce qu'il est pas toujours productif dans ma façon d'écrire.

Mais comme je le dis  et dans ma défense c'est le résultat de l'ennui et de souhaiter d'expérimenter avec NVDA.

## Interface de zRadio

Pour ouvrir l'extension il faut allez dans le menu NVDA / Outils, et choisir zRadio.

Nous pouvons également attribuer un geste de commande lequel  ne vient pas défini pour ouvrir l'extension allant dans le menu NVDA / Préférences / Gestes de commandes puis rechercher zRadio, associé à la commande: "Affiche la fenêtre principale de zRadio".

Une fois ouverte l'interface celle-ci se compose d'une liste en arborescence qui a 3 catégories, à partir de haut en bas nous trouvons d'abord l'écran Général,    le deuxième Favoris et le troisième Moteur de recherche. Lorsque nous sommes sur la liste en arborescence, on peut la parcourir avec les flèches haut ou bas. Je vais résumer  rapidement les trois catégories:

* Général, dans lequel les stations que nous prédéterminons depuis la zone de recherche. Cela sera expliqué plus loin.

* Favoris, où nous avons  les stations que on entend le plus et que au préalable nous avons ajouté.

* Moteur de recherche, dans cette catégorie, vous pouvez effectuer soit une recherche générale de radios, par pays, par langue ou par étiquette.

Eh bien, lorsque le focus est mis sur la catégorie sélectionnée pour l'activer, appuyez sur la touche TAB, et nous tomberons dans un champ de recherche soit pour rechercher une station ou pour sélectionner une catégorie dans une zone de liste déroulante si nous sommes dans la catégorie Moteur de recherche.

Une fois que vous avez écrit ce que vous voulez vous trouver appuyez sur le bouton Rechercher.  Vous pouvez également appuyer sur la touche Entrée après la saisie d'une recherche sur ledit champ. Par conséquent, cette action serait la même chose que si on avait appuyé sur le bouton Rechercher.

Si nous faisons Tabulation  nous trouvons la liste des stations. Lorsque nous sommes sur la liste, on peut passer à travers d'elle avec les touches fléchées, une fois sur le nom de la station, et en appuyant sur  la touche applications ou maj+f10 pour afficher les options disponibles pour la radio.
 
Si nous continuons à tabuler et nous avons rien à jouer nous tomberons sur une barre de volume que par défaut la première fois est à 50%, si nous jouons quelque chose nous tomberons  sur les boutons qui contrôlent la lecture.

Dans le contrôle du volume, nous pouvons utiliser les flèches gauche ou droite et les flèches haut et bas pour augmenter et diminuer le volume. Je vais résumer  rapidement les boutons:

* Arrêter, qui arrêtera  toute lecture.

* Recharger, qui va recharger la station qui était en cours de lecture. Ceci est utile si le tampon est perdu et ne nous souhaitons pas chercher à nouveau la station.

* Couper le son, ce bouton changera de nom lorsque nous l'utilisons en Remettre le son et vice versa pendant la lecture.

Si nous faisons Tabulation une fois nous tombons dans une barre de boutons dans lequel maintenant seule est le bouton Quitter, mais bientôt nous aurons plus d'options.

## Écran Général

Sur cet écran la première chose est que nous tombons dans un champ de recherche où nous pouvons mettre tout ce que nous voulons rechercher. Dire  de ce champ qu'en tapant indistinctement des majuscules ou des minuscules et il nous donnera le résultat contenant ce que nous avons tapé.

Par exemple, si nous tapons onda nous retournera toutes les stations contenant ce mot, attention si nous tapons la lettre o nous retournera toutes les stations contenant la lettre o, cela peut entraîner un retard dans les résultats de recherche si nous sommes dans une très grande liste de stations et il y a beaucoup qui contiennent la lettre o.

Si nous faisons Tabulation  nous avons le bouton Rechercher, lorsque nous appuyons sur ce bouton il commencera la recherche et ledit bouton va changer son nom en Nettoyer. Pour retrouver la liste  des stations nous devons appuyer sur le bouton Nettoyer.

Note: Vous pouvez également appuyer sur la touche Entrée après la saisie d'une recherche sur ledit champ. Par conséquent, cette action serait la même chose que si on avait appuyé sur le bouton Rechercher.

Si nous faisons une fois de plus Tabulation nous avons une liste avec les stations ou avec le résultat de  recherche en fonction de ce que nous avons fait dans la zone de recherche.

## Écran Favoris

Sur cet écran, vous pouvez ajouter ces stations que nous utilisons plus souvent de cette façon nous les aurons plus à portée de main, c'est-à-dire que nous ajoutons tout ce que nous désirons et même dupliquer les noms.

L'espace de travail est exactement comme l'écran Général donc je ne vais pas le décrire à nouveau.

Annoter que pour la liste tantôt des stations comme la de résultats de  recherche nous pouvons passer rapidement en appuyant sur une lettre, ce que Nous amènera s'il y a une première station avec cette lettre au début de son nom.

Dans l'interface zRadio pour la nouvelle version 0.3, je viens d'ajouter de nouvelles fonctionnalités telles que:

* Trier les stations dans les favoris.

* Ajouter, modifier et retirer des favoris.

* Maintenant, vous avez la possibilité de lancer spécifiquement 5 stations rapides par un Geste de Commandes associé à chaque commande appelée "Jouer la station rapidement et suivie d'une numérotation de 1 à 5" dans le dialogue Geste de Commandes de NVDA puis rechercher   zRadio.

Veuillez consulter la section "Journal des changements" pour la version 0.3 ci-dessous, pour plus de détails sur l'utilisation des nouvelles fonctionnalités.

## Écran Moteur de recherche

Cet écran diffère des écrans précédents parce que la première chose que nous trouvons est une zone de liste déroulante qui contient différentes catégories où rechercher.

Dans la première catégorie, Recherche générale de radios nous pouvons rechercher dans tout le catalogue de radios.

Nous pouvons également effectuer une recherche par pays,  par langue ou par étiquette. Dans le cas d'une recherche par étiquette:

Eh bien, si nous cherchons Rock nous donnera toutes les étiquettes avec cette classification.

Eh bien lorsque nous sommes sur  une quelconque  des catégories précédentes nous pouvons  effectuer une recherche, mais seulement dans la catégorie Général nous pouvons  jouer directement  depuis cette catégorie ainsi que d'ajouter aux favoris et copier l'URL de la station.

Dans les autres catégories, nous pouvons ajouter simplement ce que nous choisissons à l'écran Général et dans ledit écran Général l'explorer.

## En relation avec les touches, les gestes et les menus contextuels

Dans chaque liste de résultats soit des stations ou de recherche nous pouvons lancer un menu contextuel afin d'interagir avec ce que nous avons sélectionné.

Nous lançons le dite menu avec la touche applications ou Maj + F10 sur les ordinateurs  ne disposant pas de la touche applications.

Dans l'écran Général, vous pouvez interagir avec les éléments suivants, soit dans la liste des stations ou  de recherche:

* Jouer, lit la station.

* Ajouter aux favoris, ajoute la station à l'écran Favoris.

* Copier l'URL, copie l'URL de la station dans le presse-papiers pouvant l'ouvrir dans un navigateur Web ou le partager.

Dans l'écran Favoris vous pouvez interagir avec les éléments suivants:

Liste des stations:

* Jouer, lit la station sélectionnée.

* Retirer des favoris, suppression de la station des favoris.

* Copier l'URL, copie l'URL de la station au presse-papiers.

Liste de recherche:

* Jouer, lit la station.

* Copier l'URL, copie l'URL de la station au presse-papiers.

Dans l'écran Moteur de recherche vous pouvez interagir avec les éléments suivants:

Après la recherche effectuée en utilisant la catégorie Recherche générale de radios:

Dans la liste des résultats de recherche générale:

* Jouer

* Ajouter aux favoris

* Copier l'URL

Comme expliqué ci-dessus.

Dans les catégories Recherche par pays, Recherche par langue et Recherche par étiquette nous ne pouvons utiliser tantôt dans la liste des stations comme   dans une liste de recherche l'élément suivant:

* Mettre par défaut dans Général, Si nous choisissons cela dans  l'écran Général nous avons les stations qui correspondent à ce que nous   avons choisi.

Si nous observons ces 3 catégories ont un nombre qui correspond à combien de stations ont une telle sélection.

Dire que parfois, si nous choisissons une par exemple qu'il y a 9 stations et quand nous  allons  à l'écran Général se charge seulement 8 est parce que la qui manque n'a pas le bon lien.

### Raccourcis clavier:

En fait, chaque bouton a une touche de raccourci comme il a été expliqué ci-dessus, je ne vais pas les mettres à nouveau, notre NVDA nous donnera les raccourcis quand nous tombons sur eux.

Mais s'il y a une combinaison qui ne figure pas et est seulement lorsque la fenêtre  de zRadio est focalisée et ouverte.

* Alt +V, cette combinaison de touches nous amènera rapidement à la barre de volume afin que nous puissions interagir avec elle avec les touches fléchées.

Dire aussi que nous pouvons sortir de la fenêtre de zRadio soit avec le bouton  Quitter, avec Alt+F4 ou avec Échap.

### Gestes de commandes

Dans le menu NVDA / Préférences / Gestes de commandes / zRadio nous pouvons affecter un geste de commande c'est-à-dire des combinaisons de touches aux commandes suivantes qui se trouve ci-dessous afin d'interagir depuis n'importe où y compris avec sa fenêtre en utilisant zRadio.

Rappelez-vous que la combinaison de touches ne soit pas assignée  à une autre fonction ou ne se chevauchent pas avec l'une des applications que nous utilisons.

Par défaut zRadio vient sans attribuer aucune touche en laissant à l'utilisateur à sa guise cette configuration.

Je dis également que ces touches servent  tantôt avec la fenêtre  ouverte de zRadio, ainsi que si nous l'avions fermée.

zRadio fournit les commandes suivantes pour permettre à l'utilisateur d'ajouter un geste de commande:

* Affiche la fenêtre principale de zRadio

* Arrêter la lecture

* Augmenter le volume

* Baisser le volume

* Connaître la station en cours de lecture

* Couper et remettre le son

* Recharger la lecture

## Traducteurs et contributeurs:

* Français: Rémy Ruiz
* Portugais: Ângelo Miguel Abrantes
* Anglais: slanovani
* Italien: Simone Dal Maso
* Arabe: Wafiq Taher

# Journal des changements.
## Version 0.4a.

* Ajout de la traduction Italien, Arabe 

## Version 0.4.

* Optimisé le code en réduisant sa taille à plus de la moitié.

Le code a été optimisé de manière à ce que l'installation soit réduite à 60%. Cela affecte que la performance est meilleure.

* Ajout d'un petit cache qui aide à accélérer le démarrage de l'extension.

Parfois, une minorité de démarrage, le lecteur d'écran NVDA peut prendre un peu pour démarrer, ceci est un problème de  communication de l'extension avec le serveur.

 Avant dans la version 0.3, il a toujours fallu beaucoup de temps pour démarrer, avec le cache que j'ai mis dans l'extension cela se produira maintenant très rarement.

Eh bien, le fichier Cache.DAT est mis à jour chaque fois que vous redémarrez NVDA car c'est celui qui contient le compteur des fois qu'il doit prendre le nombre de démarrages et quand il atteint 5 à la sixième fois, le fichier radio_cache.dat sera également mis à jour.

Les fichiers cache.dat et radio_cache.dat sont enregistrés dans le répertoire zRadio que nous trouvons dans le répertoire de configuration NVDA.

* Les dictionnaires des pays ont été traduits de sorte que lorsque nous sélectionnons la langue de NVDA "Utilisateur par défaut"dans la catégorie Générale de la boîte de dialogue  "Paramètres de NVDA" que ce soit la langue  "Français, fr", "Portugais (Portugal, Brésil), pt_PT / pt_BR" ou "Anglais en", lesquels sont actuellement les trois langues supportés  par l'extension zRadio, outre l'espagnol, les noms des pays sont correctement affichés dans le cas d'une recherche par pays.

Par défaut, zRadio est configuré pour utiliser la langue "Espagnol, es", mais si vous avez choisi "Utilisateur par défaut" et que votre langue n'est pas encore traduite, vous aurez toujours l'interface de l'extension en espagnol.

* Ajout de la traduction Portugaise (Portugal / Brésil) et anglais.

## Version 0.3.

* Ajoutée   la possibilité de trier les stations dans les favoris.

Cette nouvelle option est pour les favoris et nous pouvons déplacer la station qui a le focus vers le haut ou vers le bas avec Alt + Flèche haut ou bas.

Lors de l'arriver tantôt vers la partie supérieure comme vers la partie inférieure de la liste se jouera un son pour nous avertir que nous sommes au début ou à la fin de la liste.

Le son est différent afin d'identifier bien où nous sommes.

* Ajoutée   la possibilité d'ajouter, modifier et retirer des favoris.

Lorsque nous sommes dans la catégorie Favoris s'affichera un nouveau bouton appelé Action avec la touche rapide Alt + a.

Ce bouton apparaît uniquement lorsque nous sommes dans la catégorie Favoris.

On peut appeler le bouton de n'importe où de l'interface et se compose d'un menu qui sera affiché avec les options suivantes:

* Nouvelle station: Nous allons ouvrir une boîte de dialogue pour entrer une station personnelle.

* Modifier la station: Modifiera la station qui a le focus dans Favoris.

* Retirer des favoris: Ceci supprimera  la station qui a le focus. Ce n'est pas réversible.

La boîte de dialogue tantôt pour Nouvelle station comme pour Modifier la station, est la même pour les deux options.

ladite boîte de dialogue comprend deux champs d'édition pour le nom de la station et l'adresse  URL de la station.

Ces champs sont obligatoires et ne peuvent pas être vide.

Dans la liste des favoris, vous pouvez avoir des stations avec le même nom, mais il est recommandé d'avoir des noms différents pour notre meilleure compréhension.

Nous avons aussi deux boutons, OK et Annuler.

Si nous faisons OK, les changements seront enregistrées en fonction de ce que nous faisons soit  Nouvelle station ou Modifier la station.

Si nous faisons Annuler, toutes les données seront perdues et rien ne sera enregistré.

De plus, nous pouvons fermer la boîte de dialogue en appuyant sur Alt + F4 ou Échap dans ces deux actions se perdra ce que nous avons fait.

* Ajoutée la possibilité des stations rapides.

Cette nouvelle option nous permettra de commencer à jouer rapidement une station.

Bien maintenant nous pouvons avoir 5 stations rapides, ces stations seront celles que nous avons mis dans les favoris dans les 5 premières positions.

Pour cette nouvelle option ils ont été ajoutés 5 nouveaux gestes de commandes que nous allons devoir configurer  en allant dans le menu NVDA / Préférences / Gestes de commandes... / zRadio.

Bien, les nouveaux gestes de commandes sont appelés Jouer la station rapidement et suivie d'une numérotation de 1 à 5.

Bien, chaque geste de comande que nous configurons correspondra à la station que Nous avons dans Favoris.

Si nous configurons Jouer la station rapidement 1 et dans Favoris nous avons  Radio de tests, lorsque  nous appuyons de n'importe où soit avec la fenêtre ouverte  de zRadio ou avec la fenêtre fermée, la combinaison de touches que nous avons attribuées à cette commande commencera à jouer cette station.

Cela est valable que pour les 5 premières stations dans Favoris toujours tant que nous avons attribué  un geste de commande pour chaque favori. Cette option ainsi que la précédente documentée afin de pouvoir trier les stations se complètent afin de pouvoir  avoir 5 stations préférées pour un accès rapide.

## Version 0.2.

* Ajout de la traduction française.

* Documentation corrigée.

* Résolu le retard dans Moteur de recherche / Recherche par étiquette.

Maintenant, il ne se bloquera plus l'interface. Sette zone a été restructurée en supprimant les résultats par défaut et ne les montrant  lors de la recherche.

* Ajoutée la possibilité d'appuyer sur Entrée dans les champs de recherche.

* Correction de bugs dans le code.

## Version 0.1.

* Version initiale.