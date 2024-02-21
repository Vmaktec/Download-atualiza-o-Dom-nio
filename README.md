# README

## Descrição
Este repositório contém um script em Python que automatiza o processo de download de arquivos de uma determinada URL utilizando a biblioteca Selenium. O script foi desenvolvido para baixar arquivos de atualização do sistema contábil hospedado no site "https://download.dominiosistemas.com.br/atualizacao/contabil/".

## Requisitos
- Python
- Selenium
- Chrome WebDriver
- ChromeDriverManager




## Instalação
1. Clone este repositório em sua máquina local usando o comando:
git clone https://github.com/Vmaktec/Download-atualiza-o-Dom-nio

2. Instale as dependências usando o pip:
pip install selenium webdriver_manager




## Configuração
- Defina o caminho para a pasta de download na variável `download_folder`. Por padrão, os arquivos serão baixados no diretório Downloads caso não seja alterado.
- Certifique-se de ter o Google Chrome instalado em sua máquina.




## Utilização
1. Execute o script Python `juntos.py`.
python juntos.py

2. O script abrirá uma instância do Google Chrome automaticamente e acessará a URL especificada.
3. Ele clicará nos links relevantes para iniciar o download dos arquivos de atualização.
4. Os arquivos serão baixados em Downloads ou na pasta configurada em `download_folder`.





## Observações
- Certifique-se de que a versão do ChromeDriver corresponde à versão do Google Chrome instalada em sua máquina.
- O script foi projetado para baixar arquivos específicos da URL fornecida. Modificações podem ser necessárias para adaptá-lo a outras URLs ou requisitos específicos.
- Se desejar adicionar uma pausa antes de fechar o navegador, descomente a linha `input("Pressione Enter para sair...")`. Isso permitirá que você veja o navegador antes de fechar.

## Autores
Este script foi desenvolvido por [Victor Altenhofen](https://github.com/Vmaktec).

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request para propor melhorias ou correções.
