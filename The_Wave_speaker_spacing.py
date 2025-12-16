# Creates an Audio Routes panner compliant speaker configuration for Vertigo ApS' The Wave. 

# Save the output of this program to a new line in the 'coll' object in the 'Speakers' 
# subpatcher of the Audio Routes v1.5.1 panner. Add the name of the new speaker 
# configuration, set below, to the range/enum (inspector) attribute of the live.menu 
# inputting to the 'Speakers' subpatcher. 
# alex.levinson555@gmail.com

####
numSpeakers = 40
nameOfConfiguration = "40speaker"
#### Enter Desired Parameters Above

print(numSpeakers, end=" ")
print(nameOfConfiguration, end=", ")

# Set azimuth angle left of the center of The Wave.
for i in range(1,int((numSpeakers/2)+1)): {
    print(i, end=' '),
    print(-90, end=' '), 
}
    
# Set azimuth angle right of the center of The Wave.
for i in range(1,int((numSpeakers/2)+1)): {
    print(int(numSpeakers/2) + i, end=' '),
    print(90, end=' ')
}

# Set spacing left of the center of The Wave.
for i in range(0,int(numSpeakers/2)): {
    print(round(1-((i*2)/(numSpeakers-1)),2), end=' '),
}

# Set spacing right of the center of The Wave. 
for i in range(0,int(numSpeakers/2)): {
    print(round(1-(((numSpeakers)-((i+1)*2))/(numSpeakers-1)),2), end=' ')
}

print(";")
