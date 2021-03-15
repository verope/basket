import base64
import dash_html_components as html

footer = html.Div([
    html.Div([
        html.A('Github', className="footer-link",  href="https://github.com/verope/basket"),
        html.A('Medium', className="footer-link", href="https://ringle-czechitas.medium.com/spot%C5%99ebn%C3%AD-potravinov%C3%BD-ko%C5%A1-c171d38c906d"),
    ], className="footer-container"), 
], className="footer")