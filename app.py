from pathlib import Path

import pandas as pd
import plotly.express as px
from shiny import reactive
from shiny.express import input, ui
from shinywidgets import render_plotly

ui.page_opts(title="Sales Dashboard", fillable=True)

ui.input_numeric("num", label="Enter a number of Items", value=5, min=0, max=20)


@reactive.calc
def dat():
    infile = Path(__file__).parent / "data/sales.csv"
    return pd.read_csv(infile)


with ui.layout_columns():
    # @render_plotly
    # def plot1():
    #     df = dat()
    #     return px.histogram(px.data.tips(), y="tip")

    # @render_plotly
    # def plot2():
    #     return px.histogram(px.data.tips(), y="total_bill")

    @render_plotly
    def plot3():
        df = dat()
        top_sales = df.groupby('product')['quantity_ordered'].sum().nlargest(input.num()).reset_index()
        return px.bar(top_sales, x='product', y='quantity_ordered')

    # @render.data_frame
    # def data():
    #     return dat()
    ui.input_selectize(
        "city",
        "Select a City:",
        [
            "Dallas (TX)",
            "Boston (MA)",
            "Los Angeles (CA)",
            "San Francisco (CA)",
            "Seattle (WA)",
            "Atlanta (GA)",
            "New York City (NY)",
            "Portland (OR)",
            "Austin (TX)",
            "Portland (ME)",
        ],
        multiple=False,
        selected='Boston (MA)'
    )
