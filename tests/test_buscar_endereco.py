import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.buscar_endereco import PaginaBuscaEndereco

@pytest.fixture
def navegador():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    yield navegador
    navegador.close()
    navegador.quit()

def test_buscar_endereco_por_cep(navegador):
    cep = '08247060'
    pagina_busca = PaginaBuscaEndereco(navegador)
    pagina_busca.carregar()
    pagina_busca.buscar_pelo_cep(cep)
    time.sleep(0.5)
    pagina_busca.clicar_botao()
    time.sleep(2)
    endereco = pagina_busca.obter_resultado_endereco()
    bairro = pagina_busca.obter_resultado_bairro()
    cidade = pagina_busca.obter_resultado_cidade()
    assert 'Rua Amanari' == endereco
    assert 'Vila Santa Teresinha' == bairro
    assert 'São Paulo/SP' == cidade