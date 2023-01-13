"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Dev_Py."""


if __name__ == "__main__":
    main(prog_name="dev_py")  # pragma: no cover
