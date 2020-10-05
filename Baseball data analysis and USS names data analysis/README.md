# A6_pandas_with_joins
## IS590PR Fall 2018
Analytical queries with Pandas requiring the joining of multiple DataFrames.
Also this involves team collaboration through shared GitHub repositories.

### Getting started
* Decide on your team (2 or 3 students per team).
* ONE of your team create a fork of this repository
* As before, remove the "All_Students" from having access to your repository. 
* Add your teammates to have Write permission to your repository. That allows 
them to commit & push to it.

### The Data
For this assignment, you’ll need to download data from two completely
different data sources and then properly load and join data frames
(similar to SQL joins), as discussed in class.

* Download the 2018 edition of Lahman’s Baseball Database, in the Zipped
CSV format. It is available at
http://www.seanlahman.com/files/database/baseballdatabank-master_2018-03-28.zip
The database is documented here http://www.seanlahman.com/files/database/readme2017.txt

* Download the “National data” file from the US Social Security names
database at https://www.ssa.gov/oact/babynames/limits.html  This is also
a Zipped collection of CSV files.  Tip:  There are many examples in the
McKinney book that load and analyze these baby name files using Pandas.

**IMPORTANT!  Do not try to commit those ZIP or CSV data files into your
GitHub repository.**  It can overflow our GitHub storage quota and
there’s no need to do it anyway.  Set your PyCharm or other git client
to ignore those data files (leave them as “unversioned files”).

### The Programming

Your final product should be a Jupyter Notebook that clearly documents 
and shows results of your work to analyze some of the following queries.  
Work in your team by dividing the work, trying independently, then doing
code review for each other and finally present the best-quality completed
work you can as a single notebook. You may write functions in the
notebook or in a separate Python module that you import into the notebook.

Tips for collaborating through Git:
If 2-3 people are simultaneously editing the same notebook and you try 
committing, you will find that trying to do a "git merge" on a Jupyter 
Notebook is nearly impossible.  So you might want to each work on 
distinct files to avoid merge conflicts and then combine 
the parts into the final notebook.  

## For Baseball-specific analysis (__*do any 3 of these*__):

NOTE: You can ignore the Post-season data files for these analyses 
(e.g. "BattingPost.csv", "PitchingPost.csv", etc.). Just use the main 
regular-season files. 

* List the top 20 players in career success for stealing bases.  Use
total of “Stolen Bases” – total of “Caught Stealing” and call that result 
"Net Stolen Bases". Also compute their success rate as a percentage of 
attempts.  In the results, show their name & the calculated numbers. 
(Join People and Batting tables)

* Calculate and plot a chart showing the mean (average) height of all
active players per year.  (The player must be listed in a team roster 
for the year to be “active”, so join People & Appearances)

* Calculate the correlation between batting average and salary.  However,
don't include pitchers in this since they are not hired for hitting ability. 
You can determine pitchers either from the Appearances or Pitching tables. 
(Join People, Appearances, and Batting tables)

* List the 20 most dangerous pitchers derived from their career total 
statistics.  Specifically, those with the highest career rates of hitting 
batters.  (Join People & Pitching tables.  Use the formula 
total “Batters Hit By Pitch” / total “Outs Pitched”)

* List the top schools by number of alumni who were inducted into the
Hall of Fame. (Join Schools, CollegePlaying, HallOfFame)

## For cross-database integration analysis (__*do 1 of the following*__) two queries.

Notice that the People table has fields called "nameFirst", "nameLast", and 
"nameGiven".  For many of the players, the nameFirst column actually contains 
their _nickname_.  See Babe Ruth as an example, whose real first name was "George". 
Another is Cornelius Ryan who went by 'Connie'. So many of these nicknames are 
typically female that you have to extract their real first names to do a sensible 
analytical comparison with the SSN database.

* List all player given names that are statistically more common among
baseball players than among males in the general population for their
year of birth. Sort results by the proportion of commonality.

* Alphabetically list the full names of all players having given names
that were more commonly given to female babies in the same year the player
was born.

Tips for these queries: Use the Baseball People table to extract player's 
real first names and dates of birth. Then properly join them with the 
“Baby Names” data matching their year of birth.  That's a multi-column join.
