# Tables

## Inputs

### Model Parameters

The following table supplement the model parameter input description in {doc}`inputs`.

**Table 6** Model parameters for which ‘value’ can be specified by use of ’key’ in the “Models” block of the edcrop.yaml input file. Notice that ‘key’ is a case sensitive name. FPN is short for ‘floating point number’.
<dic id="table6" />

| Key            | Model parameter | Description                                                                                                     |
|----------------|-----------------|-----------------------------------------------------------------------------------------------------------------|
| wbfunc         |                 | A string specifying which water balance function to use. 'value' must be ed or evacrop; default is ed.          |
| stepsperday    |                 | Number of time steps per day that is used when wbfunc = ed. 'value' must be an integer larger than 0.           |
| Cr             | $C_r$           | Initial capacity of root zone to hold water. FPN.                                                           |
| Cb             | $C_b$           | Initial capacity of subzone to hold water. FPN.                                                             |
| Cu             | $C_u$           | Initial capacity of upper root zone. FPN.                                                                   |
| Vs             | $V_s$           | Initial water content of snow reservoir. FPN.                                                               |
| Vr             | $V_r$           | Initial water content of root zone. FPN.                                                                    |
| Vb             | $V_b$           | Initial water content of subzone. FPN.                                                                      |
| Ve             | $V_e$           | Initial water content of evaporation zone. FPN.                                                             |
| Vu             | $V_u$           | Initial water content of upper root zone. FPN.                                                              |
| VI             | $V_I$           | Initial content of intercepted water. FPN.                                                                  |
| ci             | $c_i$           | Interception capacity constant. FPN.                                                                        |
| cm             | $c_m$           | Degree day factor for snow melt. FPN.                                                                       |
| Tm             | $T_m$           | Threshold temperature for snow melt. FPN.                                                                   |
| ce             | $c_e$           | Evaporation factor for dry soil. FPN.                                                                       |
| kp             | $k_p$           | Extinction coefficient. FPN.                                                                                |
| zmax           | $z_{max}$       | Depth of simulated soil profile. FPN.                                                                       |
| winterperiod   |                 | A list of two dates defining beginning and end of winter, respectively. See  1 and 2.                           |
| irrigationperiod |               | A list of two dates defining beginning and end of irrigation season, respectively. See 1 and 2.                 |
| irrigationdate |                 | A list containing dates of forced irrigation. See 1 and 2.                                                      |
| irrigation     |                 | The rate for forced irrigation. FPN.                                                                        |
| autoirrigate   |                 | A boolean specifying whether to simulate irrigation automatically. 'value' must be false or true; default is false.|
| tlim           | $t_{lim}$       | The irrigation time limit in days with respect to maturing. An integer value.                                   |
| tfreq          | $t_{freq}$      | Minimum number of days between automatic irrigation. 'value' must be positive integer.                          |
| clim           | $c_{lim}$       | Factor limiting water content requiring automatic irrigation. FPN.                                          |
| Plim           | $P_{lim}$       | Precipitation limit for automatic irrigation. FPN.                                                          |
| Imin           | $I_{min}$       | Minimum amount of automatic irrigation. FPN.                                                                |
| Imax           | $I_{max}$       | Maximum amount of automatic irrigation. FPN.                                                                |
| iprnd          |                 | 'value' must be integer 1, 2, 3, or 4; default is 1. Specifies predefined list of time series variables for writing daily and yearly outputs to print files. The higher number, the more variables are output. |
| prlistd        |                 | Text string of time series variables for writing of daily output to print file. In the string, a space character must separate two variable names. |
| prlisty        |                 | Text string of time series variables for writing of yearly output to print file. In the string, a space character must separate two variable names. |
| plotseries     |                 | Specifies whether to make plots of simulation output. 'value' must be yes or no; default is no.                 |

1. A date is given in the format %Y-%m-%d; an example using this format is 2019-12-31, where first four digits give year (2019), next two digits give month (12), and last two digits give day (31). 
1. Only day and month is used, every simulated year.

**Table 7** A second example of “Models” block input in edcrop.yaml file. Two model runs, named M1 and M2, will be executed.
<dic id="table7" />

