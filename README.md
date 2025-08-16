# Swiping Minds: Exploring the Relationship Between Screen Time in Young Males and Violence Trends Against Women  

[Swiping Minds GitHub Repository](https://github.com/Saavesh/Swiping-Minds)

## Project Description  
This project investigates the potential relationship between screen time in young males and violence trends against women. Using national survey data, we examined how behavioral patterns, media exposure, and societal changes may be connected to broader trends in violence and victimization. The project combines datasets from the American Time Use Survey (ATUS) and the National Crime Victimization Survey (NCVS) to provide both behavioral context and crime trends across decades.  

## Research 
- How does screen time among young males correlate with trends in violence against women?  
- Do patterns in victimization rates differ by sex across different categories of violent crime?  
- What insights can data-driven analysis provide about potential social and behavioral risks linked to technology use?  

## Datasets  
- **American Time Use Survey (ATUS)** – Provides data on daily activities, including media consumption and screen time.  
- **National Crime Victimization Survey (NCVS)** – Provides detailed victimization data (1993–2023) on violent crime, including rape/sexual assault, assault, and robbery, broken down by sex and age group.  

## Techniques Applied  
- **Data Cleaning and Preprocessing:** Removed missing values, standardized column labels, and merged datasets.  
- **Exploratory Data Analysis:** Used Pandas and visualization libraries (Matplotlib, Seaborn) to uncover trends and patterns.  
- **Classification & Clustering:** Grouped results by age, sex, and crime type to explore contextual relationships.  
- **Visualization:** Created time-series plots, bar charts, and comparative graphs of male vs female victimization trends.  

## Code Organization  
All code for this project is contained within Jupyter Notebooks inside the `notebooks/` folder:  
- `01_load_clean_atus.ipynb`: Loads and cleans the American Time Use Survey data.  
- `02_load_clean_ncvs.ipynb`: Loads and cleans the National Crime Victimization Survey data.  
- CSV files were not included in this repo to avoid a large repository, but they can be accessed in the Sources section. 

Each notebook includes:  
1. Data import and cleaning steps.  
2. Preprocessing and merging logic for analysis.  
3. Exploratory data analysis with summary statistics.  
4. Visualization code for generating graphs and plots.  

This structure ensures that the workflow can be reproduced from raw data to final visualizations directly within the notebooks.  

## Key Results  
- Female victimization rates for rape/sexual assault have been consistently higher than male rates, though both show declines since the early 1990s.  
- Young males demonstrate higher screen time averages compared to other groups, with patterns of heavy digital use becoming more common in the last decade.  
- Broader trends suggest possible intersections between cultural exposure (through screen-based activities) and patterns of violence, warranting deeper study.  

## Applications  
- Informing **policy makers** about the long-term societal impacts of digital behavior.  
- Supporting **educators and parents** with data-driven insights about adolescent screen time and behavioral risks.  
- Providing **researchers** with a combined framework for studying behavioral data alongside crime victimization statistics.  

## Visualizations  
This project includes several visualizations such as:  
- Line plots showing victimization rates by sex over time (1993–2023).  
- Bar charts comparing crime types between males and females.  
- Screen time activity distributions across different demographic groups.  

## Final Project Paper  
You can view the full project writeup here:  
[Final Writeup (PDF)](reports/Writeup.pdf)  


## Sources
- **American Time Use Survey (ATUS)** — Detailed time-use data from the Bureau of Labor Statistics. Official site: https://www.bls.gov/tus/  
- **ATUS Data Tools** — Download microdata and time series from the ATUS database: https://www.bls.gov/tus/database.htm  
- **NCVS Dashboard (N-DASH)** — Interactive crime victimization data (1993–2023) from the Bureau of Justice Statistics: https://ncvs.bjs.ojp.gov/  
- **NCVS Multi-Year Trends by Crime Type** — Time-series visuals on violent victimization rates by sex and crime type: https://ncvs.bjs.ojp.gov/multi-year-trends/crimeType  