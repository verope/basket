import dash_html_components as html
from filters.date_range import date_range_picker

datepicker = html.Div([date_range_picker], className="filter__container")
