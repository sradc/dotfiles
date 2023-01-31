"""Create symlinks to the dotfiles in this repo.
"""
import sys
from pathlib import Path
from subprocess import run

if sys.platform == "darwin":
    print("\nMacOS detected...\n")
else:
    raise RuntimeError("Only for MacOS supported currently.")

########## Setup dotfiles ##########
print("Setting up dotfile symlinks...")
repo_root: Path = Path(__file__).parent
home: Path = Path.home()
files = [
    (repo_root / "justfile", home / "justfile"),
    (repo_root / ".aliases", home / ".aliases"),
]
for source, target in files:
    if target.exists():
        assert target.is_symlink() and target.resolve() == source
        print(f"[x] (exists) {target} -> {source}")
        continue
    target.symlink_to(source)
    assert target.is_symlink() and target.resolve() == source
    print(f"[x] (created) {source} -> {target}")

########## Setup global gitignore ##########
run(
    [
        "git",
        "config",
        "--global",
        "core.excludesfile",
        str(repo_root / ".gitignore_global"),
    ]
)
print()
print("Configured git to use global .gitignore_global.")
