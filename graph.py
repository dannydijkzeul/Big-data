import matplotlib.pyplot as plt


data_labels = ["10K","20K","50K","100K","250K", "500K", "1M", "2M", "5M", "10M", "20M", "30M", "50M"]
data = [10000, 20000, 50000, 100000, 250000, 500000, 1000000, 2000000, 5000000,10000000,20000000, 30000000, 50000000]

data_types = ["NoPart", "partitionIntersect", "partSearch", "partSmart"]

data_x = []

for type in data_types:
    list = []
    for label in data_labels:

        with open("Log/"+ type+ "/"+ label + "-_A_, _B_, _C_, _D_.log", "r") as file:


            
            for line in file:
                continue

            list.append(float(line.strip('\n')))

        file.close()
    data_x.append(list)

print(data_x[0])

print(data_x[1])

fig, ax = plt.subplots()


ax.plot(data, data_x[0], label ="No partition")
ax.plot(data, data_x[1], label ="Partition with intersection")
ax.plot(data, data_x[2], label ="Partition search")
ax.plot(data, data_x[3], label ="Partition smart search")

ax.set_xlabel("Unique entries in database")
ax.set_ylabel("Output speeds in seconds")

# tweak the axis labels
xlab = ax.xaxis.get_label()
ylab = ax.yaxis.get_label()

xlab.set_style('italic')
xlab.set_size(10)
ylab.set_style('italic')
ylab.set_size(10)

ax.set_title("Output speed for labels ABCD per lookup technique")
# tweak the title
ttl = ax.title
ttl.set_weight('bold')

plt.legend()

ax.grid('on')
plt.show()