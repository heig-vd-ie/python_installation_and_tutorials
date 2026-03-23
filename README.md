# Power System Notebooks, 1<sup>st</sup> edition

Welcome to the main repository of Power Systems and High Voltage for electrical engineers course at HEIG-VD.

## Before we start from scratch

Both Jupyter Notebook and Python scripts have their own advantages and disadvantages when it comes to energy efficiency. [Python is known to be less energy efficient than other programming languages such as C++ and Java](https://thenextweb.com/news/python-progamming-language-energy-analysis).

However, Jupyter Notebook can be more energy efficient than Python scripts because it allows you to run code in smaller chunks, [which can help you avoid running unnecessary code](https://cloud.google.com/blog/products/ai-machine-learning/best-practices-that-can-improve-the-life-of-any-developer-using-jupyter-notebooks).

That being said, it’s important to note that energy efficiency is just one of many factors that you should consider when choosing between Jupyter Notebook and Python scripts. Other factors include ease of use, flexibility, and compatibility with your existing codebase.

## Installation and clean setup

- If you are on Windows 10 or 11, please follow the [detailed installation instructions in this section](INSTALL.md).
- If you are on macOS or Linux, please follow the [detailed installation instructions in this section](INSTALL.md#installing-python-with-mambaforge).

## Quickly look at a few notebook, without executing any code

> [!IMPORTANT]
> To quickly consult the notebooks and tutorials, click on the following link:

- [github.com's notebook viewer](./index.ipynb) is also fine but isn't ideal (it's slower and equations aren't always displayed correctly, and large notebooks don't always open).

<!-- * <a href=""><img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" alt="Render nbviewer" /></a> -->

Or directly open the notebooks from there:

0. [Welcome to Jupyter](./tutorials/00_welcome_to_jupyter.ipynb)
1. [The Basics of Python](./tutorials/01_basics.ipynb)
2. [NumPy Quick Start Guide](./tutorials/02_numpy.ipynb)
3. [Pandas Quick Start Guide](./tutorials/03_pandas.ipynb)
4. [An Introduction to **panda**power](./tutorials/04_pandapower.ipynb)
5. [Your first class demo notebook](./tutorials/05_class_demo.ipynb)

## FAQ & other requirements

> [!NOTE]
> How do I update my Python libraries to the latest versions, when using Mambaforge? 
> See [UPDATELIBRARIES.md](UPDATELIBRARIES.md)

If you get many problems with your git branch or repo, please get in touch with [Luca](mailto:luca.tomasini@heig-vd) or [Antoine](mailto:antoine.giraldi@heig-vd.ch).

## Contributors

This repository and the code were created by the following people from the Institut des Énergies at HEIG-VD:

- Luca Tomasini, Chargé de Ra&D HES
- Antoine Giraldi, Collaborateur scientifique HES
- Thierry Fracheboud, Assistant HES-SO & Research Engineer
- Mokhtar Bozorg, Professor HES-SO
- Marc Pellerin, Senior lecturer HES-SO
