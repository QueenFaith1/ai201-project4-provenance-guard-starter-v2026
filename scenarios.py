"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""
SCENARIOS = [
    {
        "name": "human writing",
        "criterion": 1,
        "texts": [
            "Los angeles is full of diverse people, Armenians who live in glendale black people in inglewood, baldwin hills, Hispanic people in San fernando valley, White people in beverly hills, Santa monica and Asians in Pasadena, San gabriel Valley, it makes the State look like a melting pot",
            "Gym bros says the rule to bulking or shredding is eating carbs, lean meat & cruciferous veggies, like rice, greenbeans and chicken breast.",
            "Michigan has some great lakes, lake Superior, Sleeping bear dunes, higgins lake, torch lake.",
            "Data Structures & Algorithms, Sql, Python, Excel are courses in Computer Science.",
            "There are 50 states in America, each presenting its unique beauty, culture and people.",
        ],
    },
    {
        "name": "ai writing",
        "criterion": 2,
        "texts": [
            "Effective time management is essential for academic success. By prioritizing tasks, setting clear goals, and minimizing distractions, students can significantly improve their productivity. Furthermore, consistent routines help build sustainable habits over time. Ultimately, a balanced approach leads to better outcomes and reduced stress.",
            "Remote work has transformed the modern workplace in several important ways. It offers flexibility, reduces commuting time, and expands access to talent across the globe. However, it also presents challenges such as communication barriers and difficulty maintaining work-life boundaries. Organizations must therefore adopt thoughtful strategies to support their teams.",
            "Regular physical activity provides numerous benefits for both body and mind. It strengthens the cardiovascular system, improves mood, and enhances overall energy levels. Additionally, exercise can help reduce the risk of chronic conditions. For these reasons, incorporating movement into daily life is highly recommended.",
            "Renewable energy sources play a crucial role in addressing climate change. Solar and wind power, in particular, have become increasingly cost-effective in recent years. By investing in clean infrastructure, communities can reduce emissions while creating new economic opportunities. A sustainable future depends on continued innovation and collaboration.",
            "Effective communication is a cornerstone of strong relationships, both personal and professional. It involves not only expressing ideas clearly but also listening attentively to others. When people feel heard and understood, trust naturally develops. Therefore, investing in communication skills yields long-term benefits for everyone involved.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "   ", "creator_id": "eval_bad_spaces"},
        ],
    },
]

     
    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
