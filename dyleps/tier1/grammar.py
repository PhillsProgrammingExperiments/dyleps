import re
from dyleps.tier1.exceptions import Tier1ParsingException
from dyleps.tier1.structs import Tier1ParseTree, Tier1ParseLeaf

# switch to matching from index

class Tier1Grammar:
    def __init__(self):
        self.rules = {}    # name -> Tier1Rule
        self.tokens = {}   # name -> regex str

    def parse(self, txt, root_rule):
        rule = self.rules[root_rule]
        for alt_name, alt_tuple in rule.alternatives.items():
            match, rest = self._match_alternative(alt_tuple, txt)
            if not match is None:
                match_str = ""
                for m in match:
                    match_str += m.match
                return Tier1ParseTree(
                    root_rule,
                    alt_name,
                    match_str,
                    rest,
                    match
                ), rest
        return None, txt



    def _match_alternative(self, alt_tuple, txt ):
        matched = []
        rest = txt
        for name in alt_tuple:
            if name in self.rules:
                match, rest = self.parse(rest, name)
            elif name in self.tokens:
                match, rest = self._match_token(rest, name)
            else:
                raise Tier1ParsingException("Name %r isn't neither rule, nor token!" % name)
            if match is None:
                break
            else:
                matched.append(match)

        if len(matched) != len(alt_tuple):
            return None, txt

        return matched, rest

    def _match_token(self, txt, name):
        rgx = self.tokens[name]
        match = re.match(rgx, txt)  # add flags
        if match is None:
            return None, txt
        return Tier1ParseLeaf(
            name,
            match.group()
        ), txt[match.end():]