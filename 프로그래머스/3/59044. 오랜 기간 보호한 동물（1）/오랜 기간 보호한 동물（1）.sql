-- 코드를 입력하세요
SELECT a.NAME, a.DATETIME
from animal_ins a
left join animal_outs b
on a.ANIMAL_ID = b.ANIMAL_ID
where b.NAME is null and a.NAME is not null
order by a.datetime asc
limit 3;