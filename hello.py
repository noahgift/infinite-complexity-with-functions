import click

def one(x):
    """input is variable, unit is work is x+1, result is return"""
    return x + 1


def two(xx):
    """input, unit of work, result"""

    return xx + 2


def three(xxx):
    """input, unit of work, result"""

    return xxx + 3

@click.command()
@click.option("--myinput")
def main(myinput):
    from_click = int(myinput)
    x = one(from_click)
    print(x)
    xx = two(x)
    print(xx)
    xxx = three(xx)
    click.echo(click.style(f"Click CLI returns {xxx}", fg='green'))
    return xxx


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
