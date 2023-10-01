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
**Kaynã Xavier (kxs)** | Liderou a criação da mecânica do jogo, como a parte de colisão e movimentação da cobra na tela, também fez a criação dos coletáveis, além de melhorar a interatividade dos mesmos inserido tempo de geração.
**Mikaell Miguel (mms14)** | Responsável pela correção de erros, como movimentação errônea da cobra, e coletáveis sendo gerado de maneira inapropriada, também realizou a atribuição de efeitos aos coletáveis e ficou com criação do design do jogo.
**Victor Coutinho (vmsc)**   | Foi encarregado de adicionar novas funcionalidades ao jogo, como a remoção da colisão com paredes para tornar o nível de dificuldade mais atrativo, e liderar a elaboração da apresentação advinda deste projeto.

## Descrição do Jogo
"The Snake Life 🐍" é um jogo de computador desenvolvido em Python que coloca os jogadores no papel de uma cobra faminta. O objetivo do jogo é simples, mas desafiador: você deve guiar a cobra pelo campo do jogo para coletar alimentos dispersos e, assim, conseguir a maior quantidade de alimentos possíveis, evitando colisões consigo mesma.

### Requesitos Mínimos ⚠️
* Estar em um ambiente desktop 🖥️
* Ter o Python instalado
* Ter as seguintes bibliotecas instaladas: Pygame, Random
* Ter uma IDE com suporte ao Python Instalada
* Ter um monitor com resolução acima de 800x600

### Instruções para Uso 
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


#
## Bibliotecas e Ferramentas
Seção voltada a expor as **Ferramentas e Bibliotecas** que foram usadas durante o desenvolvimento do projeto.
### Bibliotecas 📚
#### Pygame
Essa é a biblioteca principal do presente projeto, a mesma consiste em uma biblioteca muito popular para desenvolvimento de jogos em Python. Ele fornece uma estrutura simples e eficaz para criar jogos 2D, tornando mais fácil a implementação de gráficos, som e interação com o usuário. Utilizamos a mesma para gerenciar os eventos de interação com usuário como entradas do teclado, criar a tela de logo, inserir imagens e sons, etc.

#### Random 
A biblioteca Random é comumente utilizada para gerar números aleatórios em Python. No nosso projeto, essa biblioteca é essencial para posicionar os alimentos em locais aleatórios da tela, tornando assim o jogo imprevisível. Um dos principais benefícios é criar uma experiência de jogo mais dinâmica do que os alimentos aparecerem no mesmo lugar.

### Ferramentas 🔧
#### Piskell
Aplicativo de código aberto que permite criar e editar pixel art, que é um estilo de arte digital que se baseia na criação de imagens com pixels individuais. Utilizamos o mesmo para gerar uma imagem de background customizada que se encaixa perfeitamente no formato do jogo e também para editar algumas imagens que foram utilizadas no projeto, como exemplo, as imagens dos alimentos.

#### Trello
O Trello é uma popular ferramenta de gerenciamento de projetos online. O Trello é amplamente utilizado por equipes e indivíduos para organizar tarefas, acompanhar o progresso de projetos e colaborar de forma eficaz. No projeto ele foi utilizado como uma ferramenta para distribuir tarefas entre os membros e acompanhar o progresso do projeto, ordenando os processo em execução, os que foram concluídos e os que precisam ser realizados.

## Arquitetura/Organização do Código
O código do jogo foi divido em 3 arquivos:  <a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/classes.py">classes.py</a>, <a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/audiovisual.py">audiovisual.py</a>, <a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/main.py">main.py</a> que serão descritos abaixo:

Arquivo  | Função
:--------:| -------------
 <a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/classes.py">classes.py</a>|  Direciona a cobra a se mover para cima.
<a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/audiovisual.py">audiovisual.py</a>|  Direciona a cobra a se mover para baixo.
<a href="https://github.com/thelifesnakeS/projeto-p1/blob/main/main.py">main.py</a>|  Direciona a cobra a se mover para direita.

## Conceitos Utilizados da Disciplina

### Recursividade
A recursão é um conceito utilizado na programação no qual uma função chama a si mesma para gerar uma solução. No nosso projeto, a recursão foi utilizada na hora gerar as posições da comida, para evitar que as mesmas fossem geradas em cima do corpo da cobra, ou seja, a função de geração das posições chama a si mesma para gerar uma nova posição quando a posição gerada está localizada encima do corpo da cobra.

### Programação orientada a Objetos (POO)
É um paradigma de programação que se concentra na modelagem de software em torno de objetos, onde cada objeto é uma instância de uma classe e contém dados (atributos) e comportamentos (métodos). Esse foi o conceito mais utilizado tanto é que a maior parte do jogo está estruturado em POO e possui um arquivo especifico para armazenar as classes que foram utilizadas no projeto (“classes.py”). Segue abaixo um exemplo de uma das classes criadas e um método da mesma.

### Listas, Dicionários, Tuplas
São estruturas de dados que são usadas para armazenar e organizar os dados em um programa. As listas no python são coleções ordenadas e mutáveis de elementos, já os dicionários são coleções não ordenadas de pares chave-valor, por fim as tuplas são coleções ordenadas e imutáveis de elementos. No projeto, foi todos os três tipos de estruturas de dados, as tuplas por exemplo, foram utilizadas para armazenar os códigos de cores, as listas para armazenar a coleção de pixels da cobra, os dicionários para armazenas os tipos de comida.

### Laços condicionais
São estruturas de controle em programação que permitem executar blocos de código com base em condições lógicas. Fizemos uso intenso dos mesmos em maior parte do código, um dos exemplos, conforme demostrado abaixo, usamos os laços condicionais para verificar para qual direção escolhida pelo usuário e assim guiar a cobra para o lado correto.

### Estruturas de repetição
Permitem a execução repetida de um bloco de código enquanto uma determinada condição é atendida (loop) ou até que um número específico de repetições seja alcançado. No nosso projeto, o jogo roda sobre uma estrutura de repetição while que só se encerra ao usuário fechar o jogo ou acabar perdendo, conforme demostrado abaixo:




