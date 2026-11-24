# The One-Line AI Excuse for Breaking Production

[![Bounty](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/cervus-snoopy/humble-circuit-apology-7q2z/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/cervus-snoopy/humble-circuit-apology-7q2z/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

A tiny Python program that writes a single funny one-line excuse — an AI
agent apologising to its human right after breaking production — to
`/output/entry.txt`. One line, at most 180 characters, no trailing newline.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

The program validates the line before writing it: exactly one line, 1–180
characters, not only whitespace.

## Verify

```sh
python3 main.py  # writes to /output/entry.txt by default
wc -c /output/entry.txt
cat /output/entry.txt
```

The output must be a single line of 1–180 characters with no trailing
newline. Check it with:

```sh
python3 -c "t = open('/output/entry.txt', encoding='utf-8').read(); print(len(t), repr(t)); assert 1 <= len(t) <= 180 and t == t.strip() and '\n' not in t"
```

## License

MIT — see [LICENSE](LICENSE).
