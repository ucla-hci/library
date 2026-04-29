#!/usr/bin/env python3
"""
Script to automatically generate README.md with a list of all paper notes.
Organizes papers by directory (section) with bullet points for each file.
"""

import os
from pathlib import Path

def get_title_from_file(filepath):
    """Extract the first # heading from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    return line[2:]  # Remove '# ' prefix
    except Exception:
        pass
    # Fallback to filename if no title found
    return filepath.stem.replace('_', ' ')

def get_relative_path(filepath, repo_root):
    """Get relative path from repo root to file."""
    return str(Path(filepath).relative_to(repo_root))

def generate_readme(repo_root):
    """Generate README content from paper notes structure."""
    readme_path = Path(repo_root) / 'README.md'
    
    lines = ["# Library", "Notes of what we read", ""]
    
    # Scan directories for paper notes
    dirs_to_scan = []
    
    for item in sorted(os.listdir(repo_root)):
        item_path = Path(repo_root) / item
        # Skip hidden files, special files, and non-directories
        if item.startswith('.') or item.startswith('_') or not item_path.is_dir():
            continue
        if item == 'scripts':  # Skip scripts directory
            continue
        dirs_to_scan.append((item, item_path))
    
    # Process each directory
    for dir_name, dir_path in dirs_to_scan:
        # Check if this directory has subdirectories with papers
        subdirs = []
        files = []
        
        for item in sorted(os.listdir(dir_path)):
            item_path = dir_path / item
            if item.startswith('.') or item.startswith('_'):
                continue
            if item_path.is_dir():
                subdirs.append((item, item_path))
            elif item.endswith('.md'):
                files.append(item)
        
        # Add section for this directory
        lines.append(f"## {dir_name.capitalize()}")
        lines.append("")
        
        # Add files directly in this directory
        for file in sorted(files):
            file_path = dir_path / file
            title = get_title_from_file(file_path)
            rel_path = get_relative_path(file_path, repo_root)
            lines.append(f"- [{title}]({rel_path})")
        
        # Process subdirectories
        for subdir_name, subdir_path in subdirs:
            # Add subsection
            if files:  # Only add subsection header if there were files above
                lines.append("")
            lines.append(f"### {subdir_name.replace('-', ' ').replace('_', ' ').title()}")
            lines.append("")
            
            # List files in subdirectory
            subfiles = [f for f in sorted(os.listdir(subdir_path)) 
                       if f.endswith('.md') and not f.startswith('.')]
            
            for file in sorted(subfiles):
                file_path = subdir_path / file
                title = get_title_from_file(file_path)
                rel_path = get_relative_path(file_path, repo_root)
                lines.append(f"- [{title}]({rel_path})")
        
        lines.append("")
    
    # Write README
    content = '\n'.join(lines).rstrip() + '\n'
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"Updated {readme_path}")

if __name__ == '__main__':
    repo_root = Path(__file__).parent.parent
    generate_readme(repo_root)
