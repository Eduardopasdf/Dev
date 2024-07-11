import re
import matplotlib.pyplot as plt

# Função para ler o arquivo de log
def read_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return logs

# Função para analisar os logs
def analyze_logs(logs):
    error_pattern = re.compile(r'ERROR')
    error_count = 0
    error_types = {}

    for log in logs:
        if error_pattern.search(log):
            error_count += 1
            error_type = log.split()[2]  # Supondo que o tipo de erro esteja na terceira coluna
            if error_type in error_types:
                error_types[error_type] += 1
            else:
                error_types[error_type] = 1

    return error_count, error_types

# Função para plotar os erros
def plot_errors(error_types):
    plt.bar(error_types.keys(), error_types.values())
    plt.xlabel('Tipos de Erros')
    plt.ylabel('Contagem de Erros')
    plt.title('Distribuição dos Tipos de Erros')
    plt.show()

def main():
    # Caminho para o arquivo de log
    log_file_path = 'server.log'
    
    # Ler os logs
    logs = read_log(log_file_path)
    
    # Analisar os logs
    error_count, error_types = analyze_logs(logs)
    
    # Exibir resultados no console
    print(f'Total de Erros: {error_count}')
    print(f'Tipos de Erros: {error_types}')
    
    # Plotar os erros
    plot_errors(error_types)

if __name__ == '__main__':
    main()
