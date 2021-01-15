# Manual do ZRadio para o NVDA
## Observações importantes do autor

Este add-on surge da vontade e do desejo de experimentar o NVDA.

zRadio é um plugin muito pesado, cerca de 120 MB depois de instalado.

Esta situação só acontece se continuares a usar versões antigas, pois, com a versão 0.4, houve modificações significativas. Para maiores detalhes, consulta, mais em baixo, a secção de modificações.

É recomendável usar zRadio em computadores não comerciais e computadores com hardware aceitável.

Em alguns computadores com poucos recursos, o extra/complemento  pode tornar o NVDA mais lento, por isso é recomendado desinstalar o plug-in. Esta situação só é válida para outras versões, que não esta.

O autor não se responsabiliza pelo uso do plugin ou por problemas que daí possam surgir.

O autor informa ainda que as estações de rádio do complemento são todas online pelo que o responsável pelos links é a página que disponibiliza os referidos links, além disso, não se responsabiliza por avarias ou avarias da responsabilidade da parte correspondente à emissão das rádios .

Este add-on foi desenvolvido num computador de alto desempenho para que não haja lentidão, esta parte pode ser reescrita nas observações que me foram fornecidas pelas diferentes mídias.

Algumas notas no caso de o add-on ser desinstalado.

O plugin salva apenas 3 arquivos no diretório zRadio, que encontramos no diretório de configuração do NVDA, que são os seguintes:

* Options.dat

* opt_radio.dat

* fav_radios.dat

Isto aplicam-se para as versões anteriores à presente. nesta versão, são instalados os seguintes ficheiros:

* cache.dat

* radio_cache.dat

A partir de agora, o extra/complemento passará a guardar cinco ficheiros, na pasta de configurações do utilizador.

Para aqueles programadores que sabem muito, não me repreendam pela forma do meu código e por não colocar comentários e fazer tudo que um programador não precisa fazer se quiser que fique arrumado.

A minha forma de programar está na minha cabeça e eu não saberia explicar que tenho todo o código na minha cabeça e que surge de repente, e tento seguir orientações que sempre quebro porque não sou produtivo na minha escrita.

Mas, como disse e em minha defesa, isso é o resultado do tédio e da vontade de experimentar o NVDA.

## interface do zRadio

Para abrir o add-on teremos que ir ao menu do NVDA / Ferramentas e lá encontraremos o o zRadio.

Também podemos atribuir-lhe uma tecla de atalho, para abrir o add-on, que não está definida, acedendo ao menu do NVDA / configurações / definir comandos, e procurar zRadio, associando-lhe um atalho: "Mostrar janela principal do zRadio".

Uma vez aberta a interface, ela consiste numa lista em árvore que possui 3 categorias, começando de cima para baixo, primeiro, encontramos o ecrã "Geral", o segundo corresponde aos Favoritos e o terceiro é um Motor de busca. Quando estamos na lista da árvore, podemos nos mover através dela com as setas para cima e para baixo. Resumo rapidamente as 3 categorias:

* Geral, em que teremos as estações que predefinimos na área de pesquisa. isso será explicado mais tarde.

* Favoritos, onde teremos as estações que mais ouvimos e que adicionámos anteriormente.

* Motor de busca, nesta categoria podemos fazer uma pesquisa geral de rádios, por países, por idioma ou por etiqueta.

Quando o foco está na categoria seleccionada, para a ativar, pressionamos a tecla TAB, e cairemos em um campo de pesquisa, seja para pesquisar uma estação ou para seleccionar uma categoria numa caixa de combinação se estivermos na categoria Pesquisar por países.

Depois de escrever o que deseja encontrar, pressione o botão Pesquisar. Também pode pressionar a tecla Enter depois de inserir uma pesquisa nesse campo. Portanto, esta ação seria a mesma que se tivéssemos pressionado o botão Pesquisar.

Depois de efectuada a pesquisa, se tabularmos, encontraremos a lista de estações. Quando já estivermos na lista podemos percorrê-la com as setas e, uma vez no nome da estação, basta pressionar a tecla de aplicativos ou shift + f10 para mostrar as opções disponíveis para a rádio.

Se tabularmos novamente e não tivermos nada a tocar, cairemos numa barra de volume que, por padrão, está em 50% na primeira vez; se estivermos a tocar algo, cairemos nos botões que controlam a reprodução.

No controlo de volume, podemos usar as setas para a esquerda ou direita e para cima e para baixo para aumentar e diminuir o volume. 

Resumo rápido dos botões:

* Parar, o que interromperá toda a reprodução.

* Recarregar, para recarregar a estação que estava a tocar. Isso será útil no caso de perda do buffer e não desejarmos procurar a estação novamente.

* Silenciar, este botão mudará seu nome quando o usarmos para Ativar o som e vice-versa durante a reprodução.

Se tabularmos novamente, cairemos em uma barra de botões na qual agora é apenas para sair, mas logo terá mais opções.

## Ecrã Geral

