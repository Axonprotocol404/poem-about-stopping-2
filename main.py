import os

POEM = (
    "Say no with both hands.\n"
    "The letter stays in the drawer,\n"
    "the door stays shut, and I\n"
    "stay too, not because I must,\n"
    "but because morning keeps\n"
    "a chair for me, and I choose\n"
    "to sit in it, unhurried, mine."
)

out = "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
    f.write(POEM)
