from datetime import date


class Paciente:

    def __init__(self, paciente_nome, paciente_cpf):
        self.paciente_nome = ""
        self.paciente_cpf = ""


class Receita:

    def __init__(self, dados_paciente: dict, dados_medicamento: dict):
        self.paciente_nome = dados_paciente["nome"]
        self.paciente_cpf = dados_paciente["cpf"]
        self.receita_numero = dados_medicamento["numero"]
        self.receita_status = dados_medicamento["status"]
        self.medicamento_nome = dados_medicamento["medicamento"]
        self.medicamento_quantidade = dados_medicamento["quantidade"]
        self.medicamento_validade = dados_medicamento["validade"]


nome, cpf = "Aurelio Soares", "956.021.270-20"
paciente = Paciente(nome, cpf)
receita = Receita(dict(nome=nome, cpf=cpf), dict(numero="123",
                                                 status="Receita Nova",
                                                 medicamento="paracetamol",
                                                 quantidade=15,
                                                 validade="25/04/2021"))


class Farmaceutico:

    def dispensar_medicamento(self, receita: Receita):
        if not self.validar_receita(receita):
            print("FALHA NA VALIDAÇÃO DA RECEITA")
        elif not self.verificar_estoque_medicamento(receita):
            print("FALHA NA ETAPA DE ESTOQUE")
        else:
            self.finalizar_dispensa_medicamento(receita)
            print("Dispensa realizada com sucesso!")

    # CHAMADA POR dispensar_medicamento()
    def validar_receita(self, receita: Receita):
        if not self.validar_paciente_cpf_nome(receita.paciente_cpf, receita.paciente_nome):
            print("CPF ou Nome do paciente não conferem.")
        elif not self.validar_status_receita(receita.receita_status):
            print("Receita já utilizada ou cancelada")
        # elif not self.validar_validade_receita(receita.medicamento_validade):
        #     print("Receita fora de validade")
        elif not self.validar_nome_medicamento(receita.medicamento_nome):
            print("Nome do medicamento inexistente ou digitado incorretamente.")
        else:
            return True
        return False

    # CHAMADA POR dispensar_medicamento()
    def verificar_estoque_medicamento(self, receita: Receita):
        medicamento = receita.medicamento_nome
        quantidade = receita.medicamento_quantidade

        with open("DB_Estoque.txt") as f:
            medicamentos_cadastrados = f.readlines()
        for cad_medicamento in medicamentos_cadastrados:
            cad_medicamento = cad_medicamento.split(";")
            if medicamento == cad_medicamento[1] and quantidade <= int(cad_medicamento[2]):
                return True
        else:
            print("Quantidade de medicamento insuficiente no estoque.")
            return False

    def finalizar_dispensa_medicamento(self, receita):
        self.mudar_status_receita(receita)
        self.computar_saida_medicamento_stoque(receita)

    # CHAMADA POR finalizar_dispensa_medicamento()
    def mudar_status_receita(self, receita: Receita):
        receita.receita_status = "Receita usada"
        pass

    # CHAMADA POR finalizar_dispensa_medicamento()
    def computar_saida_medicamento_stoque(self, receita: Receita):
        medicamento = receita.medicamento_nome
        quantidade = receita.medicamento_quantidade

        with open("DB_Estoque.txt") as f:
            medicamentos_cadastrados = f.readlines()

        for linha in range(len(medicamentos_cadastrados)):
            cad_medicamento = medicamentos_cadastrados[linha].strip().split(";")
            novo_total_medicamentos = int(cad_medicamento[2]) - quantidade
            cad_medicamento[2] = str(novo_total_medicamentos)+"\n"
            medicamentos_cadastrados[linha] = ";".join(cad_medicamento)
            break
        with open("DB_Estoque.txt", "w") as f:
            f.write("".join(medicamentos_cadastrados))

    # CHAMADA POR validar_receita()
    def validar_paciente_cpf_nome(self, cpf: str, nome: str):
        with open("DB_cpf.txt") as f:
            cpfs_cadastrados = f.readlines()
        for pessoa in cpfs_cadastrados:
            pessoa = pessoa.strip().split(";")
            if cpf == pessoa[0] and nome == pessoa[1]:
                return True
        return False

    # CHAMADA POR validar_receita()
    def validar_status_receita(self, status):
        if status == "Receita Nova":
            return True
        return False

    # CHAMADA POR validar_receita()
    # def validar_validade_receita(self, validade):
    #     hoje = (date.today().strftime("%d/%m/%Y")
    #     if xxxxxxxxxxxxxxxxxx

    # CHAMADA POR validar_receita()
    def validar_nome_medicamento(self, medicamento: str):
        medicamento = receita.medicamento_nome

        with open("DB_Estoque.txt") as f:
            medicamentos_cadastrados = f.readlines()
        for cad_medicamento in medicamentos_cadastrados:
            cad_medicamento = cad_medicamento.split(";")
            if medicamento == cad_medicamento[1]:
                return True
        return False

farmaceuticoYuri = Farmaceutico()
farmaceuticoYuri.dispensar_medicamento(receita)
