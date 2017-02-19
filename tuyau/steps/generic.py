from tuyau.pipeline import Step, setStepObject
import click, subprocess


class EchoStep(Step):
    def run(self):
        click.echo(self.parameters[0])

setStepObject('echo', EchoStep)


class ShStep(Step):
    def run(self):
        click.echo(subprocess.check_output(self.parameters.values()))

setStepObject('sh', ShStep)
