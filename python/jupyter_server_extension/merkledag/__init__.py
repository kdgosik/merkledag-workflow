
# Example From: https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html#Defining-the-bundler-extension
# import tarfile
# import io
# import os
# import nbformat
#
# def _jupyter_bundlerextension_paths():
#     """Declare bundler extensions provided by this package."""
#     return [{
#         # unique bundler name
#         "name": "tarball_bundler",
#         # module containing bundle function
#         "module_name": "my_tarball_bundler",
#         # human-redable menu item label
#         "label" : "Notebook Tarball (tar.gz)",
#         # group under 'deploy' or 'download' menu
#         "group" : "download",
#     }]
#
#
# def bundle(handler, model):
#     """Create a compressed tarball containing the notebook document.
#
#     Parameters
#     ----------
#     handler : tornado.web.RequestHandler
#         Handler that serviced the bundle request
#     model : dict
#         Notebook model from the configured ContentManager
#     """
#     notebook_filename = model['name']
#     notebook_content = nbformat.writes(model['content']).encode('utf-8')
#     notebook_name = os.path.splitext(notebook_filename)[0]
#     tar_filename = '{}.tar.gz'.format(notebook_name)
#
#     info = tarfile.TarInfo(notebook_filename)
#     info.size = len(notebook_content)
#
#     with io.BytesIO() as tar_buffer:
#         with tarfile.open(tar_filename, "w:gz", fileobj=tar_buffer) as tar:
#             tar.addfile(info, io.BytesIO(notebook_content))
#
#         # Set headers to trigger browser download
#         handler.set_header('Content-Disposition',
#                            'attachment; filename="{}"'.format(tar_filename))
#         handler.set_header('Content-Type', 'application/gzip')
#
#         # Return the buffer value as the response
#         handler.finish(tar_buffer.getvalue())



def _jupyter_server_extension_paths():
    return [{
        "module": "merkledag"
    }]

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `merkle_dag` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="merkledag",
        # _also_ in the `nbextension/` namespace
        require="merkledag/index")]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("my module enabled!")
