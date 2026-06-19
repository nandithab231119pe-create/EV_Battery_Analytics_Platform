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