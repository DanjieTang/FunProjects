# /// script
# requires-python = ">=3.10"
# dependencies = ["typesafe-sdk", "python-dotenv"]
# ///
"""Send one Noul question to TypeSafe's Jev model to check the API is reachable.

Run with:  uv run main.py ["some statement to check"]
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from typesafe_sdk import Noul, TypeSafeClient

load_dotenv(Path(__file__).parent / ".env")

statement = (
    sys.argv[1]
    if len(sys.argv) > 1
    else "The Great Wall of China is visible from the Moon with the naked eye."
)

# The SDK looks for TYPESAFE_API_KEY by default, so pass our key explicitly.
with TypeSafeClient(api_key=os.environ["JEV_API_KEY"]) as client:
    response = client.system_one(
        model="jev-latest",
        state=statement,
        questions={
            "is_true": Noul(instructions="Is this statement factually true?"),
        },
    )

# noul is the probability (0 to 1) that the answer is yes.
p_true = response.answers["is_true"].noul

print(f"Model:     {response.model}")
print(f"Statement: {statement}")
print(f"P(true):   {p_true:.2f}")
if p_true >= 0.7:
    print("Verdict:   true")
elif p_true <= 0.3:
    print("Verdict:   false")
else:
    print("Verdict:   unsure")
print(f"Usage:     {response.usage}")
