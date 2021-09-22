# Routing
Repositório criado para armazenar códigos que tem como função consultar rotas utilizando API Bing. Esses scripts foram elaborados pela necessidade de validação de instalações de fibras em clientes das quais não poderiam ultrapassar uma determinada metragem. Tal funcionalidade foi utilizada para realizar auditoria de materiais utilizados nas intalações (Material Previsto x Material Aplicado informado pelos técnicos).

## ONE_ROUTE.py

Conta com uma interface um pouco mais elaborada que a elaborada no Geocoder, contando com campos a serem preenchidos com as coordenadas decimais do ponto de início e destino. Basicamente é uma calculadora de rotas.

![print_one_route](https://github.com/sergiusfelipe/Imagens/blob/main/Anota%C3%A7%C3%A3o%202021-09-22%201507319.png)

Por padrão, é configurado para consultar rodas a pé, indiferente no que diz a sentido das vias. mas há a possivilidade de mudar essa configuração, seguindo a documentação da [API Rest](https://docs.microsoft.com/en-us/bingmaps/rest-services/routes/calculate-a-route?redirectedfrom=MSDN).

```python
BASE_URL = 'http://dev.virtualearth.net/REST/v%s/' % version
self.BASE_URL = BASE_URL
self.routes_url = BASE_URL + 'Routes/Walking'
```
