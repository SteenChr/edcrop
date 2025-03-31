# Changelog

Log of version changes to Edcrop code.

### Version 1.0.1

**Bug fixes**

- Statement moved in TimeSeries.watbal_ed_step(). Bug caused miscalculation of Ept and thus Eat for crop covered land.

- Fixed bug in CropParameters.initialize() which made initialization of spruce forest parameters fail.

- Fixed bug that made simulation fail for crop SBG when simulating it using a sequence of models. Fix was made in run_model().

- Fixed minor bug in CropParameters.initialize() causing error in making of error message.

- In TimeSeries.print_from_dictionary(), changed resample statement to try-except statements to make compatible with newer version of pandas.



