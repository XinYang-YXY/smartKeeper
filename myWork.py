### Import Libs
import os
import pandas as pd

import datetime #For date range checking
from datetime import date #For date range checking
from dateutil.rrule import rrule, DAILY #For date range checking

from pathlib import Path
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates #matplotlib dates
counter = ""

#Data Visualization
#SOlve convertor problem
#import pandas.plotting._converter as pandacnv
#pandacnv.register()

#####
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#####

#from pandas.tseries import converter
#converter.register() 

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def timeGraph(data, graphPurpose):
    dates = list(dict.fromkeys(data["Date"]))
    spend = [0] * len(dates)

    for date in dates:
        for record, value, itemNum in zip(data["Date"], data["itemPrice(S$)"], data["itemNum"]):
            if date == record:
                spend[dates.index(record)] += (value * itemNum)
    

    #plt.style.use("fivethirtyeight")
    #plt.xkcd()
    plt.style.use("seaborn")
    dates = pd.to_datetime(dates)
    plt.plot_date(dates, spend, linestyle="solid")
    plt.gcf().autofmt_xdate() #the dates are rotated
    plt.tight_layout()
    plt.title(graphPurpose)
    plt.xlabel("Time")
    plt.ylabel("S$")
    plt.grid(True)
    plt.show()
    
    spendSorted = spend
    spendSorted.sort()
    print(color.RED+"If graph is not shown, please RE-RUN the program"+color.END)
    print("On", str(dates[spend.index(spendSorted[-1])])[:-9], "You have the HIGHEST spending of S$" + str(spendSorted[-1]),"In one day")
    print("On", str(dates[spend.index(spendSorted[0])])[:-9], "You have the LOWEST spending of S$" + str(spendSorted[0]),"In one day")

#Get the full record given a date range
def startDate():
    return input("Start Date ")
def endDate():
    return input("End Date ")
def searchDate(data):
    gettingDates = [startDate, endDate]
    dates = ["", ""]
    progress = 0
    
    while progress < len(gettingDates):
        dates[progress] = gettingDates[progress]()
        if dates[progress] == "00":
            progress -= 1
            if progress < 0:
                print("\U0001F4A5"*3 + "Session Abandoned!" + "\U0001F4A5"*3)
                return
        elif dates[progress] == "000":
            print("\U0001F4A5"*3 + "Session Abandon!" + "\U0001F4A5"*3)
            return
        else:
            progress += 1
    
    df = pd.DataFrame(data)
    result = pd.DataFrame()


    a = datetime.datetime.strptime(dates[0], "%Y-%m-%d")
    b = datetime.datetime.strptime(dates[1], "%Y-%m-%d")
    for dt in rrule(DAILY, dtstart=a, until=b):
        temp = df.loc[df["Date"] == dt.strftime("%Y-%m-%d")]
        result = pd.concat([result, temp])
    if result.empty:
        print("No record found given the date range")
    else:
        print(result)
#Get the full record given a date range

#Above New features, less stable 

#Define a new type of ERROR to catch
class emptyError(Exception):
    pass


#UserMenu
def userMenu():
    print("User Menu\U0001F4D6")
    print("""
    \U0001F4CEUseful Things
        \U0001F4CC '000': Abandon the inputting session.
        
        \U0001F4CC '00' : Jump back to previous input field 
                  or abandon session if previous field does not exist. 
    
    
    \U0001F4CEHow does the program deal with your data
        \U0001F4CC The program will store all the data 
           you input into 3 files in the same location
           of the program.

        \U0001F4CC If the filename you input does not exist,
           it will create a file with that filename,
           if it exists, the data in the file will be 
           loaded.
           
       """)
#Getting the NAME of the item
def getName():
    while True:
        try:
            itemName = input("Item Name: ")
            if itemName == "":
                raise emptyError
            return itemName
            break
        except emptyError:
            print("Empty input is invalid")
#Getting the TYPE of the item
def getBrand():
    while True:
        try:
            itemType = input("Item Type: ")
            if itemType == "":
                raise emptyError
            return itemType
            break
        except emptyError:
            print("Empty input is invalid")
