from os.path import join, dirname
import pandas as pd
import numpy as np

from bokeh.io import output_file, show, curdoc
from bokeh.layouts import gridplot, column, row, layout
from bokeh.models import ColorBar, ColumnDataSource, Legend, Span
from bokeh.plotting import figure
from bokeh.palettes import Category20_20
from bokeh.transform import factor_cmap

# Bring in data
df = pd.read_csv(join(dirname(__file__), 'data.csv'))

# Convert Date column to datetime from object
df.Date = pd.to_datetime(df.Date).dt.date

# %% X and Y axis ratios
# x = ['C2-Phenanthrenes/Anthracenes/Phytane','C2-Dibenzothiophenes/C2-Phenanthrenes/Anthracenes','C2-Dibenzothiophenes/C2-Phenanthrenes/Anthracenes',
#        'C1-Phenanthrenes/Anthracenes/Pristane','C1-Dibenzothiophenes/Pristane','27dia S/Tm','Bsnh/Hop','28S TAS/Tm']

# y = ['C1-Phenanthrenes/Anthracenes/Pristane','C1-Dibenzothiophenes/C1-Phenanthrenes/Anthracenes','C1-Phenanthrenes/Anthracenes/Pristane',
#        'MP2/Benzo[e]pyrene','27dia S/Tm','MP2/Benzo[e]pyrene','MP2/Perylene','27bb R/Hop']

x = ['C2-Dibenzothiophenes/C2-Phenanthrenes/Anthracenes','28S TAS/Tm','MP2/Perylene','MP2/Benzo[e]pyrene','27bb S/Hop','MP2/Perylene',
     'n-Tetracosane (C24)/Hop','Benzo[e]pyrene/Hop','Bsnh/Hop','Bsnh/H29','C2-Phenanthrenes/Anthracenes/Phytane','C2-Dibenzothiophenes/C2-Phenanthrenes/Anthracenes',
     'C2-Dibenzothiophenes/C2-Phenanthrenes/Anthracenes','C1-Phenanthrenes/Anthracenes/Pristane','C1-Dibenzothiophenes/Pristane','27dia S/Tm','Bsnh/Hop','28S TAS/Tm']

y = ['2,6,10 Trimethyldodecane (1380)/C4-Decalins','C1-Dibenzothiophenes/C1-Phenanthrenes/Anthracenes','28S TAS/Tm','28S TAS/Tm','C26 Tricyclic Terpane-22S/H29',
     'Tm/Bsnh','Bsnh/Hop','Bsnh/Hop','H29/Hop','29Ts/Hop','C1-Phenanthrenes/Anthracenes/Pristane','C1-Dibenzothiophenes/C1-Phenanthrenes/Anthracenes',
     'C1-Phenanthrenes/Anthracenes/Pristane','MP2/Benzo[e]pyrene','27dia S/Tm','MP2/Benzo[e]pyrene','MP2/Perylene','27bb R/Hop']

# %% Bokeh Plot
source = ColumnDataSource(df)

TOOLS = "box_zoom,wheel_zoom,pan,box_select,lasso_select,hover,reset,help"

ttips = [("Sample", "@Sample"),("Type", "@Type")]

pw = 450
ph = 450
ms = 9
fa = 0.75 
pl = []

colors = factor_cmap('Type', palette=Category20_20, factors=df.Type.unique())

hline = Span(location=0, dimension='height', line_color='gray', line_width=2, line_alpha=fa)
vline = Span(location=0, dimension='width', line_color='gray', line_width=2, line_alpha=fa)

for cnt in np.arange(0,len(x)):
    plot = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
    plot.scatter(x[cnt], y[cnt], source=source, fill_alpha=fa, size=ms, color=colors)
    plot.xaxis.axis_label = x[cnt]
    plot.yaxis.axis_label = y[cnt]
    plot.renderers.extend([vline, hline])
    pl.append(plot)

# For the timeline plot
plot = figure(tools=TOOLS, plot_width=900, plot_height=ph, title=None, tooltips=ttips, x_axis_type='datetime')
plot.scatter('Date', 'Rank', source=source, fill_alpha=fa, size=ms, color=colors, legend_field='Type', muted_color=colors, muted_alpha=0.2)
plot.xaxis.axis_label = 'Date'
plot.yaxis.axis_label = 'Rank'
plot.legend.location = (100,55)
pl.append(plot) 

# For the sample group plot
plot = figure(tools=TOOLS, plot_width=1800, plot_height=ph, title=None, tooltips=ttips)
plot.scatter('Type', 'Rank_Type', source=source, fill_alpha=fa, size=ms, color=colors, legend_field='Type', muted_color=colors, muted_alpha=0.2)
plot.xaxis.axis_label = 'Group'
plot.yaxis.axis_label = 'Number'
plot.legend.location = (100,55)
pl.append(plot) 

# Setting up the layout for gridplot
a1 = row(pl[0],pl[1],pl[2],pl[3])
a2 = row(pl[4],pl[5],pl[6],pl[7])
a3 = row(pl[8],pl[9],pl[10],pl[11])
a4 = row(pl[12],pl[13],pl[14],pl[15])
a5a = row(pl[16],pl[17])
a5b = row(pl[18])
a5 = row(a5a,a5b)
a6 = row(a6)

# p = gridplot([pl[0:4],pl[4:8],pl[8:12],pl[12:16],pl[16:19]],sizing_mode='scale_height', toolbar_location='right', toolbar_options=dict(logo='grey'))

p = gridplot(children=[[a1],[a2],[a3],[a4],[a5],[a6]],sizing_mode='fixed', toolbar_location='right', toolbar_options=dict(logo='grey'))
            
# output_file("DLV.html")
curdoc().add_root(p)    # Enable for Binder
# show(p)                   # Enable in Spyder, Jupyter                 


















