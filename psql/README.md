# Slash commands
* \l - вывод списков всех базы данных
* \c - показывает через какого юзера и к какой базе-д мы подключены
* \с name_of_db - покл.чение к какой-то базе-данных
* \du - список всех юзеров в postges 
* \dt - список всех таблиц в текущей бд
* \d+ - более подробная информация о таблицах в текущей бз
* \d+ name_of_table - более подробная информация о таблице
* \q - выход из субд (psql)


# создание базы-данных и таблиц
```sql
CREATE DATABASE name_of_db;
-- создание бз
```


```sql
CREATE TABLE name_of_tale (
    column1 data_type1,
    column data_type2,
    ...
);
--создание таблицы полями
```

# Удаление бд и таблиц
```sql
DROP DATABASE name_of_db;
--удаление 
```


# Заполнеине таблиц
```sql
INSERT INTO name_of_db VALUES
(val1, val2),
(val1.2, val2.2);
-- запись данных в таблицу (заполнение всех полей)
```


# Вывод данных из таблицы
```sql
SELECT * FROM name_of_table;
--вывод всех записей со всеми полями 
```

```sql
SELECT column1, column3 FROM name_of_table;
-- вывод конкретных полей
```

# Условия
```sql
DELETE FROM name_of_table WHERE codition;
--удаление всех записей из таблиы соответсввующих данному условию
```

```sql
SELECT * FROM name_of _table WHERE column = 'hello';
--сторогое равенство
```


```sql
SELECT * FROM name_of_table WHERE column LIKE '%hello%';
--записи влючающие в себя данную строку с учетом регистра
--aaahello
--hello
--hello world
--Hello World - не продут (потому что регистр другой)
```


```sql
--записи влючающие в себя данную строку с учетом регистра
--aaahello
--hello
--hello world
--Hello World - пройдет потому что ILIKE не учитывает регистр 
--HELLO
```

```sql
SELECT * FROM name_of_table ORDER BY column;
--сортировка записей по данному полю в порядке возростания 
```


```sql
SELECT * FROM name_of_table ORDER BY column DESC;
--сортировка записей по данному полю в порядке убывания
```

```sql
SELECT * FROM name_of_table LIMIT 10(любое число);
--вывод до определенного числа (или же до 10) 
```


```sql
SELECT * FROM name_of_table OFFSET 10(любое число);
--пропускаем до определенного числа (или же до 10) 
```


```sql
SELECT * FROM name_of_table LIMIT 10 OFFSET 5;
--пропускаем первые 5 записей 
--вытаскиваем 10 записей после 5
```

# Обновление таблицы
```sql
ALTER TABLE name_of_table ADD COLUMN col_name col_type constraint;
-- добавляем новую колонку в таблицу
 ```

 ```sql
 ALTER TABLE name_of_table RENAME COLUMN col_name TO new_col_name;
 --переименнование колонки
```

```sql
ALTER TABLE name_of_table ALTER COLUMN col_name SET DATA TYPE new_type;
--изменение типа данных у поля 
```



# Ограничения (counstrints)
* UNIQUE - не разрешает дубликаты 
* NOT NULL - требует обязательного заполнения поля 
* PRIMERY KEY - как UNIQUE и  NOT NULL + строит binary tree для быстрого поиска 
* FOREIGN KEY - ссылается на pk в другой таблице и проверяет существует ли такой ID 



# Связи 
## Виды связей
> Один к одному (one to one)
* один человек - один профиль 
* один автор - одна автобиография 

> Один ко многим (one to many)
* один блогер - много постов 
* одна марка - много моделей
* одна страна - много областей

> Многие ко многим (many to many)
* один разработчик - много проектов. один проект - много разрабов 



task
'3'
SELECT title, genretype FROM work WHERE genretype = 'p';



## Реализация one2many в postgres
```sql
CREATE TABLE blogger (
    id serial PRIMARY KEY,
    title varchar(100)
    body text,
    blogger_id int,

    CONSTRAINT fk_post-blogger 
    FOREIGN KEY (blogger_id) REFERENCES blogger (id)
    );
```

# JOINS
> **JOIN** - инструкция, которая позваляет одним SELECT, брать данные из двух таблиц (у которых есть связанные поля)
>**INNER JOIN (JOIN)** - достаются записи у которых есть данные в обоих таблицах
>**FULL JOIN** - достаются все записи и с первой таблицы и со второй 


# Арегатные функции 
> все агрегатые функции исползуются с 'group by'
**SUM** -  считает сумму все записей в сгрупированном поле 



```sql
select customer.name, SUM(product.price) from customer 
join cart on customer.id = cart.customer_id
join product on product.id = cart.product_id 
group by (customer.id);
```

>**AVG** - считает среднее значение всех записец в сгруппированном поле 

```sql
select customer.name, AVG(product.price) from customer 
join cart on customer.id = cart.customer_id
join product on product.id = cart.product_id 
group by (customer.id);
```