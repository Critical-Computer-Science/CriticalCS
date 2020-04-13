import names as n
import random as r

#O(N)
def createData(fname, magnitude):
    genders = ["male", "female", "None"]
    header = ["Name", "ID", "Age", "Gender", "Illness", "Admittor", "Hospital"]
    admittors = [n.get_full_name() for i in range(magnitude//3)]
    ID_set = set()
    illnesses = ["AIDS", "Coronavirus", "Pregnancy", "Back Pain", "Headache", "Chest Pain", "Broken Bone"]
    hospitals = ["Honor Grave General Hospital", "Progress Medical Center", "Hallmark Clinic", "Diamond Grove Clinic", "Bellevue Medical Clinic", "Summer Springs Medical Center", "Kindred Medical Clinic", "Jade Forest General Hospital", "Healthstone Medical Center", "Trinity Clinic"]
    
    f = open(fname, "w")
    
    temp = str()
    for i in header:
        temp = temp + i + "\t"
    f.write(temp.strip()+"\n")
    #f.write("\n")
    
    for i in range(magnitude):
        temp = str()
        
        age = r.randint(18, 90)
        #Age
        
        current_gender = r.choice(genders)
        #Gender
        
        name = n.get_full_name(gender=current_gender)
        #Name
        
        ID = r.randint(100000, 999999)
        while ID in ID_set:
            ID = r.randint(100000, 999999)
        ID_set.add(ID)
        #ID

        illness = r.choice(illnesses)
        while illness.lower() == "pregnancy" and current_gender.lower() == "male":
            illness = r.choice(illnesses)
        #Illness
        
        admittor = r.choice(admittors)
        #Admittor
        
        hospital = r.choice(hospitals)
        #Hospital 
        
        temp = temp + name + "\t" + str(ID) + "\t" + str(age) + "\t" + current_gender + "\t" + illness + "\t" + admittor + "\t" + hospital
        f.write(temp+"\n")
    f.close()

#O(N^3) or O(N^2)
def multiCreate(pre_dot, post_num, start, magnitude, count, sequence=None):
    num = start
    if sequence:
        sequence = sequence.lower()
    for i in range(1, count+1):
        createData("{}{}{}".format(pre_dot, i, post_num), num)
        if sequence in {"g", "geometric"}:
            num = num*magnitude
        elif sequence in {"a", "arithmetic"}:
            num = num+magnitude
        else:
            num = num+magnitude


if __name__ == "__main__":
    #createData("data_set_4.tsv", 10000)
    multiCreate("new_data_", ".tsv", 50, 50, 10)
    