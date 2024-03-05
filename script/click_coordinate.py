import matplotlib.pyplot as plt

class ClickCoordinates:
    def __init__(self, image_path):
        self.image_path = image_path
        self.coordinates = []

    def onclick(self, event):
        if event.xdata is not None and event.ydata is not None:
            print(f'Clicked at x={event.xdata:.2f}, y={event.ydata:.2f}')
            self.coordinates.append((event.xdata, event.ydata))

    def run(self):
        image = plt.imread(self.image_path)

        fig, ax = plt.subplots()
        ax.imshow(image)
        ax.set_title('Click on the image to get coordinates')

        cid = fig.canvas.mpl_connect('button_press_event', self.onclick)

        plt.show()

        return self.coordinates

if __name__ == '__main__':
    # 替换以下路径为你的实际路径
    image_path = 'D:\\learn\\script\\demo\\data\\background\\0016.jpg'

    clicker = ClickCoordinates(image_path)
    coordinates = clicker.run()

    print('Clicked coordinates:', coordinates)
