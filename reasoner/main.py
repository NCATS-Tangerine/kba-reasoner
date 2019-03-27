import connexion
from openapi_server import encoder
from flask import redirect

ARGUMENTS = {
    'title': 'OpenAPI for NCATS Biomedical Translator Reasoners'
}

PORT=8080

def main(name:str):
    """
    Sets up and runs the web application.
    Usage in server/openapi_server/__main__.py:

        from reasoner import main
        if __name__ == '__main__':
            main(__name__)
    """
    app = connexion.App(name, specification_dir='./openapi/')

    app.app.json_encoder = encoder.JSONEncoder
    app.app.json_encoder.include_nulls = True

    api = app.add_api(
        'openapi.yaml',
        arguments=ARGUMENTS
    )

    app.add_error_handler(404, lambda e: redirect('{}/ui/'.format(api.base_path)))

    app.run(port=PORT)
