# Projeto de Tradutor Gestual

Este projeto consiste em uma aplicação interativa que utiliza a biblioteca OpenCV e MediaPipe e para a interface gráfica o framework Pygame. Com isto quero tornar possivel aprendizagem de linguagem gestual utilizando a deteção de gestos das mãos. O objetivo é desafiar o jogador a realizar gestos específicos, memorizar e por fim desafiar o mesmo, usando um sistema de pontuação.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal do projeto.
- **OpenCV**: Para captura de vídeo e detecção de mãos/poses e faces.
- **Pygame**: Para interface do jogador e exibição gráfica.
- **Mediapipe**: Biblioteca utilizada para a detecção de gestos/faces.

---
## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/ineslidorio12/PROJAPP.git
   ```

2. Vá até o diretório do projeto:
   ```bash
   cd PROJAPP
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

---
## AVISO
- Presença de uma pasta "not used" que contém dois ficheiros python com a possivel implementação da deteção de poses.

## Execução do Projeto

Para iniciar a aplicação, execute o seguinte comando:

```bash
python project/app/main.py
```

A aplicação iniciará e abrirá a interface principal com as seguintes opções de menu.

---

## Funcionalidades do Projeto

### 1. Menus
O projeto inclui menus intuitivos:

- **Pagina Inicial:**
  - Jogar
  - Sair

- **Menu Principal:**
  - Aprender
  - Treinar
  - Desafio
  - Pagina Inicial
  - Sair

### 2. Modos de Jogo

#### Modo Aprender
Este modo consiste na identificação dos gestos associados às palavras e na replicação dos mesmos. 

#### Modo Treinar
Na exibição das palavras, o jogador tem de corresponder o gesto que está associado à mesma.


#### Modo Desafio
O jogador, tem um limite de 30 segundos para executar o maior número possível de gestos correspondentes às palavras que são apresentadas de forma aleatória
no ecrã. Este modo vai apresentar uma contagem em tempo real cada vez que o jogador acerta uma palavra. 

### 3 .Configurações Usadas

- **Deteção de gestos:**
  - OLA! - gesto de palma aberta
  - ADEUS! - gesto de punho fechado
  - OBRIGADA - gesto de "thumbs up" (polegar para cima)
  - TUDO BEM? - gesto de "peace" (sinal de paz)
  - AJUDA - gesto de 3 dedos levantados

- **Deteção de face**
  - No fim do modo desafio, é detetada a face do jogador, e é adicionada uma máscara.

- **Pontuação:**
  - Cada gesto correto aumenta a pontuação.
  - Feedback positivo é mostrado na tela ao acertar um gesto.

- **Tempo de Jogo:**
  - 30 segundos para tentar acertar o máximo de gestos possíveis.

---

## Interface Gráfica
A interface é composta por:
- Exibição da câmera ao vivo com a detecção dos gestos/face.
- Contadores de tempo e pontuação.
- Feedback visual (cores e mensagens informativas).

---

## Melhorias Futuras
- Adicionar suporte para mais gestos personalizados.
- Melhorar a estabilidade da detecção da mão usando IA.
- Suporte para multiplataforma (Windows, Linux, macOS).

---

## Problemas Conhecidos
- A detecção da face pode variar dependendo das condições de iluminação.
- Pequenos atrasos podem ocorrer em hardwares de baixo desempenho.
- Dificuldade na deteção das poses devido ao ambiente.

---

## Autores
- **Inês Lidório** 

