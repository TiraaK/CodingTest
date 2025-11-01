-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.NAME
from animal_ins a
left join animal_outs b
on a.animal_id = b.animal_id
where a.datetime > b.datetime
order by a.datetime asc;