![Hero](https://github.com/Suchisrit/dataviz-for-mental-health/blob/master/screenshots/hero.png)

# Mental Health Visualized

Mental health has recently been making headlines, so we wanted to take a closer look at trends in mental health data by visualizing them. We created 3 visualizations using the Dash API and plotly library.

## Inspiration
With Simone Biles making headlines and a year's worth of working remotely taking a toll on mental health, we thought that mental health would be a fascinating topic to explore through visualizations in data.

## What it does
Our data visualizations take a look at 3 datasets, showing the percentage of population with mental health disorders by country, the number of people who have mental health disorders and who have discussed it formally with their employer in a survey, and the number of people in the tech industry who have sought treatment for their mental health condition. Our visualizations are interactive with the ability to slide through years, hover to see more responses, and click to see more results.

## How we built it
We built these data visualizations using the Dash python API. We found datasets in csv format, loaded it into panda dataframes and used the plotly library to generate graphs and charts. Dash then allowed us to use python to compile all the graphs onto a single webpage with its html components library. We also wrote some css to style the webpage of the compiled graphs.

## Challenges we ran into
Our main challenge was finding and cleaning datasets so that we could use them. Inconsistencies with the country names, country codes, and missing countries gave us a lot of trouble with the map data. We also had to fiddle a lot with the plotly express library in order to achieve the results we wanted. This included things like hover text, color scales, sunburst charts, etc.

## Accomplishments that we're proud of
This was our first time being introduced to the Dash API and the plotly library, and one of our first introductions to working with large datasets, so we are happy with how we cleaned up the messy data from the real world into clean looking visualizations with a new library.

## What we learned
Do not underestimate the messiness of real world datasets.

## Built With

    python
    pandas
    dash 
    plotly 
    html5 
    css3 

## Screenshots

![viz-1](https://github.com/Suchisrit/dataviz-for-mental-health/blob/master/screenshots/viz-1.png)

![viz-2](https://github.com/Suchisrit/dataviz-for-mental-health/blob/master/screenshots/viz-2.png)

![viz-3](https://github.com/Suchisrit/dataviz-for-mental-health/blob/master/screenshots/viz-3.png)