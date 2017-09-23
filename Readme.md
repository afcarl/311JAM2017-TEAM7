Beta NYC 2017: # Team 7


## Challenge Guide #7
How can 311 data be used with performance data in the Mayor’s Management Report to help inform and improve agency performance by providing predictive insight or highlighting equity issues?

Full [Detail](https://docs.google.com/document/d/1ajjQJtK4t3YtoiBppA8EkgXVFpfxUiNW95yIzgGRzHc/edit#)


## Participants:

Amit Bhatia | amit@taprecruit.co | github.com/amiglobe

Anela Chan | anelachan@gmail.com | http://anela.co

Frank Donnelly | francis.donnelly@baruch.cuny.edu | github.com/frankpd

Claire Gerson | clairegerson@gmail.com | github.com/cgerson

Lizette Leano | lizleano35@gmail.com | github.com/lizleano

Robin Newman | rnewman@hugeinc.com |robinerinnewman.com/ saynomoregame.com

Kevin Nguyen | kvn219@nyu.edu | github.com/Kvn219

Nidhin pattaniyil | npatta01@gmail.com | http://npatta01.github.io/

Sophie Rand | s.rand525@gmail.com | 

Justin Ryan | justin@jry.se | github.com/carillonator

Eric Schles | ericschles@gmail.com | github.com/EricSchles

Matthew Ström | matthew.h.strom@gmail.com | matthewstrom.com


# Helpful datasets

## PMMR (Preliminary Mayor's Management Report)
- [FY16](https://data.cityofnewyork.us/City-Government/FY16-PMMR-Agency-Performance-Indicators/q5za-zqz7)
- [FY17](https://data.cityofnewyork.us/City-Government/FY17-PMMR-Agency-Performance-Indicators/him9-7gri)

Example Query
```
# MMR FY - July 1, 2016 through June 30, 2017
SELECT
 unique_key,
 created_date,
 closed_date,
 agency,
 agency_name,
 complaint_type,
 descriptor,
 location_type,
 incident_zip,
 incident_address,
 street_name,
 school_name,
 school_code,
 address_type,
 city,
 landmark,
 facility_type,
 status,
 due_date,
 resolution_description,
 resolution_action_updated_date,
 community_board,
 borough,
 latitude,
 longitude,
 location
FROM
 `bigquery-public-data.new_york.311_service_requests`
WHERE
 created_date BETWEEN TIMESTAMP("2016-07-01 00:00:00.000")
 AND TIMESTAMP("2017-07-01 00:00:00.000")
```

