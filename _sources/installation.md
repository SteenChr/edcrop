# Installation and Quickstart
## Installation

Edcrop (v. 1.0.0) is coded in and requires Python 3.8.8 or higher. It uses the packages numpy (v. 1.20.1), pandas (v. 1.2.4), matplotlib (v. 3.3.4), and yaml (pyyaml v. 5.4.1).

Edcrop is available from the Python Package Index (PyPI.org) repository. It is installed by executing from the command line:

&ensp;&ensp;&ensp;&ensp; **pip install edcrop**

This installation uses the following dependencies of other Python packages:

```
dependencies = [
		"numpy >=1.20.1",
		"matplotlib >= 3.3.4",
		"pandas >=1.2.4",
		"pyyaml >=5.4.1"
	]
```

To install Edcrop without caring for dependencies, use instead:

&ensp;&ensp;&ensp;&ensp; **pip install --no-deps edcrop**

The above commands install Edcrop into the Python site-packages directory. The edcrop directory contains a sub-directory named Examples, containing example of data files required to make Edcrop run.

To learn more about installation by use of pip (the package installer for Python), consult the pip documentation, e.g. https://pip.pypa.io/en/stable/cli/pip_install/.

Edcrop and example releases can also be found on https://github.com/SteenChr/edcrop.

## Quickstart

Running Edcrop can be done in two ways:

The first way is to run Edcrop from own script by including in the script both the statement:

&ensp;&ensp;&ensp;&ensp; `from edcrop import edcrop`

and the function call:

&ensp;&ensp;&ensp;&ensp; `edcrop.run_model()`

The function call may include two optional arguments:

&ensp;&ensp;&ensp;&ensp; `yaml=<name of yaml input file>`

&ensp;&ensp;&ensp;&ensp; `log=<name of log output file>`

with the defaults:
&ensp;&ensp;&ensp;&ensp; `yaml='edcrop.yaml'`

&ensp;&ensp;&ensp;&ensp; `log='edcrop.log'`

The second way is to run Edcrop as a script by executing from the command line:

&ensp;&ensp;&ensp;&ensp; `python –m edcrop`

with the optional arguments:

&ensp;&ensp;&ensp;&ensp; `--yaml <name of yaml input file>`

&ensp;&ensp;&ensp;&ensp; `--log <name of log output file>`

Users can get started via the Jupyter Notebook: {doc}`notebooks/quick-start`.