##Processos a ser executados e o como foram executados.

1.	Fazer a modelagem conceitual dos dados;
2.	Criação da infraestrutura necessária;
3.	Criação de todos os artefatos necessários para carregar os arquivos para o banco criado;
4.	Desenvolvimento de SCRIPT para análise de dados;
5.	(opcional) Criar um relatório em qualquer ferramenta de visualização de dados.


- 1 - Utilizando um jupyter notebook fiz a checagem dos 
  tipos de dados pelo csv para me auxiliar a verificar os schemas para
  as colunas
  
- 2 - Baseado nas informações, e algumas deduções(pois nao tive acesso ao dicionario de dados) rodei o script create_table_mysql

- 3 - Foram Criados os seguintes arquivos para efetuar a carga
    - 01-insert_person_table
    - 02 - insert_customer_table
    - 03 - insert_sales_order_header_table
    - 04 - insert_sales_order_detail_table
    - 05 - insert_special_offer_product_table
    - 06 - insert_product_table
  
- 4 Os seguintes arquivos foram criados para inicio de limpeza dos dados, neles foi limpo os campos NaN 
  em caso onde foi possivel, pois em alguns datasets(CSV) se fosse limpo, iria ficar vazio
   - Customer.ipynb
   - Person.ipynb
   - Product.ipynb
   - Sales_Order_Detail.ipynb
   - Sales_Order_Header.ipynb
   - Sales_Special_Offer.ipynb
  
- 5 O repositório criado esta no endereco https://github.com/serpaulos/rox-project
    - a branch datafactory foi usada para colocar os dados
    - no datafactory criei as estrutura para pegar o conteudo de arquivo csv e gravar no banco de dados criado previamente
  