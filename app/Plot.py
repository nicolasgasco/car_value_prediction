import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class Plot:
    def __init__(self, data, x_prop, y_prop, theta0=0, theta1=0):
        self._x_prop = x_prop
        self._y_prop = y_prop

        self._theta0 = theta0
        self._theta1 = theta1

        self._data = data

        self._labels = {
            'x_label': 'Mileage',
            'y_label': 'Price',
            'title': 'Mileage vs Price'
        }

    def show(self, linear_regression=False):

        x_data = self._data[self._x_prop]
        y_data = self._data[self._y_prop]

        plt.clf()
        plt.title(self._labels['title'])
        plt.scatter(x_data, y_data, alpha=0.5, s=10)
        plt.xlabel(self._labels['x_label'])
        plt.ylabel(self._labels['y_label'])

        # Format number on both axes
        formatter = ticker.FuncFormatter(lambda x, pos: f'{x/1000:.0f}k')
        plt.gca().xaxis.set_major_formatter(formatter)
        plt.gca().yaxis.set_major_formatter(formatter)

        plt.grid(True, which='both', linestyle='--', linewidth=0.5)

        if (linear_regression):
            estimated_y_data = self._theta0 + self._theta1 * x_data

            plt.plot(x_data, estimated_y_data, 'y-')

        plot_name = self._labels['title'].lower().replace(' ', '_')
        plot_name += '-linear_regression' if linear_regression else ''
        plot_name += '.png'

        plt.savefig(plot_name, bbox_inches='tight', pad_inches=0, dpi=500)
