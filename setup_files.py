"""Create symlinks to the dotfiles in this repo.
"""
import sys
from pathlib import Path

if sys.platform == 'darwin':
    print('\nMacOS detected, setting up dotfiles...\n')
else:
    raise RuntimeError('Only for MacOS supported currently.')

########## Setup dotfiles ##########
repo_root: Path = Path(__file__).parent
home: Path = Path.home()
files = [
    (repo_root / 'justfile', home / 'justfile'),
    (repo_root / '.aliases', home / '.aliases'),
]
for source, target in files:
    if target.exists():
        assert target.is_symlink() and target.resolve() == source
        print(f'[x] (exists) {target} -> {source}')
        continue
    target.symlink_to(source)
    assert target.is_symlink() and target.resolve() == source
    print(f'[x] (created) {source} -> {target}')