#Getting the PRICE of the item
def getPrice():
    while True:
        try:
            itemPrice = input("Item Price: S$")
            if float(itemPrice) < 0:
                raise ValueError
            elif itemPrice == "0":
                raise ValueError
            return itemPrice
            break
        except ValueError:
            print("Please enter a valid value!")
#Getting the WEIGHT of the item
def getWeight():
     while True:
        try:
            itemWeight = input("Item Weight(kg): ")
            if float(itemWeight) < 0:
                raise ValueError
            elif itemWeight == "0":
                raise ValueError
            else:
                return itemWeight
            break
        except ValueError:
            print("Please enter a valid value!")
#Getting the Number of the item
def getNum():
    while True:
        try:
            itemNum = input("Number of item ")
            if float(itemNum) < 0:
                raise ValueError
            elif itemNum == "0":
                raise ValueError
            return itemNum
            break
        except ValueError:
            print("Please enter a valid value!")
 #Getting the ORIGIN of the item
def getOrigin():
    while True:
        try:
            itemOrigin = input("Country Origin: ")
            if itemOrigin == "":
                raise emptyError
            return itemOrigin
            break
        except emptyError:
            print("Empty input is invalid")
            
#Function to get a set of 5 fields from user
def gettingInputs(data, data2):
    itemName = ""
    itemType = ""
    itemPrice = 0
    itemWeight = 0
    itemNum = 0
    itemOrigin = ""

    date = str(pd.datetime.now().date())
    gettingVariables = ["", "", 0, 0, 0, ""]
    gettingFunctions = [getName, getBrand, getPrice, getWeight, getNum, getOrigin]
    progress = 0
    
    while progress < len(gettingVariables):
        gettingVariables[progress] = gettingFunctions[progress]()
        
        if gettingVariables[progress] == "00":
            progress -= 1
            if progress < 0:
                print("\U0001F4A5"*3 + "Session Abandoned!" + "\U0001F4A5"*3)
                return
        elif gettingVariables[progress] == "000":
            print("\U0001F4A5"*3 + "Session Abandon!" + "\U0001F4A5"*3)
            return
        else:
            progress += 1
    
    data["Date"].append(date)
    
    data["itemName"].append(gettingVariables[0])
    data2["itemName"].append(gettingVariables[0])
    
    data["itemType"].append(gettingVariables[1])
    
    data["itemPrice(S$)"].append(float(gettingVariables[2]))
    
    data["itemWeight(KG)"].append(float(gettingVariables[3]))
    
    data["itemNum"].append(float(gettingVariables[4]))
    data2["itemNum"].append(float(gettingVariables[4]))
    
    data["itemOrigin"].append(gettingVariables[5])
    
def takeItemsName():
    while True:
        try:
            itemName = input("Item Name: ")
            if itemName == "":
                raise emptyError
            return itemName
            break
        except emptyError:
            print("Empty input is invalid")
def takeItemsNum():
    while True:
        try:
            itemNum = input("Number of item ")
            if float(itemNum) < 0:
                raise ValueError
            elif itemNum == "0":
                raise ValueError
            return itemNum
            break
        except ValueError:
            print("Please enter a valid value!")
def takeItems(data2, data3, data4):
    progress = 0
    takingVariables = ["", 0]
    takingFunctions = [takeItemsName, takeItemsNum]
    
    while progress < len(takingFunctions):
        takingVariables[progress] = takingFunctions[progress]()
        
        if takingVariables[progress] == "00":
            progress -= 1
            if progress < 0:
                print("\U0001F4A5"*3 + "Session Abandoned!" + "\U0001F4A5"*3)
                return
        elif takingVariables[progress] == "000":
            print("\U0001F4A5"*3 + "Session Abandon!" + "\U0001F4A5"*3)
            return
        else:
            progress += 1
    #Changes to data2
    index = data2["itemName"].index(takingVariables[0])
    data2["itemNum"][index] -= float(takingVariables[1])
    
    #Record down to data3
    data3["itemName"].append(takingVariables[0])
    data3["itemNum"].append(float(takingVariables[1]))
    
    date = str(pd.datetime.now().date())
    data3["Date"].append(date)
    
    #Record down to data4
    data4["itemName"].append(takingVariables[0])
    data4["itemNum"].append(float(takingVariables[1]))
    