```
Models:
   M1:
        wbfunc: evacrop
        winterperiod: [1900-11-02, 1901-03-02]
        irrigationperiod: [1900-04-02, 1900-09-03]
        irrigationdate: [1900-07-07, 1900-07-17, 1900-08-07, 1900-08-17]
        irrigation: 16.
        iprnd: 2
        plotseries: true
    # M2 implicitly uses the default, which is wbfunc: ed
    M2:
        stepsperday: 4
        autoirrigate: true
        tlim: 20
        tfreq: 5
        clim: .9
        Plim: 7.
        Imin: 25.
        Imax: 35.
        prlistd: Ep Ea Db
```
### Soil types and parameters

**Table 8** Predefined soil types, with oral and quantitative characterization. Valid ‘key’ type names are JB1 to JB7. Notice that ‘key’ is a case sensitive name. The soil types are from Olesen and Heidmann (2002), who used the soil classification of Madsen and Holst (1987).
<dic id="table8" />

| Soil type Key   | Soil description            | Clay < 2 µm | Silt 2-20 µm | Fine sand 20-200 µm | Total sand 20-2000 µm |
|-----------------|-----------------------------|-------------|--------------|---------------------|-----------------------|
| JB1             | Coarse sandy                | 0-5 %       | 0-20 %       | 0-50 %              | 75-100 %              |
| JB2             | Fine sandy                  | 0-5 %       | 0-20 %       | 50-100 %            |                       |
| JB3             | Coarse sandy with clay      | 5-10 %      | 0-25 %       | 0-40 %              | 65-95 %               |
| JB4             | Fine sandy with mix of clay | 10-15 %     | 0-30 %       | 40-95 %             |                       |
| JB5             | Clayey with coarse sand     | 10-15 %     | 0-30 %       | 0-40 %              | 55-90 %               |
| JB6             | Clayey with fine sand       | 10-15 %     | 0-30 %       | 40-90 %             |                       |
| JB7             | Clayey                      | 15-25 %     | 0-35 %       |                     | 40-85 %               |

**Table 9** Soil parameters for which ‘value’ can be specified by use of ‘key’ in the “Soils” block of the edcrop.yaml input file. Notice that ‘key’ is a case sensitive name. FPN is short for ‘floating point number’.
<dic id="table9" />

| Key         | Model Parameter                                   | Description                                                                      |
|-------------|---------------------------------------------------|----------------------------------------------------------------------------------|
| soiltype    | A predefined soil type ‘key’ chosen from Table 8. | A string.                                                                        |
| name        | A descriptive name for the soil.                  | A string.                                                                        |
| thf         | $θ_F$                                             | Plant available water content of the soil. List of four FPN’s; one value for each of four 25 cm depth intervals. (Total soil depth is 100 cm – unless the model parameter value maxz is changed.)                                                |
| Ce          | $C_e$                                             | Capacity of evaporation zone. FPN.                                               |
| kqr         | $k_{qr}$                                          | Drainage constant for root zone.                                                 |
| kqb         | $k_{qb}$                                          | Drainage constant for sub zone. FPN.                                             |
| Kmp         | $K_{mp}$                                          | Maximum rate of macro-pore drainage. FPN. Only used when wbfunc = ed (see Table 6)  |
| Cmp         | $C_{mp}$                                          | Water content threshold at which macro-pore drainage is initiated. FPN.          |
| Vmprel      | $V_{mp - rel}$                                    | Relative water content threshold below which macro-pore drainage can occur. FPN. |
| Kro         | $K_{ro}$                                          | Maximum rate of surface runoff. FPN. Only used when wbfunc = ed (see Table 6).   |
| thsat       | $θ_{s,1} - θ_{r,1}$                               | Water content at which macro-pore flow is initiated. FPN. Only used when both wbfunc = ed (see Table 6) and soilmodel = lin. For soilmodel = mvg, thsat is calculated internally from water content values given for the top soil horizon.  |
| horizon     | name $θ_s$ $θ_r$ $α$ $n$ $K_s$ $I$                | Definition of soil horizon, which is a dictionary with key being name given to horizon (string) and value being a list of six Mualem – van Genuchten parameter values (FPN). Only used when both wbfunc = ed (see Table 6) and soilmodel = mvg. Definition of default horizons is in Edcrop’s `SoilParameters.horizon` dictionary.                                                                                                                                                                |
| soilhorizons| Name of four horizons making the soil profile.    | List of four strings, where each string is the name of a soil horizon. Each horizon must either be given as input or be found in Edcrop’s `SoilParameters.horizon` dictionary. Definition of default soil horizons for the soil types in Table 8 is found in Edcrop’s `SoilParameters.MvG_soilhorizons` dictionary. |
| soilmodel   | A string specifying which soil drainage model to use, | linear or Mualem – van Genuchten. ‘value’ must be lin or mvg; default is lin. Only used when wbfunc = ed (see Table 6). |

