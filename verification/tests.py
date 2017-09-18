"""
TESTS is a dict with all you tests.

Keys for this will be categories' names.
Each test is a dict with:
    "input" -- input data for user function
    "answer" -- the expected answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "sdsffffse",
            "answer": 4,
            "explanation": "'ffff'"
        },
        {
            "input": "ddvvrwwwrggg",
            "answer": 3,
            "explanation": "'www' and 'ggg' have a length of 3"
        }
    ],
    "Extra": [
        {
            "input": "",
            "answer": 0,
            "explanation":
                "The longest substring of an empty " +
                "string can only have a length of 0"
        },
        {
            "input": "'abababaab'",
            "answer": 2,
            "explanation": "'aa'"
        },
        {
            "input": "'abababa'",
            "answer": 1,
            "explanation": "'a' and 'b' have a length of 1"
        },
        {
            "input": "aa",
            "answer": 2,
            "explanation": "'aa'"
        }
    ]
}
