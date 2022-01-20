from time import sleep
import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import URL

usuario_facebook = input("Digite o nome de usuário: ")
senha = getpass.getpass("Digite sua senha:")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
print("--Abrindo Facebook--")
sleep(2)

campo_usuario = driver.find_element_by_id('email')
campo_usuario.send_keys(usuario_facebook)

campo_senha = driver.find_element_by_id('pass')
campo_senha.send_keys(senha)

print('--Inserindo senha--')

botao_login = driver.find_element_by_name('login')
botao_login.click()

print('--Completando o acesso--')
input('--Pressione uma tecla para sair--')
driver.quit()
print('--Teste finalizado--')