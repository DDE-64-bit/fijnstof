# Air Quality Data Analysis

This code analyzes air quality data collected from various sensors. The script uses the **Pandas** and **Matplotlib** libraries to read, manipulate, and visualize the data.

## Getting started

To get started, you will need to have **Python 3.x** installed on your computer. You will also need to install the **Pandas** and **Matplotlib** libraries.

```` terminal
pip install pandas matplotlib
````

Once you have **Python** and the necessary libraries installed, you can run the script using the following command:

```` terminal
python main.py
````

The script will prompt you to enter an ID for the air quality data you wish to analyze. Once you have entered a valid ID, the script will read the data from a **CSV** file, clean and transform the data, and plot a graph of the data for the specified ID.

## Data Cleaning and Transformation

The script performs the following cleaning and transformation steps on the air quality data:

* Copies the original **CSV** file to a new file named **data.csv**.
* Reads the data from **data.csv** into a **Pandas** **DataFrame**.
* Prompts the user to enter an ID for the data they wish to analyze.
* Rounds the time values in the **DataFrame** to the nearest 10 minutes.
* Extracts the last part of the ID string from the first column in the **DataFrame**.
* Filters the **DataFrame** to only include rows with the specified ID.

## Visualization

Once the data has been cleaned and transformed, the script plots a graph of the data using **Matplotlib**. The graph shows the amount of different air pollutants (**pm1**, **pm2.5**, **pm4**, and **pm10**) over time.

## Conclusion

This script provides a simple example of how to read, clean, transform, and visualize air quality data using **Python** and the **Pandas** and **Matplotlib** libraries. With some modifications, this script could be adapted to analyze other types of time series data as well.