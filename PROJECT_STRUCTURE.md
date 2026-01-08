# Project Structure - The WordPress Lab

This document describes the structure and organization of **The WordPress Lab** project.

## 📁 Directory Overview

```
the-wordpress-lab/
│
├── 📄 Documentation Files
│   ├── README.md                 # Main project documentation
│   ├── QUICKSTART.md             # Quick start guide
│   ├── CHANGELOG.md              # Version history
│   ├── CONTRIBUTING.md           # Contribution guidelines
│   ├── LICENSE                   # GPL v2 License
│   ├── AUTHORS.md                # Author information
│   ├── PROJECT_STRUCTURE.md      # This file
│   └── screenshots/              # Project screenshots
│
├── 🗂️ WordPress Core Files
│   ├── index.php                 # Main entry point
│   ├── wp-config-sample.php      # Configuration template
│   ├── wp-config.php             # Configuration file (create during setup)
│   ├── wp-load.php               # Bootstrap file
│   ├── wp-settings.php           # Core settings
│   ├── wp-blog-header.php        # Blog header
│   ├── wp-cron.php               # Cron jobs
│   ├── wp-login.php              # Login page
│   └── [other WordPress core files]
│
├── 🎛️ WordPress Admin
│   ├── wp-admin/                 # Admin dashboard
│   │   ├── css/                  # Admin stylesheets
│   │   ├── js/                   # Admin JavaScript
│   │   ├── images/               # Admin images
│   │   ├── includes/             # Admin core functionality
│   │   └── [admin PHP files]
│
├── 📦 WordPress Content
│   ├── wp-content/               # User-generated content
│   │   ├── themes/               # Installed themes
│   │   │   ├── twentytwentyfive/ # Latest default theme
│   │   │   ├── twentytwentyfour/ # Previous default theme
│   │   │   └── [other themes]    # 15 total themes
│   │   ├── plugins/              # Custom plugins
│   │   │   └── index.php         # Security file
│   │   ├── uploads/              # Media uploads (created after install)
│   │   ├── cache/                # Cache directory (auto-generated)
│   │   └── upgrade/              # Upgrade directory (auto-generated)
│
├── 🔧 WordPress Core Libraries
│   ├── wp-includes/              # WordPress core files
│   │   ├── css/                  # Core stylesheets
│   │   ├── js/                   # Core JavaScript
│   │   ├── [PHP core files]      # Core PHP classes and functions
│   │   └── version.php           # Version information
│
├── 🛠️ Project Tools
│   ├── verify_ownership.py       # Ownership verification script
│   ├── setup.sh                  # Setup script
│   ├── verification_report.json  # Verification report (generated)
│   └── .gitignore                # Git ignore rules
│
└── ⚙️ Configuration Files
    ├── .editorconfig             # Editor configuration
    ├── .htaccess                 # Apache configuration (auto-generated)
    └── license.txt               # WordPress license
```

## 📂 Directory Details

### Documentation Files

| File | Description |
|------|-------------|
| `README.md` | Main project documentation with full details |
| `QUICKSTART.md` | Quick start guide for fast setup |
| `CHANGELOG.md` | Version history and changes |
| `CONTRIBUTING.md` | Guidelines for contributors |
| `LICENSE` | GPL v2 License file |
| `AUTHORS.md` | Author and contributor information |
| `PROJECT_STRUCTURE.md` | This file - project structure documentation |

### WordPress Core Files

| File | Purpose |
|------|---------|
| `index.php` | Main entry point for frontend |
| `wp-config.php` | WordPress configuration (create during setup) |
| `wp-config-sample.php` | Configuration template |
| `wp-load.php` | Bootstrap file that loads WordPress |
| `wp-settings.php` | Core WordPress settings and initialization |
| `wp-login.php` | User login page |
| `wp-admin/install.php` | WordPress installation wizard |

### wp-content Directory

#### Themes (`wp-content/themes/`)

The project includes 15 default WordPress themes:

