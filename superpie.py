import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np

def helpfulPie(answer1, answer2, answer3, answer4):

    # make figure and assign axis objects
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
    fig.subplots_adjust(wspace=0)

    # pie chart parameters
    overall_ratios = [.25, .25, .25, .25]
    labels = [answer1, answer2, answer3, answer4]
    # rotate so that first wedge is split by the x-axis
    angle = -180 * overall_ratios[0]
    wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                        labels=labels)

    # bar chart parameters
    incorrectpin_ratio = [1]
    incorrectpin_ratio2 = [0]
    pin_label = ["Incorrect guesses"]
    pin_label2 = ["Correct guesses"]
    bottom = 1
    width = .2

    # Adding from the top matches the legend.
    for j, (height, label) in enumerate(reversed([*zip(incorrectpin_ratio, pin_label)])):
        bottom -= height
        bc = ax2.bar(0, height, width, bottom=bottom, color='purple', label=label,
                    alpha=0.4 + 0.25 * j)
        ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

    for j, (height, label) in enumerate(reversed([*zip(incorrectpin_ratio2, pin_label2)])):
        bottom -= height
        bc = ax2.bar(0, height, width, bottom=bottom, color='brown', label=label,
                    alpha=0.4 + 0.25 * j)
        ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

    ax2.set_title('Total percent of correct and incorrect guesses')
    ax2.legend()
    ax2.axis('off')
    ax2.set_xlim(- 5 * width, 8 * width)

    # use ConnectionPatch to draw lines between the two plots
    theta1, theta2 = wedges[0].theta1, wedges[0].theta2
    center, r = wedges[1].center, wedges[1].r
    bar_height = sum(incorrectpin_ratio)

    # draw top connecting line
    x = r * np.cos(np.pi / 90 * theta2) + center[0]
    y = r * np.sin(np.pi / 90 * theta2) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                        xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    con.set_linewidth(4)
    ax2.add_artist(con)

    # draw bottom connecting line
    x = r * np.cos(np.pi / 90 * theta1) + center[0]
    y = r * np.sin(np.pi / 90 * theta1) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                        xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    ax2.add_artist(con)
    con.set_linewidth(4)

    plt.show()
