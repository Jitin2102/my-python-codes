import time  as t
def Calperiod():
    product=1
    for i in range(1,800):
        product=product*i
    return product
startTime=t.time()
prod=Calperiod()
endTime=t.time()
print('The result is %s digits long.'% (len(str(prod))))
print('took %s seconds to calculate.'% (endTime-startTime))    