def display(counter):
    if "520" in counter and "*" in counter:
        print("        " + "\U0001F496"*3 + "\U0001F48F" + "\U0001F496"*3)
        return counter
    elif "520" in counter:
        print("        " + "\U0001F496"*3 + "\U0001F48F" + "\U0001F496"*3)
        print("\U0001F495"*16 + """
\U0001F49ETo my cute cute sweetie\U0001F428\U0001F43C  \U0001F49E
\U0001F49Ethanks for being here with me\U0001F49E
\U0001F49Ealways love you and miss you~\U0001F49E""" + "\n" + "\U0001F495"*16)
        counter += "*"
        return counter
    else:
        return counter
def sortFile2(data2):
    itemNames = list(dict.fromkeys(data2["itemName"]))
    nameTimes = [0] * len(itemNames)
    for itemName in itemNames:
        for record, value in zip(data2["itemName"], data2["itemNum"]): 
            if itemName == record:
                nameTimes[itemNames.index(record)] += value
    
    data2["itemName"] = itemNames
    data2["itemNum"] = nameTimes
    
def saveBack(data, data2, data3, data4, fileName):
    
    df = pd.DataFrame(data)
    df2 = pd.DataFrame(data2)
    df3 = pd.DataFrame(data3)
    df4 = pd.DataFrame(data4)
 
    df.to_csv(FILENAME + "/" + fileName)   #*****************
    df2.to_csv(FILENAME + "/current" + fileName)  #*****************
    df3.to_csv(FILENAME + "/sold" + fileName)   #*****************
    df4.to_csv(FILENAME + "/totalSold" + fileName)   #*****************

def displayInfo(data, data2, data3, data4):
    df = pd.DataFrame(data)
    df2 = pd.DataFrame(data2)
    df3 = pd.DataFrame(data3)
    df4 = pd.DataFrame(data4)
    
    print()
    print("\U0001F4A0"*5 + "All Collected Data" + "\U0001F4A0"*5)
    print("\U0001F4DC"*3 +"Full Record" + "\U0001F4DC"*3)
    print(df, end="\n\n")
    print("\U0001F6AA"*3 + "Current items inside the storeroom" + "\U0001F6AA"*3)
    print(df2, end="\n\n")

    print("\U0001F4B5"*3 + "Selling record" + "\U0001F4B5"*3)
    print(df3, end="\n\n")
    print("\U0001F4B0"*3 + "Total Selling record" + "\U0001F4B0"*3)
    print(df4, end="\n\n")
def displayInfo1(data):
    df = pd.DataFrame(data)
    print()
    print("\U0001F4DC"*3 + "Full Record" + "\U0001F4DC"*3)
    print(df, end="\n\n")
def displayInfo2(data2):
    df = pd.DataFrame(data2)
    print()
    print("\U0001F6AA"*3 + "Current items inside the storeroom" + "\U0001F6AA"*3)
    print(df, end="\n\n")
def displayInfo3(data3):
    df = pd.DataFrame(data3)
    print()
    print("\U0001F4B5"*3 + "Selling Record" + "\U0001F4B5"*3)
    print(df, end="\n\n")
def displayInfo4(data4):
    df = pd.DataFrame(data4)
    print()
    print("\U0001F4B0"*3 + "Total Selling Record Of Each Item" + "\U0001F4B0"*3)
    print(df, end="\n\n")
def whatRunningLow(data2):
    df = pd.DataFrame(data2)
    print(df.sort_values(["itemNum"], ascending=[True]))


print("\U0001F4AE"*5 + "Welcome" + "\U0001F4AE"*5)
userMenu()
fileName = input("Name of your file\U0001F5C3: ") + ".csv"
FILENAME = fileName[:-4]

if os.path.isdir(FILENAME):     #*****************
    #File 1 fileName.csv
    df = pd.read_csv(os.path.join(FILENAME,fileName))  #********************
    data = df.to_dict("list")
    del data["Unnamed: 0"]

    #File 2 currentfilename.csv
    df2 = pd.read_csv(os.path.join(FILENAME,"current" + fileName)) #********************
    data2 = df2.to_dict("list")
    del data2["Unnamed: 0"]

    #File 3 soldfileName.csv
    df3 = pd.read_csv(os.path.join(FILENAME,"sold" + fileName)) #********************
    data3 = df3.to_dict("list")
    del data3["Unnamed: 0"]
    
    #File 4 totalSoldfileName.csv
    df4 = pd.read_csv(os.path.join(FILENAME,"totalSold" + fileName))  #********************
    data4 = df4.to_dict("list")
    del data4["Unnamed: 0"]
