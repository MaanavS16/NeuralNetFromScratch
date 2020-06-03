from network import network

n1 = network(2)
n1.addLayer(3)
n1.addLayer(1)

#n1.printStructure()

n1.forwardPropogate([2,-1])

n1.printStructure()

print(n1.getWeightList())
