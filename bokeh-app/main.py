from os.path import join, dirname
import pandas as pd
import numpy as np

from bokeh.io import output_file, show, curdoc
from bokeh.layouts import gridplot
from bokeh.models import ColorBar, ColumnDataSource, Legend, Span
from bokeh.plotting import figure
from bokeh.palettes import Category20_20
from bokeh.transform import factor_cmap

# Bring in data
df = pd.read_csv(join(dirname(__file__), 'data.csv'))

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
cnt = 0
p = []

#legend_field="Type"

# order = np.array(['Res Oils','MC20 Sampled Oils','Seds 2007','Seds PC & Box','Seds DC','DSUH','DSLH',
#                   'Group U','Group 2','Group 3','Group 3a','Group 4','W','POs Post-Con'])

colors = factor_cmap('Type', palette=Category20_20, factors=df.Type.unique())

hline = Span(location=0, dimension='height', line_color='gray', line_width=2, line_alpha=fa)
vline = Span(location=0, dimension='width', line_color='gray', line_width=2, line_alpha=fa)

for cnt in np.arange(0,len(x)):
    plot = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
    plot.scatter(x[cnt], y[cnt], source=source, fill_alpha=fa, size=ms, color=colors)
    plot.xaxis.axis_label = x[cnt]
    plot.yaxis.axis_label = y[cnt]
    plot.renderers.extend([vline, hline])
    p.append(plot)


plot = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
plot.scatter(y[17], y[17], source=source, fill_alpha=fa, size=ms, color=colors, legend_field='Type', muted_color=colors, muted_alpha=0.2)
plot.xaxis.axis_label = 'Legend'
plot.legend.location = "top_left"
p.append(plot) 

p = gridplot([p[0:4],p[4:8],p[8:12],p[12:16],p[16:]], toolbar_location='right', toolbar_options=dict(logo='grey'))
# p = gridplot([[a0,a1,a2,a3],[a4,a5,a6,a7]])

# output_file("DLV.html")
curdoc().add_root(p)
# show(p)


















