from sanic import Sanic

app = Sanic.get_app('Main')


@app.listener("before_server_start")
async def listener_1(app, loop):
    print("listener_1")