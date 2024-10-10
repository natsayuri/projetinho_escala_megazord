import random
from datetime import date, timedelta

class SistemaEscala:
    def __init__(self):
        self.funcionarios = []
        self.funcionarios_ferias = []
        self.escala_atual = {}
        self.escala_historico = []

    def adicionar_funcionario(self, nome):
        if nome not in self.funcionarios:
            self.funcionarios.append(nome)
            print(f"Funcionário {nome} adicionado com sucesso.")
        else:
            print(f"Funcionário {nome} já existe no sistema.")

    def marcar_ferias(self, nome):
        if nome in self.funcionarios and nome not in self.funcionarios_ferias:
            self.funcionarios_ferias.append(nome)
            print(f"Funcionário {nome} marcado de férias.")
        elif nome in self.funcionarios_ferias:
            print(f"Funcionário {nome} já está de férias.")
        else:
            print(f"Funcionário {nome} não encontrado no sistema.")

    def gerar_escala_mensal(self):
        funcionarios_disponiveis = [f for f in self.funcionarios if f not in self.funcionarios_ferias]
        
        if not funcionarios_disponiveis:
            print("Não há funcionários disponíveis para gerar a escala.")
            return

        hoje = date.today()
        primeiro_dia_mes = date(hoje.year, hoje.month, 1)
        ultimo_dia_mes = date(hoje.year, hoje.month + 1, 1) - timedelta(days=1)
        
        self.escala_atual = {}
        
        dia_atual = primeiro_dia_mes
        while dia_atual <= ultimo_dia_mes:
            funcionario_escolhido = random.choice(funcionarios_disponiveis)
            self.escala_atual[dia_atual.strftime("%Y-%m-%d")] = funcionario_escolhido
            dia_atual += timedelta(days=1)

        print("Nova escala mensal gerada com sucesso.")

    def mostrar_escala(self):
        if not self.escala_atual:
            print("Nenhuma escala gerada ainda.")
            return

        print("Escala de trabalho atual:")
        for data, funcionario in self.escala_atual.items():
            print(f"{data}: {funcionario}")

    def menu(self):
        while True:
            print("\n--- Sistema de Escala de Trabalho ---")
            print("1. Adicionar novo funcionário")
            print("2. Marcar funcionário de férias")
            print("3. Gerar nova escala mensal")
            print("4. Mostrar escala atual")
            print("5. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                nome = input("Digite o nome do novo funcionário: ")
                self.adicionar_funcionario(nome)
            elif opcao == "2":
                nome = input("Digite o nome do funcionário que entrará de férias: ")
                self.marcar_ferias(nome)
            elif opcao == "3":
                self.gerar_escala_mensal()
            elif opcao == "4":
                self.mostrar_escala()
            elif opcao == "5":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Exemplo de uso
if __name__ == "__main__":
    sistema = SistemaEscala()
    sistema.menu()