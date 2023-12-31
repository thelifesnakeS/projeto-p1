<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/48f72b36-a4bf-4409-8fd1-3fed3703e150"  />
</div>

<h1 align="center">The Life Snake 🐍</h1> 
  <h3 align="center">Projeto de Programação 1 - 2023.1 CIn/UFPE - Jogo Python em POO</h3>

<p align="center">
<br />
  <a href="https://github.com/thelifesnakeS/projeto-p1"><strong>Ir para o repositório »</strong></a>
<br />
</p>

#
## Membros e Divisão de Tarefas
Membro  | Tarefas Realizadas
:--------:| -------------
**Kaynã Xavier (<a href="https://github.com/kxsilva"><strong>kxs</a>)** | Liderou a criação da mecânica do jogo, como a parte de colisão e movimentação da cobra na tela, também fez a criação dos coletáveis, além de melhorar a interatividade dos mesmos inserido tempo de geração.
**Mikaell Miguel (<a href="https://github.com/mikaellmiguel"><strong>mms14</a>)** | Responsável pela correção de erros, como movimentação errônea da cobra, e coletáveis sendo gerado de maneira inapropriada, também realizou a atribuição de efeitos aos coletáveis e ficou com criação do design do jogo.
**Victor Coutinho (<a href="https://github.com/vmscoutinho"><strong>vmsc</a>)**   | Foi encarregado de adicionar novas funcionalidades ao jogo, como a remoção da colisão com paredes para tornar o nível de dificuldade mais atrativo, e liderar a elaboração da apresentação advinda deste projeto.

## Descrição do Jogo
"The Snake Life 🐍" é um jogo de computador desenvolvido em Python que coloca os jogadores no papel de uma cobra faminta. O objetivo do jogo é simples, mas desafiador: você deve guiar a cobra pelo campo do jogo para coletar alimentos dispersos e, assim, conseguir a maior quantidade de alimentos possíveis, evitando colisões consigo mesma. Quanto a parte visual, o jogo foi baseado no jogo da "Snake" do google que é disponibilizado nos navegadores.

### Requesitos Mínimos ⚠️
* Estar em um ambiente desktop 🖥️
* Ter o Python instalado
* Ter as seguintes bibliotecas instaladas: Pygame, Random
* Ter uma IDE com suporte ao Python Instalada
* Ter um monitor com resolução acima de 800x600

### Instruções do Jogo
Para comecar a jogar o jogo criando neste presente projeto é necessário clonar ou baixar o repositório e na pasta 📁 executar o código que está localizado no arquivo “**main.py**” para que o jogo seja iniciado.

### Movimentos
A Cobra é um elemento controlável pelo jogador, onde deve-se utilizar as setas dos teclados para guiar a movimentação da cobra. É valido ressaltar que a cobra segue movimento continuo mesmo sem o jogador está segurando alguma seta, além disso, a cobra não se move na direção oposta, por exemplo, se a cobra está se movendo para cima, não pode se mover para baixo apenas para os lados.

Tecla  | Ação
:--------:| -------------
⬆️|  Direciona a cobra a se mover para cima.
⬇️|  Direciona a cobra a se mover para baixo.
➡️|  Direciona a cobra a se mover para direita.
⬅️|  Direciona a cobra a se mover para esquerda.

### Coletáveis

<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/f52c64bf-42c3-46cd-aa73-c5bef5a08df1" width="702px" />
</div>

**Normal (vermelho)**: Este coletável é responsável por aumentar o tamanho da cobra em 1 bloco e aumentar a velocidade em apenas 3%. O mesmo oferece ao jogador **1 ponto** no score final.

**Nerf (Preto)**: Este coletável aumenta o tamanho da cobra, além disso, é responsável por aumentar a velocidade da cobra em 10% dificultando o controle sobre a mesma. O mesmo oferece ao jogador **2 pontos** no score final.

**Buff (Amarelo)**: Esse é o coletável mais raro, ele é responsável por diminuir 1 bloco de tamanho da cobra e diminuir 20% da velocidade melhorando o controle sobre a mesma. Apesar de fornecer esses benefícios o Buff **não oferece pontos ao jogador**, sendo assim, o jogador tem que realizar esse gerenciamento de quando pegar o buff ou quando tem que pegar os outros coletáveis para aumentar o seu score.
#
## Bibliotecas e Ferramentas
Seção voltada a expor as **Ferramentas e Bibliotecas** que foram usadas durante o desenvolvimento do projeto.
### Bibliotecas 📚


