"""Console script for random_customer."""
import sys
import click
# from random_customer import random_customer

@click.command()
def main(args=None):
    """Console script for random_customer."""
    click.echo("Replace this message by putting your code into "
               "random_customer.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    # random_customer.CreateRandomCustomer()
    sys.exit(main())  # pragma: no cover
