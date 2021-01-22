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

# X and Y axis ratios
x = ['C2-Phenanthrenes/Anthracenes/Phytane','C2-Dibenzothiophenes/C2-Phenanthrenes/Anthracenes','C2-Dibenzothiophenes/C2-Phenanthrenes/Anthracenes',
       'C1-Phenanthrenes/Anthracenes/Pristane','C1-Dibenzothiophenes/Pristane','27dia S/Tm','Bsnh/Hop','28S TAS/Tm']

y = ['C1-Phenanthrenes/Anthracenes/Pristane','C1-Dibenzothiophenes/C1-Phenanthrenes/Anthracenes','C1-Phenanthrenes/Anthracenes/Pristane',
       'MP2/Benzo[e]pyrene','27dia S/Tm','MP2/Benzo[e]pyrene','MP2/Perylene','27bb R/Hop']

# %% Bokeh Plot
source = ColumnDataSource(df)

TOOLS = "box_zoom,wheel_zoom,pan,box_select,lasso_select,hover,reset,help"

ttips = [("Sample", "@Sample"),("Type", "@Type")]

pw = 450
ph = 450
ms = 9
fa = 0.75 
cnt = 0

#legend_field="Type"

# order = np.array(['Res Oils','MC20 Sampled Oils','Seds 2007','Seds PC & Box','Seds DC','DSUH','DSLH',
#                   'Group U','Group 2','Group 3','Group 3a','Group 4','W','POs Post-Con'])

colors = factor_cmap('Type', palette=Category20_20, factors=df.Type.unique())

hline = Span(location=0, dimension='height', line_color='gray', line_width=2, line_alpha=fa)
vline = Span(location=0, dimension='width', line_color='gray', line_width=2, line_alpha=fa)

cnt = 0
a0 = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
a0.scatter(x[cnt], y[cnt], source=source, fill_alpha=fa, size=ms, color=colors)
a0.xaxis.axis_label = x[cnt]
a0.yaxis.axis_label = y[cnt]
a0.renderers.extend([vline, hline])

cnt += 1
a1 = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
a1.scatter(x[cnt], y[cnt], source=source, fill_alpha=fa, size=ms, color=colors)
a1.xaxis.axis_label = x[cnt]
a1.yaxis.axis_label = y[cnt]
a1.renderers.extend([vline, hline])

cnt += 1
a2 = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
a2.scatter(x[cnt], y[cnt], source=source, fill_alpha=fa, size=ms, color=colors)
a2.xaxis.axis_label = x[cnt]
a2.yaxis.axis_label = y[cnt]
a2.renderers.extend([vline, hline])

cnt += 1
a3 = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
a3.scatter(x[cnt], y[cnt], source=source, fill_alpha=fa, size=ms, color=colors)
a3.xaxis.axis_label = x[cnt]
a3.yaxis.axis_label = y[cnt]
a3.renderers.extend([vline, hline])

cnt += 1
a4 = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
a4.scatter(x[cnt], y[cnt], source=source, fill_alpha=fa, size=ms, color=colors)
a4.xaxis.axis_label = x[cnt]
a4.yaxis.axis_label = y[cnt]
a4.renderers.extend([vline, hline])

cnt += 1
a5 = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
a5.scatter(x[cnt], y[cnt], source=source, fill_alpha=fa, size=ms, color=colors)
a5.xaxis.axis_label = x[cnt]
a5.yaxis.axis_label = y[cnt]
a5.renderers.extend([vline, hline])

cnt += 1
a6 = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
a6.scatter(x[cnt], y[cnt], source=source, fill_alpha=fa, size=ms, color=colors)
a6.xaxis.axis_label = x[cnt]
a6.yaxis.axis_label = y[cnt]
a6.renderers.extend([vline, hline])

cnt += 1
a7 = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
a7.scatter(x[cnt], y[cnt], source=source, fill_alpha=fa, size=ms, color=colors)
a7.xaxis.axis_label = x[cnt]
a7.yaxis.axis_label = y[cnt]
a7.renderers.extend([vline, hline])

# a7.add_layout(Legend(), 'right')

p = gridplot([[a0,a1,a2,a3],[a4,a5,a6,a7]], toolbar_location='right', toolbar_options=dict(logo='grey'))
# p = gridplot([[a0,a1,a2,a3],[a4,a5,a6,a7]])

# output_file("DLV.html")
curdoc().add_root(p)
# show(p)


















