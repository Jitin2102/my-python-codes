import random

def getAnswer(answerNum):
    if answerNum==1:
        return 'It is certain'
    elif answerNum==2:
        return 'It is decidely so'
    elif answerNum==3:
        return 'Yes'
    elif answerNum==4:
        return 'Try again'
    elif answerNum==5:
        return 'Ask again later'
    elif answerNum==6:
        return 'Concentrate and ask again'
    elif answerNum==7:
        return 'My reply is no'
    elif answerNum==8:
        return 'Outlook not so good'
    elif answerNum==9:
        return 'Very Doubtful'

r=random.randint(1,9)
fortune=getAnswer(r)
print(fortune)    