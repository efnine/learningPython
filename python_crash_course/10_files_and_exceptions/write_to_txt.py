file_name = 'writing_test.txt'

with open(file_name, 'a') as file_object:
    u_id = input("What is your name? ")
    file_object.write(u_id + "\n")
    print("All done!")
