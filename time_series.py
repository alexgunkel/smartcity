#!/usr/bin/env python3
import pandas as pd

pd.options.plotting.backend = "plotly"
import plotly.express as px

df = pd.DataFrame(
    data=dict(
        Dresden=[14, 24, 6, 3],
        Leipzig=[17, 12, 14, 22],
        Chemnitz=[56, 61, 53, 56],
    ),
    index=[int(2019), int(2020), int(2021), int(2022)],
)
fig = df.plot(title='Platzierung im Bitkom Smart City Index 2019–2022', template="simple_white",
              labels=dict(index="Jahr", value="Platzierung", variable="Stadt"))
fig.update_yaxes(range=[81, 0])
fig.update_layout(
    xaxis=dict(
        tickmode='linear',
        tick0=1,
    )
)
fig.write_image('./build/gesamt_entwicklung.jpg')
