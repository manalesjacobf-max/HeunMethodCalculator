import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import io
import base64


def generate_plot(x_vals, y_vals):

    plt.figure(figsize=(7, 4))

    plt.plot(
        x_vals,
        y_vals,
        marker='o',
        linewidth=2
    )

    plt.title("Heun Method Approximation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    buffer = io.BytesIO()

    plt.savefig(
        buffer,
        format='png',
        bbox_inches='tight'
    )

    buffer.seek(0)

    image_png = buffer.getvalue()

    buffer.close()

    graph = base64.b64encode(image_png)

    graph = graph.decode('utf-8')

    plt.close()

    return graph        