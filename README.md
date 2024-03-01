# Extração de Classes das Questões baixadas do Repositório [Arcade](https://github.com/qxcodepoo/arcade) utilizando o [TKO - Test Kit Operations](https://github.com/senapk/tko)

Este script Python foi desenvolvido para facilitar a extração das classes dos arquivos "Solver.java" das questões de Programação Orientada a Objetos (POO) do repositório [Arcade](https://github.com/qxcodepoo/arcade), baixados através do [TKO - Test Kit Operations](https://github.com/senapk/tko). O objetivo é proporcionar uma maneira simples de extrair as classes presentes em Solver para promover uma separação facilitando a análise e o desenvolvimento de soluções.

## Funcionalidades 🛠️

### Extração de Classes dos Arquivos "Solver.java":
- O script analisa os arquivos "Solver.java" presentes nos pacotes correspondentes a cada questão baixada do repositório "Arcade" pelo TKO.
- Ele extrai todas as classes, interfaces ou enums contidas nos arquivos "Solver.java", mantendo os métodos e atributos da classe a serem extraídos.

### Criação de Arquivos Java:
- Para cada classe extraída, o script cria um novo arquivo Java no mesmo diretório em que o arquivo "Solver.java" original estava localizado.
- O nome do arquivo Java é baseado no nome da classe extraída.

## Como Usar 📝

### Instalação e Configuração:
    1. Certifique-se de ter o Python instalado em seu sistema.
    2. Faça o download do script.

### Execução do Script:


1- No diretório base onde está localizado o diretório que contém todas as questões baixadas, execute o seguinte comando no terminal 

No Linux:

```bash
find diretorio_onde_estao_questoes/ -type d -name "poo_*" -exec bash -c 'cd "$0" && mv draft.java Solver.java' {} \;
```

Este comando buscará por diretórios que correspondam ao padrão "poo_*" dentro do diretório fornecido (`diretorio_onde_estao_questoes/`). Em seguida, entrará em cada um desses diretórios e renomeará o arquivo `draft.java` para `Solver.java`.

2 - No script Python fornecido, você precisa modificar o caminho para o diretório principal onde estão armazenados os pacotes de cada questão. Faça essa alteração no argumento `base_directory` ao chamar a função `create_class_files()`.

Exemplo:

```python
create_class_files("/caminho/do/seu/diretorio/base/POO_IS_FUN")
```

3 - Execute o código em uma IDEA de desenvolvimento pressionando "run".

4 - Ele procurará por arquivos "Solver.java" nos subdiretórios do diretório base, extrairá as classes e criará novos arquivos Java para cada classe extraída.

### Observações:

- Este script foi desenvolvido para operar exclusivamente com os padrões de arquivos e organização de pacotes do repositório "Arcade" e do "TKO", utilizando a linguagem Java.
- Se desejar, você pode personalizar o script para atender a outros padrões ou requisitos específicos do seu projeto.


## Contribuição 🚀
Este script está em sua primeira versão e há espaço para muitas melhorias e evoluções. Fique à vontade para contribuir.

Se você deseja contribuir, siga os passos abaixo:

```bash
git clone https://github.com/ma-elissa/refactor-solver.git
```
    
    git checkout -b feature/SEU_NOME    

Ao finalizar suas alterações, abra um [Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request) explicando o problema resolvido ou a funcionalidade adicionada. Se possível, inclua capturas de tela das modificações visuais e aguarde a revisão!

---
