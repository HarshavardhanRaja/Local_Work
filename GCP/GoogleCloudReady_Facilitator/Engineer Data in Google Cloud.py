
# https://chriskyfung.github.io/blog/qwiklabs/Engineer-Data-in-Google-Cloud-Challenge-Lab

# Task 1: Clean your training data

"""
Select
  pickup_datetime,
  pickup_longitude AS pickuplon,
  pickup_latitude AS pickuplat,
  dropoff_longitude AS dropofflon,
  dropoff_latitude AS dropofflat,
  passenger_count AS passengers,
  ( tolls_amount + fare_amount ) AS fare_amount
FROM
  `taxirides.historical_taxi_rides_raw`
WHERE
  trip_distance > 0
  AND fare_amount >= 2.5
  AND pickup_longitude > -75
  AND pickup_longitude < -73
  AND dropoff_longitude > -75
  AND dropoff_longitude < -73
  AND pickup_latitude > 40
  AND pickup_latitude < 42
  AND dropoff_latitude > 40
  AND dropoff_latitude < 42
  AND passenger_count > 0
  AND RAND() < 999999 / 1031673361
"""
# save the results in a destination table with name taxi_training_data




# Task 2: Create a BQML model called taxirides.fare_model
"""
CREATE or REPLACE MODEL
  taxirides.fare_model OPTIONS (model_type='linear_reg',
    labels=['fare_amount']) AS
WITH
  taxitrips AS (
  SELECT
    *,
    ST_Distance(ST_GeogPoint(pickuplon, pickuplat), ST_GeogPoint(dropofflon, dropofflat)) AS euclidean
  FROM
    `taxirides.taxi_training_data` )
  SELECT
    *
  FROM
    taxitrips




#Evaluate model performance
#standardSQL
SELECT
  SQRT(mean_squared_error) AS rmse
FROM
  ML.EVALUATE(MODEL taxirides.fare_model,
    (
    WITH
      taxitrips AS (
      SELECT
        *,
        ST_Distance(ST_GeogPoint(pickuplon, pickuplat), ST_GeogPoint(dropofflon, dropofflat)) AS euclidean
      FROM
        `taxirides.taxi_training_data` )
      SELECT
        *
      FROM
        taxitrips ))

"""





# Task 3: Perform a batch prediction on new data
"""
store your results in a table called 2015_fare_amount_predictions




"""
