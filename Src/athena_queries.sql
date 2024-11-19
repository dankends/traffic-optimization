-- Create Database
CREATE DATABASE IF NOT EXISTS traffic_data_analysis;

-- Create Table for Processed Traffic Data
CREATE EXTERNAL TABLE IF NOT EXISTS traffic_data_analysis.traffic_data (
    traffic_light_id STRING,
    timestamp BIGINT,
    vehicle_count INT,
    average_speed INT,
    CO2_level FLOAT,
    high_traffic BOOLEAN
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://your-bucket-name/processed-data/';

-- Query: Average CO2 level by traffic light location
SELECT traffic_light_id, AVG(CO2_level) AS avg_CO2
FROM traffic_data_analysis.traffic_data
GROUP BY traffic_light_id;

-- Query: Identify top high-traffic locations
SELECT traffic_light_id, COUNT(*) AS high_traffic_count
FROM traffic_data_analysis.traffic_data
WHERE high_traffic = true
GROUP BY traffic_light_id
ORDER BY high_traffic_count DESC
LIMIT 5;

-- Query: Analyze average speed by traffic light and time period
SELECT traffic_light_id, AVG(average_speed) AS avg_speed, DATE_FROM_UNIX_TIMESTAMP(timestamp) AS date
FROM traffic_data_analysis.traffic_data
GROUP BY traffic_light_id, date;
