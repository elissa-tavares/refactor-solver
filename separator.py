import os


def extract_classes(file_path):
    """
    Extrai classes de um arquivo Java.

    Args:
        file_path (str): O caminho para o arquivo Java.

    Returns:
        dict: Um dicionário onde as chaves são os nomes das classes
        e os valores são os conteúdos das classes.
    """
    classes = {}  # Dicionário para armazenar as classes extraídas

    with open(file_path, 'r') as file:
        class_name = None  # Variável para armazenar o nome da classe atual
        class_content = ''  # Variável para armazenar o conteúdo da classe atual
        inside_class = False  # Indicador se estamos dentro de uma classe ou não
        brace_count = 0  # Contador para rastrear as chaves de abertura e fechamento

        for line in file:  # Itera sobre cada linha do arquivo
            if any(keyword in line for keyword in ['class', 'interface', 'enum']) and not inside_class:
                # Se encontrarmos uma declaração de classe, interface ou enum e não estivermos dentro de uma classe
                if 'class' in line or 'interface' in line:
                    # Adiciona 'public' se a declaração não começar com 'public'
                    if not line.strip().startswith('public'):
                        line = 'public ' + line

                # Identifica a palavra-chave (class, interface ou enum) na linha atual
                keyword = [keyword for keyword in ['class', 'interface', 'enum'] if keyword in line][0]

                # Extrai o nome da classe
                class_name = line.split(' ')[line.split(' ').index(keyword) + 1].strip()
                inside_class = True  # Marcamos que estamos dentro de uma classe
                class_content += line  # Adiciona a linha ao conteúdo da classe
                brace_count = 1  # Inicializa o contador de chaves

            elif inside_class:  # Se estivermos dentro de uma classe
                class_content += line  # Adiciona a linha ao conteúdo da classe
                brace_count += line.count('{') - line.count('}')  # Atualiza o contador de chaves

                if brace_count == 0:  # Se o contador de chaves indicar o fim da classe
                    inside_class = False  # Marcamos que não estamos mais dentro de uma classe
                    classes[class_name] = class_content.strip()  # Armazena a classe no dicionário
                    class_name = None  # Reinicializa o nome da classe
                    class_content = ''  # Reinicializa o conteúdo da classe

    return classes  # Retorna o dicionário contendo as classes extraídas


def create_class_files(base_directory):
    """
    Cria arquivos Java para as classes extraídas de arquivos "Solver.java"
    em um diretório base.

    Args:
        base_directory (str): O diretório base para começar a busca de arquivos.
    """
    for root, dirs, files in os.walk(base_directory):  # Percorre os diretórios e subdiretórios
        for file_name in files:  # Para cada arquivo encontrado
            if file_name == "Solver.java":  # Se o arquivo for "Solver.java"
                full_file_path = os.path.join(root, file_name)  # Caminho completo do arquivo
                package_name = os.path.relpath(root, base_directory).replace(os.path.sep, '.')  # Nome do pacote
                classes = extract_classes(full_file_path)  # Extrai classes do arquivo "Solver.java"

                # Para cada classe extraída, cria um novo arquivo Java no mesmo diretório
                for class_name, class_content in classes.items():
                    # Constrói o conteúdo da nova classe com o pacote apropriado
                    new_class_content = f"""package {package_name};

{class_content}
"""
                    if class_name.endswith('{'):  # Remove caracteres extras do nome da classe, se houver
                        class_name = class_name[:-1].strip()

                    # Constrói o caminho para o novo arquivo Java
                    new_file_name = f"{class_name}.java"
                    new_file_path = os.path.join(root, new_file_name)

                    # Escreve o conteúdo da nova classe no novo arquivo
                    with open(new_file_path, 'w') as new_file:
                        new_file.write(new_class_content)

                    print(f"Classe '{class_name}' movida para '{new_file_path}'")  # Mensagem informativa


# Extrai classes e cria arquivos para todos os pacotes
create_class_files("/home/sousx/Documentos/POO_IS_FUN/")  # Chama a função com o diretório base
