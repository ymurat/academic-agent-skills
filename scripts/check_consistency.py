#!/usr/bin/env python3
"""
Consistency checks for academic-agent-skills repository.

Validates:
- SKILL.md files have valid YAML frontmatter with name and description
- Skill names match folder names
- README catalog entries match actual skills
- LICENSE-upstream files match THIRD_PARTY.md entries
- No personal email addresses in the repo
- No em dashes in key documentation files
- CITATION.cff is valid YAML and version matches CHANGELOG
"""

import os
import re
import sys
import yaml
from pathlib import Path
from typing import List, Tuple, Set


def check_skill_frontmatter(skills_dir: Path) -> List[str]:
    """Check that every SKILL.md has valid frontmatter with name and description."""
    errors = []
    
    for skill_folder in sorted(skills_dir.iterdir()):
        if not skill_folder.is_dir() or skill_folder.name.startswith('.'):
            continue
        
        skill_md = skill_folder / 'SKILL.md'
        if not skill_md.exists():
            errors.append(f"Missing SKILL.md in {skill_folder.name}/")
            continue
        
        content = skill_md.read_text(encoding='utf-8')
        
        # Extract frontmatter
        if not content.startswith('---\n'):
            errors.append(f"{skill_folder.name}/SKILL.md: Missing YAML frontmatter")
            continue
        
        parts = content.split('---\n', 2)
        if len(parts) < 3:
            errors.append(f"{skill_folder.name}/SKILL.md: Malformed frontmatter")
            continue
        
        try:
            frontmatter = yaml.safe_load(parts[1])
        except yaml.YAMLError as e:
            errors.append(f"{skill_folder.name}/SKILL.md: Invalid YAML frontmatter - {e}")
            continue
        
        # Check required fields
        if 'name' not in frontmatter:
            errors.append(f"{skill_folder.name}/SKILL.md: Missing 'name' in frontmatter")
        elif frontmatter['name'] != skill_folder.name:
            errors.append(
                f"{skill_folder.name}/SKILL.md: name '{frontmatter['name']}' "
                f"does not match folder name '{skill_folder.name}'"
            )
        
        if 'description' not in frontmatter:
            errors.append(f"{skill_folder.name}/SKILL.md: Missing 'description' in frontmatter")
        elif not isinstance(frontmatter['description'], str) or not frontmatter['description'].strip():
            errors.append(f"{skill_folder.name}/SKILL.md: 'description' must be a non-empty string")
    
    return errors


def check_readme_catalog(repo_root: Path, skills_dir: Path) -> List[str]:
    """Check that README catalog matches actual skill folders."""
    errors = []
    
    readme_path = repo_root / 'README.md'
    readme_content = readme_path.read_text(encoding='utf-8')
    
    # Extract skill names from catalog (lines with [`skill-name`](skills/skill-name/))
    catalog_pattern = r'\[`([^`]+)`\]\(skills/([^/]+)/\)'
    catalog_skills = set()
    
    for match in re.finditer(catalog_pattern, readme_content):
        catalog_name = match.group(1)
        catalog_path = match.group(2)
        if catalog_name != catalog_path:
            errors.append(
                f"README.md: Catalog entry [`{catalog_name}`] path mismatch: "
                f"expected skills/{catalog_name}/, got skills/{catalog_path}/"
            )
        catalog_skills.add(catalog_name)
    
    # Get actual skill folders
    actual_skills = {
        d.name for d in skills_dir.iterdir() 
        if d.is_dir() and not d.name.startswith('.')
    }
    
    # Check for missing entries
    missing_in_catalog = actual_skills - catalog_skills
    if missing_in_catalog:
        errors.append(
            f"README.md: Skills missing from catalog: {', '.join(sorted(missing_in_catalog))}"
        )
    
    # Check for extra entries
    extra_in_catalog = catalog_skills - actual_skills
    if extra_in_catalog:
        errors.append(
            f"README.md: Catalog entries pointing to non-existent skills: "
            f"{', '.join(sorted(extra_in_catalog))}"
        )
    
    return errors


def check_license_files(repo_root: Path, skills_dir: Path) -> List[str]:
    """Check LICENSE-upstream files match THIRD_PARTY.md entries."""
    errors = []
    
    third_party_path = repo_root / 'THIRD_PARTY.md'
    third_party_content = third_party_path.read_text(encoding='utf-8')
    
    # Parse THIRD_PARTY.md for adapted skills
    # Look for skill names as headers (e.g., "## skill-name")
    adapted_skills = set()
    for line in third_party_content.split('\n'):
        if line.startswith('## ') and not line.startswith('## Türkçe'):
            skill_name = line[3:].strip()
            if skill_name and not skill_name.startswith('Site-query'):
                adapted_skills.add(skill_name)
    
    # Check each skill folder
    for skill_folder in sorted(skills_dir.iterdir()):
        if not skill_folder.is_dir() or skill_folder.name.startswith('.'):
            continue
        
        has_license_upstream = any(
            f.name.startswith('LICENSE-') for f in skill_folder.glob('LICENSE-*')
        )
        is_adapted = skill_folder.name in adapted_skills
        
        if is_adapted and not has_license_upstream:
            errors.append(
                f"{skill_folder.name}/: Listed in THIRD_PARTY.md but missing LICENSE-upstream file"
            )
        
        # Note: We don't error on has_license_upstream and not is_adapted because
        # some skills might have LICENSE files in subdirectories
    
    return errors


