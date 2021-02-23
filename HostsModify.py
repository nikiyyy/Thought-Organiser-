def listSites():
    with open(r"C:\Windows\System32\drivers\etc\hosts","r") as f:
        fileContent=f.readlines()
        for i in fileContent:
            print(i)


def addSite():
    website=input("Please enter website URL or enter /// to exit \nExample: www.example.com \n")
    if website != "///":
        with open(r"C:\Windows\System32\drivers\etc\hosts","a") as f:
            f.write("\n127.0.0.1		"+website)
            
            
def removeSite():
    website=input("Please enter website URL or enter /// to exit \nExample: www.example.com \n")
    if website != "///":
        rows=[]
        
        with open(r"C:\Windows\System32\drivers\etc\hosts","r") as f:
            fileContent=f.readlines()
            for i in fileContent:
                if website in i:
                    continue
                rows.append(i)   
        with open(r"C:\Windows\System32\drivers\etc\hosts","w") as f:
            for i in rows:
                f.write(i)              

try:
    choise = 0
    while choise != "///":
        choise=input("Please enter the corresponding number : \n1. List all blocked websites\n2. Add website URL to The blocked website list\n3. Remove website URL to The blocked website list\n4. Exist\n")
        if choise == '1':
            listSites()
            
        elif choise == '2':
            addSite()
            
        elif choise == '3':
            removeSite()
            
        elif choise == '4':
            break
   
    
except:
   print("Something went wrong!")    
