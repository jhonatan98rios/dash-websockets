from dash_extensions.enrich import DashProxy, html, dcc, Input, Output, callback_context
from dash_extensions import WebSocket
from dash import html, Input, Output, State

# Create example app.
app = DashProxy(prevent_initial_callbacks=True)


app.layout = html.Div([
    WebSocket(url="ws://127.0.0.1:3000/ws", id="ws"),
    dcc.Store(id="message-store", data=[]),
    dcc.Input(id="input", autoComplete="off", type="text", placeholder="Type a message"), 
    html.Button("Click", id="send-btn"),
    html.Div(id="output"),
])

@app.callback(
    [Output("ws", "send"),  # Send message to WebSocket
     Output("message-store", "data")],  # Update message list
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
        messages.append(f"You: {input_value}")
        # Send the message to WebSocket
        return input_value, messages

    # If a new WebSocket message is received
    elif triggered_id == "ws":
        # Append server's message to the message store
        messages.append(f"Server: {received_message['data']}")
        return None, messages

    return None, messages


# Callback to display all messages
@app.callback(
    Output("output", "children"),
    Input("message-store", "data")
)
def display_messages(messages):
    # Render each message as a div
    return [html.Div(message) for message in messages]

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050)