from neuron import Neuron
import math

def sigmoid(x):
    return 1 / (1 + math.e**(-x))

class network:

    def __init__(self, layerOneSize=5):
        self.NetworkStruct = []
        self.NetworkStruct.append([])
        self.weights = []
        for i in range(layerOneSize):
            self.NetworkStruct[-1].append(Neuron(1, i+1))

    def addLayer(self, layerSize):
        self.NetworkStruct.append([])
        for i in range(layerSize):
            self.NetworkStruct[-1].append(Neuron(len(self.NetworkStruct), i+1))


        #weights[second layer number, position of 1st neuron on last layer, position of 2nd neuron on current layer]
        self.weights.append([])
        for i in range(len(self.NetworkStruct[-2])):
            self.weights[-1].append([])
            for _ in range(len(self.NetworkStruct[-1])):
                self.weights[-1][-1].append(.5)

    def getWeight(self, firstLayer, firstPosition, secondPosition):
        return self.weights[firstLayer+1][firstPosition][secondPosition]

    def getWeightList(self):
        return self.weights

    def updateWeight(self, firstLayer, firstPosition, secondPosition, newValue):
        self.weights[firstLayer+1][firstPosition][secondPosition] = newValue


    def forwardPropogate(self, inputLayer):
        # layer
        for i in range(len(self.NetworkStruct)):
            #print(i)
            if i != 0:
                # point B

                for j in range(len(self.NetworkStruct[i])):
                    sum = 0
                    #point A
                    for k in range(len(self.NetworkStruct[i-1])):
                        sum += self.weights[i-1][k][j] * self.NetworkStruct[i-1][k].getValue() + self.NetworkStruct[i-1][k].getBias()
                    self.NetworkStruct[i][j].updateValue(sigmoid(sum))
            else:
                for j in range(len(self.NetworkStruct[i])):
                    self.NetworkStruct[i][j].updateValue(inputLayer[j])

    def printStructure(self):
        print(self.NetworkStruct)
        for i in self.NetworkStruct:
            for j in i:
                print(j.getLocation(), j.getValue())
            print("\n")
