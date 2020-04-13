# File Explanation

## attempt.py
This is the actual prototyped solution of HW7. There are three functions in the file. The `tsvDicts` function takes a full file name and turns it into a list of dictionaries. The top row of the file becomes the keys for each dictionary and the rest of the rows become the different dictionaries. The file just needs to be a standard TSV. If your data set is another file type, there are many spreadsheet format converters online. The most recent version of `attempt.py` under the drive folder will check if the value can be turned into a float or integer, which will store the value in that way. The other two functions rely on tsvDicts. The `searchByCriteria` functions serves two purposes. If it's given a file name and key appropriate to the data set of the file, it will return a list of dictionaries that are sorted by the value under that key. If it's given a file name, a key, and a value to search for, it will simply filter the dictionary list so that only entrees of that criteria will remain (unsorted). The last function, `crossSearch`, will need a file name, key number 1, value number 1, key number 2, and value number 2. It will filter the list of dictionaries so that only the entrees with both criteria remain. This function only relies on the tsvDicts function. There are some print statements for the functions under the `if __name__ == "__main__":` statement if you want to uncomment some of them.

## data_creator.py
This function was designed to make a diverse data set that the attempt.py program could run code off of before the data sets were decided on. The createData function will ask for a file name and size to make a randomized data set as the file you gave it with the number of entrees dictated by the size given at a time complexity of O(N). The reason I mention the order notation is because of multiCreate. It takes the first half of a file name (the stuff before the dot) and the second half of the file name (everything to the right of the dot, including the dot), as well as a starting size, a magnitude (geometric rate of change), a number of files, and an optional sequence id. It will create the number of files you told it to, that will have the starting size you gave it, increasing at a rate of the magnitude you gave it. Each file will have the name of the first half you gave, a number, and the second half you gave all concatenated. The optional sequence id will determine if it’s increasing geometrically or arithmetically (default is arithmetic). 

### Example 1
When calling:
- `multiCreate("new_data_", ".tsv", 50, 50, 5)`
- `multiCreate("new_data_", ".tsv", 50, 50, 5, “a”)`
- `multiCreate("new_data_", ".tsv", 50, 50, 5, “arithmetic”)`

You actually called:
- `createData("new_data_1.tsv", 50)`
- `createData("new_data_2.tsv", 100)`
- `createData("new_data_3.tsv", 150)`
- `createData("new_data_4.tsv", 200)`
- `createData("new_data_5.tsv", 250)`

### Example 2
When calling:
- `multiCreate("new_data_", ".tsv", 50, 2, 5, “g”)`
- `multiCreate("new_data_", ".tsv", 50, 2, 5, “geometric”)`

You actually called:
- `createData("new_data_1.tsv", 50)`
- `createData("new_data_2.tsv", 100)`
- `createData("new_data_3.tsv", 200)`
- `createData("new_data_4.tsv", 400)`
- `createData("new_data_5.tsv", 800)`

## Time Complexity (TODO figure this out)
For the geometric sequence, the time complexity is something like *O(N^3)* while the arithmetic sequence has a time complexity of *O(N^2)*. 

The rest of the `data_set_X.tsv` files in the folder are just some files generated off of calling the geometric versions of the `multiCreate` function.

