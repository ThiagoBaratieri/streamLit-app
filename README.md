# Principais funções Streamlit

## Descrição

Este aplicativo foi desenvolvido usando Streamlit, uma biblioteca Python que permite criar aplicativos web interativos de forma rápida e fácil. O objetivo deste aplicativo é calcular o preço de aluguel de um carro com base na quantidade de quilômetros percorridos e o número de dias de aluguel.

## Funcionalidades

### 1. `st.sidebar`

- **Descrição**: O `st.sidebar` é utilizado para criar uma barra lateral na interface do aplicativo. É ideal para adicionar elementos de entrada e informações que você deseja destacar fora da área principal do aplicativo.
- **Uso**: Permite a inclusão de títulos, cabeçalhos e texto explicativo.

### 2. `st.title()`

- **Descrição**: Exibe um título grande na parte superior da página principal do aplicativo.
- **Uso**: Utilizado para definir o título principal da página.

### 3. `st.header()`

- **Descrição**: Exibe um cabeçalho de nível 1. É menor que o título e é usado para organizar o conteúdo em seções.
- **Uso**: Ideal para criar uma seção de informações ou títulos secundários.

### 4. `st.write()`

- **Descrição**: Exibe texto na interface do aplicativo. Pode ser usado para mostrar informações, instruções ou resultados de cálculos.
- **Uso**: Versátil para exibir qualquer tipo de conteúdo textual.

### 5. `st.number_input()`

- **Descrição**: Exibe um campo de entrada numérica, permitindo que o usuário insira números. Pode incluir opções como valor mínimo, máximo e valor inicial.
- **Uso**: Ideal para capturar valores numéricos dos usuários, como a quantidade de quilômetros percorridos ou dias de aluguel.

### 6. `st.button()`

- **Descrição**: Exibe um botão que o usuário pode clicar para acionar uma ação, como calcular um valor ou submeter um formulário.
- **Uso**: Utilizado para acionar cálculos ou outras ações no aplicativo.

### 7. `st.code()`

- **Descrição**: Exibe um bloco de código formatado, ideal para mostrar trechos de código ou resultados com uma formatação especial.
- **Uso**: Pode ser utilizado para exibir resultados calculados de forma clara e formatada.

### 8. `st.columns()`

- **Descrição**: Cria um layout de colunas para organizar o conteúdo em várias colunas lado a lado. É útil para exibir múltiplos itens de forma organizada.
- **Uso**: Permite a criação de uma disposição de conteúdo em colunas, facilitando a visualização de informações agrupadas.

## Instruções de Uso

1. **Instalação**: Certifique-se de ter o Streamlit instalado. Você pode instalar o Streamlit usando o pip:
```bash
pip install streamlit
```

2. **Execução**: Salve o código em um arquivo Python (por exemplo, main.py) e execute o aplicativo usando o comando:
```bash
streamlit run main.py
```

3. **Interface**: O aplicativo abrirá em um navegador web, mostrando a barra lateral com informações e os elementos principais da página para interação com o usuário.

## Observações
Este README serve como um guia geral para os componentes do Streamlit usados no aplicativo. Para projetos futuros, o código pode ser modificado e atualizado para adicionar novas funcionalidades e interfaces.