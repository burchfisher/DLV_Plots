# DLV_Plots
Bokeh plots of chemical ratios for sharing with colleagues.

This project was greatly aided by the blog post of Arturo Moncada-Torres at the following URL and differs slightly from the binder example referenced below.

https://arturomoncadatorres.com/creating-a-shareable-bokeh-dashboard-with-binder/

https://github.com/binder-examples/bokeh

I had an issue initially with the figure running on binder fine but then a blank screen would show up instead of the bokeh plots. This has been an issue at least one other person has had that I have seen. For me the issue was solved by using curdoc().add_root() instead of show() like you would in a Jupyter notebook. I still don't fully understand what curdoc does but it worked. I am a newbie to Bokeh as well so that was not immediately evident to me.    

To run:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/burchfisher/DLV_Plots/HEAD?urlpath=%2Fproxy%2F5006%2Fbokeh-app)
