import math
import random
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser(description='This is an example program put together so that users may visualize different equations for distribution')
parser.add_argument('-d','--distributionType', type=str, help='the distribution type to use', required=True)

# args = parser.parse_args()
args = vars(parser.parse_args())
# print(args.)
# print(args.accumulate(args.integers))

distributionType = args['distributionType']

#-------------------------------------------------------------------------------


def GetDistribution(distributionStartTime, totalDurationInSeconds, numberOfPointsToDistribute, distributionType):
  distribution = []
  startTime = 0
  durationInSeconds = 1

  for i in range(0, numberOfPointsToDistribute):
    # print("-------------------------")
    # selectedPointOnInterval = startTime + (random.random() * durationInSeconds)
    selectedPointOnInterval = random.random()
    changeInValue = ((startTime + durationInSeconds) - startTime)

    if(distributionType == "LinearIn"):
      selectedPointOnInterval = ApplyLinearInDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)

    elif(distributionType == "QuadraticEaseIn"):
      selectedPointOnInterval = ApplyQuadraticEaseInDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "QuadraticEaseOut"):
      selectedPointOnInterval = ApplyQuadraticEaseOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "QuadraticEaseInOut"):
      selectedPointOnInterval = ApplyQuadraticEaseInOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "QuadraticEaseInOutIn"):
      selectedPointOnInterval = ApplyQuadraditicInOutIn(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)

    elif(distributionType == "CubicEaseIn"):
      selectedPointOnInterval = ApplyCubicEaseInDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "CubicEaseOut"):
      selectedPointOnInterval = ApplyCubicEaseOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "CubicEaseInOut"):
      selectedPointOnInterval = ApplyCubicEaseInOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)

    elif(distributionType == "QuarticEaseIn"):
      selectedPointOnInterval = ApplyQuarticEaseInDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "QuarticEaseOut"):
      selectedPointOnInterval = ApplyQuarticEaseOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "QuarticEaseInOut"):
      selectedPointOnInterval = ApplyQuarticEaseInOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)

    elif(distributionType == "QuinticEaseIn"):
      selectedPointOnInterval = ApplyQuinticEaseInDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "QuinticEaseOut"):
      selectedPointOnInterval = ApplyQuinticEaseOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "QuinticEaseInOut"):
      selectedPointOnInterval = ApplyQuinticEaseInOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)

    elif(distributionType == "SinusoidalEaseIn"):
      selectedPointOnInterval = ApplySinusoidalEaseInDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "SinusoidalEaseOut"):
      selectedPointOnInterval = ApplySinusoidalEaseOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "SinusoidalEaseInOut"):
      selectedPointOnInterval = ApplySinusoidalEaseInOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)

    elif(distributionType == "ExponentialEaseIn"):
      selectedPointOnInterval = ApplyExponentialEaseInDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "ExponentialEaseOut"):
      selectedPointOnInterval = ApplyExponentialEaseOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "ExponentialEaseInOut"):
      selectedPointOnInterval = ApplySinusoidalEaseInOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)

    elif(distributionType == "CircularEaseIn"):
      selectedPointOnInterval = ApplyCircularEaseInDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "CircularEaseOut"):
      selectedPointOnInterval = ApplyCircularEaseOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)
    elif(distributionType == "CircularEaseInOut"):
      selectedPointOnInterval = ApplySinusoidalEaseInOutDistributionToValue(selectedPointOnInterval, startTime, changeInValue, durationInSeconds)

    elif(distributionType == "Squared"):
      selectedPointOnInterval = ApplySquaredDistributionToValue(selectedPointOnInterval, durationInSeconds)

    # elif(distributionType == "CatMullRom"):
    #   # def ApplyCatMullRomDistribution(currentTime, pointOne, pointTwo, pointThree, pointFour):
    #   # ApplyCatMullRomDistribution(selectedPointOnInterval, 0, 0.375, 0.625, 1)
    #   # ApplyCatMullRomDistribution(selectedPointOnInterval, 0, 0.5, 0.5, 1)
    #   # ApplyCatMullRomDistribution(selectedPointOnInterval, 0, 0, 1, durationInSeconds)

    #   # for (i = 0; i < N; i++)
    #   # {
    #   selectedPointOnInterval = ApplyCatMullRomDistribution((selectedPointOnInterval/durationInSeconds),
    #                                                         -5,
    #                                                         0,
    #                                                         1,
    #                                                         5)
    #   selectedPointOnInterval = (0 * selectedPointOnInterval) + (durationInSeconds * (1 - selectedPointOnInterval))
    #   # selectedPointOnInterval = ApplyCatMullRomDistribution((selectedPointOnInterval/durationInSeconds), 0, 0, 1, durationInSeconds)
    #   #   X = (A * v) + (B * (1 - v));
    #   # }


    else:
      print("DISTRIBUTION TYPE SPECIFIED DOES NOT EXIST. PLEASE RETRY WITH VALID DISTRIBUTION TYPE")
      exit()

    selectedPointOnInterval = distributionStartTime + (selectedPointOnInterval * totalDurationInSeconds)
    selectedPointOnInterval = int(selectedPointOnInterval)
    # print("Selected Point on Interval: " + str(selectedPointOnInterval))

    distribution.append(selectedPointOnInterval)
  return distribution;

