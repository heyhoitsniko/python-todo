from datetime import datetime
#Get today's date
today = datetime.today().date()


print( "The current date: ", today)

def greeting(name, Birth_Year):
    Age = today.year - Birth_Year
    print (name + " is " + str(Age) + " years old")


greeting("Niko", 1996)
greeting(name = "Adam", Birth_Year= 1996)


