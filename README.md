A RESTful Service to provide the basic bank details.

- To Register a New User:

    curl -X POST -d "username=<username>&password=<password>" https://hk-bank-api-service.herokuapp.com/api/register

- To Generate a Token:

    curl -X POST -d "username=<username>&password=<password>" https://hk-bank-api-service.herokuapp.com/api/token/


- To Refresh Token:

    curl -X POST -H "Content-Type: application/json" -d '{"refresh":"<Refresh Token>"}' https://hk-bank-api-service.herokuapp.com/api/refresh/



- To Get Bank Details for given IFSC:

    curl -H "Authorization: Bearer <Access Token>" "https://hk-bank-api-service.herokuapp.com/api/getBankDetails/?ifsc=<ifsc>"



- To Get Bank Details for given name & city (Default Pagination Size : 1):

    curl -H "Authorization: Bearer <Access Token>" "https://hk-bank-api-service.herokuapp.com/api/getBankDetails/?city=<city>&name=<name>"


    - To add limit & offset.

    curl -H "Authorization: Bearer <Access Token>" "https://hk-bank-api-service.herokuapp.com/api/getBankDetails/?city=<city>&name=<name>&limit=<limit>&offset=<offset>"
