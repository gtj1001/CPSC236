     -Test Generator-
Created by Garrett Jones
===================================
This program is in the .ipynb format and is intended to be run in the Jupyter Notebook environment.
Some functions may not behave correctly if run outside of it.

This program requires "CPSC 236 TestBank.csv" to be present in the same directory in order
to run. If you wish to generate your own test bank, the proper formatting is as follows.
Be sure to include the first key row.

Question	Option A	Option B	Option C	Correct Answer
[question text]	[answer]	[answer]	[answer]	(A/B/C)
...		...		...		...		...

The program will generate a number of .txt files containing student results in the same
directory as the notebook file. These files will be formated as
"FIRSTNAME_LASTNAME_STUDENTID.txt"
Ensure that the notebook location is an appropriate place for these results to be stored.

The program is suited to receive input from multiple students without being restarted. 
The program will prompt for and clear the console when another student needs to use the 
program without seeing the responses 