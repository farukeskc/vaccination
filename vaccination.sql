SET daily_vaccinations = (
  SELECT vaccination_median
  FROM (
    SELECT country, MEDIAN(daily_vaccinations) OVER (PARTITION BY country) AS vaccination_median
    FROM vaccination_data
    WHERE daily_vaccinations IS NOT NULL
  ) tbl
  WHERE tbl.country = vaccination_data.country
)
WHERE daily_vaccinations IS NULL;