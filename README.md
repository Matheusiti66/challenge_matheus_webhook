#  Challenge Matheus - WEBHOOK


#### Serviço responsável pelo recebimento via WEBHOOK das faturas pagas no banco StarkBank e transferência dos valores com desconto das taxas

## Funcionalidades do projeto

 * Funções - core/services arquivo starkbank.py
    - calculate_tax: Responsável pelo calculo das taxas inclusas no valor original da transferência
    - send_transfer: Responsável pela transferência do valor pago - taxas

* arquivo server.py
    - Local onde é gerado o servidor flask + ngrok e a rota WebHook

## :hammer: Instalação e execução

 *  Criação do .env com parâmetros necessários para execução
    - private_key;
    - project_id.

    usar .env_example