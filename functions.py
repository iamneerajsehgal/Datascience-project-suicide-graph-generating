__author__ = 'hp'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#graph generating function for one state for all ages
def one_sate_graph(state, cause, year):
    df = pd.read_csv("data.csv")
    df = df[(df["STATE/UT"] == state) & (df["CAUSE"] == cause) & (df["Year"] == year)]
    df.set_index("Year", inplace=True)
    x_pos = np.arange(1, 14)
    df = df[df.columns[2:]]
    y = df.loc[year, :].values
    print(y)
    x = list(df)
    ax = plt.subplot()
    ax.set_xticks(x_pos)
    ax.set_xticklabels(x)
    plt.xticks(rotation="-90")
    p1 = plt.bar(x_pos, y)
    plt.title("Chart for %s and %s" % (state, cause))
    plt.xlabel(year)
    plt.ylabel("Victims", rotation="vertical")
    auto_label(p1,ax)
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.tight_layout()
    plt.show()


# two years differnce  function
def two_years_difference_graph(state, cause, year,year2):
    df=pd.read_csv("data.csv")
    df = df[(df["STATE/UT"] == state) & (df["CAUSE"] == cause)]
    df=df[(df["Year"] == year) | (df["Year"] == year2)]
    df.set_index("Year", inplace=True)
    x_pos = np.arange(1, 14)
    df = df[df.columns[2:]]
    y = df.loc[year, :].values
    y2=df.loc[year2,:].values
    x = list(df)
    ax = plt.subplot()
    ax.set_xticks(x_pos)
    ax.set_xticklabels(x)
    plt.xticks(rotation="-90")
    p1 = plt.bar(x_pos-0.2, y,width=0.5,label="first year="+str(year))
    p2=plt.bar(x_pos+0.2,y2,width=0.5,label="first year="+str(year2))
    plt.title("Chart for %s and %s" % (state, cause))
    plt.xlabel(year)
    plt.ylabel("Victims", rotation="vertical")
    auto_label(p1,ax)
    auto_label(p2,ax)
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.tight_layout()
    plt.legend()
    plt.show()


#two states graph
def two_states_difference_graph(state1,state2,cause,year):
    df=pd.read_csv("data.csv")
    df=df[((df["STATE/UT"]==state1) | (df["STATE/UT"]==state2)) & ((df["Year"] == year) & (df["CAUSE"]==cause)) ]
    df.set_index("STATE/UT", inplace=True)
    x_pos = np.arange(1, 14)
    df = df[df.columns[2:]]
    y = df.loc[state1, :].values
    y2=df.loc[state2,:].values
    x = list(df)
    ax = plt.subplot()
    ax.set_xticks(x_pos)
    ax.set_xticklabels(x)
    plt.xticks(rotation="-90")
    p1 = plt.bar(x_pos-0.2,y,width=0.5,label="first State="+state1)
    p2=plt.bar(x_pos+0.2,y2,width=0.5,label="Another State="+state2)
    plt.title("Chart for %s and %s  for  %s" % (state1,state2, cause))
    plt.xlabel(year)
    plt.ylabel("Victims", rotation="vertical")
    auto_label(p1,ax)
    auto_label(p2,ax)
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.tight_layout()
    plt.legend()
    plt.show()









# this function is used for labeling the x axis bar graphs

def auto_label(reacts, ax_sub):
    """
    Attach a text label above each bar displaying its height
    """
    ax = ax_sub
    for rect in reacts:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.005 * height,
                '%d' % int(height),
                ha='center', va='bottom')


