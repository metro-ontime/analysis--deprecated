# Metro On-Time Project 

### A "Health Monitor" App for the LA Metro 

./App: Contains our logging application and database analysis. 

./GTFS: Relevant static data - stops & schedule info

Tracking_Data_Rough_Analysis.ipynb: Analysis of vehicle GPS updates and their frequency, geographic distribution. Here we are trying to determine how the positioning system works in order to better inform our arrival time estimations.
Requires: Jupyter Notebook (Anaconda)

distance_calculations.qgz: QGIS project mapping all the points and lines - we will use this to get an accurate calculation of distances between stations. Should be able to line up vehicle coordinates with the shapefiles.
Requires: QGIS (https://qgis.org/en/site/)
