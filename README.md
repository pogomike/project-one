# project-one
First project for our data viz bootcamp

To run bls.py you will need config.py wth your bureau of labor statistics api key named r_key

bls.py retrieves the codes Evelyn had plus the ones I suggested (see below)
It places them in a single file education_data.csv and also in separate files named for the series id. All of these files are in the output directory.

I am currently working on mung to put the data in a dataframe with columns for the below categories so we can do a stacked bar graph

What I understand is that this is educational spending for a year for households in the given categories.

LB10	02	Origin of reference person: Hispanic or Latino	0	T	10020

LB10	03	Origin of reference person: Not Hispanic or Latino	0	T	10030

LB10	04	Not Hispanic or Latino: White and All Other Races	1	T	10040

LB10	05	Not Hispanic or Latino: Black or African-American	1	T	10050

LB11	02	Region of residence: northeast	0	T	11020

LB11	03	Region of residence: midwest	0	T	11030

LB11	04	Region of residence: south	0	T	11040

LB11	05	Region of residence: west	0	T	11050

LB13	02	Total, less than college graduate	0	T	13020

LB13	03	Less than high school graduate	1	T	13030

LB13	04	High school graduate	1	T	13040

LB13	05	High school graduate with some college	1	T	13050

LB13	06	Associate degree	1	T	13060

LB13	07	Total, college graduate	0	T	13070

LB13	08	Bachelor's degree	1	T	13080

LB13	09	Master's, professional, doctorate	1	T	13090

Added

LB08	06	Type of area: urban	0	T	8060

LB08	07	Type of area: urban: central city(from 2003)	1	T	8070

LB08	08	Type of area: urban: other urban(from 2003)	1	T	8080

LB08	09	Type of area: rural	0	T	8090

----------------------------------------------------------------------------------------------------
CENSUS DATA

ACS 1-Year Estimates by Geographic Region

Years of data: 2017, 2016, 2015, 2012, 2011, 2010

Age and Sex (S0101)

Educational Attainment (S1501)

Poverty Status in the Past 12 Months (S1701)

Mean Income in the Past 12 Months (in 2017 Inflation-Adjusted Dollars) (S1902)

Employment Status (S2301)

Race (B02001)

Hispanic or Latino Origin (B03003)

Educational Attainment and Employment Status by Language Spoken at Home for the Population 25 Years and Over (C16010)
