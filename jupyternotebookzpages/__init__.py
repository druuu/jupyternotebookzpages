from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler


class Healthz(IPythonHandler):
    def get(self):
        self.set_status(200)
        self.finish('ok')

def load_jupyter_server_extension(nb_app):
    web_app = nb_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/healthz')
    web_app.add_handlers(host_pattern, [(route_pattern, Healthz)])
