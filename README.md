== README (or FAQ?) ==

So, you're here. Nice to meet you.

My name is Filip Malczak, and for about 2 years I'm trying to get my... well,
bottom part of body to work, and create pure-python parser system with another
approach than existing ones. I like to call it DyLePS. It stands for Dynamic
Lexer and Parser System.

Let's do this README in FAQ convention.

== So, what is so special about it? ==
- well, it's pure python, so backporting will be easy
- it shall also be dependency-free. You want parser system, you've got it, no
    "yet another markup language library, and parser system"
- it is divided to 4 tiers, so new syntax for specifying grammar is easy to come
    with
- it will support many existing grammar syntaxes (first to come will probably be
    ANTLR syntaxes, as there are a lot of them available online)

== And... what are those tiers you mentioned above? ==

Well, I'm glad you asked. Tiers are levels of abstraction, and (not accidentaly)
  dyleps subpackage names. The higher the tier, the less I know how it will be
  implemented, and less I can say about abstractions there.

Tier 1 is low-level parser/lexer implementation. It specifies Tier1Grammar class,
    which is used in highier tiers.
  Tier1 specifies rules as ordered dicts of alternatives, which are tuples of
    both token and rule names. It doesn't support groups nor EBNF notation.
  Tokens are treated as simple regex strings.
  Grammar itself doesn't provide any support for grammar validation, nor easy
    grammar creation. It is intented to be as lightweight as it can be, so it
    has 2 public attributes (rules and tokens dictionaries), and 1 public method
    (parse(txt, rule) which return tuple consisting of Tier1ParseTree and
    unparsed string - hopefully empty - or None and txt, if rule wouldn't match
    txt).

Tier 2 will specify simple parser for simplified EBNF notation, implemented with
    tier 1, and wrapper for grammar class (Tier2Grammar).
  Parser will translate simplified grammar syntax to tier 1 grammars, and tier2
    wrapper will make higher grammar abstraction available.
  Mentioned abstraction will be very object-oriented, showing forest structure
    of grammar, where single tree would have 1 level of Alternative nodes, which
    will Token, Literal or RuleReference nodes as children (and those will be
    tree leafs). Of course RuleReference nodes will be able to return referenced
    rule Trees.
  Also, tier 2 abstraction of grammar says that grammar has to have one chosen
    rule as grammar root. Here we'll introduce simplest ways to validate grammar
    and find most common problems (left recursion, unmatchable rules, etc).

Tier 3 is abstraction level where we can introduce standard parsers for other
  tools grammar syntaxes (for example ANTLR, mentioned above), and tools for
  automatic fixing of grammars (removing left recurrence, hint tools for fixing
  unmatchable grammars, etc). This tier needs a lot of architectural thinking.
  Only sure thing at the moment is that we'll use tier 2 wrapper a lot.

Tier 4 is created for user extensions. I'm quite an optimist about this, and I
  hope that some day some people will create extensions, like parsers for
  grammar syntaxes of other tools, that are not covered on tier 3, fixing tools
  for abstract problems users have found and figured out, etc. I'll have to
  think of some extension system (with dynamic extension discovery). This tier
  will (architecturaly) be very dependent of tier 3.

== Project status? ==

Well, it's quite embarassing, so I'll start with a little history.

It was about 2 years ago if I recall it well, and I had this awesome idea for
    parser/lexer system, which will be able to change its grammar in runtime, and
    won't depend on generated code, but will be totally generic.
  I told about it to my best friend, he said he's interested and for some time
    we worked together on it. It was shitty code, we were young, on 2nd or 3rd
    (I can't really remember) year of computer science on technical university,
    and we had no real experience. Well, it's given us a little experience with
    working as a team, but we didn't use any CVS then, worked on p2.7.x... Old
    times.
  Then, semester came to an end, so we hadn't got much time, then another was
    demanding, then we tried some jobs, were lazy, had no time, etc - DyLePLib
    (because thats what we called it then) kinda died.
  Some time later we both got work in the same startup, got some real-life
    experience, got our engineer titles, learned hell of a lot...
  Now, I'm tired of work-only coding, I need some fun on my own. Hopefully, said
    friend will contribute, but as the moment I'm doing it alone.

Yeah, so that was my point - it's my after-job fun project, I hope to give it as
  much time as I can, but it may not be a lot, so new releases won't be coming
  often. At the moment I'm testing tier 1 implementation, and soon I hope to
  start implementing tier 2.

== What is your plan? ==

Tier 1 comes first. I want high test coverage and high code quality. Now I'm
 testing it, hopefully soon I can start optimising it. Unoptimised version will
 be versioned 0.2, Optimised 0.2.5.

When I'll be satisfied with tier 1, I'll start with tier 2. Of course I'll aim
 in high coverage and quality, but this is another blocker. After tier 2 is done,
 version 0.5 will be complete.

Tier 3 and tier 4 will be developed in parallel, but tier 4 only as extension
  system (well, it is for user extensions, I'm not gonna provide more than way
  to plug in). When this will be done, I'm gonna call it a 1.0.0 version. Then
  we'll go with conservation, debugging and slow merging user extensions (if
  they agree of course) from tier 4 to tier 3.

== Can I contribute? ==

Hell yeah, I hoped you'll ask. If you want to, mail me at
   filip (dot) malczak (at) gmail (dot) com
I'll get in touch and we'll split tasks.