Neste ecrã, a primeira coisa em que cairemos é um campo de busca onde podemos colocar o que queremos pesquisar. Digamos que esse campo seja indiferente se colocarmos letras maiúsculas ou minúsculas e que ele retornará o resultado que contém os termos que escrevemos.

Por exemplo, se colocarmos "wave", ele retornará todas as estações que contenham essa palavra, cuidado se colocarmos apenas a letra "o", retornará todas as estações que contiverem a letra "o", isso pode causar um atraso na busca de resultados, se estivermos numa lista muito grande de estações e houver muitas que contenham a letra "o".

Se tabularmos, teremos o botão "Pesquisar", que, ao ser pressionado, iniciará a pesquisa; o referido botão mudará o seu nome para "Limpar". Para voltar à lista de estações, teremos que pressionar o botão "Limpar".

Observação:  Também pode pressionar a tecla Enter depois de inserir uma pesquisa nesse campo. Portanto, esta ação seria a mesma que se tivéssemos pressionado o botão Pesquisar.

Se voltarmos a tabular, teremos uma Lista de estações ou o resultado da pesquisa, dependendo do que fizemos na caixa de pesquisa.

## Ecrã de favoritos

Neste ecrã, podemos adicionar as estações que queremos ter à mão, rapidamente, ou seja, podemos adicionar todas as que quisermos mesmo duplicando os nomes.

A área de trabalho é exatamente igual à tela Geral, portanto não a descreverei novamente.

Comento que, quer pela lista de estações quer pela de resultados da pesquisa podemos nos mover rapidamente pressionando uma letra, o que nos levará à primeira estação que tem aquela letra no início do seu nome.

## Ecrã do Pesquisador

Este ecrã difere dos anteriores porque a primeira coisa que encontraremos é uma caixa de combinação que contém diferentes categorias onde pesquisar.

Na primeira categoria, "Pesquisa geral de rádios", podemos pesquisar todo o catálogo de rádios.

Também podemos pesquisar por país, idioma ou etiqueta. No caso de uma pesquisa por etiqueta:

Se procurarmos por "Rock",  obteremos todos os rótulos com essa classificação.

Em qualquer uma das categorias anteriores podemos pesquisar, mas apenas na categoria "Geral" podemos reproduzir directamente dessa categoria, bem como adicionar aos favoritos e copiar o URL da estação.

Nas demais categorias, podemos apenas adicionar o que escolhermos ao ecrã "Geral" e explorá-lo aí.

## Relacionado a teclas, gestos e menus contextuais

Em cada lista de resultados, seja de estações ou de pesquisa, podemos activar um menu contextual para interagir com o que selecionamos.

Iniciaremos este menu com a tecla de aplicativos ou com Shift + F10, nos computadores que não possuem a tecla de aplicativos.

No ecrã Geral, podemos interagir com o seguinte na lista de estações ou a partir de uma pesquisa:

* Reproduzir, vamos tocar a estação.

* Adicionar aos favoritos, adicionaremos a estação ao ecrã "Favoritos".

* Copiar URL, iremos copiar o URL da estação para a área de transferência e podemos abri-lo num navegador da web ou compartilhá-lo.

No ecrã Favoritos, podemos interagir com o seguinte:

Lista de estações:

* reproduzir, vamos tocar a estação seleccionada.

* Remover dos favoritos, removeremos a estação dos favoritos.

* Copiar URL, iremos copiar o URL da estação para a área de transferência.

Listar uma pesquisa:

* reproduzir, vamos tocar a estação.

* Copiar URL, iremos copiar o URL da estação para a área de transferência.

No ecrã do pesquisador, podemos interagir com o seguinte:

Depois de pesquisar usando a categoria Pesquisa geral de rádio:

Na lista de resultados de uma pesquisa geral:

* Reproduzir

* Adicionar aos favoritos

* Copiar URL

Tudo isto foi já explicado anteriormente.

Nas categorias Pesquisa por países, Pesquisa por idioma e Pesquisa por etiqueta, só podemos usar o seguinte na lista de estações e na lista de uma pesquisa:

* Definido por padrão como Geral, se escolhermos esta opção, no ecrã Geral teremos as estações que correspondem ao que escolhemos.

Se olharmos para estas 3 categorias, elas apresentam  um número que corresponde a quantas estações têm essa selecção.

Digamos que, às vezes, se escolhemos um, por exemplo, que tem 9 estações e quando vamos para o ecrã Geral são carregadas apenas 8 é porque o link que falta não está certo.

### Teclas rápidas:

Na verdade, cada botão tem a sua própria tecla de atalho, portanto, como já expliquei anteriormente, não vou colocar a explicação de novo, o nosso NVDA nos dará os atalhos quando os encontrarmos.

Mas se houver uma combinação que não aparece e é apenas para quando a janela do zRadio está focada e aberta.

* Alt + V, esta combinação de teclas leva-nos rapidamente à barra de volume para que possamos interagir com ela com as teclas de seta.

Digamos também que podemos sair da janela zRadio com o botão sair, com Alt + F4 ou com Escape.

### definir comandos