def GetSquaredDistribution(intervalMax, numberOfPointsToDistribute):
  distribution = []
  for i in range(0, numberOfPointsToDistribute, 1):
    selectedPointOnInterval = (random.random() * intervalMax)
    distribution.append(selectedPointlWithSquaredDistributionApplied);
  return distribution


#-------------------------------------------------------------------------------
# t - current time
# b - start time
# c - change in value (wat)
# d - duration

def ApplyLinearInDistributionToValue(currentTime, startTime, changeInValue, duration):
  # return c*t/d + b;
  return changeInValue*currentTime/duration + startTime;

def ApplyQuadraticEaseInDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d;
  # return c*t*t + b;
  # print("-------------------------")
  # print("CurrentTime: " + str(currentTime))
  # print("Start Time: " + str(startTime))
  # print("Change In Value: " + str(changeInValue))
  # print("Duration: " + str(duration))

  currentTime = currentTime/duration
  # return changeInValue*currentTime*currentTime + startTime;
  returnValue = changeInValue*currentTime*currentTime + startTime;
  # print("Return Value: " + str(returnValue))
  return returnValue

def ApplyQuadraticEaseOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d;
  # return -c * t*(t-2) + b;
  currentTime = currentTime/duration
  return (-changeInValue)*currentTime*(currentTime-2) + startTime;

def ApplyQuadraticEaseInOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d/2;
  # if (t < 1) return c/2*t*t + b;
  # t--;
  # return -c/2 * (t*(t-2) - 1) + b;
  currentTime = currentTime/(duration/2)
  if(currentTime < 1):
    return changeInValue/2*currentTime*currentTime + startTime
  currentTime -= 1
  return (-changeInValue)/2 * (currentTime*(currentTime-2) - 1) + startTime

def ApplyQuadraditicInOutIn(currentTime, startTime, changeInValue, duration):
  # NOTES: for visualization the duration and changeInValue variables need to be cast to ints in order
  #         to resolve discrepancies with distribution over evenly spaced integer intervals.
  #         for float values this doesn't matter and should not be cast to, however the current time
  #         should have its modulo changed to 'currentTime%(duration/<number of easing intervals>)'
  #         respectively as that will truly represent one-third of the the current time instead
  pointOverInterval = (currentTime/duration)
  # print("point over interval: " + str(pointOverInterval))
  currentTime = currentTime%3
  duration = int(duration/3)
  changeInValue = int(changeInValue/3)
  # print("current time: " + str(currentTime))
  if(pointOverInterval <= 0.33):
    # print("first third")
    # return ApplyLinearInDistributionToValue(currentTime, 0, changeInValue, duration);
    # return 0
    return ApplyQuadraticEaseInDistributionToValue(currentTime, 0, changeInValue, duration);
  elif(pointOverInterval > 0.33 and pointOverInterval < 0.66):
    # print("second third")
    # return 3 + ApplyQuadraticEaseOutDistributionToValue(currentTime, 0, changeInValue, duration);
    # print("---------------------------------")
    # print("Current Time: " + str(currentTime))
    # print("Start Time: " + str(0))
    # print("Change In Value: " + str(changeInValue))
    # print("Duration: " + str(duration))
    return 3 + ApplyLinearInDistributionToValue(currentTime, 0, changeInValue, duration);
  elif(pointOverInterval > 0.66 and pointOverInterval < 1):
    # print("final third")
    # return 6 + ApplyQuadraticEaseInDistributionToValue(currentTime, 0, changeInValue, duration);
    # return 6 + ApplyLinearInDistributionToValue(currentTime, 0, changeInValue, duration);
    # return 10
    return 6 + ApplyQuadraticEaseOutDistributionToValue(currentTime, 0, changeInValue, duration);
  else:
    print("ERROR ERROR ERROR ERROR")

def ApplyCubicEaseInDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d;
  # return c*t*t*t + b;
  currentTime = currentTime/duration
  return changeInValue*currentTime*currentTime*currentTime + startTime

def ApplyCubicEaseOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d;
  # t--;
  # return c*(t*t*t + 1) + b;
  currentTime = currentTime/duration
  currentTime -= 1
  return changeInValue*(currentTime*currentTime*currentTime + 1) + startTime;

def ApplyCubicEaseInOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d/2;
  # if (t < 1) return c/2*t*t*t + b;
  # t -= 2;
  # return c/2*(t*t*t + 2) + b;
  currentTime = currentTime/(duration/2)
  if(currentTime < 1):
    return changeInValue/2*currentTime*currentTime*currentTime + startTime
  currentTime -= 2
  return changeInValue/2*(currentTime*currentTime*currentTime + 2) + startTime

def ApplyQuarticEaseInDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d;
  # return c*t*t*t*t + b;
  currentTime = currentTime/duration
  return changeInValue*currentTime*currentTime*currentTime*currentTime + startTime

def ApplyQuarticEaseOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d;
  # t--;
  # return -c * (t*t*t*t - 1) + b;
  currentTime = currentTime/duration
  currentTime -= 1
  return (-changeInValue) * (currentTime*currentTime*currentTime*currentTime - 1) + startTime

def ApplyQuarticEaseInOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d/2;
  # if (t < 1) return c/2*t*t*t*t + b;
  # t -= 2;
  # return -c/2 * (t*t*t*t - 2) + b;
  currentTime = currentTime/(duration/2)
  if(currentTime < 1):
    return changeInValue/2*currentTime*currentTime*currentTime*currentTime + startTime
  currentTime -= 2
  return (-changeInValue)/2 * (currentTime*currentTime*currentTime*currentTime - 2) + startTime


def ApplyQuinticEaseInDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d;
  # return c*t*t*t*t*t + b;
  currentTime = currentTime/duration
  return changeInValue*currentTime*currentTime*currentTime*currentTime*currentTime + startTime

def ApplyQuinticEaseOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d;
  # t--;
  # return c*(t*t*t*t*t + 1) + b;
  currentTime = currentTime/duration
  currentTime -= 1
  return changeInValue * (currentTime*currentTime*currentTime*currentTime*currentTime + 1) + startTime

def ApplyQuinticEaseInOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d/2;
  # if (t < 1) return c/2*t*t*t*t*t + b;
  # t -= 2;
  # return c/2*(t*t*t*t*t + 2) + b;
  currentTime = currentTime/(duration/2)
  if(currentTime < 1):
    return changeInValue/2*currentTime*currentTime*currentTime*currentTime*currentTime + startTime
  currentTime -= 2
  return changeInValue/2 * (currentTime*currentTime*currentTime*currentTime*currentTime + 2) + startTime

def ApplySinusoidalEaseInDistributionToValue(currentTime, startTime, changeInValue, duration):
  # return -c * Math.cos(t/d * (Math.PI/2)) + c + b;
  return (-changeInValue) * math.cos(currentTime/duration * (math.pi/2)) + changeInValue + startTime

def ApplySinusoidalEaseOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # return c * Math.sin(t/d * (Math.PI/2)) + b;
  return changeInValue * math.sin(currentTime/duration * (math.pi/2)) + startTime

def ApplySinusoidalEaseInOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # return -c/2 * (Math.cos(Math.PI*t/d) - 1) + b;
  return (-changeInValue)/2 * (math.cos(math.pi * currentTime/duration) - 1) + startTime

def ApplyExponentialEaseInDistributionToValue(currentTime, startTime, changeInValue, duration):
  # return c * Math.pow( 2, 10 * (t/d - 1) ) + b;
  return changeInValue * math.pow(2, (10 * (currentTime/duration - 1)) ) + startTime

def ApplyExponentialEaseOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # return c * ( -Math.pow( 2, -10 * t/d ) + 1 ) + b;
  return changeInValue * (-math.pow( 2, (-10 * currentTime/duration)) + 1 ) + startTime

def ApplyExponentialEaseInOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d/2;
  # if (t < 1) return c/2 * Math.pow( 2, 10 * (t - 1) ) + b;
  # t--;
  # return c/2 * ( -Math.pow( 2, -10 * t) + 2 ) + b;
  currentTime = currentTime/(duration/2)
  if(t < 1):
    return changeInValue/2 * math.pow( 2, (10 * (t - 1)) ) + startTime
  currentTime -= 1
  return changeInValue/2 * ( -math.pow( 2, (-10 * t) ) + 2 ) + startTime

def ApplyCircularEaseInDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d;
  # return -c * (Math.sqrt(1 - t*t) - 1) + b;
  currentTime = currentTime/duration
  return -changeInValue * (math.sqrt(1 - currentTime * currentTime) - 1) + startTime


def ApplyCircularEaseOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d;
  # t--;
  # return c * Math.sqrt(1 - t*t) + b;
  currentTime = currentTime/duration
  currentTime -= 1
  return changeInValue * math.sqrt(1 - currentTime * currentTime) + startTime

def ApplyCircularEaseInOutDistributionToValue(currentTime, startTime, changeInValue, duration):
  # t /= d/2;
  # if (t < 1) return -c/2 * (Math.sqrt(1 - t*t) - 1) + b;
  # t -= 2;
  # return c/2 * (Math.sqrt(1 - t*t) + 1) + b;
  currentTime = currentTime/(duration/2)
  if(t < 1):
    return (-changeInValue)/2 * (math.sqrt(1 - currentTime*currentTime) - 1) + b
  currentTime -= 2
  return changeInValue/2 * (math.sqrt(1 - currentTime*currentTime) + 1) + startTime

def ApplySquaredDistributionToValue(currentTime, duration):
  return ((currentTime * currentTime)/duration)

def ApplyCatMullRomDistribution(currentTime, pointOne, pointTwo, pointThree, pointFour):
  return 0.5 * ((2 * pointTwo)
                + (-pointOne + pointThree) * currentTime
                + (2 * pointOne - 5 * pointTwo + 4 * pointThree - pointFour) * currentTime * currentTime
                + (-pointOne + 3 * pointTwo - 3 * pointThree + pointFour) * currentTime * currentTime * currentTime)

# intervalMax is the total duration in seconds that the generation should be performed over
def DistributeGenerationObjectsOverInterval(startTime, durationInSeconds, numberOfGenerationObjectsToDistribute, distributionType ):
  generationObjects = []
  numbersDictionary = dict()

  print("Performing " + distributionType + " Distribution")
  for i in range(0, 10000, 1):
    ############################################################################
    generationObjects = GetDistribution(startTime, durationInSeconds, numberOfGenerationObjectsToDistribute, distributionType);

    ############################################################################
    #matplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, **kwargs)
    for generationObject in generationObjects:
      if(generationObject not in numbersDictionary):
        numbersDictionary[generationObject] = 1
      else:
        numbersDictionary[generationObject] = numbersDictionary[generationObject] + 1

  # for number in generationObjects:
  #   print(number);
  barValues = []
  barHeights = []
  for key, value in numbersDictionary.items():
    print('key: ' + str(key) + ' value: ' + str(value))
    barValues.append(key)
    barHeights.append(value)

  # plt.bar([0,1,2,3,4], [5, 1, 1, 1, 1])
  plt.bar(barValues, barHeights)
  plt.title('Interval That Each Object Was Generated At Over Time')
  plt.xlabel('Time Interval Generated At')
  plt.ylabel('Number of Objects Generated')

  plt.show()
#-------------------------------------------------------------------------------
# distributionType = "NONE"

# distributionType = "LinearIn"

# distributionType = "QuadraticEaseIn"
# distributionType = "QuadraticEaseOut"
# distributionType = "QuadraticEaseInOut"

# distributionType = "CubicEaseIn"
# distributionType = "CubicEaseOut"
# distributionType = "CubicEaseInOut"

# distributionType = "QuarticEaseIn"
# distributionType = "QuarticEaseOut"
# distributionType = "QuarticEaseInOut"

# distributionType = "QuinticEaseIn"
# distributionType = "QuinticEaseOut"
# distributionType = "QuinticEaseInOut"

# distributionType = "SinusoidalEaseIn"
# distributionType = "SinusoidalEaseOut"
# distributionType = "SinusoidalEaseInOut"

# distributionType = "ExponentialEaseIn"
# distributionType = "ExponentialEaseOut"
# distributionType = "ExponentialEaseInOut"

# distributionType = "CircularEaseIn"
# distributionType = "CircularEaseOut"
# distributionType = "CircularEaseInOut"

# distributionType = "Squared"

# distributionType = "CatMullRom"

# distributionType = "QuadraticEaseInOutIn"

DistributeGenerationObjectsOverInterval(30, 10, 1, distributionType)

