#!/usr/bin/env python3
import pathlib as p, random, sys as s; print(random.choice(s.argv[1:] if s.argv[1:] else [x.strip() for x in open(p.Path("~/.lunchrc").expanduser())] if p.Path("~/.lunchrc").expanduser().exists() else [f"Usage: {s.argv[0]} [option1, option2, ...]\nor add entries one-per-line to {p.Path('~/.lunchrc').expanduser()}"]))
