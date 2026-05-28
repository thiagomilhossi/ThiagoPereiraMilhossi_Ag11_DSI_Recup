from colorama import init, Fore, Style

# Inicializa o colorama. 
# O parâmetro autoreset=True garante a restauração do estilo padrão do terminal após cada print.
init(autoreset=True)

# 1. Utilizar uma lista para armazenar os níveis/mensagens do reservatório
mensagens_niveis = [
    "Situação: Muito baixo (crítico)",
    "Situação: Baixo",
    "Situação: Médio",
    "Situação: Alto",
    "Situação: Muito alto (alerta)"
]

# 2. Criar uma função responsável por definir a cor da mensagem conforme o nível
def definir_cor(nivel):
    """
    Retorna a cor correspondente baseada no nível de risco.
    """
    if nivel == 1:
        return Fore.RED      # Vermelho
    elif nivel == 2:
        return Fore.YELLOW   # Amarelo
    elif nivel == 3:
        return Fore.GREEN    # Verde
    elif nivel == 4:
        return Fore.CYAN     # Ciano
    elif nivel == 5:
        return Fore.BLUE     # Azul
    else:
        return Fore.WHITE    # Padrão caso seja um nível inválido

# 3. Simulação de um ambiente real de monitoramento (sem entrada do usuário)
def iniciar_simulacao():
    print("=== Sistema de Monitoramento do Reservatório de Água ===\n")
    
    # Simulando a leitura dos níveis de 1 a 5
    for nivel_atual in range(1, 6):
        # Acessa a mensagem na lista (índice é nível - 1)
        mensagem = mensagens_niveis[nivel_atual - 1]
        
        # Obtém a cor para o nível atual
        cor_alerta = definir_cor(nivel_atual)
        
        # 4. Exibir no terminal a situação atual do reservatório com a cor correspondente
        print(f"{cor_alerta}Nível {nivel_atual} - {mensagem}")
        
    print("\n========================================================")

# Executa o programa
iniciar_simulacao()