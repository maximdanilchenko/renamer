# RENAMER

Find all files in current directory or in subdirectories by pattern, 
rename it with given regex patterns (like re.sub in python) and 
save it by given path

### Usage:
```
positional arguments:
  pattern_file  pattern for files to search
  path_to       path where to save result files
  pattern_from  regex for file name to find substrings
  pattern_to    replacing string with backreferences from regex pattern_from
                argument

optional arguments:
  -h, --help    show this help message and exit
  --r           find recursively in all subdirectories
```

### Example:
```
> renamer.py *.con result .(\d*)_(\d*).* \2_0\1 --r
```
Will find all files with pattern ```*.con```, 
change names with given patterns (like ```d123_456.con``` -> ```456_0123```) 
and save it in directory ```result```
