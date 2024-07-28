-- queries.sql

[default_query]
SELECT * FROM data LIMIT {limit};

[another_query]
select * from data where Date > "2024-05-18" and Promotion is null order by date desc;

[second_query]
select transaction_id, date, product from data limit 10;