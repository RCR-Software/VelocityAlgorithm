def calulateVelocity():
    #Variables needed for caluation
    sumBMPTimes = 0
    sumBMPTimes2 = 0
    sumAlt = 0
    sumAltTimes = 0
    leftSide = 0
    rightSide = 0
    
    #Find sums for BMP
    for i in range(0, NUM_ALT_READINGS):
        sumBMPTimes += BMPTimes[i]
        sumBMPTimes2 += (BMPTimes[i]**2)
        sumAlt += altitudes[i]
        sumAltTimes += (altitudes[i] * BMPTimes[i])        

    #Calulate left side of equation
    leftSide =  ((sumBMPTimes * sumAlt) - (NUM_ALT_READINGS * sumAltTimes)) / (((sumBMPTimes)**2) - (NUM_ALT_READINGS* sumBMPTimes2))

    #Calculate rightSide of equation
    for i in range((NUM_ACCEL_READINGS/2),(NUM_ACCEL_READINGS-1),1):
        rightSide += (.5*(accelerationFromBNO[i] + accelerationFromBNO[i+1])*(BNOTimes[i+1]-BNOTimes[i]))

    return (leftSide + rightSide)

NUM_ACCEL_READINGS = 10
NUM_ALT_READINGS = 10

run = True

accelerationFromBNO = range(0,NUM_ACCEL_READINGS)
BNOTimes = range(0,NUM_ACCEL_READINGS)
altitudes = range(0,NUM_ALT_READINGS)
BMPTimes = range(0,NUM_ALT_READINGS)

for i in range (NUM_ALT_READINGS,0,-1):
    accelerationFromBNO.insert(0,int(i))
    BNOTimes.insert(0,int(i))
    altitudes.insert(0,int(i))
    BMPTimes.insert(0,int(i))

while run:
    for i in range(0,NUM_ACCEL_READINGS,1):
        print("{0}, {1}, {2}, {3}".format(accelerationFromBNO[i], BNOTimes[i], altitudes[i], BMPTimes[i]))
    print("Final Velocity = {}".format(calulateVelocity()))
    run = False
