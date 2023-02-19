CLI Calculator
Author: Shams Ahsanullah

About the calculator-
The CLI calculator has all the required features mentioned in the gist.

Additionally, it is able to take in an unlimited number of arguments to the add and multiply operations. It is designed in a way that if an addtional operation is needed, it can be easily added.

(Important: The app has been tested to run in both Linux (Ubuntu) and Windows environments. However, the automation tests only run in Linux)

How to run -
1. Download the source code either from github or zip file. Extract zip file.
2. go to the source folder and from there, run the following command-
   python3 ./main.py <your provided argument>
   
   (if it does not work, try python instead of python3.)

Testing-
The solution has 11 unit tests designed to test different usecases. Feel free to add more automation tests if needed.

In Linux, to run these tests, go to the source folder and use the following command-

python3 -m unittest tests/test_solution_service.py
