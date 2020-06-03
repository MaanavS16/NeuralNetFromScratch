class Neuron:
    def __init__(self, layer, position, bias=0, value=0):
        self.value = value
        self.bias = bias
        self.layer = layer
        self.position = position

    def getValue(self):
        return self.value

    def getBias(self):
        return self.bias

    def updateValue(self, newValue):
        self.value = newValue

    def updateBias(self, newBias):
        self.bias = newBias

    def getLocation(self):
        return (self.layer, self.position)
