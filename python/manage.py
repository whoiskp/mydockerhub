import os
import unittest

from src import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)

# project_root_path = os.path.join(os.path.dirname(app.root_path))


@manager.command
def run(port=5000):
    print('app running..')
    app.run(host='0.0.0.0', port=port, debug=True)


if __name__ == "__main__":
    manager.run()
