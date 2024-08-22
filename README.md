#Learning PySpark
# Project Documentation
I will be documenting issues that i faced in every step and how i resolved them so if anyone else look at this repo hopefully they would not spend some time banging their head ;)
## Issue: Importing `dotenv` in Virtual Environment

While setting up the project, I encountered an issue where attempting to import the `dotenv` module resulted in a `ModuleNotFoundError`. Despite installing the module within my virtual environment, the error persisted.

### Error Message:
ModuleNotFoundError: No module named 'dotenv'

## Solution

To resolve the issue, I installed `python-dotenv` globally rather than within the virtual environment. This allowed the module to be accessible, and the import error was resolved.

### Steps:
1. Open the terminal.
2. Install `python-dotenv` globally:
   ```bash
   pip install --user python-dotenv

Note: Although this solves the issue, it's generally recommended to use virtual environments to manage dependencies. Consider reinstalling within a virtual environment if possible.

Reference:
The solution was inspired by a discussion on [Stack Overflow](https://stackoverflow.com/questions/59572174/no-module-named-dotenv-python-3-8)

# Next Step
now we are ready to download our data set. Here we use the data from Chicago Data Portal. The dataset is the [Crimes - 2001 to Present](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/jzptg8t2/about_data).