**Table 10** A second example of “Soils” block input in edcrop.yaml file. JB1 is a predefined soil to be simulated using the Mualem- van Genuchten drainage model. JB10 is a new soil type with two horizons changed from the default of the JB1 soil.
<dic id="table10" />

```
Soils:
    JB1:
        soilmodel: mvg
    JB10: soiltype: JB1
    # The following defines two new horizons
    horizon: {B_JB10: [0.3, 0.0, 0.06, 1.445, 800., -0.3], C_JB10: [0.25, 0.0, 0.06, 1.6, 1000., 1.3]}
    # The following defines the horizons of the JB10 soil
    soilhorizons: [A_JB1, B_JB1, B_JB10, C_JB10]
    soilmodel: mvg
```

### Vegetation types and parameters

**Table 11** Predefined crop or vegetation types, with characterization. Notice that ‘key’ is a case sensitive name. The first ten types are taken from Olesen and Heidmann (2002).
<dic id="table11" />

| Type | Crop or Vegetation Description |
|------|--------------------------------|
| BS   | Bare soil                      |
| G1   | Grass with grazing             |
| G2   | Grass for hay                  |
| WW   | Winter wheat                   |
| SB   | Spring barley                  |
| POT  | Potato                         |
| FB   | Fodder beet                    |
| SR   | Spring rape                    |
| PEA  | Pea                            |
| SBG  | Spring barley with grass       |
| MZ   | Maize                          |
| DF   | Deciduous forest               |
| SF   | Spruce forest                  |
| WL   | Wetland                        |
| WM   | Wet meadow                     |


**Table 12** Crop or vegetation parameters for which ‘value’ can be specified by use of ‘key’ in the “Crops” block of the edcrop.yaml input file. Notice that ‘key’ is a case sensitive name. FPN is short for ‘floating point number’.
<dic id="table12" />

| Key         | Model Parameter                  | Description                                                                              |
|-------------|----------------------------------|------------------------------------------------------------------------------------------|
| name        | A descriptive name for the crop. | A string.                                                                                |
| cb          | $c_b$                            | Bend point for relative transpiration function. List of twelve FPN’s, one for each month.|
| cr          | $c_r$                            | Root growth velocity during spring season. FPN.                                          |
| cre         | $c_re$                           | Root growth velocity during fall season. FPN.                                            |
| zrv         | $z_rv$                           | Root depth during winter season (for winter crop). FPN.                                  |
| zrx         | $z_{max}$                        | Maximum root depth. FPN.                                                                 |
| Lm          | $L_m$                            | Maximum leaf area. FPN.                                                                  |
| Lv          | $L_v$                            | Leaf area during winter (for winter crop). FPN.                                          |
| Lc          | $L_c$                            | Leaf area after cutting (for grass). FPN.                                                |
| Lym         | $L_{ym}$                         | Yellow leaf area at maturity. FPN.                                                       |
| So          | $S_o$                            | Temperature sum for sprouting. FPN.                                                      |
| Sf          | $S_f$                            | Temperature sum for full leaf area. FPN.                                                 |
| Sr          | $S_r$                            | Temperature sum for beginning of maturing. FPN.                                          |
| Sm          | $S_m$                            | Temperature sum for end of maturing. FPN.                                                |
| Soe         | $S_{oe}$                         | Temperature sum for sprouting during fall (for winter crop). FPN.                        |
| Sfe         | $S_{fe}$                         | Temperature sum for full leaf area during fall (for winter crop). FPN.                   |
| kcmin       | $k_{c,min}$                      | Minimum crop coefficient. FPN.                                                           |
| kcmax       | $k_{c,max}$                      | Maximum crop coefficient. FPN.                                                           |
| sowdate     |                                  | Date of sowing. Give date as explained in 1 and 2. Not used for grass crops since they are permanent. |
| harvestdate |                                  | Date of harvesting. Give date as explained in 1 and 2. For crop G1, grass for grazing, this is not used since it is a permanent crop. For crop G2, grass for hay, this must be a list containing dates of cutting. For crop SBG, spring barley with grass, this must be a list with date for barley harvest, followed by date(s) of grass cutting. |
| autoharvest |                                  | Only for crops: a boolean specifying whether to simulate harvest automatically. Harvest will occur 7 days after Lg < 0.001. ‘value’ must be true or false; default is false. |
| leaflife    |                                  | Only for deciduous forest: list of four dates for leaf_out_begin, leaf_out_end, leaf_loss_begin, and leaf_loss_end, respectively. Give each date as explained in 1 and 2.    |

