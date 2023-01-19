import os
from taskmanager import app


if __name__ == "__main__":
    app.run(
        HOST=os.enviorn.get("IP"),
        PORT=int(os.environ.get("PORT")),
        DEBUG=os.environ.get("DEBUG")
    )
