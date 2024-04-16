# Where the Wind Blows: An Analysis Tool for Windfarm Feasibility

## Getting our Data

For this project I used the WTK-LED CONUS dataset, a configurable set of data fields from a national collection of wind stations. This data represents wind-speed, temperature, direction, and air pressure values at multiple heights above the surface for the years 2019 and 2020. It was collected and is currently hosted by the National Renewable Energy Labratory (NREL) and can be found ![here](https://developer.nrel.gov/docs/wind/wind-toolkit/wtk-led-conus-download/)

## Analyzing our Data

#### Wind Turbine Power Generation

The power output ![equation](https://latex.codecogs.com/svg.image?\(P\)) of a wind turbine can be calculated using the formula:

![equation](https://latex.codecogs.com/svg.image?\[P=\frac{1}{2}\rho&space;A&space;v^3&space;C_P\])

where:
- ![equation](https://latex.codecogs.com/svg.image?\\rho\) is the air density (kg/m^3), which can be calculated from air pressure and temperature.
- ![equation](https://latex.codecogs.com/svg.image?\(A\)) is the swept area of the turbine blades (m^2).
- ![equation](https://latex.codecogs.com/svg.image?\(v\)) is the wind speed at the height of the turbine hub (m/s).
- ![equation](https://latex.codecogs.com/svg.image?\(C_P\)) is the power coefficient, which depends on the turbine design and the operational conditions.

##