def check_no_personal_emails(repo_root: Path) -> List[str]:
    """Check for personal email addresses in the repo (excludes vendored resources)."""
    errors = []
    
    # Common personal email domains
    personal_domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com']
    email_pattern = r'\b[A-Za-z0-9._%+-]+@(' + '|'.join(re.escape(d) for d in personal_domains) + r')\b'
    
    # Files to check (exclude hidden files, build artifacts, and vendor resources)
    exclude_patterns = {'.git', '__pycache__', 'node_modules', '.venv', 'venv', 'resources', 'common'}
    
    for file_path in repo_root.rglob('*'):
        # Skip if any part of the path matches exclude patterns
        if file_path.is_file() and not any(
            part.startswith('.') or part in exclude_patterns 
            for part in file_path.parts
        ):
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                matches = re.findall(email_pattern, content, re.IGNORECASE)
                if matches:
                    rel_path = file_path.relative_to(repo_root)
                    errors.append(f"{rel_path}: Contains personal email address")
            except (UnicodeDecodeError, PermissionError):
                pass  # Skip binary files and permission errors
    
    return errors


def check_no_em_dashes(repo_root: Path) -> List[str]:
    """Check for em dashes in key documentation files."""
    errors = []
    
    # Files to check
    key_files = ['README.md', 'CHANGELOG.md', 'CONTRIBUTING.md']
    em_dash = '\u2014'
    
    for filename in key_files:
        file_path = repo_root / filename
        if file_path.exists():
            content = file_path.read_text(encoding='utf-8')
            if em_dash in content:
                line_numbers = [
                    i + 1 for i, line in enumerate(content.split('\n'))
                    if em_dash in line
                ]
                errors.append(
                    f"{filename}: Contains em dash (—) on line(s) {', '.join(map(str, line_numbers[:5]))}"
                    + (" ..." if len(line_numbers) > 5 else "")
                )
    
    return errors


def check_citation_cff(repo_root: Path) -> List[str]:
    """Check CITATION.cff is valid YAML and version matches CHANGELOG."""
    errors = []
    
    citation_path = repo_root / 'CITATION.cff'
    if not citation_path.exists():
        return ["CITATION.cff: File not found"]
    
    # Parse CITATION.cff
    try:
        citation_content = citation_path.read_text(encoding='utf-8')
        citation_data = yaml.safe_load(citation_content)
    except yaml.YAMLError as e:
        return [f"CITATION.cff: Invalid YAML - {e}"]
    
    if 'version' not in citation_data:
        errors.append("CITATION.cff: Missing 'version' field")
        return errors
    
    citation_version = citation_data['version']
    
    # Parse CHANGELOG.md for latest version
    changelog_path = repo_root / 'CHANGELOG.md'
    if not changelog_path.exists():
        errors.append("CHANGELOG.md: File not found")
        return errors
    
    changelog_content = changelog_path.read_text(encoding='utf-8')
    
    # Find first version heading (## [X.Y.Z])
    version_pattern = r'^##\s+\[?(\d+\.\d+\.\d+)\]?'
    for line in changelog_content.split('\n'):
        match = re.match(version_pattern, line)
        if match:
            changelog_version = match.group(1)
            break
    else:
        errors.append("CHANGELOG.md: No version heading found")
        return errors
    
    # Compare versions
    if citation_version != changelog_version:
        errors.append(
            f"Version mismatch: CITATION.cff has '{citation_version}', "
            f"CHANGELOG.md has '{changelog_version}'"
        )
    
    return errors


def main() -> int:
    """Run all consistency checks."""
    repo_root = Path(__file__).parent.parent
    skills_dir = repo_root / 'skills'
    
    all_errors = []
    
    print("Running consistency checks...\n")
    
    # Run checks
    checks = [
        ("SKILL.md frontmatter", lambda: check_skill_frontmatter(skills_dir)),
        ("README catalog", lambda: check_readme_catalog(repo_root, skills_dir)),
        ("LICENSE files", lambda: check_license_files(repo_root, skills_dir)),
        ("Personal emails", lambda: check_no_personal_emails(repo_root)),
        ("Em dashes", lambda: check_no_em_dashes(repo_root)),
        ("CITATION.cff", lambda: check_citation_cff(repo_root)),
    ]
    
    for check_name, check_func in checks:
        print(f"Checking {check_name}...")
        errors = check_func()
        if errors:
            print(f"  ✗ {len(errors)} error(s) found")
            all_errors.extend(errors)
        else:
            print(f"  ✓ OK")
    
    # Report results
    print("\n" + "=" * 70)
    if all_errors:
        print(f"\n{len(all_errors)} consistency error(s) found:\n")
        for error in all_errors:
            print(f"  - {error}")
        print()
        return 1
    else:
        print("\n✓ All consistency checks passed!")
        return 0


if __name__ == '__main__':
    sys.exit(main())
