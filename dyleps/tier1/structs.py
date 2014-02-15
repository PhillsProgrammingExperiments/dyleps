from collections import OrderedDict
from dyleps.utils.structs import named_validable_tuple

Tier1Rule = named_validable_tuple("Tier1Rule", [
    ("alternatives", OrderedDict)   # alternative name -> tuple of str
                                    # (rule/token names)
])

Tier1ParseTree = named_validable_tuple("Tier1ParseTree", [
    ("rule", str),
    ("alternative", str),
    ("match", str),
    ("rest", str),
    ("body", OrderedDict)   # rule element -> Tier1Parse{Tree, Leaf}
])

Tier1ParseLeaf = named_validable_tuple("Tier1ParseLeaf", [
    ("token", str),
    ("match", str)
])