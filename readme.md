# Elucidata

#### How to Run this project:
Clone this repository and change the directory to 'elucidta' by using 'cd elucidata' command

check the version of python by using 'python' command and then install the other requirements by using the following command in your terminal:
pip install -r requirements.txt

run the server by using 'python manage.py runserver' command.

#### About the project:

After you run the server you will need to upload an xlsx file that captures the output of a mass spec machine after an experiment run.

You can upload this file on the home page.

Below the submit button you will see 3 urls:

1) Filtered Files - filters out all the data for metabolite ids ending with: ‘PC’, ‘LPC’ and ‘plasmalogen’, and create 3 child datasets (1 for each compound id) from the data in input file

2) Rounded Files - Adds a new column in the parent dataset with the name “Retention Time Roundoff (in mins)”. This column should have rounded-off values of the corresponding retention time

3) Mean files - finds the mean of all the metabolites which have same "Retention Time Roundoff" across all the samples.

To run The test cases -  on the terminal, run the test cases by using 'python manage.py test'