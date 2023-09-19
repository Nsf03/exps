import pandas as pd
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np

num = 0

def onclick(event):
    if event.dblclick:
         print(event.button)

def on_click(event):
    if event.button is MouseButton.RIGHT:
        print(f'xy {round(event.xdata, 2)} {round(event.ydata, 2)}')


data = pd.read_excel('trelax_LEDpower.xlsx')


t = data['t']

bg = data['bg-wt']
wt1 = data['wt-1']
wt2 = data['wt-2']
wt3 = data['wt-3']


fig = plt.figure()

plt.connect('button_press_event', on_click)

plt.plot(wt2)
plt.show()


