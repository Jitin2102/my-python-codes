def modify(original):
    original +=" that has been modified."
def modifyReturn(original):
    original+=" that has been modified." 
    return original
testString="This is a test string"
print(testString)

testString=modifyReturn(testString)
print(testString)   