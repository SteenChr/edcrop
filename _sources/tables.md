# Tables of input and output

| `key`          | Model parameter c.f. Ch. 1 | Description                                                                                                     |
|----------------|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| wbfunc         |                            | A string specifying which water balance function to use. 'value' must be ed or evacrop; default is ed.          |
| stepsperday    |                            | Number of time steps per day that is used when wbfunc = ed. 'value' must be an integer larger than 0.           |
| Cr             | \( C_r \)                  | Initial capacity of root zone to hold water. **FPN**.                                                           |
| Cb             | \( C_b \)                  | Initial capacity of subzone to hold water. **FPN**.                                                             |
| Cu             | \( C_u \)                  | Initial capacity of upper root zone. **FPN**.                                                                   |
| Vs             | \( V_s \)                  | Initial water content of snow reservoir. **FPN**.                                                               |
| Vr             | \( V_r \)                  | Initial water content of root zone. **FPN**.                                                                    |
| Vb             | \( V_b \)                  | Initial water content of subzone. **FPN**.                                                                      |
| Ve             | \( V_e \)                  | Initial water content of evaporation zone. **FPN**.                                                             |
| Vu             | \( V_u \)                  | Initial water content of upper root zone. **FPN**.                                                              |
| VI             | \( V_I \)                  | Initial content of intercepted water. **FPN**.                                                                  |
| ci             | \( c_i \)                  | Interception capacity constant. **FPN**.                                                                        |
| cm             | \( c_m \)                  | Degree day factor for snow melt. **FPN**.                                                                       |
| Tm             | \( T_m \)                  | Threshold temperature for snow melt. **FPN**.                                                                   |
| ce             | \( c_e \)                  | Evaporation factor for dry soil. **FPN**.                                                                       |
| kp             | \( k_p \)                  | Extinction coefficient. **FPN**.                                                                                |
| zmax           | \( z_{max} \)              | Depth of simulated soil profile. **FPN**.                                                                       |
| winterperiod   |                            | A list of two dates defining beginning and end of winter, respectively. See 1) and 2).                          |
| irrigationperiod |                          | A list of two dates defining beginning and end of irrigation season, respectively. See 1) and 2).               |
| irrigationdate |                            | A list containing dates of forced irrigation. See 1) and 2).                                                    |
| irrigation     |                            | The rate for forced irrigation. **FPN**.                                                                        |
| autoirrigate   |                            | A boolean specifying whether to simulate irrigation automatically. 'value' must be false or true; default is false.|
| tlim           | \( t_{lim} \)              | The irrigation time limit in days with respect to maturing. An integer value.                                   |
| tfreq          | \( t_{freq} \)             | Minimum number of days between automatic irrigation. 'value' must be positive integer.                          |
| clim           | \( c_{lim} \)              | Factor limiting water content requiring automatic irrigation. **FPN**.                                          |
| Plim           | \( P_{lim} \)              | Precipitation limit for automatic irrigation. **FPN**.                                                          |
| Imin           | \( I_{min} \)              | Minimum amount of automatic irrigation. **FPN**.                                                                |
| Imax           | \( I_{max} \)              | Maximum amount of automatic irrigation. **FPN**.                                                                |
| iprnd          |                            | 'value' must be integer 1, 2, 3, or 4; default is 1. Specifies predefined list of time series variables for writing daily and yearly outputs to print files. The higher number, the more variables are output. |
| prlistd        |                            | Text string of time series variables for writing of daily output to print file. In the string, a space character must separate two variable names. |
| prlisty        |                            | Text string of time series variables for writing of yearly output to print file. In the string, a space character must separate two variable names. |
| plotseries     |                            | Specifies whether to make plots of simulation output. 'value' must be yes or no; default is no.                 |


| Soil type `key` | Soil description            | Clay < 2 µm | Silt 2-20 µm | Fine sand 20-200 µm | Total sand 20-2000 µm |
|-----------------|-----------------------------|-------------|--------------|---------------------|-----------------------|
| JB1             | Coarse sandy                | 0-5 %       | 0-20 %       | 0-50 %              | 75-100 %              |
| JB2             | Fine sandy                  | 0-5 %       | 0-20 %       | 50-100 %            |                       |
| JB3             | Coarse sandy with clay      | 5-10 %      | 0-25 %       | 0-40 %              | 65-95 %               |
| JB4             | Fine sandy with mix of clay | 10-15 %     | 0-30 %       | 40-95 %             |                       |
| JB5             | Clayey with coarse sand     | 10-15 %     | 0-30 %       | 0-40 %              | 55-90 %               |
| JB6             | Clayey with fine sand       | 10-15 %     | 0-30 %       | 40-90 %             |                       |
| JB7             | Clayey                      | 15-25 %     | 0-35 %       |                     | 40-85 %               |