else:
    #Data structure to hold the collected data, dict + list
    os.makedirs(FILENAME)    #**********************
    data = {"Date": [],
            "itemName": [],
            "itemType": [],
            "itemPrice(S$)": [],
            "itemWeight(KG)": [],
            "itemNum": [],
            "itemOrigin": []
    }
    data2 = {
        "itemName": [],
        "itemNum": []
    }
    data3 = {
        "Date" : [],
        "itemName": [],
        "itemNum": []
    }
    data4 = {
        "itemName": [],
        "itemNum": []
    }

fileName2 = "used"+fileName
config2 = Path(os.path.join(FILENAME,fileName2))
if config2.is_file():
    f = open(os.path.join(FILENAME,fileName2), "r+")
    counter = f.read()
else:
    f = open(os.path.join(FILENAME,fileName2), "a")

while True:
    print()
    counter = display(counter)
    print("\U0001F338"*5 + "Home  Menu" + "\U0001F338"*5 )
    print("    1)Input data to the databases\U0001F4E5")
    print("    2)Sell Items\U0001F4B5")
    print("    3)Check collected data\U0001F575")
    print("    4)Handy tools\U0001F9F0")
    print("    5)Stop the program\U0001F91A")
    userOption = int(input("Which operation do you want to carry out(1/2/3/4/5/[32\U0001F47B]): "))

    while userOption == 1:
        gettingInputs(data, data2)
        sortFile2(data2)
        saveBack(data, data2, data3, data4, fileName)
        repeatAgain = input("Do you want to continue to input data(y/n)?\U0001F503 ").lower()
        if repeatAgain == "n":
            break

    if userOption == 2:
        takeItems(data2, data3, data4)
        sortFile2(data4)
        saveBack(data, data2, data3, data4, fileName)
        #sortFile2(data3)
        counter += "2"

    if userOption == 3:
        print()
        print("\U0001F4D6"*3 + "Which database" + "\U0001F4D6"*3)
        print("    1)Full Buying Record\U0001F4DC")
        print("    2)Current items inside the storeroom\U0001F6AA")
        print("    3)Selling Record\U0001F4B5")
        print("    4)Total Selling Record Of Each Item"+ "\U0001F4B0")
        print("    5)ALL")
        userOption2 = int(input("Take a closer look\U0001F9D0 "))
        
        if userOption2 == 1:
            displayInfo1(data)   
        elif userOption2 == 2:
            displayInfo2(data2)  
        elif userOption2 == 3:
            displayInfo3(data3)
        elif userOption2 == 4:
            displayInfo4(data4)
        elif userOption2 == 5:
            displayInfo(data, data2, data3, data4)
            
    if userOption == 32:
        displayInfo2(data2)
    
    if userOption == 0:
        counter += "0"

    if userOption == 4:
        print()
        print("\U0001F97A"*5 + "Your cute cute handy tools!" + "\U0001F97A"*5)
        print("    1)What To Buy Next Time?", "\U0001F6D2"*3)
        print("    2)Spending Over time", "\U0001F4B9"*3)
        print("    3)Buying Record Given A Date Range", "\U0001F552"*3)
        print("    4)Taking Record Given A Date Range", "\U0001F55E"*3)

        toolToUse = int(input("Which tool do you want to use(1/2/3/4/5): "))

        if toolToUse == 1:
            whatRunningLow(data2)
        if toolToUse == 2:
            if len(data["itemName"]) != 0:
                timeGraph(data, "Spending Over Time")
        if toolToUse == 3:
            searchDate(data)   #See if can also apply to taking record or not
        if toolToUse == 4:
            searchDate(data3)
            

    if userOption == 5:
        saveBack(data, data2, data3, data4, fileName)  #Changes
        print("Thanks for using the Program, Good Byte!\U0001F916")
        counter+= "5"
        #Solve the self multiple problem in used.csv
        f.seek(0)
        f.truncate()
        f.write(counter)
        f.close()
        break
