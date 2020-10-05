import requests
import lxml.html
import urllib
import os
import lxml
from lxml import etree
import pandas as pd
from Senator import senators
from threading import Timer

session_list = ['114_1', '114_2', '115_1', '115_2']
session_dict = dict()
for session in session_list:
    r = requests.get("https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_{}.xml".format(session))
    session_dict[session] = dict()
    session_dict[session]['vote_number'] = []
    session_dict[session]['year'] = []
    tree = None
    tree = lxml.html.fromstring(r.content)
    vote_num = []
    session_dict[session]['year'] = tree.xpath("//congress_year/text()")
    vote_num_1 = tree.xpath("//issue[(starts-with(text(), 'H.R.')) or (starts-with(text(), 'S.'))]/ancestor::vote/vote_number/text()")
    vote_num_2 = tree.xpath("//question[(contains(text(), 'On Overriding the Veto')) or (contains(text(), 'On Passage of the Bill'))]/ancestor::vote/vote_number/text()")
    vote_num = list(set(vote_num_1) & set(vote_num_2))
    vote_num_3 = tree.xpath("//question[contains(text(), 'On the Nomination')]/ancestor::vote/vote_number/text()")
    session_dict[session]['vote_number'].append(sorted(list(set(vote_num) | set(vote_num_3))))
print(session_dict)

def createDirectory():
    if os.path.isdir("Files"):
        print("Directory already exists")
    else:
        os.makedirs("Files")
        print("Directory named Files created")

print(session_dict[session]['vote_number'])
def download_files():
    for session in session_dict:
        session_n = session.replace('_', '')
        for num in session_dict[session]['vote_number'][0]:
            filename = "Files\{a}_{b}.txt ".format(a=session, b=num)
            if os.path.isfile(filename):
                continue
            else:
                url = "https://www.senate.gov/legislative/LIS/roll_call_votes/vote{c}/vote_{a}_{b}.xml".format(a=session, b=num, c=session_n)
                test = requests.get(url)
                response = urllib.request.urlopen(url)
                html = response.read()
                print("Year:", *session_dict[session]['year'], "Vote number:", num)
                open(filename, 'xb').write(html)


def get_majority(tree):
    ''' This method takes xml tree as an input and evaluate the what party voted in what majority in favor of the bill or not in favor'''
    republic_count = tree.xpath("count(//members/member/party[text() = 'R'])") #get total number of republic candidates for particular bill
    republic_count_yay = tree.xpath(
        "count(//members/member/party[text() = 'R']/following-sibling::vote_cast[text() = 'Yea'])") # get number of Republic candidates who voted Yea
    republic_count_nay = tree.xpath(
        "count(//members/member/party[text() = 'R']/following-sibling::vote_cast[text() = 'Nay'])") # get number of Republic candidates who voted Nay
    republic_novote = republic_count - (republic_count_yay + republic_count_nay) #number of people republicans who didn't vote on this particular bill
    democrats_count = tree.xpath("count(//members/member/party[text() = 'D'])") #get total number of democratic candidates for particular bill
    democrats_count_yay = tree.xpath(
        "count(//members/member/party[text() = 'D']/following-sibling::vote_cast[text() = 'Yea'])")# get number of Democratic candidates who voted Yea
    democrats_count_nay = tree.xpath(
        "count(//members/member/party[text() = 'D']/following-sibling::vote_cast[text() = 'Nay'])")# get number of Democratic candidates who voted Nay
    democrats_novote = democrats_count - (democrats_count_yay + democrats_count_nay)#number of people Democrats who didn't vote on this particular bill

    independent_count = tree.xpath("count(//members/member/party[text() = 'I'])") #get total number of independet candidates for particular bill
    independent_count_yay = tree.xpath(
        "count(//members/member/party[text() = 'I']/following-sibling::vote_cast[text() = 'Yea'])") # get number of Independent candidates who voted Yea
    independent_count_nay = tree.xpath(
        "count(//members/member/party[text() = 'I']/following-sibling::vote_cast[text() = 'Nay'])")# get number of Independent candidates who voted Nay
    independent_novote = independent_count - (independent_count_yay + independent_count_nay) #number of people Independent candidates who didn't vote on this particular bill

    #conditions to evaluate what party have what majority(Yay,Nay or No Majority)
    if democrats_count_yay > democrats_count_nay:
        demo_majority = 'Yea'
    elif democrats_count_nay > democrats_count_yay:
        demo_majority = 'Nay'
    else:
        demo_majority = 'No Majority'

    if republic_count_yay > republic_count_nay:
        rep_majority = 'Yea'
    elif democrats_count_nay > republic_count_yay:
        rep_majority = 'Nay'
    else:
        rep_majority = 'No Majority'

    if independent_count_yay > independent_count_nay:
        ind_majority = 'Yea'
    elif independent_count_nay > independent_count_yay:
        ind_majority = 'Nay'
    else:
        ind_majority = 'No Majority'


    return (demo_majority,rep_majority,ind_majority)


