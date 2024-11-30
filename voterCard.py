class voterid:
    def __init__(self,name, age, address, constitution):
        self.name=name
        self.age=age
        self.address=address
        self.constitution=constitution

    def validateVoter(self,):
        if self.age > 18:
            print(f"{self.name} is valid voter")
            return True

    def printvoter(self):
        print(self.name, self.age)

voterDict=[{"name": "syam", "age":20}, {"name": "syam", "age": 28}]

for votertemp in voterDict:
    print(votertemp)
    voter1=voterid(name=votertemp.get("name"), age=votertemp.get("age"))
    status=voter1.validateVoter()
    if status == True:
        voter1.printvoter()



