#author : sayed shazeb

def read_data(file_path):
    try:
        with open(file_path) as fobj:
            for line in  fobj:
                #initializing the variables
                date_range = []
                landslides = []
                max_wind = 0
                #getting the header values
                id_cyclone,name,rows = get_header(line)
                print("Storm System Id : ",id_cyclone)
                print("Storm Name:" ,name)
                #extracting the reevant information
                for i in range(0,rows):
                    cyclone_row= fobj.readline().split(',')
                    date = cyclone_row[0]
                    date = date[0:4]+"-"+date[4:6]+"-"+date[6:]
                    date_range.append(date)
                    if cyclone_row[2].strip():
                        landslides.append(cyclone_row[2])
                    max_wind = max_wind if int(cyclone_row[6]) < max_wind else int(cyclone_row[6])



                print("Cyclone date range :", date_range)
                print("Maxwind :", max_wind)
                print("Number of Landfall :", len(landslides))
                landslides.clear()
                date_range.clear()

    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno, strerror))
    except Exception as es:
        print(es)
        print("Some error occured")





#author : sayed shazeb
#function to get the header values of each storm or hurricane
def get_header(line):
    header = line
    header = header.split(',')
    id_cyclone, name, rows = header[0:len(header) - 1]
    id_cyclone, name, rows = id_cyclone.strip(), name.strip(), int(rows.strip())
    return [id_cyclone,name,rows]


#Coded by Smriiti Singhal
def summary(file_path):
    number_of_hurrincanes__peryear = {}
    number_of_storms__peryear = {}
    try:
        with open(file_path) as fobj1:
            for line1 in fobj1:
                #getting the variables for cyclone
                id_cyclone, name, rows = get_header(line1)

                #extracting hurricane and storms from the data
                for i in range(0, rows):
                    cyclone_row = fobj1.readline().split(',')
                    year = cyclone_row[0][:4]
                    if (cyclone_row[3].strip() == "HU"):
                        if year in number_of_hurrincanes__peryear.keys():
                            number_of_hurrincanes__peryear[year].add(id_cyclone)
                        else:
                            number_of_hurrincanes__peryear[year] = set([id_cyclone])

                if year not in number_of_hurrincanes__peryear.keys():
                    if year in number_of_storms__peryear.keys():
                        number_of_storms__peryear[year].append(id_cyclone)
                    else:
                        number_of_storms__peryear[year] = [id_cyclone]
            #displaying the information
            print("Year ", "Number of Hurricanes")
            for year in number_of_hurrincanes__peryear.keys():
                print(year, len(number_of_hurrincanes__peryear[year]))
            print("\n")
            print("*****************************************************************************")
            print("\n")
            print("Year ", "Number of Storms")
            for year in number_of_storms__peryear.keys():
                print(year, len(number_of_storms__peryear[year]))
    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno, strerror))
    except Exception as es:
        print(es)
        print("Some error occured")








file_path = "C:\\files\\Atlantic.txt"
read_data(file_path)
summary(file_path)