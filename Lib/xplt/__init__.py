""" Plotting routines based on Gist (requires X-server)

  All Gist functions are also available as xplt.<command>

    histogram -- Plot a histogram.
    barplot   -- Construct a barplot.
    errorbars -- Draw connected points with (y-only) errorbars.
    legend    -- Construct and place a legend.
    arrow     -- Draw an arrow.
    plot      -- Plot curves.
    surf      -- Plot surfaces (no axes currently plotted).
    xlabel    -- Place a label on the x-axis.
    ylabel    -- Place a label on the y-axis.
    title     -- Place a title above the plot.
    hold      -- Draw subsequent plots over the current plot.
    matplot   -- Plot many curves in a matrix against a single x-axis.
    addbox    -- Add a box to the current plot.
    imagesc   -- Draw an image.
    imagesc_cb -- Draw an image with a colorbar.
    movie     -- Play a sequence of images as a movie.
    figure    -- Create a new figure.
    full_page -- Create a full_page window.
    subplot   -- Draw a sub-divided full-page plot.
    plotframe -- Change the plot system on a multi-plot page.
    twoplane  -- Create a plot showing two orthogonal planes of a
                 three-dimensional array.

Xplt is basically a wrapper around the lower-level gist plotting library
used with Yorick.  Simpler commands are provided, but all of the low-level
commands of gist are still available.
"""

from gist import *
import os, sys
from Mplot import *
from write_style import *
import scipy_base
base_file = os.path.split(scipy_base.__file__)[0]
gistpath = os.path.join(base_file[:-5],'xplt','gistdata')
os.environ['GISTPATH'] = gistpath

display = os.environ.get('DISPLAY')

maxwidth=os.environ.get('XPLT_MAXWIDTH')
maxheight=os.environ.get('XPLT_MAXHEIGHT')

# added check for X DISPLAY being available before calling xwininfo.
# It causes crashes on telnet sessions without a display otherwise.
if display and (maxwidth is None or maxheight is None):
    import commands
    str1 = commands.getoutput('xwininfo -root')
    # Hmmm.  errors still seem to be occuring occasionally even
    # with the display check.  Added try block to protect against
    # this causing import scipy to fail.
    try:
        ind1 = str1.find('Width:')
        ind2 = str1.find('\n',ind1)
        maxwidth=int(str1[ind1+6:ind2])-8
        ind1 = str1.find('Height:')
        ind2 = str1.find('\n',ind1)
        maxheight=int(str1[ind1+7:ind2])-60
        os.environ['XPLT_MAXWIDTH']=str(maxwidth)
        os.environ['XPLT_MAXHEIGHT']=str(maxheight)
    except ValueError:
        if maxwidth is None: maxwidth = 800
        if maxheight is None: maxheight = 600
else:
    maxwidth = 800
    maxheight = 600

