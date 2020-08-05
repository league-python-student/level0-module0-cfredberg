from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0;
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question = ""
    answer = ""
    #      // 3.  Use an if statement to check if their answer is correct
    for i in range(4):
        if i == 0:
            question = simpledialog.askstring(None, "What is the creator of this program's name?")
            answer = "charlie"
        elif i == 1:
            question = simpledialog.askstring(None, "What programming language was used to make this game?")
            answer = "python"
        elif i == 2:
            question = simpledialog.askstring(None, "What is the creator of this program's favorite programming language?")
            answer = "java"
        elif i == 3:
            question = simpledialog.askstring(None, "What does the creator of this program do with DOSBox?")
            answer = "run old versions of windows"
        if question.lower() == answer:
            #      // 4.  if the user's answer was correct, add one to their score
            score+=1
        else:
            score-=1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(None, "You got " + str(score) + "/4 points")
    # Run the window's .mainloop() method
    window.mainloop()