class Classroom:
    Name=""
    Age=0
    Gender=""
    Class=45
    Mobile_number=12
    def inv(self):
        print('''
            Welcome {0}
                Age:{1}
                Gender:{2}
                Class:{3}
                Mobile_number:{4}
                '''.format(self.Name,self.Age,self.Gender,self.Class,self.Mobile_number))
room=Classroom()
room.Name=input("Enter name:")
room.Age=int(input("Enter age:"))
room.Gender=input("Enter M/F:")
room.Class=int(input("Enter class:"))
room.Mobile_number=int(input("Enter mobile number:"))
print(room.inv())





