from metaL import *

import config

import os

import flask
from flask_socketio import SocketIO

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#################################################### Flask web engine /wrapped/
class Flask(Object):
    def __init__(self, V):
        super().__init__(V)
        self.app = flask.Flask(self.value)
        self.app.config['SECRET_KEY'] = os.urandom(64)
        self.socketio()
        self.watch()

    # front/back async messaging
    def socketio(self):
        self.sio = SocketIO(self.app)
        @self.sio.on('connect')
        def connect(): self.sio.emit('localtime', Time().json())

    # reload on file changes
    def watch(self):
        class Handler(FileSystemEventHandler):
            def __init__(self, sio):
                super().__init__()
                self.sio = sio

            def on_modified(self, event):
                self.sio.emit('reload', [event.src_path])
        self.observer = Observer()
        self.observer.schedule(
            Handler(self.sio), path='static', recursive=True)
        self.observer.schedule(
            Handler(self.sio), path='templates', recursive=True)
        self.observer.start()

    # index global with path
    def lookup(self, path):
        ret = glob
        for i in path.split('/'):
            ret = ret[i]
        return ret

    # run in context
    def eval(self, env, app):
        #
        @self.app.route('/')
        def index(): return flask.render_template('index.html', app=app, env=env)

        @self.app.route('/dump/<path:path>')
        def dump(path): return flask.render_template(
            'index.html', app=app, env=self.lookup(path))
        #
        self.sio.run(self.app, debug=True, host=config.HOST, port=config.PORT)

############################################################### web application
class App(Object):
    def __init__(self, V):
        super().__init__(V)
        self['engine'] = Flask(V)
        glob >> self

    def eval(self, env):
        return self['engine'].eval(env, self)
