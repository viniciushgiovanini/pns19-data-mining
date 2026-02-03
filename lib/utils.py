import pickle


def save_variables(file_name: str, variable: str):
    with open(file_name, "wb") as arquivo:
        pickle.dump(variable, arquivo)


def load_variables(file_name: str) -> object | None:
    dados_carregados = None
    with open(file_name, "rb") as arquivo:
        dados_carregados = pickle.load(arquivo)
    return dados_carregados
