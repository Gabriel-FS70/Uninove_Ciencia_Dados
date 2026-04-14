import pandas as pd

dados_estoque = {
    'Produto': ['Notebook VAIO', 'Mouse Gamer', 'Monitor 4K', 'Teclado Mecânico', 'Webcam HD'],
    'Preço': [4500, 150, 2800, 450, 300],
    'Quantidade': [5, 50, 2, 15, 8]
}

df_loja = pd.DataFrame(dados_estoque)

filtro_urgente = df_loja[(df_loja['Preço'] > 400) & (df_loja['Quantidade'] < 10)]

print("--- Inventário Completo ---")
print(df_loja)

print("\n--- Alerta de Reposição (Preço > 400 e Estoque < 10) ---")
print(filtro_urgente)