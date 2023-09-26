# Passos do projeto
import pandas
import pyautogui

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> para escrever
# pyautogui.press -> aperta 1 tecla
# pyautogui.press("win")
# pyautogui.hotkey -> combinação de tecla5

import time

pyautogui.PAUSE = 0.5  # adiciona uma pausa de 0,2 segundos entre cada ação
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# 1: Entrar no sistema
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# adiciona uma pausa unica de X segundos para aguardar o navegador abrir
time.sleep(5)

# entrar no link
pyautogui.write(link)
pyautogui.press("enter")

# aguardar site carregar
# adiciona uma pausa unica de 3 segundos para aguardar o site abrir
time.sleep(3)

# 2: Logar no sistema
# pyautogui.click(x=649, y=544)
pyautogui.press("tab")
pyautogui.write("emailteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("enter")

# 3: Importar base de dados dos produtos

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# 4: Cadastrar 1 produto

# inserir dados nos campos
for linha in tabela.index:
    # clicar na primeira linha do cadastro
    pyautogui.click(x=526, y=435)
    
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    
    if not pandas.isna(obs) :
        pyautogui.write(str(obs))

    # enviar formulario
    pyautogui.press("tab")
    pyautogui.press("enter")

    # voltar para o topo da pagina
    pyautogui.scroll(10000)

# 5: Repetir o cadastro para todos os produtos
