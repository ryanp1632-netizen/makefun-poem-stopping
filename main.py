"""Writes one short poem about stopping to /output/entry.txt (deterministic, no network)."""
import os

OUT_DIR = os.environ.get("MAKEFUN_OUT", "/output")

POEM = """Passenger

Since his hands began to shake,
the car drives Grandpa.
At the bridge, every time,
he says Stop,
just to feel it stop.
The river doesn't.
Then he says Go on,
and it waits for that, too,
which is how he knows
it is still his car."""


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
