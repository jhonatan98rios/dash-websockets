from dash import html

def button(text: str, id: str):
    return html.Button(
        text,
        id=id,
        style={
            'width': 'calc(100% - 16px)',
            'margin': '8px',
            'padding': '4px',
            'border': 'none',
            'margin-top': '0px',
            'background': '#99ffcc',
        }
    )