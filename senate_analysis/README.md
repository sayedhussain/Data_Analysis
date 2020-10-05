# A7_senate_analysis
## Assignment 7 - HTTP requests, XML parsing with XPath, Object Oriented Coding, Data Analysis

## Purpose
In this assignment, you’ll need to create a program that has several parts.  The purpose will be to automatically download a specific portion of recent US Senate voting data, load the Senators and selected bill numbers into a custom Python data structure and then do some analysis.

Using the process below within your program, your solution needs to extract all the data fields necessary so that you can analyze and report on this concept:  _The campaign propaganda from a current politician claimed that “He represents his constituents and that ‘following the party line’ is not his priority.” In other words, he claims that he does not vote in ways that match what the leaders in his political party want._

That claim is something we can directly prove or disprove for all Senators (or Representatives) using Python and analytical methods.

## Technical Requirements 
- [ ] Like before, one student per team creates a fork then removes “All_Students” team from permissions and adds the team members with Write access.  The Teams are determined during class and are or will be listed in your Moodle section.
- [ ] Discuss, plan, and divide up the work through your team so that you can efficiently collaborate.
- [ ] Design and create one or more object-oriented class as appropriate for your program.  
- [ ] Write well-designed and well-documented functions for each part of the program and assemble it into a complete working Python (.py) script – NOT a Jupyter notebook.  
- [ ] Create Doctest(s) for each function to reasonably demonstrate and assure that they work properly.  
- [ ] For the HTTP (web) requests, use the “requests” package in Python.
- [ ] For parsing the XML, use the “lxml” package, especially XPath and etree.  Once you’ve used XPath to get the node(s) you need, it’s fine to use Regexes and other string manipulation to parse exactly what you want from within text nodes.  But do not try to avoid properly using XPath to navigate the document object model.Especially for the parts that do web requests, use exception handling as needed in case of things like a bad Internet connection or a down website.
- [ ] For efficiency and to employ best practices for net citizenship, make your program save each downloaded vote record detail file on your hard drive and check so that when you re-run the program, it should NOT re-request those files from the web that it already has downloaded successfully.
- [ ] Final Submissions should be here in GitHub.  The README.md file needs to list all team members and have a summary of which parts of the work they worked on.  Include the resulting analysis file as a text file.

## Algorithm steps will include these (and more, as needed):
1.	The program needs to first download the XML versions of the Senate Roll Call vote indexes from 2015 through 2018.  These are indexed at pages like: https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_115_2.htm with the XML version URL identical except for file extension, like: https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_115_2.xml That URL refers to the 115th Congress, 2nd Session, which is 2018.  115_1 would be the 2017 session.
2.	We’re going to ignore Resolutions and Amendments, to focus on the votes for Passage of Bills and Nominations by the Senate.  So, your program needs to parse the XML index files to extract only the <vote> nodes and child data where:
a.	the <issue> looks like “H.R. #” or “S. #” AND where the <question> contains “On Passage of the Bill” or “On Overriding the Veto”, OR  
b.	OR where the <question> contains “On the Nomination”.
3.	Have the program display a summary of those matches as it runs. Include the Year, Vote 
4.	Using the <vote_number> extracted from each match in step 2, construct the correct URL and automatically download the XML roll call vote record for that.  An example is https://www.senate.gov/legislative/LIS/roll_call_votes/vote1151/vote_115_1_00199.xml  
5.	From that you’ll need to parse each XML to determine which Senators voted Yea, Nay, or didn’t vote.  
6.	For each Bill or Nomination, you need to determine whether each of the two main Parties (Republican & Democrat) supported or opposed an issue.  You can do that by counting which way the majority of each party’s Senators voted on it.  An alternate and more difficult method would be by assuming that the Party’s Majority Leader or Minority Leader will by definition vote in the way their Party Leadership wants.  

## Output Format:
Your program’s analytical output needs to list all Senators in a single table format, one senator per row.  Include these columns: 
* Senator Name
* State
* Party (‘D’, ‘R’, or ‘I’)  NOTE: For the few “Independent” party Senators, you can leave the rest blank:
* Count and Percentage of votes matching their Party
* Count and Percentage of votes opposing their Party
* Count and Percentage of times marked as “Not voting”
