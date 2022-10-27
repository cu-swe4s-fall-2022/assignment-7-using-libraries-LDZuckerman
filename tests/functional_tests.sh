test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# test plotter.py
run test_plotter.py python plotter.py \
   --boxplot_filename='iris_boxplot.png' \
   --scatterplot_filename='petal_width_v_length_scatter.png' \
   --comboplot_filename='multi_panel_figure.png' \

filepath='iris_boxplot.png'
echo $filepath
if [ -f "$filepath" ]; then
   echo ' TEST 1 PASSED: found '$filepath$' in expected directory'
else
   echo ' TEST 1 FAILED: did not find '$filepath$' in expected directory'
fi

filepath='petal_width_v_length_scatter.png'
echo $filepath
if [ -f "$filepath" ]; then
   echo ' TEST 2 PASSED: found '$filepath$' in expected directory'
else
   echo ' TEST 2 FAILED: did not find '$filepath$' in expected directory'
fi

filepath='multi_panel_figure.png'
echo $filepath
if [ -f "$filepath" ]; then
   echo ' TEST 3 PASSED: found '$filepath$' in expected directory'
else
   echo ' TEST 3 FAILED: did not find '$filepath$' in expected directory'
fi

assert_exit_code 0