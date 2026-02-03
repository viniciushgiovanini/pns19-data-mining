import pandas as pd

from lib.utils import load_variables


class Explorer:
    def __init__(self, excel_path: str):
        self.excel_path = excel_path
        self.my_variables = {
            "C": [],
            "D": [],
            "F": [],
            "I": [],
            "J": [],
            "P": [],
            "Q": [],
        }
        self.df = self.read_df_preprocess(excel_path)
        self.load_variables()
        self.df = self.__rename_header(self.df)

    def read_df_preprocess(self, excel_path: str) -> pd.DataFrame:
        df = pd.read_excel(excel_path, skiprows=1)
        df = df.drop_duplicates().dropna(axis=0)
        df = self.__rename_header(df)
        df = self.__filter_per_module(df)
        return df

    def __rename_header(self, df: pd.DataFrame) -> pd.DataFrame:
        new_columns = {
            "Código\nda\nvariável": "Código da Váriavel",
            "Unnamed: 4": "Quesito - Descrição",
            "Quesito": "Quesito - N°",
            "Categorias": "Categorias - Tipo",
            "Unnamed: 6": "Categorias - Descrição",
        }
        return df.rename(columns=new_columns)

    def __filter_per_module(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[
            df["Quesito - N°"].str.startswith(
                ("C", "D", "F", "I", "J", "P", "Q")
            )
        ]

    def load_variables(self, pickle_path: str = ""):
        if pickle_path:
            self.my_variables = load_variables(pickle_path)
        else:
            for row in self.df.itertuples():
                index_atr = row[3]
                self.my_variables[index_atr[0]].append((index_atr))

    def print_module_len(self):
        total = 0
        for mod, values in self.my_variables.items():
            print(f"Modulo: {mod} tem {len(values)} atributos")
            total += len(values)
        print(f"Total: {total}")

    def print_variables_per_module(self):
        for mod, values in self.my_variables.items():
            print(f"Modulo: {mod}\n")
            for each in values:
                variable = self.df[self.df["Código da Váriavel"] == each]
                if not variable.empty:
                    print(variable["Quesito - Descrição"].iloc[0], end="")
                    print(
                        " | "
                        + str(variable["Código da Váriavel"].iloc[0])
                        + "\n"
                    )
            print("\n ---X--- \n")

    def __clean_my_variables(self):
        for k, _ in self.my_variables.items():
            self.my_variables[k] = []

    def add_variables_by_description(self, descriptions: list[str]):
        self.__clean_my_variables()

        for desc in descriptions:

            variable_row = self.df[self.df["Quesito - Descrição"] == desc]

            if variable_row.empty:
                print(f"Descrição não encontrada: {desc}")
                continue

            code = variable_row["Código da Váriavel"].iloc[0]

            module = code[0]

            if module in self.my_variables:
                if code not in self.my_variables[module]:
                    self.my_variables[module].append(code)
            else:
                self.my_variables[module] = [code]

        print("Variáveis adicionadas com sucesso!")
