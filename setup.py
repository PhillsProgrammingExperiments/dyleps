from distutils.core import setup

setup(
    name="DyLePS",
    version="0.0.1",
    description="Dynamic Lexer and Parser System",
    packages = [
        "dyleps",
        "dyleps.tier1",
        "dyleps.utils"
    ],
    author="Filip Malczak",
    author_email="filip(dot)malczak(at)gmail(dot)com",
    platforms =[ "Any"],
)