#### Pygame 🎮
Essa é a biblioteca principal do presente projeto, a mesma consiste em uma biblioteca muito popular para desenvolvimento de jogos em Python. Ele fornece uma estrutura simples e eficaz para criar jogos 2D, tornando mais fácil a implementação de gráficos, som e interação com o usuário. Utilizamos a mesma para gerenciar os eventos de interação com usuário como entradas do teclado, criar a tela de logo, inserir imagens e sons, etc.

#### Random 
A biblioteca Random é comumente utilizada para gerar números aleatórios em Python. No nosso projeto, essa biblioteca é essencial para posicionar os alimentos em locais aleatórios da tela, tornando assim o jogo imprevisível. Um dos principais benefícios é criar uma experiência de jogo mais dinâmica do que os alimentos aparecerem no mesmo lugar.

#### Sys
A biblioteca Sys é uma biblioteca padrão do Python que fornece acesso a várias funcionalidades relacionadas ao sistema operacional e à interação com a linha de comando. No nosso projeto a mesma foi utilizada para realizar o fechamento do jogo através do botão presente no menu principal.

#### Time
A biblioteca time é outra biblioteca padrão do Python que lida com funções relacionadas ao tempo e ao relógio. Essa dentre as citadas anteriormente foi a menos usada, só utilizamos a mesma em apenas uma ocasião que foi para quando a cobra colidir consigo mesma ter um tempo de pausa de 1 segundo antes de ir para tela de game over para facilitar a visualição de onde ocorreu a colisão.

### Ferramentas 🔧
#### Piskell
Aplicativo de código aberto que permite criar e editar pixel art, que é um estilo de arte digital que se baseia na criação de imagens com pixels individuais. Utilizamos o mesmo para gerar uma imagem de background customizada que se encaixa perfeitamente no formato do jogo e também para editar algumas imagens que foram utilizadas no projeto, como exemplo, as imagens dos alimentos.

#### Trello
O Trello é uma popular ferramenta de gerenciamento de projetos online. O Trello é amplamente utilizado por equipes e indivíduos para organizar tarefas, acompanhar o progresso de projetos e colaborar de forma eficaz. No projeto ele foi utilizado como uma ferramenta para distribuir tarefas entre os membros e acompanhar o progresso do projeto, ordenando os processo em execução, os que foram concluídos e os que precisam ser realizados.

## Arquitetura/Organização do Código
O código do jogo foi divido em 3 arquivos:  <a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/classes.py">classes.py</a>, <a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/audiovisual.py">audiovisual.py</a>, <a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/main.py">main.py</a> que serão descritos abaixo:

Arquivo  | Função
:--------:| -------------
 <a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/classes.py">classes.py</a>|  Este arquivo, classes.py, é responsável por definir as classes e estruturas de dados que formam a base do jogo, ou seja, contém a definição dos atributos dos objetos e os seus comportamentos (os métodos). É onde está definido as propriedades e comportamentos da comida e da cobra, como por exemplo é nesse arquivo que está a maneira que foi utilizada para movimentar a cobra, também está os métodos usados para desenhar os objetos, etc. Basicamente é onde está toda nosssa estrtutura de **programação orientada a objetos**.
