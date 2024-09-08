#For question, please refer to "practice.txt" file.
#Solution

with open("demo.txt", "r") as f:
    data = f.read()
    if(data.find("Hello") != -1):
        print("Found")
    else:
        print("Not found")
    