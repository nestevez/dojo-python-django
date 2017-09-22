import random

def scores_and_grades(amt):
    ''' Generates a given number of random scores and prints the associated grade for each one '''
    print "Scores & Grades"
    for i in range(0, amt):
        score = random.randint(0,100)
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print "Score:",score,"; Your grade is", grade
    print "End of the program. Bye!"

amt = 10
scores_and_grades(amt)
