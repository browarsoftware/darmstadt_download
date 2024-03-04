# Traffic data

Traffic data from [Darmstadt opendata](https://datenplattform.darmstadt.de/verkehr/apps/opendata/#/) service stored in CSV file format.
Data is from 2024-01-06 1:00 AM to 2024-03-04 1:00 AM.

## Description

(translation from website [Darmstadt opendata](https://datenplattform.darmstadt.de/verkehr/apps/opendata/#/)):

The times are in local time. In addition, the traffic count values of the individual intersections via the sensor configuration plan (JSON, common for all traffic light systems) to the specific sensors. For example, D1Z stands for the number of vehicles  vehicles measured by the sensor with the number 1 of the selected intersection and D1B for the percentage of time that the sensor detected vehicles. the sensor has detected vehicles. The exact location of the of the individual sensors can then be determined via the intersection plan (if available) of the selected traffic light system.



| Field name						| Identifier Meaning / Description								|
|-----------------------------------|---------------------------------------------------------------|
| Datum (Date)						| Date in local time (Darmstadt)								|
| Uhrzeit (Time)					| Time in local time (Darmstadt)								|
| Intervall (Interval)				| Length in minutes												|
| Bezeichner ID (Identifier ID)		| of the traffic signal system (note: may contain spaces)		|
| DiZ 								| Number of registered vehicles from sensor with no. i			|
| DiB 								| Proportion of time with sensor no. i							|

## Project structure

- Data from sensors [data](data)
- Python script for scraping [darmstadt_download.py](darmstadt_download.py)
- Sensors configuration [config.json](config.json)
- General plan of the city [pdf](pdf/LSA_Uebersichtsplan_QM.pdf)
- Plans of individual street intersections [pdf](pdf)

![alt text](cover.jpg)

