# Report

**Date perception:**
Since the “user” for this  program would be a supermarket, I thought it would be important to keep date perception very straight-forward. For example: if someone tried to set the date of the program to 1989-25-12 just to see what it does and then forgets to set it back, the whole buy and sell system would rely on a completely wrong date. I tried to solve this as follows:  
-per function I choose which date options would make sense to use.  So I activated the appropriate date functions only there. An example is the “range” option, which is available in the function “revenue”, but not in “buy” and “sell”.
-At the beginning of each function the date is automatically set to today as a default. This, to prevent the erratic booking of a sale on Christmas Eve 1989 while we’re in 2022.

**Recycling functions:**
Where possible I’ve tried to break up functions in smaller pieces so I was able to recycle them in other functions. An example of that is **build_list_to_date** which is used in the **open_inventory** and **open_inventory_batch** function. Both functions start with **build_list_to_date** and the outcome is forwarded to the appropriate print function.

**Temp csv files**
In 2 cases a used csv files for temporary storage.  One of those cases is in the **build_list_to_date** function.  When creating a batch or inventory list at an earlier date, the program needs to alter batch amounts with the info from the sold csv file and add an “expired” flag to a batch in case it has expired. In order to protect the data on the bought csv by not altering it (just read) and to have a convenient place to store newly calculated data, I thought it would be a good idea to use a temp csv file.  The temp files are deleted at the end of the function. If for whatever reason the function would not complete, I added a “check-and-delete” at the beginning of the function. This to prevent old data being mixed up with new data.
