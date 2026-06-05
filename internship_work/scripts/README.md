# Scripts

Store helper scripts here for internship experiments:

- dataset checks
- retrieval debugging
- preprocessing helpers
- result inspection
- one-off experiment runners

## Daily Setup

Create or reopen today's note:

```bash
python3 internship_work/scripts/start_day.py --focus "today's goal"
```

Create today's note and a new experiment folder:

```bash
python3 internship_work/scripts/start_day.py \
  --focus "today's goal" \
  --experiment "short experiment name"
```

If a script becomes generally useful for FlashRAG users, move or rewrite it under the main project structure later.
