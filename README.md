# using libraries and plotting data

## Summary

This repository contains a script, data_processor.py, with functions to create, store, and read in random matrix data. In another script, plotter.py, we read in the standard iris dataset and and use create plots to visualize it.

# Tests

Unit tests for the functions and functional tests for the scripts used in this repository are included using continuous integration with GitHub workflows

## Conda Environment

This repository will work correctly using the conda envrironment stored in the
gen_env.yml file. To create this environment from this file, use 
"conda env create -f gen_env.yml"

## Usage

plotter.py can be called with the following command-line arguements:\
`--boxplot_filename` The name of the output file containing the boxplot.\
`--scatterplot_filename` The name of the output file containing the boxplot.\
`--comboplot_filename` The name of the output file containing the multi-panel plot.\

## Example

python plotter.py 
    --boxplot_filename iris_boxplot.png 
    --scatterplot_filename petal_width_v_length_scatter.png 
    --comboplot_filename multi_panel_figure.png

This produces the images iris_boxplot.png, petal_width_v_length_scatter.png, and multi_panel_figure.png in this repository


