# New York City Crime Analysis

## Introduction
Safety is a major consideration whenever people navigate life. Whether it’s picking a place to live, a new
car, or a new activity or sport, safety is usually one of the first things that are brought up. While crime is not necessarily an indicator of safety, it is something people usually look into.

With that, our team would like to explore one of America’s most visited destinations, New York. We can
utilize publicly available crime data in New York City to pull insights about crime trends. After collecting this information, we can cross-reference spikes and dips with events, and investigation factors in high and low crime periods.

## Process

We got our data from NYC Open Data’s website. The data is provided by the Police Department (NYPD) so, the data is correct and authentic. The website allowed different ways of extracting data from downloading in the CSV or GEOJSON format to using the API calls to the data in the form of CSV or JSON.

The data is public and doesn’t require a private API key and there is no hard limit on rate as well. We wrote a simple code in python which allowed us to pull data. We originally wrote a simple for loop which would get data by offsetting each time, but it was taking a lot of time to get all the data. So, to solve this we used concurrent futures modules which would run code on different cores of the machine, and this sped up the process by a lot. Instead of spending close to 4 hours, we were able to get all 5 million-plus rows in a matter of 20 minutes, and if you have a heavy-duty computer with a higher number of cores, it can be faster as well. You can see the code in the **crimeCollector_V2.py** file. The file collects all the data and uploads it to our SQL server.

For our preprocessing, we didn't have to serious cleaning since most of the data was in workable conditions. We didn't have many null values but did have quite high amounts of duplicate cases. You can see the preprocessing done in our **Preprocessing.ipynb** file.

The EDA consists of numerous graphs, word clouds, and also, some heatmaps of crimes at famous tourist spots in New York City. You can see all the EDA of graphs and word clouds in the **EDA.ipynb** file and heatmaps of tourist spots in the **Extended_Data_Analysis.ipynb** in the extendedAnalysis folder.

## Data

Attributes and their description.

- ARREST_KEY = Randomly generated persistent ID for each arrest

- ARREST_DATE = Exact date of arrest for the reported event

- PD_DESC = Description of internal classification corresponding with PD code (more granular than Offense Description)

- OFNS_DESC = Description of internal classification corresponding with KY code (more general category than PD description)

- LAW_CODE = Law code charges corresponding to the NYS Penal Law, VTL, and other various local laws

- LAW_CAT_CD = Level of offense: felony, misdemeanor, violation

- AGE_GROUP = Perpetrator’s age within a category

- PERP_SEX = Perpetrator’s sex description

- PERP_RACE = Perpetrator’s race description

- Latitude = Latitude coordinate for Global Coordinate System

- Longitude = Longitude coordinate for Global Coordinate System

- ARREST_BORO = Borough of the arrest. B(Bronx), S(Staten Island), K(Brooklyn), M(Manhattan), Q(Queens)

- ARREST_PRECINCT = Precinct where the arrest occurred

- JURISDICTION_CODE = Jurisdiction responsible for arrest. Jurisdiction codes 0(Patrol), 1(Transit) and 2 (Housing) represent NYPD whilst codes 3 and more represent non NYPD jurisdictions

- computed_region_f5dn_yrer = Community District

- computed_region_yeji_bk3q = Borough Boundaries

- computed_region_92fq_4b7q = City Council Districts

- computed_region_sbqj_enih = Police Precincts

## Acknowledgments
All work was done by [myself](https://github.com/janampatel15), [Ambrose Karella](https://github.com/ajkarella), [Naimish Bizzu](https://github.com/Naimishvinnu).

Thanks to [NYC Open Data](https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u) for the data and [Socrata](https://dev.socrata.com/) for the amazing API.