def analysis():
    ''' Function to evaluate the name,id, party, count of votes matching the party, count of votes not matching the party and count of votes marked as 'not voting' '''
    senators_dict = {} #dictionary to store senators data
    os.chdir("Files") #changing the directory
    dirs = os.listdir() #getting the list of files on the directory
    print("list of files",dirs)
    for count,file in enumerate(dirs): #looping through all the files
        with open(file, 'r') as myfile:
            tree = etree.parse(myfile) #parsing the xml formated file
            ids = tree.xpath("//members/member/lis_member_id/text()") #getting the list of Senator IDs who votes on this particular bill
            demo_majority, rep_majority, ind_majority = get_majority(tree) #calling get majority function to get what majority votes for (Yea,Nay or No Vote) for all the parties


            for i in ids: #looping through all the Senator Ids
                agree_count = 0  # how many times senators agreed with the party
                disagree_count = 0  # how many times senators disagreed with the party
                no_vote_count = 0  # how many times senators didn't vote
                total_count = 0  # how many times senators participated in the bill


                query_path= "//members/member/lis_member_id[text() = '{i}']/preceding-sibling".format(**locals())
                name = tree.xpath(query_path + '::first_name/text()') + tree.xpath(query_path + '::last_name/text()') #query to get the name od the cuurent senator id
                full_name = ' '.join(name) #changing the list to string
                party = tree.xpath(query_path + '::party/text()') #query to get the party of the current senator id
                party = ' '.join(party) #changing the list to string
                state = tree.xpath(query_path + '::state/text()')#query to get the state of the current senator id
                state = ' '.join(state) #changing the list to string
                vote = tree.xpath(query_path + '::vote_cast/text()')#query to get the vote of the current senator id
                vote = ''.join(vote) #changing the list to string
                s1 = senators(i,party,state,full_name,agree_count,disagree_count,no_vote_count, total_count)
                senators_dict = s1.senator_analysis(i,vote,rep_majority,demo_majority,ind_majority)



    print(senators_dict)
    print(len(senators_dict))

    return senators_dict



def print_output(dict):
    '''This method is used for showing the output in a table format'''

    #creatinf a dataframe with desired columns for the output
    df = pd.DataFrame(columns=('Senator Id','Name','Party','Count_Agreed','Count_Disagreed','Count_NoVote','Percentage_Matching','Percentage_NotMatching','Percentage_NotVoted'))

    #looping through the values of dictionary to fill the dataframe
    for i,id in enumerate(dict):
        df.loc[i,'Senator Id'] = id
        df.loc[i,'Name'] = dict[id]['Name']
        df.loc[i, 'Party'] = dict[id]['Party']
        df.loc[i, 'Count_Agreed'] = dict[id]['agreed']
        df.loc[i, 'Count_Disagreed'] = dict[id]['not_agreed']
        df.loc[i, 'Count_NoVote'] = dict[id]['no_vote']
        df.loc[i, 'Percentage_Matching'] = '{:.2f}'.format((dict[id]['agreed']/ dict[id]['total_count'])*100)
        df.loc[i, 'Percentage_NotMatching'] = '{:.2f}'.format((dict[id]['not_agreed'] / dict[id]['total_count']) * 100)
        df.loc[i, 'Percentage_NotVoted'] = '{:.2f}'.format((dict[id]['no_vote'] / dict[id]['total_count']) * 100)

    print(df)
    #writing output to the csvfile
    df.to_csv('\\..\\final_output.csv')




# createDirectory()
# download_files()
output_dict = analysis()
print_output(output_dict)

