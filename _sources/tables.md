# Tables of input and output


|'key'|]Model parameter c.f. Ch. 1|Description|
|---|]---|---|
|wbfunc|]   |   |
|stepsperday|]   |   |
|Cr|]$C_r$|Initial capacity of root zone to hold water. FPN.|

| `key`          | Model parameter c.f. Ch. 1 | Description                                                                                                     |
|----------------|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| wbfunc         |                            | A string specifying which water balance function to use. 'value' must be ed or evacrop; default is ed.         |
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

**Notes:**

1) The dates should be provided in the format YYYY-MM-DD.
2) Ensure that the dates fall within the simulation period.
