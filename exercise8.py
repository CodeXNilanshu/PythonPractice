# Exercise 8

# I have to use loop in this
# I have a list of questions
# Question number should be dynamic
# I have to also check answers for questions
# lower()
# final score - calculate score

number = 0
answer = [
    'Paris',
    'Jupiter',
    'Leonardo da Vinci'
]

question_list = [
"Question $number: What is the capital of France?\n"
"Question $number: What is the largest planet in our solar system?\n"
"Question $number: Who painted the Mona lisa?\n"
]



calculated_score = '$$$calculate'
your_answer = 'Your answer: '
final_score = 'Your final score is: $calculated_score'

right = 'Correct!'
Wrong = 'Incorrect. Correct answer is $asnwer'

i = 0
while i < (len(question_list)):
    print(question_list[i])
    input(your_answer)
    continue
    i+=1

