import numpy as np
import matplotlib.pyplot as plt
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()







##Measure vst strength:
arrowdir = {  0: np.array((0,1.0)),
                          1: np.array((0,-1.0)),
                        2: np.array((1,0)),
                        3: np.array((-1,0))}



num_action=4
def vst_value(grid):
    plt.figure(figsize=(4, 4))
    width=grid.grid_x
    height=grid.grid_y
    axes=0
    for y in range(height):
        for x in range(width):
            axes+=1
            value=[]
            for i in range(num_action):


                grid.set_pos(y,x)
                _,pos,_,_=grid.transition(i)
                value.append((grid.vst[pos[0],pos[1]]))
            value=softmax(value)

            plt.subplot(height, width, axes)
            plt.xticks([])
            plt.yticks([])
            max_val=np.max(value)

            plt.xlim([-max_val-0.2, max_val+0.2])
            plt.ylim([-max_val-0.2, max_val+0.2])
            for i in range(4):
                magnitude=arrowdir[i]*value[i]
                plt.arrow(0,0,magnitude[0],magnitude[1],head_width=0.1)

    plt.tight_layout(0)
    plt.show()

def ast_value(grid):
    width=grid.grid_x
    height=grid.grid_y
    plt.figure(figsize=(4, 4))
    axes=0
    for y in range(height):
        for x in range(width):
            axes+=1
            value=[]
            for i in range(num_action):
                value.append((grid.ast[i][y][x]))
            value=softmax(value)
            plt.subplot(height, width, axes)
            plt.xticks([])
            plt.yticks([])
            max_val=np.max(value)

            plt.xlim([-max_val-0.2, max_val+0.2])
            plt.ylim([-max_val-0.2, max_val+0.2])
            for i in range(4):
                magnitude=arrowdir[i]*value[i]
                plt.arrow(0,0,magnitude[0],magnitude[1],head_width=0.1)

    plt.tight_layout(0)
    plt.show()