Instructions To Run Code for DataBase here.
TO RUN THE COMMANDS, TERMINALS MUST BE OPENED IN THIS DIRECTORY
1.) If the database with all the data hasn't been created, then open a terminal or command prompt(cmd)
    and run this command "python task.py". The task.py file creates the tables and inserts all the data 
    from the csv files into the 5 tables.
2.) The second part to obtain a summary of the pre-existing data from the database, open a terminal or command prompt 
    then run the command "python summary.py", The output should show a summary of the data in the database.
3.) The third part is to insert or delete data into the database. This time the command requires arguments to be passed into the command.
    When inserting data make sure that when including the data for a table, insert the data respectively in the order of attributes of the table.
    For example, if I want to insert into Instruments, the data would be inserted with the instrument_id first, then type of instrument, then finally the key of the instrument.
    Here is a example command: "--add --table Instruments --record 13,guitar,A"
    Here is an example of the delete command: "--delete --table Instruments --record 13,guitar,A"
    When inserting arguments in the command, it will think of whitespace as separation for arguments passed, so when multiple words are include like "Hello World" insert or delete
    the record by putting underscores between each word, the program will eventually replace those underscores as spaces.
    For example running this command: "--add --table Albums --record Johnny B. Goode,26,1998,CD"
    The above command won't work and throw you an error. Therefore use the following command:
    "--add --table Albums --record Johnny_B._Goode,26,1998,CD" for this command you will see that it will insert or delete the data with whitespaces rather than underscores.