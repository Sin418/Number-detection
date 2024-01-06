import matplotlib.pyplot as plt

class grapher():
    def __init__(self, lst):
        self.lst = lst

    def visualizeGraph(self):
        data = self.lst
        if len(data[0]) == 1:  # if 1D list
            plt.plot(data)
        else:
            for i in range(len(data)):
                plt.plot(data[i])
        plt.show()