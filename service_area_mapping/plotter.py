import pandas as pd
from datetime import datetime
import plotly.figure_factory as ff


class Plotter:
    def __init__(self, df: pd.DataFrame, state: str):
        self.df = df
        self.state = state

        self.fig = None

        self.update_values()
        self.create_fig()
        self.fig.show()

    def update_values(self):
        self.df.ServiceArea.replace(True, "Service Area", inplace=True)
        self.df.ServiceArea.replace(False, "Outside of Service Area", inplace=True)

    def create_fig(self):
        self.fig = ff.create_choropleth(
            fips=self.df.FIPS,
            values=self.df.ServiceArea,
            colorscale=["rgb(222, 235, 247)", "teal"],
            scope=[self.state],
            county_outline=dict(
                color="black",
                width=0.5,
            ),
            state_outline=dict(
                color="black",
                width=1.0,
            )
        )
        self.fig.layout.template = None
        
        self.fig.update_layout(
            autosize=True,
            width=1200,
            height=600,
            font=dict(
                size=18,
            ),
        )

        self.fig.update_layout(
            legend=dict(
                orientation='h',
                yanchor="bottom",
                y=-0.1,
                xanchor="center",
                x=0.525,
            ),
        )

    def save_fig():
        today = datetime.date(datetime.now())
        fig.write_image(f'CO_map_{today.year}-{today.month}{today.day}.png')
