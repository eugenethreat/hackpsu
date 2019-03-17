##https://www.absecom.psu.edu/ONLINE_CARD_OFFICE/USER_PAGES/PSU_USER_MENU_WIN.cfm
#https://www.absecom.psu.edu/ONLINE_CARD_OFFICE/USER_PAGES/LC_90DAY_REVIEW_ACT.cfm -- transaction history


#miles/jack - login
#me - scraping
#andy - output formatting



import urllib.request
import os 
from bs4 import BeautifulSoup

def func():
    print(os.getcwd())
    #the actual function 
    aa = "https://www.absecom.psu.edu/ONLINE_CARD_OFFICE/USER_PAGES/LC_90DAY_REVIEW_ACT.cfm"    
    page = urllib.request.urlopen(aa)
    soup = BeautifulSoup(page, 'html.parser')
    
    filename = "src.txt"
        #src.txt is a placeholder; its contents is the html of the payment history 
    file = open(filename, "r")

    parser(filename)

def parser(filename):
    output = open(filename, "r")

    num_lines = sum(1 for line in open(filename,"r"))
        #362 lines total

    transList =[] #contents of the indexes where transacations occur "withdrawal" 
    transInd = [] # indexes where transactions take place 
    totalList = [] #the entire page, line by line in a list
    
    def iterator():
        for x in range(num_lines):
            #print(output.readline())
                #prints the entire function
            currStr = output.readline() #parses the line currently in the loop
            totalList.append(currStr)
            
            bbb = (currStr.find("Withdrawal") )#parsing through the string for specifics 
            if bbb != -1:
                line = x
                transList.append(currStr)
                transInd.append(x)
        return transList #returns a list with the line# that contains "withdrawal" 

    transListy = iterator() #saves the lines that contain transactions in a list

    #print(transListy) #prints the elements containing "withdrawl" 
    #print(totalList) #saves the entire document with each line as it's own element in a list 
    #print(transInd, " indexes where transactions occured")
    #print("Total transactions= ", len(transListy))

    asdf = 0

    for y in range(len(transList)): #iterates as many times as there are transactions 
        #save the indexes around it as separate strings

        #we have totallist, that contains the entire list on sepearte lines. we need the 2 before and the 4 after
        #in order to get a complete transaction history

        #grab the numbers of the "withdrawal" (from transInd
        #use that number to access the contents  from totalList

        sadf = 0
        phl = []
        indx = []
        indx2 = []
        table = str.maketrans(dict.fromkeys("\n\td<>'"))
        
        
        for z in range(len(totalList)):

            if "Campus Meal Plan" in totalList[z] or "PM" in totalList[z] or "AM" in totalList[z] or "withdrawal" in totalList[z] or "HFS" in totalList[z] or "West Wing" in totalList[z] or "Waring Square" in totalList[z]:
                indx.append(z) #should correspond to hold indexes of the items in ph1
                if "West Wing" in totalList[z] or "Waring Square" in totalList[z]:

                    money = totalList[z+3]
                    money = money.translate(table)
                    
                    phl.append(money)
                    
                strstr = str(totalList[z])
                editStr = strstr.translate(table)
                phl.append(editStr)

        phl.pop(len(phl) - 1) #removes the last element, which is the "date last edited" thing 
        #print(indx2, "index2")
        #print(indx, "index") - contains the index numbers of the elements in the list           

    for a in range(len(phl)):
        if a == 0:
            print()
        else:
            print(phl[a])
    print(phl[0], "eeeee")

    
func()
