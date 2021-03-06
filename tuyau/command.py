import tuyau.pipeline
import click

@click.group()
@click.option('--debug/--no-debug', default=False)
def execute(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@execute.command()
@click.option('--template', default=False)
def pipeline(template):
    pl = tuyau.pipeline.loadFromFile('examples/echo.pipeline')
    pl.run()
