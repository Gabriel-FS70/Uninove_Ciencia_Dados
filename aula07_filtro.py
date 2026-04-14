import pandas as pd

dados = {
    'Nome': ['Arthur', 'Ana', 'Beatriz', 'Afonso', 'Caio', 'Aline'],
    'Idade': [21, 19, 23, 20, 22, 18],
    'Curso': ['História', 'História', 'História', 'História', 'História', 'História']
}

df = pd.DataFrame(dados)

filtro_letra_a = df[df['Nome'].str.contains('^A')]

print("--- Lista Completa de Alunos ---")
print(df)

print("\n--- Alunos que começam com a letra 'A' ---")
print(filtro_letra_a)