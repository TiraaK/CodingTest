
select YEAR(a.DIFFERENTIATION_DATE) as YEAR, b.yr_max - a.size_of_colony as YEAR_DEV, a.ID 
from ecoli_data as a
join (
    select max(size_of_colony) as yr_max, YEAR(DIFFERENTIATION_DATE) as YEAR
    from ecoli_data
    group by YEAR
) as b 
on YEAR(a.DIFFERENTIATION_DATE) = b.YEAR
order by YEAR asc, YEAR_DEV asc;