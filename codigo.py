import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv("produtos.csv")

#Passo 1 Abrir a página
# 1.a. Abrir o chrome
pyautogui.press('win')  
pyautogui.write('firefox')
pyautogui.press('enter')
time.sleep(2)

#1.b. Digitar e abrir o site
pyautogui.click(x=546, y=96)
pyautogui.write(site)
pyautogui.press('enter')
time.sleep(3)

# Passo2: Fazer login
pyautogui.click(x=410, y=403)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") 
pyautogui.write("sua senha")
pyautogui.press('enter')
time.sleep(3)


# Passo 3: Importar a base de produtos

print(tabela)


# Passo 4: cadastrar produto

for linha in tabela.index:
    pyautogui.click(x=937, y=291)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)

    marca = tabela.loc[linha, 'marca']
    pyautogui.press('tab')
    pyautogui.write(marca)

    tipo = tabela.loc[linha,'tipo']
    pyautogui.press("tab") 
    pyautogui.write(tipo)

    categoria = str(tabela.loc[linha,'categoria'])
    pyautogui.press('tab')
    pyautogui.write(categoria)

    preco_unitario = str(tabela.loc[linha,'preco_unitario'])
    pyautogui.press('tab')
    pyautogui.write(preco_unitario)

    custo = str(tabela.loc[linha,'custo'])
    pyautogui.press('tab')
    pyautogui.write(custo)

    obs = str(tabela.loc[linha,'obs'])
    pyautogui.press('tab')
    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('home')

