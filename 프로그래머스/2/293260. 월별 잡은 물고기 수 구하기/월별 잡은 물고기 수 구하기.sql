select 
count(*) as FISH_COUNT, 
MONTH(TIME) as MONTH
from fish_info
group by month
order by month asc;