1. A date is given in the format %Y-%m-%d; an example using this format is 2019-12-31, where first four digits give year (2019), next two digits give month (12), and last two digits give day (31). 
1. Only day and month are used, every simulated year.

## Output Variables

**Table 13** Possible variables that can be daily or yearly output in respective print files. Notice that ‘key’ is a case sensitive name.
<dic id="table13" />

| Key      | Model Variable              | Description                                                                         |
|----------|-----------------------------|-------------------------------------------------------------------------------------|
| Date     |                             | Date.                                                                               |
| T        | $T$                         | Temperature.                                                                        |
| P        | $P$                         | Precipitation, total.                                                               |
| Pr       | $P_r$                       | Precipitation falling as rain.                                                      |
| Ps       | $P_s$                       | Precipitation falling as snow.                                                      |
| Pm       | $P_m$                       | Water made available by snow melt.                                                  |
| Er       | $E_{ref}$                   | Reference evapotranspiration.                                                       |
| Ep       | $E_p$                       | Potential evapotranspiration.                                                       |
| Ea       | $E_a$                       | Actual evapotranspiration.                                                          |
| Eas      | $E_{as}$                    | Actual evaporation from snow reservoir.                                             |
| Eae      | $E_{ae}$                    | Actual evaporation from soil.                                                       |
| Eai      | $E_{ai}$                    | Actual evaporation of intercepted water.                                            |
| Eaig     | $E_{aig}$                   | Actual evaporation of water intercepted on green leaves.                            |
| Eaiy     | $E_{aiy}$                   | Actual evaporation of water intercepted on yellow leaves.                           |
| Eat      | $E_{at}$                    | Actual transpiration.                                                               |
| Ept      | $E_{pt}$                    | Potential transpiration.                                                            |
| Epe      | $E_{pe}$                    | Potential evaporation not attenuated by vegetation.                                 |
| Epc      | $E_{pc}$                    | Potential evaporation attenuated by vegetation.                                     |
| Epcg     | $E_{pcg}$                   | Potential evaporation attenuated by green vegetation.                               |
| Epcy     | $E_{pcy}$                   | Potential evaporation attenuated by yellow vegetation.                              |
| Dr       | $D_r$                       | Drainage from root zone to sub zone.                                                |
| Db       | $D_b$                       | Drainage from sub zone.                                                             |
| Dmp      | $D_{mp}$                    | Drainage from macro pores.                                                          |
| Dsum     | $D_{sum} = D_b + D_{mp}$    | Sum of drainage from subzone and macro pores.                                       |
| Qro      | $Q_{ro}$                    | Surface runoff.                                                                     |
| I        |                             | Irrigation.                                                                         |
| Tsum     | $S_s$                       | Temperature sum driving plant growth.                                               |
| L        | L                           | Leaf area.                                                                          |
| Lg       | $L_g$                       | Green leaf area.                                                                    |
| Ly       | $L_y$                       | Yellow leaf area.                                                                   |
| zr       | $z_r$                       | Root depth.                                                                         |
| kc       | $k_c$                       | Crop coefficient.                                                                   |
| Vsum     | $V_{sum} = V_s + V_i + V_{soil}$ | Sum of stored water.                                                            |
| Vdel     |                             | Change in stored water.                                                             |
| Vs       | $V_s$                       | Water stored in snow reservoir.                                                     |
| Vi       | $V_i$                       | Water stored by interception.                                                       |
| Ve       | $V_e$                       | Water stored in evaporation zone.                                                   |
| Vu       | $V_u$                       | Water stored in upper root zone.                                                    |
| Vr       | $V_r$                       | Water stored in root zone.                                                          |
| Vb       | $V_b$                       | Water stored in sub zone.                                                           |
| Vsoil    | $V_{soil}$                  | Water stored in soil profile (equal to $V_r + V_b$).                                      |
| Cu       | $C_u$                       | Capacity of upper root zone to store water.                                         |
| Cr       | $C_r$                       | Capacity of root zone to store water.                                               |
| Cb       | $C_b$                       | Capacity of sub zone to store water.                                                |