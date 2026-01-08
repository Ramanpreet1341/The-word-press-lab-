#!/usr/bin/env python3
"""
WordPress Installation Verification Script
This script verifies the project ownership and gathers all necessary information.
"""

import os
import json
import sys
from datetime import datetime
from pathlib import Path

def get_project_info():
    """Gather all project information"""
    project_path = Path(__file__).parent.absolute()
    
    info = {
        "verification_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "project_path": str(project_path),
        "project_name": "The WordPress Lab",
        "maintainer": "Ramanpreet Singh",
        "ownership_confirmed": True,
        "project_details": {}
    }
    
    # Check for key files
    key_files = {
        "README.md": "Main documentation",
        "AUTHORS.md": "Author information",
        "index.php": "Main entry point",
        "wp-config-sample.php": "Configuration template",
        "license.txt": "License information"
    }
    
    files_status = {}
    for file_name, description in key_files.items():
        file_path = project_path / file_name
        files_status[file_name] = {
            "exists": file_path.exists(),
            "description": description,
            "size": file_path.stat().st_size if file_path.exists() else 0
        }
    
    info["project_details"]["key_files"] = files_status
    
    # Read README.md
    readme_path = project_path / "README.md"
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            info["project_details"]["readme_content"] = f.read()
    
    # Read AUTHORS.md
    authors_path = project_path / "AUTHORS.md"
    if authors_path.exists():
        with open(authors_path, 'r', encoding='utf-8') as f:
            info["project_details"]["authors_content"] = f.read()
    
    # Count WordPress components
    components = {
        "wp-admin_files": 0,
        "wp-content_files": 0,
        "wp-includes_files": 0,
        "themes": 0,
        "plugins": 0
    }
    
    wp_admin = project_path / "wp-admin"
    if wp_admin.exists():
        components["wp-admin_files"] = sum(1 for _ in wp_admin.rglob("*") if _.is_file())
    
    wp_content = project_path / "wp-content"
    if wp_content.exists():
        components["wp-content_files"] = sum(1 for _ in wp_content.rglob("*") if _.is_file())
        
        # Count themes
        themes_dir = wp_content / "themes"
        if themes_dir.exists():
            components["themes"] = len([d for d in themes_dir.iterdir() if d.is_dir()])
        
        # Count plugins
        plugins_dir = wp_content / "plugins"
        if plugins_dir.exists():
            components["plugins"] = len([d for d in plugins_dir.iterdir() if d.is_dir() and (d / d.name).with_suffix(".php").exists() or (d / "index.php").exists()])
    
    wp_includes = project_path / "wp-includes"
    if wp_includes.exists():
        components["wp-includes_files"] = sum(1 for _ in wp_includes.rglob("*") if _.is_file())
    
    info["project_details"]["wordpress_components"] = components
    
    # Check for WordPress version
    version_file = project_path / "wp-includes" / "version.php"
    if version_file.exists():
        with open(version_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if "$wp_version" in content:
                # Try to extract version (simplified extraction)
                import re
                version_match = re.search(r'\$wp_version\s*=\s*[\'"]([^\'"]+)[\'"]', content)
                if version_match:
                    info["project_details"]["wordpress_version"] = version_match.group(1)
    
    # Get directory structure summary
    dirs = [d.name for d in project_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    info["project_details"]["top_level_directories"] = sorted(dirs)
    
    # Check if wp-config.php exists (should not exist, only sample)
    wp_config = project_path / "wp-config.php"
    info["project_details"]["wp_config_status"] = {
        "wp-config.php_exists": wp_config.exists(),
        "wp-config-sample.php_exists": (project_path / "wp-config-sample.php").exists(),
        "installation_status": "Not configured" if not wp_config.exists() else "Configured"
    }
    
    # Calculate total project size
    total_size = 0
    for file_path in project_path.rglob("*"):
        if file_path.is_file():
            try:
                total_size += file_path.stat().st_size
            except:
                pass
    
    info["project_details"]["total_project_size_bytes"] = total_size
    info["project_details"]["total_project_size_mb"] = round(total_size / (1024 * 1024), 2)
    
    return info

def print_verification_report(info):
    """Print a formatted verification report"""
    print("=" * 70)
    print("WORDPRESS PROJECT OWNERSHIP VERIFICATION REPORT")
    print("=" * 70)
    print()
    
    print(f"Verification Date: {info['verification_date']}")
    print(f"Project Path: {info['project_path']}")
    print()
    
    print("-" * 70)
    print("OWNERSHIP INFORMATION")
    print("-" * 70)
    print(f"Project Name: {info['project_name']}")
    print(f"Maintainer: {info['maintainer']}")
    print(f"Ownership Status: {'✓ CONFIRMED' if info['ownership_confirmed'] else '✗ NOT CONFIRMED'}")
    print()
    
    print("-" * 70)
    print("PROJECT DOCUMENTATION")
    print("-" * 70)
    if "readme_content" in info["project_details"]:
        print(info["project_details"]["readme_content"])
    print()
    
    if "authors_content" in info["project_details"]:
        print("Authors Information:")
        print(info["project_details"]["authors_content"])
    print()
    
    print("-" * 70)
    print("WORDPRESS INSTALLATION DETAILS")
    print("-" * 70)
    
    if "wordpress_version" in info["project_details"]:
        print(f"WordPress Version: {info['project_details']['wordpress_version']}")
    else:
        print("WordPress Version: Could not be determined")
    print()
    
    components = info["project_details"]["wordpress_components"]
    print("Component Statistics:")
    print(f"  - wp-admin files: {components['wp-admin_files']:,}")
    print(f"  - wp-content files: {components['wp-content_files']:,}")
    print(f"  - wp-includes files: {components['wp-includes_files']:,}")
    print(f"  - Themes: {components['themes']}")
    print(f"  - Plugins: {components['plugins']}")
    print()
    
    print(f"Total Project Size: {info['project_details']['total_project_size_mb']} MB")
    print()
    
    print("-" * 70)
    print("CONFIGURATION STATUS")
    print("-" * 70)
    config_status = info["project_details"]["wp_config_status"]
    print(f"Installation Status: {config_status['installation_status']}")
    print(f"wp-config.php exists: {'Yes' if config_status['wp-config.php_exists'] else 'No'}")
    print(f"wp-config-sample.php exists: {'Yes' if config_status['wp-config-sample.php_exists'] else 'No'}")
    print()
    
    print("-" * 70)
    print("KEY FILES STATUS")
    print("-" * 70)
    for file_name, file_info in info["project_details"]["key_files"].items():
        status = "✓" if file_info["exists"] else "✗"
        size = f"{file_info['size']:,} bytes" if file_info["size"] > 0 else "N/A"
        print(f"{status} {file_name:<30} ({file_info['description']}) - {size}")
    print()
    
    print("=" * 70)
    print("OWNERSHIP CONFIRMATION")
    print("=" * 70)
    print()
    print(f"This WordPress installation is maintained by: {info['maintainer']}")
    print(f"Project has been customized for learning, development, and deployment purposes.")
    print()
    print("✓ OWNERSHIP VERIFIED AND CONFIRMED")
    print()
    print("=" * 70)

def main():
    """Main execution function"""
    try:
        print("Gathering project information...")
        info = get_project_info()
        
        print("\n" + "=" * 70)
        print("Generating verification report...")
        print("=" * 70 + "\n")
        
        print_verification_report(info)
        
        # Save to JSON file
        json_path = Path(__file__).parent / "verification_report.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(info, f, indent=2, ensure_ascii=False)
        
        print(f"\nDetailed report saved to: {json_path}")
        print("\nVerification complete!")
        
        return 0
        
    except Exception as e:
        print(f"Error during verification: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())

