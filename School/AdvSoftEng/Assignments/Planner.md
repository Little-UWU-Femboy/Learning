# BASIC INFORMATION

- This will use PHP, MySQL, and Linux only
- This is all on an AWS server that has 30 GiB and running a m7i-flex.large (2 vcpu's and 8 Gib of RAM)
- Use pcntl_fork() and shell_exec() where the process looks like below, but this will need to use flock() to ensure the parent process does not override this:

```mermaid
flowchart LR
    A["Read + Process (parent)"] --> B["Temp File For Data Store"] --> C["Store to DB (Child)"]
```

- All data will be read from a csv file called "tps757.csv" and this file is ~5 million lines long. This file will always be in the same directory as all the PHP files.
- Must use batch processing for more efficiency
- All code must not be in a single PHP file and must be split across multiple PHP files
- The tps757.csv file itself is to never be modified as this is the only copy of the original data.
- There will be a directory called "TemporaryData" which will be used to hold temporary created data. All data here will be deleted after two hours by a cronjob.
- All tables mentioned will be in a database called "ResourceManagement".



# Requirements

- Each line in the csv file will follow this format: Device Type, Brand. Serial Number. If it has any more or any less then this then this is not allowed and is considered an error. There are many error types, but here are the few I already found and how I want them labeled, but there could be more undiscovered
  1. ERROR: Missing device type
  2. ERROR: Missing device brand
  3. ERROR: Missing serial number
  4. ERROR: Missing device type, device brand
  5. ERROR: Missing device type, serial number
  6. ERROR: Missing device brand, serial number
  7. ERROR: All columns empty
  8. ERROR: More than three columns
  9. ERROR: Incorrect serial number size
  10. ERROR: Less than three columns
  11. ERROR: Duplicate serial number
  12. ERROR: Data in wrong column
  13. ERROR: Undiscovered error
- Must use mysqli. The information for this will be stored in a table called "accounts". It will contain the  columns: id, username, and password. When looking through the table, look for the user called "User". Use that username, and password to connect to the database. The database will always be on localhost and name (as mentioned above) for the database is ResourceManagement.
- The first PHP file to run is one called "Analyze.php". This will be used to gather information about what device types are present and brand names are there. Some of the names here for both will have incorrect symbols in the names (i.e @pple, comp-ter, micr*osof&). This means you have to first remove these special symbols (so only letters A-z allowed). Then you will find the unique names and number of times those occurred. This will make two files "BrandProcessed.csv" and "TypeProcessed.csv" which will be added to the TemporaryData directory.
- The second PHP file to run will be one called "Creation.php". This will look at those two .csv files created in the TemporaryData directory. It will create a table for each of those types (device_type and device_brand) and those tables will contain enums of the valid types. For any that occur less than 10k times, they will not be added to the table enum.
- The third php script called "Breaker.php". This file will break the tps757.csv file into smaller chunks so each process can run the information faster and everything more quickly. The separated files will be stored in a directory called "parts". However, it is important to retain the original line numbers each line had in the original csv file. This is because it the use of that line number will be needed later on when it comes to logging errors. Add the line numbers to the end of the csv line per thing of where it was in the original file.
- The fourth php script will be called "Process.php". This is where the main getting and processing of data will occur. This will read one of the broken up csv file parts from the "parts" directory (important to know to use the scandir() function, but this will get the .. and . directory too, so they need to be removed from the list). This will process each of the lines checking that there are at only three columns. By that I mean that the first three columns are: device type, device brand, and serial number. I know that there is a fourth column in which the last will contain the line number that this was originally in, which we will use. So to check to see if this is a valid row, just get the $\text{total number of columns }- 1$ as that will be the correct thing (i.e a valid row will have 3 columns only). This is where the above mentioned errors will come in. If one of those occur, then this will be written into a table called "error_data". A row is considered good if it passes all the error checks. If it passes then it will get written to the "processed_data" table. When it comes to the errors there can be more than one so this must track all the errors that row of data would have. It is important (hence why it is an error) that there are no duplicate serial numbers. Also, the serial number size is 67 characters long total; three for the prefix "SN-" and the rest of the 64 characters will be valid.
  - The error table will contain the following columns: id, actual row data (excluding the line number part), error type, line number this occurred at, and when the error occurred (use CDT time).
  - The process table will contain the following columns: id, device type (with reference to the device table for the enum), brand name (with reference to the brand table for the enum), serial number, and time written in  (use CDT time).
- The fifth script will be called "Store.php". This will be the actual script that writes the data to the database. This must use the most effective and fastest way possible. This can be batch processing, prepared statements, mixture, something else, etc.
- The sixth script will be called "Orchestrator.php". This will be the script that creates the processes so this whole processes can be completed as fast as possible.



In the end, there will be to be a .pdf file created in the TemporaryData directory called "Results.pdf" that will contain the following:

- Total number of records in the tps757.csv file
- Total number of records that were able to be stored without error
- List the total different error types and the number of occurrences each one had
- List the error you found and the line number from the CSV file where it was found
- Report must also include effective rows per second import as well as total time to import. If you are using a parallel process to import, you must state each individual process's import speeds and times as well as the aggregate effective import information.



This all needs to finish in at most 20 minutes. Hopefully can get something 