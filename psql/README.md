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