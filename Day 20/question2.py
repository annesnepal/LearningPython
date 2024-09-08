#For question, please refer to "practice.txt" file.
#Solution
with open("demo.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("Java", "Python")
print(new_data)

with open("demo.txt", "w") as f:
    f.write(new_data)
