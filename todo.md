

- [ ] Find out how to take distributional difference of observed and estiamted into account.
    - We want to somehow transform the estimated X to statistically better resemble the observed X. 
    -  https://github.com/adapt-python/adapt transfer learning/domain adaptaion.
- [ ] How to deal with missing values in observed. a has a portion missing in beinning. b and c has portion missing at the end.
- [ ] We have many features, how do we select relevant.
- [x] Convert from 15 minute intervals to hours.
- [x] Test: Make 'merge' dataset of all 

- [ ] To an ensamble learning thing by fitting several models and take the (weighted) mean of the predictions.
    - with data only from period we want to predict
    - Each location separately
    - etc. 

EDA
- [x] Plot train target for a, b and c
- [] Test with stupid few features. 
- [x] Plot target and features on same x - scale 
    - Investigate deadspots in target.
- [x] check correlation between: 
    - 'pressure_50m:hPa', 'pressure_100m:hPa', 'sfc_pressure:hPa'  = 1
    - 'snow_water:kgm2', 'snow_depth:cm'
    - 'super_cooled_liquid_water:kgm2', 'precip_5min:mm'
    - 'effective_cloud_cover:p', 'total_cloud_cover:p' = 0.9 ish


## Notes
For A:
The observed training data goes from 2019-06-02 to 2022-10-21

For B:
The observed training data goes from 2019-01-01 to 2022-05-03

For C:
From 2019-01-01 to 2022-05-01


For all locations:
The predicted training data goes from dec 2022 to may 2023. Winter/spring.

The predicted test data goes from may 2023 to july 2023. (summer) 


# Clean the data

## B
**Training data** is constant in the intervals:

Remove like this:
test = y['b'].set_index('time').drop(pd.date_range('2020-07-12','2020-08-26'))

'2020-04-02':'2020-04-15'
'2020-07-13':'2020-08-25'
'2021-02-18':'2021-04-18'
'2021-04-29':'2021-05-01'
'2021-08-26':'2021-09-03'
'2021-09-08':'2021-09-14'
'2021-09-19':'2021-09-27'
'2022-03-20':'2022-04-04' / '2022-03-20':'2022-04-13' ( de siste er litt suspekt lave)

## C

**Training data** is constant in the intervals:

'2020-02-06':'2020-02-09'
'2020-02-24':'2020-03-07'

'2023-02-01':'2023-02-07'
'2023-02-23':'2023-02-26'
'2023-03-05':'2023-03-17'