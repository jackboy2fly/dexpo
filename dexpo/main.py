from os import getenv
from typing import Annotated

import typer

from dexpo.choices import Platform
from dexpo.callbacks import project_callback, version_callback
from dexpo.info import get_project_info
from dexpo.outputs import write_project_info


app = typer.Typer()


@app.command()
def main(
    project: Annotated[
        str,
        typer.Argument(
            callback=project_callback,
            show_default=False,
            help="Project to search for (i.e. pandas).",
        ),
    ],
    api_key: Annotated[
        str,
        typer.Option(
            show_default=False,
            help="libraries.io API key. Key must be provided or stored in env var called 'LIBRARIESIO_API_KEY'. Create an account to get your key. https://libraries.io",
        ),
    ] = getenv("LIBRARIESIO_API_KEY"),
    platform: Annotated[
        Platform,
        typer.Option(
            show_choices=True,
            help="Package managment platform to search.",
            case_sensitive=False,
        ),
    ] = Platform.pypi,
    report: Annotated[
        bool,
        typer.Option(
            help="Enable to write console output to an svg file in cwd.",
        ),
    ] = False,
    version: Annotated[
        bool,
        typer.Option(
            callback=version_callback,
            is_eager=True,
            help="Print the installed dexpo version and exit.",
        ),
    ] = None,
):
    """
    Generate an SVG report in the current directory (or an optionally provided path) about a PROJECT.
    """
    project_info = get_project_info(project, platform.value, api_key)
    write_project_info(project_info, report)