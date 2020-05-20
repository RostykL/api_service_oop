from flask import request, jsonify

import config
import models
connex_app = config.connex_app


# Run Server
if __name__ == "__main__":
    connex_app.run(debug=True)