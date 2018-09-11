
def _jupyter_server_extension_paths():
    return [{
        "module": "merkle_dag"
    }]

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `merkle_dag` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="merkle_dag",
        # _also_ in the `nbextension/` namespace
        require="merkle_dag/index")]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("my module enabled!")