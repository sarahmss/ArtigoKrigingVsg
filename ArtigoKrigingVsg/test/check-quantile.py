import numpy as np
import pandas as pd

df_training = pd.read_excel("Kriging-data.xlsx", sheet_name="Training")

# Lista de métodos de interpolação
methods = [
    'inverted_cdf',
    'averaged_inverted_cdf',
    'closest_observation',
    'interpolated_inverted_cdf',
    'hazen',
    'weibull',
    'linear',
    'median_unbiased',
    'normal_unbiased'
]

# Quantis calculados no MATLAB
Q_x1 = [0.02450, 0.20350, 0.37820, 0.52330, 0.9547750]
Q_x2 = [0.07720, 0.40300, 0.58605, 0.81130, 0.98230]

# Dados de exemplo para df_training (carregar seu dataframe real)
# df_training = pd.read_excel("Kriging-data.xlsx", sheet_name="Training")

# Quantis a serem calculados
quantiles = [0.025, 0.25, 0.5, 0.75, 0.975]

# Inicializar variáveis para armazenar o melhor método e menor erro
best_method = None
lowest_error = float('inf')

for m in methods:
    print(f"Method: {m}")

    # Calcular os quantis para x1 e x2 usando o método de interpolação atual
    Qx1_method = np.quantile(df_training['x1'], quantiles, method=m)
    Qx2_method = np.quantile(df_training['x2'], quantiles, method=m)

    # Calcular o erro absoluto médio para x1 e x2
    error_x1 = np.mean(np.abs(Qx1_method - Q_x1))
    error_x2 = np.mean(np.abs(Qx2_method - Q_x2))
    
    # Calcular o erro total para ambos x1 e x2
    total_error = (error_x1 + error_x2) / 2

    # Printa os quantis e o erro
    print("Q(x1)", Qx1_method)
    print("Q(x2)", Qx2_method)
    print(f"Mean Absolute Error (x1): {error_x1}")
    print(f"Mean Absolute Error (x2): {error_x2}")
    print(f"Total Mean Absolute Error: {total_error}")
    print()

    # Atualizar o melhor método se o erro total for menor
    if total_error < lowest_error:
        lowest_error = total_error
        best_method = m

# Printar o melhor método encontrado
print(f"The best interpolation method is: {best_method} with a total error of {lowest_error}")
