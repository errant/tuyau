from tuyau.grammar import BaseClass, parse
import click


def loadFromFile(filepath):
    tokens = parse(open(filepath).read())
    return Pipeline(tokens)

class Pipeline(BaseClass):
    def __init__(self, tokens):
        super(self.__class__, self).__init__(tokens)
        self._inheritParameter('stages', tokens)
    def run(self):
        click.echo('Pipeline: %s' % self.name)
        self.stages = map(lambda stage: Stage(stage), self.stages)
        for stage in self.stages:
            stage.run()


class Stage(BaseClass):
    def __init__(self, tokens):
        super(self.__class__, self).__init__(tokens)
        self._inheritParameter('steps', tokens)
    def run(self):
        click.echo('Stage: %s' % self.name)
        self.steps = map(lambda step: stepObjects[step.type](step), self.steps)
        for step in self.steps:
            step.run()

class Step(BaseClass):
    def __init__(self, tokens):
        #super(self.__class__, self).__init__(tokens)
        self.parameters = tokens[1]

stepObjects = {}
def setStepObject(step, stepObject):
    global stepObjects
    stepObjects[step] = stepObject
