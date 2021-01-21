from os.path import join, dirname
import pandas as pd

from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.models import ColorBar, ColumnDataSource
from bokeh.plotting import figure
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap

# Bring in data
df = pd.read_csv(join(dirname(__file__), 'data.csv'))
# df = df.set_index('Sample')

# X and Y titles
x = ['C2-Phenanthrenes/Anthracenes/Phytane','C2-Dibenzothiophenes/C2-Phenanthrenes/Anthracenes','C2-Dibenzothiophenes/C2-Phenanthrenes/Anthracenes',
       'C1-Phenanthrenes/Anthracenes/Pristane','C1-Dibenzothiophenes/Pristane','27dia S/Tm','Bsnh/Hop','28S TAS/Tm']

y = ['C1-Phenanthrenes/Anthracenes/Pristane','C1-Dibenzothiophenes/C1-Phenanthrenes/Anthracenes','C1-Phenanthrenes/Anthracenes/Pristane',
       'MP2/Benzo[e]pyrene','27dia S/Tm','MP2/Benzo[e]pyrene','MP2/Perylene','27bb R/Hop']

name = ['a0','a1','a2','a3','a4','b0','b1','b2','b3']

ro = df[df.Type == 'Res Oils']
so = df[df.Type == 'MC20 Sampled Oils']
# sed07 = df[df.Type == 'Seds 2007']
# sed = df[df.Type == 'Seds PC & Box']
# sedDC = df[df.Type == 'Seds DC']
# dsuh = df[df.Type == 'DSUH']
# dslh = df[df.Type == 'DSLH']
# gu = df[df.Type == 'Group U']
# g2 = df[df.Type == 'Group 2']
# g3 = df[df.Type == 'Group 3']
# g3a = df[df.Type == 'Group 3a']
# g4 = df[df.Type == 'Group 4']
# w = df[df.Type == 'W']


# Bokeh Plot
output_file("DLV.html")

# create a column data source for the plots to share
source_ro = ColumnDataSource(ro)
source_so = ColumnDataSource(so)

TOOLS = "box_zoom,wheel_zoom,box_select,lasso_select,hover,reset,tap,help"

ttips = [("Sample", "@Sample")]

pw = 500
ph = 500
ms = 9
fa = 0.5 

a0 = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
a0.circle(x=x[0], y=y[0], fill_alpha=fa, size=ms, source=source_ro, color='black', legend_label='Res Oils')
a0.circle(x=x[0], y=y[0], fill_alpha=fa, size=ms, source=source_so, color='red', legend_label='MC20 Sampled Oils')
a0.legend.location = 'top_left'
a0.xaxis.axis_label = x[0]
a0.yaxis.axis_label = y[0]

a1 = figure(tools=TOOLS, plot_width=pw, plot_height=ph, title=None, tooltips=ttips)
a1.circle(x=x[1], y=y[1], fill_alpha=fa, size=ms, source=source_ro, color='black')
a1.circle(x=x[1], y=y[1], fill_alpha=fa, size=ms, source=source_so, color='red')

a1.xaxis.axis_label = x[1]
a1.yaxis.axis_label = y[1]


# p = gridplot([['a0','a1','a2','a3'], ['b0','b1','b2','b3']], toolbar_location='right', toolbar_options=dict(logo='gray'))
p = gridplot([[a0,a1]])

show(p)


