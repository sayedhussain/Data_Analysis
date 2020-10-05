
class senators:
    senators_dict ={} #class dictionary to store the information about the all senator ids
    def __init__(self,sid,party,state,full_name,agree_count,disagree_count,no_vote_count, total_count):

        self.sid = sid
        self.state = state
        self.full_name = full_name
        self.party = party
        self.agree_count = agree_count
        self.disagree_count  = disagree_count
        self.no_vote_count = no_vote_count
        self.total_count = total_count


    def senator_analysis(self,i,vote,rep_majority,demo_majority,ind_majority):
        ''' Make an en entry into the dictionary for that particular senator id and returns the dictionary back o the caller'''
        s = senators
        if i in s.senators_dict:  # if the current id already in the senators_dict dictionary then only modify the total_count, agreed, no_count and not agreeed values of the senator candidate id's dictionary
            s.senators_dict[i]['total_count'] += 1  # increasing the total count for particular senator id
            if self.party == 'R':  # if the senator is Republican modify the values accordingly
                if vote == 'Not Voting':
                    s.senators_dict[i]['no_vote'] += 1
                elif vote == rep_majority:
                    s.senators_dict[i]['agreed'] += 1
                else:
                    s.senators_dict[i]['not_agreed'] += 1

            if self.party == 'D':  # if the senator is Democrat modify the values accordingly
                if vote == 'Not Voting':
                    s.senators_dict[i]['no_vote'] += 1
                elif vote == demo_majority:
                    s.senators_dict[i]['agreed'] += 1
                else:
                    s.senators_dict[i]['not_agreed'] += 1

            if self.party == 'I':  # if the senator is Independent modify the values accordingly
                if vote == 'Not Voting':
                    s.senators_dict[i]['no_vote'] += 0
                elif vote == ind_majority:
                    s.senators_dict[i]['agreed'] += 0
                else:
                    s.senators_dict[i]['not_agreed'] += 0
        else:  # if the id doesn't exist in senators_dict dictionary then create new values and fill them up
            if self.party == 'R':  # if the senator is Republican initialize the values accordingly
                if vote == 'Not Voting':
                    self.no_vote_count = 1
                elif vote == rep_majority:
                    self.agree_count = 1
                else:
                    self.disagree_count = 1

            if self.party == 'D':  # if the senator is Democrat initialize the values accordingly
                if vote == 'Not Voting':
                    self.no_vote_count = 1
                elif vote == demo_majority:
                    self.agree_count = 1
                else:
                    self.disagree_count = 1

            if self.party == 'I':  # if the senator is Independent initialize the values accordingly
                if vote == 'Not Voting':
                    self.no_vote_count = 0
                elif vote == ind_majority:
                    self.agree_count = 0
                else:
                    self.disagree_count = 0

            # initialize the values of the dictionay for a particular senator id
            self.total_count = 1
            s.senators_dict[i] = dict()
            s.senators_dict[i]['Name'] = self.full_name
            s.senators_dict[i]['State'] = self.state
            s.senators_dict[i]['Party'] = self.party
            s.senators_dict[i]['agreed'] = self.agree_count
            s.senators_dict[i]['not_agreed'] = self.disagree_count
            s.senators_dict[i]['no_vote'] = self.no_vote_count
            s.senators_dict[i]['total_count'] = self.total_count


        return s.senators_dict
