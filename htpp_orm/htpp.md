# Ptorocols
> **HTPP** - Hyper Text Transfer Protocol. Протокол, который построен на протоколах **TCP/IP**

> **HTPPS** - более новая версия HTPP, где появилась шифрование и SSL сертификаты


## HTPP methods 
* **GET** - метод для получения даннных 
* **POST** - отправка данных 
* **PUT** - полное обновление или создание 
* **PATCH** - частичное обновление 
* **DELETE** - удаление 
* TRACE - трассировка (проверка связи)
* HEAD - получение headers для запроса 
* OPTIONS - получение списка методов на данныю url
 

 # Status Code 
 * 1xx - иформационные 
 * 2xx - успешные
 * 3хх - перенаправление 
 * 4хх - ошибки клиента
 * 5хх - ошибки сервера 

# URL 
> Unifirm resours locator `http://www.google.com/search?q=eminem`

> **DOMAIN** - уникальное название к которому прикреплен определенный сервер (ip adres) `www.google.com`

> **URI** - подпуть `/search`

> **Query Params** - пары ключ=значение иду  псоле ? `q=hello`