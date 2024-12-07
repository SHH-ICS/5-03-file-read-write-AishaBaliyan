# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
filehandle = open("questions.txt", "w")

num_questions = input("How many questions for your quiz: ")
filehandle.write(num_questions + "\n")

for i in range(int(num_questions)):
    print() # format

    question_number = str(i + 1)

    filehandle.write(input("Enter Question " + question_number + ": ") + "\n")

    filehandle.write(input("Option A for question " + question_number + ": ") + "\n")
    filehandle.write(input("Option B for question " + question_number + ": ") + "\n")
    filehandle.write(input("Option C for question " + question_number + ": ") + "\n")
    filehandle.write(input("Option D for question " + question_number + ": ") + "\n")

    filehandle.write(input("Correct answer for question " + question_number + ": ") + "\n")

filehandle.close()