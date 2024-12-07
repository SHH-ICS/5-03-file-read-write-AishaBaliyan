# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.

inFile = open("questions.txt", 'r')

correct_score = 0
num_questions = int(inFile.readline())

# Read 6 lines at a time
for i in range(int(num_questions)):
    print("Question " + str(i + 1) + ": " + inFile.readline() + "Option A: " + inFile.readline() + "Option B: " + inFile.readline() + "Option C: " + inFile.readline() + "Option D: " + inFile.readline())

    correct_answer = inFile.readline()

    user_answer = input("Enter your answer: ")

    if user_answer == correct_answer[0]:
        correct_score += 1
    
    print() # format

print(str(correct_score/num_questions * 100) + "%")

inFile.close()