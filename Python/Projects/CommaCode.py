spam=['apples','banana','tofu','cats']
def String(spam):
    result="\'"
    for i in range(len(spam)):
        result= result+spam[i]
        if i != 3:
             result=result +","
        else:
            result= result+"\'"     
    return result

print(String(spam))    
        
        