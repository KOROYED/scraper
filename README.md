## Best scraper 
### To execute:
  ```docker build . -t scraper```\
  \
  ```docker run --name=scraper -e -d scraper```
### Setting environment:
In main.py set variables to suit your request:
* selected_popularity_tag - type the number of tag you need
* folder_path - name of the folder which will hold results
* execute_time - write the time you want script to execute
### Result example:
In console: Data written
    
Result file will be stored in your ```folder_path``` folder, file name is 
equal to date when it was executed.

In file:

    Author: Albert Einstein
    Tags: change, deep-thoughts, thinking, world, inspirational, life, live, miracle, miracles, adulthood, success, value
    Post Count: 3
    Character Count: 313

    Author: Marilyn Monroe
    Tags: be-yourself, inspirational
    Post Count: 1
    Character Count: 111

    Author: Thomas A. Edison
    Tags: edison, failure, inspirational, paraphrased
    Post Count: 1
    Character Count: 65
