from datetime import datetime

class Tasks:
    def __init__(self, name, priorty, typeofwork):
        self.name=name
        self.priorty=priorty
        self.typeofwork=typeofwork
        self.dateAdded=datetime.today().strftime('%Y-%m-%d')
        #self.timeToComplete=timeToComplete
    
    def __str__(self):
        return '' + self.name +" "+ self.typeofwork +" "+ self.priorty +" "+ self.dateAdded
    
def addTask(task, typeofwork, priority):
    obj1 = Tasks(task, typeofwork, priority)
    with open("data.txt","a") as f:
        f.write("\n"+str(obj1))
            
    
    
def listTasks():
    with open("data.txt","r") as f:
        fileContent=f.readlines()
#        for i in fileContent:
#            print(i)
        return fileContent
#obj1 = Tasks("test2", "high", "profesional")
#print(obj1)