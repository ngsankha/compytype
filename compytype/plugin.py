from mypy.types import LiteralType
from mypy.plugin import Plugin

def type_add(ctx, *args):
    trecv = ctx.type
    targs = ctx.arg_types
    if trecv.__class__ is LiteralType and len(targs) == 1 and targs[0][0].__class__ is LiteralType:
        ret = trecv.value + targs[0][0].value
        return LiteralType(ret, fallback=ctx.api.named_generic_type('builtins.int', []))
    else:
        return None

TYPE_DICT = {
    'builtins.int.__add__': type_add
}

class ComPyTypePlugin(Plugin):

    def get_method_hook(self, fullname):
        return TYPE_DICT.get(fullname, None)

def plugin(version: str):
    # ignore version argument if the plugin works with all mypy versions.
    return ComPyTypePlugin
