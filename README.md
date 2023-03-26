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

* Copies the original CSV file to a new file named data.csv.
* Reads the data from data.csv into a Pandas DataFrame.
* Prompts the user to enter an ID for the data they wish to analyze.
* Rounds the time values in the DataFrame to the nearest 10 minutes.
* *xtracts the last part of the ID string from the first column in the DataFrame.
* Filters the DataFrame to only include rows with the specified ID.