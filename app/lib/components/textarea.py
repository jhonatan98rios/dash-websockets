from dash import dcc

def textarea(id: str):
    return dcc.Textarea(
        id=id,
        placeholder="Type a message",
        style={
            'width': 'calc(100% - 32px)',
            'margin': '8px',
            'border-radius': '8px',
            'padding': '8px',
        }
    )