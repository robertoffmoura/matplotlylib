# matplotlylib

Convert matplotlib figures to Plotly figures.

```python
import matplotlib.pyplot as plt
from matplotlylib import mpl_to_plotly

fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])

plotly_fig = mpl_to_plotly(fig)
plotly_fig.show()
```

## Install

```
pip install matplotlylib
```

## Development

```
pip install -e ".[dev]"
python -m pytest
```

The renderer is built on the vendored [mplexporter](https://github.com/mpld3/mplexporter)
framework (MIT), originally part of the mpld3 project.
