from pyparsing import *

def _constructGrammar():
    ParserElement.setDefaultWhitespaceChars(' \t')
    newline = Optional(Suppress('\n'))
    openbrace = Suppress("{")
    closebrace = Suppress("}")
    openbracket = Suppress("(")
    closebracket = Suppress(")")
    quote = Suppress("\"")
    colon = Suppress(":")

    def justStringNotList(tokens):
        return tokens[0]
    def paramGroup(tokens):
        params = {}
        i = 0
        for token in tokens:
            if len(token) > 1:
                params[token[0]] = token[1]
            else:
                params[i] = token[0]
            i += 1
        return params

    # Grammar
    name = Optional(openbracket) + quote + Word(alphanums+' ').setResultsName('name').setParseAction(justStringNotList) + quote + Optional(closebracket)
    parameter = Group(Optional(Word(alphas)) + Optional(colon) + quote + Word(alphanums+' '+'-') + quote)
    optionalParamGroup = Optional(openbracket) + OneOrMore(parameter).setParseAction(paramGroup).setResultsName('options') + Optional(closebracket) + newline
    step = Word(alphas) + optionalParamGroup
    steps = Group(Or([Keyword('with'), Word(alphas)]).setResultsName('type')  + optionalParamGroup+ Optional(Group(openbrace + newline + OneOrMore(step) + closebrace)) + newline)
    stage = Group(Keyword("stage") + name +  openbrace + newline + OneOrMore(steps).setResultsName('steps') + newline + closebrace + newline)
    options = Group(Word(alphas) + colon + Optional(quote) + Word(alphanums+' ') + Optional(quote)) + newline

    pipeline = Keyword("pipeline") + name + openbrace + newline + ZeroOrMore(options).setResultsName('options').setParseAction(paramGroup) + OneOrMore(stage).setResultsName('stages') + closebrace
    return pipeline

DSL = _constructGrammar()

def parse(pipeline):
    return DSL.parseString(pipeline)


class BaseClass(str):
    def _inheritParameter(self, parameter, tokens):
        if parameter in tokens:
            self.__dict__[parameter] = tokens.__getattr__(parameter)
    def __init__(self, tokens):
        self._inheritParameter('name', tokens)
        self._inheritParameter('options', tokens)
