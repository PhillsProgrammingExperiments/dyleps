from collections import OrderedDict
from unittest import TestCase
from dyleps.tier1.grammar import Tier1Grammar
from dyleps.tier1.structs import Tier1Rule, Tier1ParseTree, Tier1ParseLeaf


class SumGrammarTest(TestCase):
    def setUp(self):
        g = Tier1Grammar()

        g.tokens["int"] = r"\d+"
        g.tokens["plus"] = r"[+]"

        sum_rules = OrderedDict()
        sum_rules["complex"]=("int", "plus", "sum")
        sum_rules["basic"] = ("int", )
        g.rules["sum"] = Tier1Rule(
            sum_rules
        )
        self.g =g

    def test_basic_alt(self):
        basic, rest = self.g.parse("1", "sum")
        self.assertEqual(basic, Tier1ParseTree(
            "sum", "basic",
            "1", "",
            [
                Tier1ParseLeaf(
                    "int",
                    "1"
                )
            ]
        ))
        self.assertEqual(rest, "")

    def test_complex_alt(self):
        complex, rest = self.g.parse("1+2", "sum")
        self.assertEqual(complex, Tier1ParseTree(
            "sum", "complex",
            "1+2", "",
            [
                Tier1ParseLeaf(
                    "int",
                    "1"
                ),
                Tier1ParseLeaf(
                    "plus",
                    "+"
                ),
                Tier1ParseTree(
                    "sum", "basic",
                    "2", "",
                    [
                        Tier1ParseLeaf(
                            "int",
                            "2"
                        )
                    ]
                )
            ]
        ))

    def test_complex_recursive_alt(self):
        complex, rest = self.g.parse("1+2+3", "sum")
        self.assertEqual(complex, Tier1ParseTree(
            "sum", "complex",
            "1+2+3", "",
            [
                Tier1ParseLeaf(
                    "int",
                    "1"
                ),
                Tier1ParseLeaf(
                    "plus",
                    "+"
                ),
                Tier1ParseTree(
                    "sum", "complex",
                    "2+3", "",
                    [
                        Tier1ParseLeaf(
                            "int",
                            "2"
                        ),
                        Tier1ParseLeaf(
                            "plus",
                            "+"
                        ),
                        Tier1ParseTree(
                            "sum", "basic",
                            "3", "",
                            [
                                Tier1ParseLeaf(
                                    "int",
                                    "3"
                                )
                            ]
                        )
                    ]
                )
            ]
        ))