from selenium.webdriver.common.by import By
class PaginaBuscaEndereco:
    URL = 'https://buscacepinter.correios.com.br/app/endereco/index.php'
    def __init__(self, navegador):
        self.navegador = navegador

    def carregar(self):
        self.navegador.get(self.URL)
        

    def buscar_pelo_cep(self, cep):
        campo_de_input = self.navegador.find_element(By.ID, 'endereco')
        campo_de_input.send_keys(cep)
        

    def clicar_botao(self):
        btn = self.navegador.find_element(By.XPATH, "//button[text()='Buscar']")
        btn.click()
    
    def obter_resultado_endereco(self):
        return self.navegador.find_element(By.XPATH, ".//tbody/tr[1]/td[1]").text
    
    def obter_resultado_bairro(self):
        return self.navegador.find_element(By.XPATH, ".//tbody/tr[1]/td[2]").text

    def obter_resultado_cidade(self):
        return self.navegador.find_element(By.XPATH, ".//tbody/tr[1]/td[3]").text
        