No menu NVDA / configurações / definir comandos / zRadio, podemos atribuir um comando, ou seja, combinações de teclas para os seguintes comandos,  para poder interagir com o zRadio, de qualquer lugar, inclusive na  janela do zRadio.

Lembre-se de que a combinação de teclas não esteja já atribuída a outra função ou não se sobrepõe a nenhum dos aplicativos que usamos.

Por padrão, o zRadio vem sem atribuição de tecla de atalho, deixando que o utilizador escolha esta configuração.

estas teclas funcionarão com a janela do zRadio aberta ou fechada.

O zRadio fornece as seguintes possibilidades para o utilizador definir um comando:

* Diminuir o volume

* Parar a reprodução

* Mostrar a janela principal do zRadio

* Silenciar e remover o silêncio

* Recarregar a reprodução

* Saber qual a estação em reprodução

* Aumentar o volume

## Tradutores e colaboradores:

* Francês: Rémy Ruiz
* Português: Ângelo Miguel Abrantes
* Inglês: slanovani
* italiano: Simone Dal Maso
* Árabe:Wafiq Taher
# registo de alterações.
## Versão 0.4a.

* Adicionada tradução italiano, Árabe

## Versão 0.4.

* Otimizado o código reduzindo o seu tamanho para menos de metade.

O código foi otimizado para que a instalação seja 60% menor. Isto afecta o desempenho no carregamento do NVDA.

* Adicionado um pequeno cache que ajuda a acelerar a inicialização do plugin.

Por vezes, numa minoria de inicializações, o NVDA pode demorar um pouco para inicializar, este é o problema da comunicação do plugin com o servidor.

Antes, na versão 0.3, sempre demorava muito para inicializar o NVDA, com o cache que coloquei no plugin isso agora acontece muito raramente.

O ficheiro cache.dat actualiza-se de cada vez que se reinicia o NVDA, até atingir a quinta vez. Nessa altura, o ficheiro radios.dat também é actualizado. Estes ficheiros são guardados na pasta do utilizador, numa subpasta com o nome do addon.

* Os dicionários dos países foram traduzidos para que, ao selecionarmos o francês ou o português, sejam mostrados correctamente.

* Adicionada tradução em português.

## Versão 0.3.

* Adicionada a capacidade de classificar estações nos favoritos.

Esta nova opção é apenas para Favoritos e podemos mover a estação que está em foco para cima ou para baixo com Alt + Seta para cima ou Seta para baixo.

Ao chegar ao topo e ao final da lista, um som será reproduzido para nos informar que estamos no início ou no final da lista.

O som é diferente para identificar bem onde estamos.

* Adicionada a capacidade de adicionar, editar e excluir estações em Favoritos.

Quando estivermos na categoria Favoritos, um novo botão chamado "Ação" será mostrado com a tecla de atalho Alt + a.

Este botão só aparecerá quando estivermos na categoria Favoritos.

Podemos chamar o botão de qualquer parte da interface e ele conduz-nos a um menu que será exibido com as seguintes opções:

* Nova estação: Vai abrir um diálogo para adicionar uma estação pessoal.

* Editar estação: Edite a estação que está em foco em Favoritos.

* Remover dos favoritos: Exclua a estação que está em foco. Isso não é reversível.

A caixa de diálogo para Nova estação e Editar estação é a mesma para ambas as opções.

Esta caixa consiste em dois campos de edição, para o nome da estação e para a URL da estação.

Esses campos são obrigatórios e não podem ser deixados em branco.

Na lista de Favoritos pode haver estações com o mesmo nome, mas é recomendável ter os nomes diferenciados para nosso melhor entendimento.

Também temos dois botões, Aceitar e Cancelar.

Se aceitarmos, as alterações serão guardadas, dependendo do que estivermos a fazer, seja Nova estação ou Editar estação.

Se cancelarmos, todos os dados serão perdidos e nada será guardado.

Também podemos fechar a caixa de diálogo pressionando Alt + F4 ou Escape nessas duas ações, o que tivermos alterado será perdido.

* Adicionada a possibilidade de estações rápidas.

Esta nova opção permitirá começar a tocar uma estação rapidamente.

A partir de  agora, podemos ter 5 estações rápidas, essas estações serão as que colocarmos em Favoritos nas primeiras 5 posições.

Para esta nova opção, foram adicionados 5 novos comandos, que teremos que configurar, acedendo ao menu NVDA / configurações / definir comandos  / zRadio.

Os novos comandos são chamados de tocar estação rapidamente e seguidos por uma numeração de 1 a 5.

Pois bem, cada comando que configurarmos corresponderá à posição da estação que tivermos em favoritos.

## Versão 0.2.

* Adicionado idioma francês.

* Estabilizada Documentação.

* Corrigido atraso no Search Engine / pesquisar por etiqueta.

Agora a interface não travará mais. Esta área foi reestruturada, retirando os resultados padrão e aparecendo apenas quando pesquisada.

* Adicionada a capacidade de pressionar Enter nos campos de pesquisa.

* Bugs de código corrigidos.

## Versão 0.1.

* Versão inicial.