1. **Twenty Twenty-Five** (Latest) - Modern block theme
2. **Twenty Twenty-Four** - Previous default
3. **Twenty Twenty-Three** - Block theme
4. **Twenty Twenty-Two** - Full site editing
5. **Twenty Twenty-One** - Modern classic theme
6. **Twenty Twenty** - Clean and minimal
7. **Twenty Nineteen** - Block-based
8. **Twenty Seventeen** - Business-focused
9. **Twenty Sixteen** - Classic blog theme
10. **Twenty Fifteen** - Blog-focused
11. **Twenty Fourteen** - Magazine-style
12. **Twenty Thirteen** - Bold and colorful
13. **Twenty Twelve** - Responsive blog
14. **Twenty Eleven** - Classic blog
15. **Twenty Ten** - Original default theme

#### Plugins (`wp-content/plugins/`)

- Empty by default, ready for custom plugin installation
- `index.php` file present for security

#### Uploads (`wp-content/uploads/`)

- Created after WordPress installation
- Stores media files (images, videos, documents)
- Organized by year/month

### wp-admin Directory

WordPress admin dashboard files including:

- **Core Admin Files**: PHP files for admin functionality
- **CSS**: Admin stylesheets and themes
- **JavaScript**: Admin scripts and interactions
- **Images**: Icons, logos, and admin graphics
- **Includes**: Core admin functionality and classes

### wp-includes Directory

WordPress core libraries including:

- **Core Classes**: PHP classes for WordPress functionality
- **Functions**: Core WordPress functions
- **CSS**: Frontend stylesheets
- **JavaScript**: Frontend scripts
- **Version Info**: WordPress version information

## 🔐 Security Files

- `.gitignore` - Prevents sensitive files from being tracked
- `wp-config.php` - Contains database credentials (not tracked)
- `.htaccess` - Apache security and rewrite rules
- `index.php` files - Prevent directory browsing

## 📊 File Statistics

| Component | File Count |
|-----------|-----------|
| WordPress Admin | 574 files |
| Content (themes, plugins) | 1,670 files |
| Core Includes | 3,288 files |
| **Total** | **~5,500+ files** |

## 📦 Project Size

- **Total Size**: 172.27 MB
- **Core WordPress**: ~50 MB
- **Themes**: ~80 MB
- **Admin Files**: ~30 MB
- **Documentation**: ~1 MB

## 🔧 Configuration Files

### wp-config.php

Main WordPress configuration file (created from `wp-config-sample.php`):

```php
// Database configuration
define( 'DB_NAME', 'database_name' );
define( 'DB_USER', 'username' );
define( 'DB_PASSWORD', 'password' );
define( 'DB_HOST', 'localhost' );

// Security keys
define( 'AUTH_KEY', '...' );
// ... other security keys

// Debug mode (development)
define( 'WP_DEBUG', false );
```

### .htaccess

Apache configuration for permalinks and security (auto-generated).

### .gitignore

Prevents tracking of:
- `wp-config.php` (contains sensitive data)
- `wp-content/uploads/` (user-generated)
- Cache and temporary files
- OS-specific files

## 🚀 Setup Files

### setup.sh

Automated setup script that:
- Checks PHP and MySQL
- Creates `wp-config.php` from template
- Sets up necessary directories
- Sets file permissions
- Verifies project structure

### verify_ownership.py

Python script that:
- Verifies project ownership
- Generates project statistics
- Creates verification report
- Confirms project details

## 📝 Development Workflow

### Adding Custom Themes

1. Create theme directory: `wp-content/themes/your-theme/`
2. Add required files: `style.css`, `index.php`, `functions.php`
3. Activate theme: Dashboard → Appearance → Themes

### Adding Custom Plugins

1. Create plugin directory: `wp-content/plugins/your-plugin/`
2. Add main plugin file: `your-plugin.php`
3. Activate plugin: Dashboard → Plugins

### Customizing Configuration

Edit `wp-config.php` for:
- Database settings
- Debug mode
- Security keys
- Custom constants

## 🔍 Key Entry Points

| URL | Purpose |
|-----|---------|
| `/index.php` | Frontend homepage |
| `/wp-admin/` | Admin dashboard |
| `/wp-admin/install.php` | Installation wizard |
| `/wp-login.php` | Login page |
| `/wp-admin/install.php` | First-time setup |

## 📚 Related Documentation

- [README.md](README.md) - Complete project documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick setup guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Development guidelines

---

**Maintained by:** Ramanpreet Singh  
**Project:** The WordPress Lab  
**Last Updated:** 2026-01-08

