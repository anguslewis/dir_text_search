# dir_text_search
Search all .do, .py, .sh, and .txt files in a directory and all subdirectories for a search term.

The script searches all text files (at least those with the extensions .do, .py, .sh, and .txt but this could easily be changed)
in the current directory and any sub-directories. It returns instances of the search term found, organized by file, and also 
reports the line numbers the term appears in. 

The first argument is the search term. If the search term is multiple words it needs to be enclosed in quotes. 

The script takes an optional argument --no_comment, which omits commented lines in the files (lines beginning with * in .do files
and lines beginning with # in .py and .sh files).
