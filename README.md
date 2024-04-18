## Sistema Simples de Gerenciamento de Clientes

Este é um script Python que implementa um sistema simples de gerenciamento de clientes por meio de um menu interativo.

### Funcionalidades

- **Adicionar Cliente**: Permite adicionar um novo cliente ao sistema, solicitando nome, email e telefone.
- **Visualizar Clientes**: Mostra uma lista de todos os clientes cadastrados.
- **Buscar Cliente pelo Nome**: Permite buscar um cliente específico pelo nome.
- **Encerrar o Programa**: Finaliza a execução do programa.

![Exercicio3ExcutandoPyton](https://github.com/AntonioNeto504/Aplica-oCadastroCliente_ArquivoCSV_Py/assets/143558933/18deb40d-7024-48f6-b6e6-af6c04cc8ed7)
## Execução do Docker

1. Certifique-se de ter o Docker instalado em seu sistema. Você pode baixá-lo e instalá-lo a partir do site oficial do Docker.
2. Abra o terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo Dockerfile está localizado, o qual deve ser o mesmo diretório onde o seu script PowerShell está localizado.
4. Execute o comando `docker build -t nome-da-imagem .`, substituindo "nome-da-imagem" pelo nome que você deseja dar à sua imagem Docker. Este comando construirá a imagem Docker usando as instruções do seu Dockerfile. Certifique-se de incluir o ponto `.` no final para indicar que o Dockerfile está no diretório atual.
5. Após a construção da imagem, você pode executar um contêiner Docker usando o comando `docker run`. Por exemplo, se você quiser executar um contêiner interativo a partir da imagem que acabou de criar, você pode usar o comando `docker run -it nome-da-imagem`.


 seu Dockerfile e seu script PowerShell estão configurados corretamente para serem executados em um contêiner Docker. Você pode precisar ajustar algumas configurações dependendo do que seu script faz e dos requisitos do seu ambiente Docker.

Certifique-se de que![CodigocsvRodando](https://github.com/AntonioNeto504/Aplica-oCadastroCliente_ArquivoCSV_Py/assets/143558933/cfe3bab0-2e97-4846-9a91-60bde62f95f8)


Obs: O docker não possui nenhuma interação para com caminhos de pasta, logo o código dara erro caso não haja a configuração de caminhos adquados para rodar num conteiner
