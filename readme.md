# Readme
This is my attept to solve the problem you requested. 

## 1. Create the matrix
Running the `main.py` let you produce the matrix plus a table with the authors and the corresponding coauthors identified by id

## 2. How would design the test suite:
- I would create some example documents, using as a blueprint the XML schema provided, to test some simple functionalities
- I would try to create more methods in order to make both my code easier to read and easier to test.
- I would like to write the test as a sort of “guide” for future consumer of my application. That mean I would check for my functions to return what expected using example documents, trying to create test that mimic the usecase of the application

## 3. Problems I foresee when scaling
- Impossible to manage a unique XML, it’s necessary to split it in smaller documents and possibly parallelize the process
- Authors and matrix are saved in memory. While with a reduce number of articles and authors this is not going to be a problem, when the number of authors is increasing this will become a problem
- The provided solution is basic and needs to be optimized using more efficient approches (i.e. avoiding multiple for-loops)
- Python could be easy to read and write, but is not very good to manipulate huge amount of data (lack of parallelization). Probably switching to a native parallel programming language, like Java, could improve performance

