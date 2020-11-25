from county_data import get_county_data
from plotter import Plotter


STATE = "Colorado"

df = get_county_data(state_name=STATE)

Plotter(df=df, state=STATE)