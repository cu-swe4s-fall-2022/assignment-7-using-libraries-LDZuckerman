import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():

    # get data
    iris = pd.read_csv('iris.data', header=None) 
    iris.columns = ['sepal_width', 'sepal_length', 'petal_width', 'petal_length', 'species'] 

    # create iris_boxplot.png
    measurement_names = ['sepal_width','sepal_length', 'petal_width', 'petal_length']
    plt.boxplot(iris[measurement_names], labels=measurement_names)
    plt.ylabel('cm')
    plt.savefig('iris_boxplot.png')

    # create petal_width_v_length_scatter.png
    plt.figure()
    for species in set(iris['species']):
        subset = iris[iris['species'] == species]
        plt.scatter(subset['sepal_width'], subset['sepal_length'], label=species)
    plt.xlabel('sepal width (cm)')
    plt.ylabel('sepal length (cm)')
    plt.legend()
    plt.savefig('petal_width_v_length_scatter.png')

    # create multi_panel_figure.png
    fig, axs = plt.subplots(1,2, figsize=(10,5))
    measurement_names = ['sepal_width','sepal_length', 'petal_width', 'petal_length']
    axs[0].boxplot(iris[measurement_names], labels=measurement_names)
    for tick in axs[0].get_xticklabels():
        tick.set_rotation(15)
    axs[0].set_ylabel('cm')
    for species in set(iris['species']):
        subset = iris[iris['species'] == species]
        axs[1].scatter(subset['sepal_width'], subset['sepal_length'], label=species)
    axs[1].set_xlabel('sepal width (cm)')
    axs[1].set_ylabel('sepal length (cm)')
    plt.legend()
    plt.savefig('multi_panel_figure.png')

if __name__ == "__main__":
    main()