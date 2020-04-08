import time


# Takes the filename and loops through file to create database array
def createPartitionDB(fileName):
    db = [[],[],[],[]]
    with open(fileName , 'r') as file:
        next(file)
        for item in file:
            item = item.strip('\n').split(',')

            for tag in range(1,5):
                if item[tag] == ' 1': 
                    db[tag-1].append(item[0])

    file.close()

    return db

# Unionize the partitions with the correct tags
def findTags(db, tags):

    # List comprehension which selects the needed partitions
    partitions = [db[tag-1] for tag in tags]

    if len(tags) == 2:
        result = list(set(partitions[0]) & set(partitions[1]))
    elif len(tags) == 3:
        result = list(set(partitions[0]) & set(partitions[1]) & set(partitions[2]))

    else:
        result = list(set(partitions[0]) & set(partitions[1]) & set(partitions[2]) & set(partitions[3]))

    return result

# run multiple tests per tags given a specific amount
def runPerTag(tag, amount):

    tagsMatrix = { "A" : 1,
                "B" : 2,
                "C" : 3,
                "D" : 4 }

    # Open file to write logs to
    with open("Log/{}-{}.log".format(amount,str(tag).strip('[]')), "w") as logFile:

        totalTime = 0
        # Loop over the data multiple times to get an average time
        for _ in range(0,tests):
            start_time = time.time()

            findTags(db, [tagsMatrix[x] for x in tag])

            executeTime = time.time() - start_time
            totalTime = totalTime + executeTime

            # Write to log execute time
            logFile.write("{}\n".format(executeTime))

        # Write average to log
        logFile.write("{}\n".format(totalTime/tests))
        print("{} in {} sec".format(amount, totalTime/tests ))
            
    logFile.close()


# Set test amount
amounts = ["10K","20K","50K","100K","250K", "500K", "1M", "2M", "5M", "10M", "20M"]
# amounts = ["20K"]

# Tag combinations to be tested
tags = [["A","D"],["A", "C", "D"],["A", "B", "C", "D"]]

for amount in amounts:

    # Set test runs
    tests = 50 

    fileName = "data-{}.csv".format(amount)

    # Create a database based on the given datafile
    db = createPartitionDB(fileName)

    for tag in tags:
        runPerTag(tag, amount)




