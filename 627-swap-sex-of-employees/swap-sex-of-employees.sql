# Write your MySQL query statement below
update salary s
set s.sex=case 
when s.sex='f' then 'm' 
when s.sex='m' then 'f'
else sex
end