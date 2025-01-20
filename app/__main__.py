from app.lib.components.button import button
from app.lib.components.textarea import textarea
from dash_extensions.enrich import DashProxy, html, dcc, Input, Output, callback_context
from dash_extensions import WebSocket
from dash import html, Input, Output, State
import uuid

# Create example app.
app = DashProxy(prevent_initial_callbacks=True)


app.layout = html.Div([
    WebSocket(url="ws://127.0.0.1:60179/ws", id="ws"),
    dcc.Store(id="message-store", data=[]),
    textarea('input'),
    button('Click', 'send-btn'),
    html.Div(id="output"),
])

@app.callback(
    [Output("ws", "send"),  # Send message to WebSocket
    Output("message-store", "data"), # Update message list
    Output("input", "value")], # Clear input field
    [Input("send-btn", "n_clicks"),  # Triggered by Send button
    Input("ws", "message")],  # Triggered by received WebSocket message
    [State("input", "value"),  # User input value
    State("message-store", "data")],  # Current message list
    prevent_initial_call=True
)
def handle_messages(n_clicks, received_message, input_value, messages):
    # Determine the trigger
    triggered_id = callback_context.triggered_id

    # If the send button was clicked
    if triggered_id == "send-btn" and input_value:
        # Append user's message to the message store
        messages.append({ 'data': input_value, 'owner': 'you' })
        # Send the message to WebSocket
        return input_value, messages, ""

    # If a new WebSocket message is received
    elif triggered_id == "ws":
        # Append server's message to the message store
        messages.append({ 'data': received_message['data'], 'owner': 'other' })
        return None, messages, ""

    return None, messages, ""


# Callback to display all messages
@app.callback(
    Output("output", "children"),
    Input("message-store", "data")
)
def display_messages(messages):
    # Render each message as a div
    return [message_component(message['data'], message['owner']) for message in messages]

def message_component(message: str, owner: str):
    return html.Div(
        message,
        id="message_" + str(uuid.uuid4()),
        style={
            'padding': '16px',
            'background-color': '#EEE',
            'border-radius': '8px',
            'margin': '16px',
            'width': '540px',
            'max-width': '70%',
            'margin-left': 'auto' if owner == 'other' else '8px'
        }
    )



if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050)