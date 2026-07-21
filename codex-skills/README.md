# Codex Skills

Version-controlled interview practice skills for Codex.

Skills are maintained in [.cursor/skills](../.cursor/skills/) and symlinked here for Codex compatibility.

## Setup

Symlink each skill into your Codex skills directory:

```bash
ln -sf "$(pwd)/.cursor/skills/interview-learning" ~/.codex/skills/interview-learning
ln -sf "$(pwd)/.cursor/skills/interview-recap" ~/.codex/skills/interview-recap
```

Or symlink via this directory (which points to `.cursor/skills/`):

```bash
ln -sf "$(pwd)/codex-skills/interview-learning" ~/.codex/skills/interview-learning
ln -sf "$(pwd)/codex-skills/interview-recap" ~/.codex/skills/interview-recap
```

Keep system skills, plugin caches, tokens, and local Codex state out of this repository.

## Cursor

No setup needed — open this repository in Cursor and the skills in `.cursor/skills/` are available automatically.
