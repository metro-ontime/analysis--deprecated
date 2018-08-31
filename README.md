# Metro Performance Monitor

### A Health App for the Los Angeles Metro Rail system

This website, incubated at Hack for LA, tracks LA Metro trains and provides up to date statistics summarizing daily, weekly, monthly and annual performance. Our mission is to monitor and report the number of both on-time and late train arrivals on an ongoing basis for all Metro rail lines in Los Angeles. These are:
 - Blue Line
 - Red Line
 - Green Line
 - Gold Line
 - Purple Line
 - Expo Line

Currently, monitoring the LA bus network is outside the scope of this project. 

By publishing these statistics and open-sourcing our methodology, we aim to give riders an accurate and unvarnished picture of the system's state over time. Hopefully, this will correct any public misperception of Metro's track record and help inform decision-makers when assessing future improvements to the system.

Possible future directions for this project include:
 - Benchmarking the LA Metro system against other transit systems worldwide. Open-sourcing our analysis is the first step towards beginning a discussion on how to measure and compare transit systems worldwide. Due to budget constraints and ageing infrastructure, perfect GPS tracking and precise reporting of arrival times is not commonly found in rail systems. We want to develop low-cost and reliable methods to estimate train arrival times at stations. 
 - Monitoring causes of delays and providing additional statistics on these.

## For Contributors & those who want to help:

What We Need:
 - Developers (Python and/or GIS systems knowledge -- HIGH PRIORITY)
 - Transport Engineers (to assist in development of arrival time estimation algorithm -- HIGH PRIORITY)
 - Front End Developers (React, data visualization)
 - QA Testers (spotting bugs, feedback on site-design -- currently low priority)

This web application is built on a python backend, which logs and processes vehicle tracking data from Metro's real-time API. The front end is a React app hosted on a static server (GitHub or Netlify - TBC) that is recompiled daily as new performance data becomes available on our python backend. 

## This Repository:

./App: Contains our logging application and database analysis. 

./GTFS: Relevant static data - stops & schedule info

Tracking_Data_Rough_Analysis.ipynb: Analysis of vehicle GPS updates and their frequency, geographic distribution. Here we are trying to determine how the positioning system works in order to better inform our arrival time estimations.
Requires: Jupyter Notebook (Anaconda)

distance_calculations.qgz: QGIS project mapping all the points and lines - we will use this to get an accurate calculation of distances between stations. Should be able to line up vehicle coordinates with the shapefiles.
Requires: QGIS (https://qgis.org/en/site/)

## Train Tracking Logs

You can set up our logging script to track trains locally on any Unix machine running Python 3.6, SQLite3, and cron. 

### Example: set up train tracking every 3 minutes on Linux:

1. Edit crontab:
`*/3 * * * * cd path/to/analysis_folder/App && bash ./log_job.sh`
2. Start cron service:
`systemctl start cron`

Currently, you must edit log_job.sh to choose the line you wish to track - we will rewrite this to log all rail lines once we are ready to scale up.

