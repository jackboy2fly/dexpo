from os import getenv
from typing import Annotated

import typer

from .callbacks import project_callback, version_callback
from .info import get_project_info, get_vuln_info
from .outputs import write_project_info, write_vuln_info


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
    report: Annotated[
        bool,
        typer.Option(
            help="Enable to write console output to svg files in cwd.",
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
    Print basic reports (and optionally write to SVG files with `--report` flag) about a pypi PROJECT's reputation and security.
    """
    project_info = get_project_info(project, api_key)
    write_project_info(project_info, report)
    vuln_info = get_vuln_info(project, project_info["latest_release_number"])
    if vuln_info:
        write_vuln_info(vuln_info, report)
