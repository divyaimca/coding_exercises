import math

BIPOLAR_NAMES = []
BIPOLAR_LEG_LENGTH = {}
BIPOLAR_STRIDE_LENGTH = {}
BIPOLAR_IN_DATA2 = []




with open("dataset2.csv","r+") as data2:
    for line in data2:
        if "bipedal" in line:
            #print(line.split(",")[0])
            BIPOLAR_NAMES.append(line.split(",")[0])
            BIPOLAR_LEG_LENGTH[line.split(",")[0]] = line.split(",")[1]


with open("dataset1.csv","r+") as data1:
    for line in data1:
        for i in BIPOLAR_NAMES:
            if i in line:
                # print(line)
                BIPOLAR_IN_DATA2.append(i)
                BIPOLAR_STRIDE_LENGTH[i] = line.split(",")[1]
          

                

# print(BIPOLAR_NAMES)
# print(BIPOLAR_IN_DATA2)
# print(BIPOLAR_LEG_LENGTH)
# print(BIPOLAR_STRIDE_LENGTH)

g = 9.8

for din in BIPOLAR_IN_DATA2:
    STRIDE_LENGTH = float(BIPOLAR_STRIDE_LENGTH[din])
    LEG_LENGTH = float(BIPOLAR_LEG_LENGTH[din])
    #print(din,STRIDE_LENGTH,LEG_LENGTH)

    speed = abs((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)

    print(f"Speed of {din} is : {speed}m/s^2")




