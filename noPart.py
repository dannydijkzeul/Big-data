import time


# Takes the filename and loops through file to create database array
def createDB(fileName):
    db = []
    with open(fileName , 'rb') as file:

        for item in file:
            db.append(item.strip('\n').split(','))

    file.close()

    return db


# Function that loops over all records of a database and checks if all tags are present per record
# Returns all records which have all required tags present. 
def findTags(db, tags):
    result = []
    # Loop over all every record of the DB
    for data in db:
        # set that all tags will be present
        found = True

        # Check if tag is not present
        for tag in tags:
            # If tag not present set found false and break from loop. Because the statement cannot be fulfilled
            if not data[tag] == ' 1': 
                found = False
                break
         # If statement is indeed fulfilled add data to result
        if found : result.append(data)

    return result

# run multiple tests per tags given a specific amount
def runPerTag(tag, amount):

    tagsMatrix = { "A" : 1,
                "B" : 2,
                "C" : 3,
                "D" : 4 }

    # Open file to write logs to
    with open("Log/result-noPart-{}-{}.log".format(amount,str(tag).strip('[]')), "wb") as logFile:

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
amounts = ["10K","20K","50K","100K","250K", "500K", "1M", "2M"]

# Tag combinations to be tested
tags = [["A","D"],["A", "C", "D"],["A", "B", "C", "D"]]

for amount in amounts:

    # Set test runs
    tests = 50 

    fileName = "data-{}.csv".format(amount)

    # Create a database based on the given datafile
    db = createDB(fileName)

    for tag in tags:
        runPerTag(tag, amount)




