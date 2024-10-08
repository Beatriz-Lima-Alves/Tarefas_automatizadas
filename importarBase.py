import pyautogui
import time
import pandas
# Entrar no sistema
pyautogui.PAUSE = 1
# Abri navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# Pausar por 3 segundos
time.sleep(2)

# Fazer login
pyautogui.click(x=515, y=376)
pyautogui.write("teste@gmail.com")

pyautogui.press("tab")
pyautogui.write("teste senha")

# Clicar no botão de entrar para logar
pyautogui.click(x=686, y=530)
time.sleep(2)

# Importar a base de dados
tabela = pandas.read_csv('produtos.csv')

linha = 0

for linha in tabela.index:
    pyautogui.click(x=634, y=258)
    # código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")


    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)