# Metro On-Time Project 

### A "Health Monitor" App for the LA Metro 

./App: Contains our logging application and database analysis. 

## To set up train tracking every 3 minutes:

1. Edit crontab:
`*/3 * * * * cd path/to/analysis_folder/App && bash ./log_job.sh`
2. Start cron service:
`systemctl start cron`

Currently, you must edit log_job.sh to choose the line you wish to track - we will rewrite this to log all rail lines once we are ready to scale up.

./GTFS: Relevant static data - stops & schedule info

Tracking_Data_Rough_Analysis.ipynb: Analysis of vehicle GPS updates and their frequency, geographic distribution. Here we are trying to determine how the positioning system works in order to better inform our arrival time estimations.
Requires: Jupyter Notebook (Anaconda)

distance_calculations.qgz: QGIS project mapping all the points and lines - we will use this to get an accurate calculation of distances between stations. Should be able to line up vehicle coordinates with the shapefiles.
Requires: QGIS (https://qgis.org/en/site/)
