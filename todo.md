

- [ ] Find out how to take distributional difference of observed and estiamted into account.
    - We want to somehow transform the estimated X to statistically better resemble the observed X. 
    -  https://github.com/adapt-python/adapt transfer learning/domain adaptaion.
- [ ] How to deal with missing values in observed. a has a portion missing in beinning. b and c has portion missing at the end.
- [ ] We have many features, how do we select relevant.
- [ ] Convert from 15 minute intervals to hours.
- [x] Test: Make 'merge' dataset of all 

EDA
- [x] Plot train target for a, b and c
- [] Test with stupid few features. 
- [] Plot target and features on same x - scale 
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