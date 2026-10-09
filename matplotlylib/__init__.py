# ruff: noqa: F401

"""
matplotlylib
============

This module converts matplotlib figure objects into JSON structures which can
be understood and visualized by Plotly.

Most of the functionality should be accessed through the `mpl_to_plotly`
function, or through the `PlotlyRenderer` and `Exporter` classes for custom
renderers.

"""

from matplotlylib.renderer import PlotlyRenderer
from matplotlylib.mplexporter import Exporter


def mpl_to_plotly(fig, resize=False, strip_style=False, verbose=False):
    """Convert a matplotlib figure to a Plotly figure.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The matplotlib figure to convert.
    resize : bool, default False
        Resize the Plotly figure to match the matplotlib figure.
    strip_style : bool, default False
        Strip the Plotly layout and inherit the default template.
    verbose : bool, default False
        Print the conversion messages.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    renderer = PlotlyRenderer()
    Exporter(renderer).run(fig)
    if resize:
        renderer.resize()
    if strip_style:
        renderer.strip_style()
    if verbose:
        print(renderer.msg)
    return renderer.plotly_fig
