# Analisador de Currículos

Este é um projeto de análise de currículos que utiliza a API do Ollama para resumir e pontuar currículos com base na descrição de uma vaga específica. O projeto é desenvolvido em Python, com o Streamlit como front-end para a interface do usuário.

## Funcionalidades

- **Upload de Currículos em Lote**: Carregue vários currículos de uma vez para análise.
- **Análise de Currículos**: Avalie currículos com base em diferentes seções, atribuindo uma pontuação conforme a relevância para a vaga.
- **Comparação de Currículos**: Compare currículos lado a lado para uma avaliação mais detalhada.
- **Análise Crítica Descritiva**: Geração de uma análise crítica e descritiva sobre o currículo em relação à vaga.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada no projeto.
- **Streamlit**: Framework utilizado para criar a interface web de maneira rápida e interativa.
- **Groq API (Llama 3.1)**: API utilizada para resumir os currículos e gerar a pontuação.
- **Poetry**: Ferramenta de gerenciamento de dependências e ambientes virtuais em Python.

## Instalação e Execução

Para executar este projeto localmente, siga as etapas abaixo:

### Pré-requisitos

- Python 3.10 ou superior
- Poetry instalado globalmente

### Passos para instalação

1. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/asimov-academy/cv-recruter.git
   cd cv-analyser
   ```

2. Instale as dependências do projeto utilizando o Poetry:
   ```bash
   poetry install
   ```

3. Execute o projeto com o Streamlit:
   ```bash
   poetry run streamlit run analyze/app.py
   ```

4. Acesse o projeto no seu navegador através do endereço:
   ```
   http://localhost:8502
   ```

## Uso

Após subir o projeto, você poderá:

1. Cadastrar novas vagas através da interface.
2. Subir currículos em lote para análise.
3. Visualizar a análise de cada currículo por vaga, com a possibilidade de comparar currículos.
4. Gerar análises críticas descritivas sobre os currículos em relação às vagas.

## Documentação do Sistema de Pontuação

O sistema de pontuação foi projetado para avaliar currículos com base em uma vaga específica. As seções avaliadas incluem:

- **Experiência (Peso: 30%)**
- **Habilidades Técnicas (Peso: 25%)**
- **Educação (Peso: 10%)**
- **Idiomas (Peso: 10%)**
- **Pontos Fortes (Peso: 15%)**
- **Pontos Fracos (Desconto de até 10%)**

Cada seção recebe uma pontuação de 0 a 10, com justificativas para as notas atribuídas. A pontuação final é uma média ponderada das avaliações, refletindo a adequação do candidato à vaga.
