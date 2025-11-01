-- 코드를 입력하세요
SELECT b.ANIMAL_ID, b.NAME
from animal_outs b
left join animal_ins a
on a.animal_id = b.animal_id
where a.name is null and b.name is not null
order by b.animal_id;