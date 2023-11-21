# Los Angeles Crime Trends: A Focus on Identity Theft

In this project we analyzed crime trends from 2020-2022 with a focus on Identity Theft. 

Our analysis contains:

* A high level breakdown of the reported crimes from 2020-2022 (by year and month).

* Year over Year crime trends of the most and least reported crimes of 2020-2022.

* A deeper look at Identity Theft Theft crime trends and why we chose to look specifically at Identity Theft.

## Main Contributors
Ashelyn Allred, Samantha Candia, Julius Mayo

# A Look Inside the Files 

The main notebook can be found above titled: `main.ipynb`

The notebook we used to process the raw 205MB CSV with all years is `data_intake.ipynb`  
(original csv not on github due to file size constraints)

Our presentation can be found in the main folder under the name: `Group Project 1 Presentation.pdf`

Figures used in our presentation may be found in the `Output/` folder. (slight tweaks may have been made after the fact)

The `Resources/` folder contains:
* Sliced CSV files taken from the original dataset due to the file being too latge for GitHub's file size limit
* Saved config files from the main.ipynb
* Documenation that provides additional information on how to break down codes from the original dataset.

[The raw dataset that was used in our analysis can be found here](https://catalog.data.gov/dataset/crime-data-from-2020-to-present
).

# Limitations of our Analysis:

* Only looking at reported crimes (not looking at outcome of crimes)

* Only looking at data for the city of Los Angeles, CA

  -Trends may differ across cities, states, and countries

* Our analysis on Identity Theft only takes into account records that have Identity Theft listed as the main crime.

  -There were multiple crime codes possible for a given incident
  
  -Crimes were listed in descending order of severity, so we are only looking at the ‘main’ crime
* Analysis was done within the years of 2020 to 2022

  -Data existed from 2023, but we excluded it from our scope

  -We wanted full years only
