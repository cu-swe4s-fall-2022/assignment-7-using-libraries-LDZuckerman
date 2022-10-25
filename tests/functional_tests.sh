#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# test plotter.py
wget -O 
wget 
run test_plotter.py python plotter.py

filepath='iris_boxplot.png'
echo $filepath
if [ -f "$filepath" ]; then
   echo ' TEST 1 PASSED: found '+filename+' in expected directory'
else
   echo ' TEST 1 FAILED: did not find '+filename+' in expected directory'
fi
assert_exit_code 0

filepath='petal_width_v_length_scatter.png'
echo $filepath
if [ -f "$filepath" ]; then
   echo ' TEST 2 PASSED: found '+filename+' in expected directory'
else
   echo ' TEST 2 FAILED: did not find '+filename+' in expected directory'
fi
assert_exit_code 0

filepath='multi_panel_figure.png'
echo $filepath
if [ -f "$filepath" ]; then
   echo ' TEST 3 PASSED: found '+filename+' in expected directory'
else
   echo ' TEST 3 FAILED: did not find '+filename+' in expected directory'
fi
assert_exit_code 0
