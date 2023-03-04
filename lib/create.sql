CREATE TABLE bears (
    -- define the columns in the table &
    -- the specific type of data each column will store.
    -- column names should be lowercase and snake case
    -- datatype Uppercase
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    sex INTEGER,
    color TEXT,
    temperament TEXT,
    alive INTEGER
    -- INTEGER bc alive or not will be represented as 1 or 0, but can't just write alive 1
    -- alive BOOLEAN works
    -- alive FALSE or alive TRUE not correct, test would pass bc test is faulty
    -- boolean don't exist in SQL!!
);