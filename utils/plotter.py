import matplotlib.pyplot as plt
import uuid


def generate_plot(x_values, y_values):

    filename = f"{uuid.uuid4().hex}.png"

    path = f"static/graphs/{filename}"

    plt.figure(figsize=(8, 5))

    plt.plot(

        x_values,
        y_values,

        marker='o',
        linewidth=2

    )

    plt.title(
        "Heun Method Approximation"
    )

    plt.xlabel("x")

    plt.ylabel("y")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(path)

    plt.close()

    return filename