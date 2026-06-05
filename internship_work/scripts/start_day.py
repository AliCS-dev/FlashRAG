import argparse
import re
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
WORK_ROOT = REPO_ROOT / "internship_work"
TEMPLATE_DIR = WORK_ROOT / "templates"
DAILY_NOTES_DIR = WORK_ROOT / "notes" / "daily"
EXPERIMENTS_DIR = WORK_ROOT / "experiments"
CONFIGS_DIR = WORK_ROOT / "configs"


def slugify(value):
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_") or "experiment"


def titleize(slug):
    return slug.replace("_", " ").title()


def read_template(name):
    return (TEMPLATE_DIR / name).read_text(encoding="utf-8")


def write_if_missing(path, content):
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def next_experiment_id():
    max_id = 0
    for path in EXPERIMENTS_DIR.glob("exp_[0-9][0-9][0-9]_*"):
        match = re.match(r"exp_(\d{3})_", path.name)
        if match:
            max_id = max(max_id, int(match.group(1)))
    return max_id + 1


def create_daily_note(today, focus):
    note_path = DAILY_NOTES_DIR / f"{today}.md"
    content = read_template("daily_note.md").format(date=today)
    if focus:
        content = content.replace("## Today Focus\n\n- ", f"## Today Focus\n\n- {focus}")
    created = write_if_missing(note_path, content)
    return note_path, created


def create_experiment(name, today):
    slug = slugify(name)
    existing = sorted(EXPERIMENTS_DIR.glob(f"exp_[0-9][0-9][0-9]_{slug}"))
    if existing:
        exp_dir = existing[0]
        created = []
    else:
        exp_id = next_experiment_id()
        exp_dir = EXPERIMENTS_DIR / f"exp_{exp_id:03d}_{slug}"
        exp_dir.mkdir(parents=True, exist_ok=True)
        created = [exp_dir]

    replacements = {
        "date": today,
        "experiment_title": f"Experiment {exp_dir.name[4:7]}: {titleize(slug)}",
    }
    template_map = {
        "README.md": "experiment_README.md",
        "commands.md": "commands.md",
        "observations.md": "observations.md",
        "summary.md": "summary.md",
    }

    for output_name, template_name in template_map.items():
        content = read_template(template_name).format(**replacements)
        path = exp_dir / output_name
        if write_if_missing(path, content):
            created.append(path)

    shared_config = CONFIGS_DIR / f"{exp_dir.name}.yaml"
    config_content = read_template("config.yaml").replace('save_note: ""', f'save_note: "{exp_dir.name}"')
    if write_if_missing(shared_config, config_content):
        created.append(shared_config)

    local_config = exp_dir / "config.yaml"
    local_config_content = shared_config.read_text(encoding="utf-8")
    if write_if_missing(local_config, local_config_content):
        created.append(local_config)

    return exp_dir, created


def main():
    parser = argparse.ArgumentParser(description="Create a clean daily internship workspace.")
    parser.add_argument("--focus", default="", help="Short focus for today's note.")
    parser.add_argument("--experiment", default="", help="Experiment name, for example: retrieval error analysis.")
    parser.add_argument("--date", default=str(date.today()), help="Override date in YYYY-MM-DD format.")
    args = parser.parse_args()

    note_path, note_created = create_daily_note(args.date, args.focus)

    print(f"Daily note: {note_path.relative_to(REPO_ROOT)}")
    print("Daily note status:", "created" if note_created else "already exists")

    if args.experiment:
        exp_dir, created = create_experiment(args.experiment, args.date)
        print(f"Experiment: {exp_dir.relative_to(REPO_ROOT)}")
        if created:
            print("Created:")
            for path in created:
                print(f"- {path.relative_to(REPO_ROOT)}")
        else:
            print("Experiment status: already exists")


if __name__ == "__main__":
    main()