<a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/audiovisual.py">audiovisual.py</a>| O arquivo audiovisual.py é responsável por lidar com a maior parte **visual e de áudio** do jogo, o mesmo foi utilizado para realizar o carregamento das imagens que estão localizadas na pasta "imagens" presente neste repositório, além disso, como descrito anteriormente esse arquivo lida com a parte sonora do jogo, nele é iniciado o mixer e carregado os sons (que estão na pasta "sound") que serão utilizados no decorrer do jogo.
<a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/menuPrincipal.py">menuPrincipal.py</a> | O arquivo "menuPrincipal.py" é um módulo do nosso projeto que desempenha um papel fundamental em nosso programa. Ele foi projetado para fornecer um menu inicial interativo para os usuários quando executamos o programa.
<a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/main.py">main.py</a>| O arquivo main.py é o que deve ser executado para que o usuário tenha acesso ao jogo, é nele que são criado os objetos (cobra e alimentos) usando as classes criadas em classe.py, além disso, o mesmo é o que lida com a entrada do jogador, no nosso caso, com as teclas que são apertadas. Esse arquivo também é encarregado de gerenciar o loop principal do jogo, é através dele que é definido o fluxo que as coisas devem ocorrer dentro do loop que roda o jogo e as condições de parada. Os outros dois arquivos (classes.py e audiovisual.py) servem de apoio para a execução do main.py.
#
## Conceitos Utilizados da Disciplina

### Recursividade
A recursão é um conceito utilizado na programação no qual uma função chama a si mesma para gerar uma solução. No nosso projeto, a recursão foi utilizada na hora gerar as posições da comida, para evitar que as mesmas fossem geradas em cima do corpo da cobra, ou seja, a função de geração das posições chama a si mesma para gerar uma nova posição quando a posição gerada está localizada encima do corpo da cobra.

<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/aa24804d-601d-4797-85de-f05643e08701" />
</div>

### Programação orientada a Objetos (POO)
É um paradigma de programação que se concentra na modelagem de software em torno de objetos, onde cada objeto é uma instância de uma classe e contém dados (atributos) e comportamentos (métodos). Esse foi o conceito mais utilizado tanto é que a maior parte do jogo está estruturado em POO e possui um arquivo específico para armazenar as classes que foram utilizadas no projeto (“classes.py”). Segue abaixo um exemplo de uma das classes criadas e um método da mesma.

<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/70d17bfa-3c4b-49a2-8f5b-faa1051303a2" />
</div>

### Listas, Dicionários, Tuplas
São estruturas de dados que são usadas para armazenar e organizar os dados em um programa. As listas no python são coleções ordenadas e mutáveis de elementos, já os dicionários são coleções não ordenadas de pares chave-valor, por fim as tuplas são coleções ordenadas e imutáveis de elementos. No projeto, foi todos os três tipos de estruturas de dados, as tuplas por exemplo, foram utilizadas para armazenar os códigos de cores, as listas para armazenar a coleção de blocos da cobra, os dicionários para armazenas os tipos de comida.

<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/05c5cc09-a08a-4209-990b-5763654a2d64" />
</div>
<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/569534df-be18-4176-b776-5ca2a3d83c90" width="800px" />
</div>
<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/4c47938f-ec80-48c7-9b55-bf1eabf8e1f3" width="800px" />
</div>


### Laços condicionais
São estruturas de controle em programação que permitem executar blocos de código com base em condições lógicas. Fizemos uso intenso dos mesmos em maior parte do código, um dos exemplos, conforme demostrado abaixo, usamos os laços condicionais para verificar para qual direção escolhida pelo usuário e assim guiar a cobra para o lado correto.

<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/8b9f3681-442b-463f-8f12-3f92d8239802" />
</div>

### Estruturas de repetição
Permitem a execução repetida de um bloco de código enquanto uma determinada condição é atendida (loop) ou até que um número específico de repetições seja alcançado. No nosso projeto, o jogo roda sobre uma estrutura de repetição while que só se encerra ao usuário fechar o jogo ou acabar perdendo, conforme demostrado abaixo:

<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/5c6ef177-5ed3-49f0-a2da-98bb82c51497" />
</div>

#
## Desafios, Erros e Lições aprendidas

### Maior Desafio
        
#### Github e Git
De início não sabíamos utilizar muito bem o GitHub e o Git, tivemos que dedicar no início do projeto, tempo ao estudo de ambas as plataformas, conseguimos com estudo rapidamente superar esse desafio e conseguimos criar o repositório e começar efetivamente a desenvolver o projeto, ainda com algumas dúvidas, mas as mesmas foram resolvidas logo na primeira semana de uso das plataformas.
#### Programação Orientada a Objetos (POO)
Alguns colaboradores do projeto nunca tiveram contato com essa forma de programar, com isso inicialmente tivemos problemas para desenvolver e entender o jogo em POO de forma correta, entretanto, esse desafio fui superado devido a ajuda mútua entre os membros do projeto sanando duvidas de quem possuía maior dificuldade no assunto.

