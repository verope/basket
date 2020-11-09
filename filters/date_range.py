import dash_core_components as dcc
import dash_html_components as html
import datetime
from datetime import datetime as dt
from db_connection import itescoKosDf

date_range_picker = html.Div(
    [   
        html.P('Select Date Range:'),
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date=itescoKosDf['date'].min(),
            end_date=dt.now().date() - datetime.timedelta(days=1),
            clearable=True,
            display_format="MMM DD, YYYY",
            first_day_of_week=1,
            number_of_months_shown=2,
            stay_open_on_select=True
        )
    ], className="filter_cell")
