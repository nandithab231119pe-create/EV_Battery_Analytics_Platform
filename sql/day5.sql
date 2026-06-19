SELECT e.brand,
       COUNT(*) AS models
FROM ev_specs e
INNER JOIN charging_specs c
ON e.brand = c.brand
GROUP BY e.brand
ORDER BY models DESC;

SELECT e.brand,
       e.model,
       c.charging_category
FROM ev_specs e
LEFT JOIN charging_specs c
ON e.brand = c.brand;

SELECT c.charging_category,
       COUNT(*) AS total_models
FROM ev_specs e
INNER JOIN charging_specs c
ON e.brand = c.brand
GROUP BY c.charging_category
ORDER BY total_models DESC;

SELECT c.charging_category,
       ROUND(AVG(e.range_km)::numeric,2) AS avg_range
FROM ev_specs e
INNER JOIN charging_specs c
ON e.brand = c.brand
GROUP BY c.charging_category
ORDER BY avg_range DESC;

SELECT brand,
       model,
       range_km,
       ROW_NUMBER() OVER(
           ORDER BY range_km DESC
       ) AS row_num
FROM ev_specs;
select* 
from (
     SELECT brand,
       model,
       battery_capacity_kwh,
       RANK() OVER(
           ORDER BY battery_capacity_kwh DESC
       ) AS battery_rank FROM ev_specs) t where t.battery_rank <=10;

select * from (	   
	   SELECT brand,
       model,
       efficiency_wh_per_km,
       DENSE_RANK() OVER(
           ORDER BY efficiency_wh_per_km ASC
       ) AS efficiency_rank
FROM ev_specs) t where t.efficiency_rank =1;