#### Conclusão
Sendo assim, O maior desafio enfrentado durante o projeto foi a falta de familiaridade de alguns membros da equipe com as ferramentas e conceitos essenciais, como Git, GitHub e Programação Orientada a Objetos (POO). Isso exigiu um esforço extra na fase inicial para treinamento e nivelamento de conhecimento. No entanto, esse desafio se transformou em uma oportunidade de aprendizado valiosa, que fortaleceu a equipe e contribuiu para o crescimento individual de cada membro.

### Maior Erro
O maior erro cometido, que ocorreu devido à necessidade de alguns membros se ausentarem temporariamente do projeto para atender às demandas de outras disciplinas, foi a divisão de tarefas que não foi possível estipular e definir de maneira estática desde o início. Sendo assim, para lidar com esse erro, tivemos que constantemente ajustar a divisão de tarefas realizada no início, de acordo com a disponibilidade que cada membro possuía no momento. Apesar de algumas tarefas terem extrapolado o prazo inicialmente definido, conseguimos, atribuindo tarefas de maneira mais dinâmica, atender ao prazo estabelecido para a conclusão do projeto. Essa adaptação contínua foi uma lição valiosa sobre a importância da flexibilidade e da capacidade de resposta às mudanças durante o desenvolvimento de um projeto.
### Lições Aprendidas
**Uso do Git e Github**: Como descrito anteriormente, alguns membros da equipe não possuíam conhecimento sobre o Git e GitHub. Embora isso tenha se revelado um desafio inicial, o projeto se tornou uma grande oportunidade para aprender efetivamente o uso dessas ferramentas. À medida que a equipe se familiarizava com o Git e GitHub, começaram a experimentar os benefícios de um controle de versão eficiente e colaboração mais eficaz. O aprendizado contínuo se tornou uma parte integrante do processo de desenvolvimento.

**Comunicação é fator Essencial**: Através desse presente projeto, nós como equipe, vimos que a comunicação em um ambiente de desenvolvimento é um fator essencial para o sucesso do projeto. Foi através da comunicação que os membros conseguiram sanar dúvidas referentes ao projeto e ao conteúdo abordado nele. Além disso, a comunicação eficaz evitou que tivéssemos problemas e conflitos durante o decorrer do desenvolvimento. A troca de informações e ideias permitiu que todos estivessem alinhados quanto aos objetivos e tarefas, resultando em um ambiente de trabalho mais colaborativo e produtivo. 

**Compreensão de POO**: Este presente projeto foi o primeiro contato com a programação orientada a objetos para a maioria dos membros. Como mencionado anteriormente, inicialmente, dominar essa forma de programar representou um desafio significativo. No entanto, à medida que o projeto avançava, todos os membros começaram a compreender melhor os conceitos de POO. Acreditamos que o aprendizado durante o projeto proporcionou uma base sólida para futuros projetos e uma compreensão mais profunda da estruturação do código e da reutilização de componentes.

**Planejamento é crucial**: Definir metas, alocar tarefas de maneira eficiente, identificar riscos e obstáculos antes mesmo de começar a implementar nos ajudou a moldar melhor a nossa ideia conforme nossa capacidade atual. O planejamento foi algo crucial para que o projeto ocorresse sem falhas muito significativas, sendo um dos principais fatores para o sucesso do projeto. Através do planejamento, conseguimos manter o projeto no caminho certo e minimizar surpresas indesejadas ao longo do desenvolvimento. 
#

<h1 align="center">Capturas de Tela do Jogo</h1>

#
<h2 align="center">Menu inicial</h2>

<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/dab07cad-0493-43f8-b7ec-675e7c4ccde0" />
</div>


<h2 align="center">Tela de Gameplay</h2>

<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/606584f0-2367-4c17-b528-1fe050d61b7e" />
</div>

<h2 align="center">Tela de GameOver</h2>

<div align="center">
<img src="https://github.com/thelifesnakeS/projeto-p1/assets/144696910/ff8caabb-4b30-499f-ac27-a2e62d52bec1" />
</div>
