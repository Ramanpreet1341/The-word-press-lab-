# The WordPress Lab

<div align="center">

![WordPress Version](https://img.shields.io/badge/WordPress-7.0--alpha--61450-blue?style=for-the-badge&logo=wordpress)
![PHP](https://img.shields.io/badge/PHP-7.2%2B-777BB4?style=for-the-badge&logo=php&logoColor=white)
![License](https://img.shields.io/badge/License-GPL%20v2-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Customized-yellow?style=for-the-badge)

**A fully customized WordPress installation maintained by Ramanpreet Singh**

*A development lab for WordPress customization, learning, and experimentation*

[Features](#-key-features) • [Installation](#-installation) • [Configuration](#-configuration) • [Project Structure](#-project-structure) • [License](#-license)

</div>

---

## 📸 Project Screenshots & Output

### Dashboard Overview
![WordPress Dashboard](screenshots/dashboard.png)
*WordPress Admin Dashboard - Main interface after installation*

### Theme Customization
![Theme Customization](screenshots/theme-customization.png)
*Custom theme configuration and UI/UX customization*

### Frontend View
![Frontend](screenshots/frontend.png)
*Public-facing website view with custom theme*

### Installation Screen
![Installation](screenshots/installation.png)
*WordPress installation and setup process*

---

## 📋 Table of Contents

- [About](#-about)
- [Quick Start](#-quick-start)
- [Key Features](#-key-features)
- [Project Statistics](#-project-statistics)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Development](#-development)
- [Maintainer](#-maintainer)
- [License](#-license)
- [Contributing](#-contributing)
- [Acknowledgments](#-acknowledgments)

---

## 🚀 Quick Start

Want to get started quickly? Check out the **[Quick Start Guide](QUICKSTART.md)** for a 5-minute setup!

**Using the Setup Script:**
```bash
./setup.sh
```

Then edit `wp-config.php` with your database credentials and visit `wp-admin/install.php`.

For detailed installation instructions, see the [Installation](#-installation) section below.

---

## 🎯 About

**The WordPress Lab** is a customized WordPress-based web project that has been modified, configured, and maintained by **Ramanpreet Singh** for learning, development, and deployment purposes.

This project serves as a development lab where WordPress customization, experimentation, and learning take place. Built on WordPress 7.0-alpha-61450, it includes custom configurations, theme customizations, and optimization settings tailored for modern web development practices.

### Ownership Verification

✅ **Ownership Status:** CONFIRMED  
👤 **Maintainer:** Ramanpreet Singh  
📅 **Last Verified:** 2026-01-08  
🏷️ **Project Name:** The WordPress Lab

---

## ✨ Key Features

This WordPress installation includes the following customizations and features:

### 🎨 Customization Features
- ✅ **Custom Theme Configuration** - Pre-configured themes with custom settings
- ✅ **Plugin Integration and Setup** - Ready for plugin installation and configuration
- ✅ **UI/UX Customization** - Enhanced user interface and experience
- ✅ **Performance Optimization** - Optimized for speed and efficiency
- ✅ **Security Configuration** - Enhanced security settings and best practices

### 📦 Included Components
- 15 pre-installed WordPress themes
- Complete WordPress core files
- Admin dashboard with all standard features
- Media library management
- User management system
- Content management tools

---

## 📊 Project Statistics

| Component | Count | Details |
|-----------|-------|---------|
| **Total Project Size** | 172.27 MB | All files included |
| **WordPress Admin Files** | 574 files | Core admin functionality |
| **Content Files** | 1,670 files | Themes, plugins, uploads |
| **Core Includes Files** | 3,288 files | WordPress core libraries |
| **Installed Themes** | 15 themes | Default WordPress themes |
| **Plugins** | 0 plugins | Ready for custom plugins |
| **WordPress Version** | 7.0-alpha-61450 | Latest alpha release |

### Theme List

The following themes are included in this installation:

1. Twenty Twenty-Five (Latest)
2. Twenty Twenty-Four
3. Twenty Twenty-Three
4. Twenty Twenty-Two
5. Twenty Twenty-One
6. Twenty Twenty
7. Twenty Nineteen
8. Twenty Seventeen
9. Twenty Sixteen
10. Twenty Fifteen
11. Twenty Fourteen
12. Twenty Thirteen
13. Twenty Twelve
14. Twenty Eleven
15. Twenty Ten

---

## 💻 System Requirements

### Minimum Requirements

- **PHP:** Version 7.2.24 or greater
- **MySQL:** Version 5.5.5 or greater
- **Web Server:** Apache or Nginx
- **Memory:** 128MB RAM minimum

### Recommended Requirements

- **PHP:** Version 8.3 or greater
- **MySQL:** Version 8.0 or greater (or MariaDB 10.6+)
- **Apache Module:** mod_rewrite enabled
- **HTTPS:** SSL certificate support
- **Memory:** 256MB RAM or higher

### PHP Extensions Required

- `mysqli` or `mysql`
- `curl`
- `gd` or `imagick`
- `mbstring`
- `xml`
- `zip`

---

## 🚀 Installation

### Quick Installation (5-Minute Setup)

1. **Extract the Files**
   ```bash
   # Extract The WordPress Lab to your web server directory
   cd /path/to/your/webserver
   unzip the-wordpress-lab.zip
   ```

2. **Set Up Database**
   - Create a MySQL database for WordPress
   - Create a database user and grant privileges
   - Note the database name, username, password, and host

3. **Configure WordPress**
   - Copy `wp-config-sample.php` to `wp-config.php`
   - Edit `wp-config.php` with your database details:
     ```php
     define( 'DB_NAME', 'your_database_name' );
     define( 'DB_USER', 'your_database_user' );
     define( 'DB_PASSWORD', 'your_database_password' );
     define( 'DB_HOST', 'localhost' );
     ```

4. **Run the Installation**
   - Navigate to `http://yourdomain.com/wp-admin/install.php` in your browser
   - Follow the installation wizard
   - Set your site title, admin username, password, and email

5. **Complete Setup**
   - Log in to the admin dashboard
   - Configure your site settings
   - Install plugins and customize themes as needed

### Using the Setup Wizard

1. Navigate to `wp-admin/install.php` in your browser
2. Follow the on-screen instructions
3. The wizard will help you create the `wp-config.php` file automatically
4. Complete the installation by creating your admin account

### Manual Configuration

If the automatic setup doesn't work:

1. Copy `wp-config-sample.php` to `wp-config.php`
2. Edit `wp-config.php` with a text editor
3. Fill in your database connection details
4. Save the file
5. Run `wp-admin/install.php`

---

## ⚙️ Configuration

### Database Configuration

Edit `wp-config.php` to configure your database connection:

```php
/** The name of the database for WordPress */
define( 'DB_NAME', 'database_name_here' );

/** Database username */
define( 'DB_USER', 'username_here' );

/** Database password */
define( 'DB_PASSWORD', 'password_here' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset */
define( 'DB_CHARSET', 'utf8mb4' );

/** Database collate type */
define( 'DB_COLLATE', '' );
```

### Security Keys

Generate unique security keys at: https://api.wordpress.org/secret-key/1.1/salt/

Replace the placeholder keys in `wp-config.php`:

```php
define( 'AUTH_KEY',         'put your unique phrase here' );
define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
define( 'NONCE_KEY',        'put your unique phrase here' );
define( 'AUTH_SALT',        'put your unique phrase here' );
define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
define( 'NONCE_SALT',       'put your unique phrase here' );
```

### Debugging Mode

For development, enable debugging in `wp-config.php`:

```php
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', false );
```

---

## 📁 Project Structure

```
the-wordpress-lab/
│
├── wp-admin/                 # WordPress admin dashboard files
│   ├── css/                  # Admin stylesheets
│   ├── images/               # Admin images and icons
│   ├── includes/             # Admin core functionality
│   └── js/                   # Admin JavaScript files
│
├── wp-content/               # User-generated content
│   ├── plugins/              # Custom plugins (empty by default)
│   ├── themes/               # Installed themes (15 themes)
│   └── uploads/              # Media uploads (created after installation)
│
├── wp-includes/              # WordPress core files
│   ├── css/                  # Core stylesheets
│   ├── js/                   # Core JavaScript
│   └── [core files]          # PHP core files and classes
│
├── index.php                 # Main entry point
├── wp-config-sample.php      # Configuration template
├── wp-config.php             # Configuration file (create during installation)
├── wp-load.php               # Bootstrap file
├── wp-settings.php           # Core settings file
│
├── README.md                 # This file
├── AUTHORS.md                # Author information
├── license.txt               # GPL License
└── verification_report.json  # Project verification report
```

### Key Files

- `index.php` - Front-end entry point
- `wp-config.php` - Configuration file (created during setup)
- `wp-admin/install.php` - Installation wizard
- `wp-login.php` - Login page
- `wp-content/themes/` - Theme directory
- `wp-content/plugins/` - Plugin directory

---

## 📖 Usage

See [QUICKSTART.md](QUICKSTART.md) for a quick start guide, or follow the detailed instructions below.

### Initial Setup

1. **Access Admin Dashboard**
   - Navigate to `http://yourdomain.com/wp-admin`
   - Log in with your admin credentials

2. **Configure Site Settings**
   - Go to Settings → General
   - Set site title, tagline, and URL
   - Configure timezone and date format

3. **Select a Theme**
   - Navigate to Appearance → Themes
   - Activate your preferred theme
   - Customize theme settings

4. **Create Content**
   - Add pages: Pages → Add New
   - Write posts: Posts → Add New
   - Upload media: Media → Add New

### Common Tasks

**Installing Plugins:**
```
Dashboard → Plugins → Add New → Search → Install → Activate
```

**Customizing Theme:**
```
Dashboard → Appearance → Customize
```

**Managing Users:**
```
Dashboard → Users → Add New
```

**Configuring Permalinks:**
```
Dashboard → Settings → Permalinks
```

---

## 💻 Development

### Project Structure

For detailed information about the project structure, see **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)**.

### Development Tools

- **Setup Script**: Run `./setup.sh` for automated setup
- **Verification Script**: Run `python3 verify_ownership.py` to verify project details
- **Editor Config**: `.editorconfig` included for consistent code style

### Contributing

Want to contribute to The WordPress Lab? See **[CONTRIBUTING.md](CONTRIBUTING.md)** for guidelines and instructions.

### Version History

See **[CHANGELOG.md](CHANGELOG.md)** for version history and changes.

### License

This project is licensed under **GPL v2**. See **[LICENSE](LICENSE)** for full license details.

---

## 👤 Maintainer

**Ramanpreet Singh**

This WordPress installation has been customized and maintained by Ramanpreet Singh for:
- Learning and educational purposes
- Development and testing
- Deployment and production use

### Project Customization

This project includes:
- Custom configurations optimized for development
- Security enhancements
- Performance optimizations
- UI/UX customizations

---

## 📄 License

This project is licensed under the **GNU General Public License (GPL) version 2** or later.

See **[LICENSE](LICENSE)** for the full license text.

### License Details

- **License Type:** GPL v2+
- **Original Project:** WordPress (https://wordpress.org)
- **License File:** See [license.txt](license.txt) for full license text

### What this means:

✅ You are free to use, modify, and distribute this software  
✅ You can use it for commercial or non-commercial purposes  
✅ You must include the license and copyright notices  
✅ Any modifications must also be licensed under GPL  

For more information, visit: https://www.gnu.org/licenses/gpl-2.0.html

---

## 🤝 Contributing

We welcome contributions to **The WordPress Lab**! 

Please read **[CONTRIBUTING.md](CONTRIBUTING.md)** for guidelines on:
- Code of conduct
- How to contribute
- Development process
- Coding standards
- Submission guidelines

See **[CHANGELOG.md](CHANGELOG.md)** for version history.

---

## 🙏 Acknowledgments

### Original Project

- **WordPress** - https://wordpress.org
- Copyright 2011-2026 by the WordPress contributors
- Based on b2/cafélog by Michel Valdrighi

### Resources

- [WordPress Documentation](https://wordpress.org/documentation/)
- [WordPress Support Forums](https://wordpress.org/support/)
- [WordPress Developer Resources](https://developer.wordpress.org/)
- [WordPress Codex](https://codex.wordpress.org/)

---

## 📝 Verification

This project has been verified and confirmed to belong to **Ramanpreet Singh**.

### Verification Details

Run the verification script to confirm ownership:

```bash
python3 verify_ownership.py
```

This will generate:
- Verification report
- Project statistics
- Ownership confirmation

See `verification_report.json` for detailed verification information.

---

## 🔧 Troubleshooting

### Common Issues

**Issue: Cannot connect to database**
- Verify database credentials in `wp-config.php`
- Ensure database user has proper permissions
- Check if database server is running

**Issue: White screen after installation**
- Check PHP error logs
- Enable `WP_DEBUG` in `wp-config.php`
- Verify file permissions (755 for directories, 644 for files)

**Issue: Permalinks not working**
- Enable mod_rewrite in Apache
- Ensure `.htaccess` file exists and is writable
- Check Apache configuration for AllowOverride

**Issue: Media upload errors**
- Check `wp-content/uploads` directory permissions
- Verify PHP upload limits in `php.ini`
- Check available disk space

### Getting Help

- WordPress Support: https://wordpress.org/support/
- Documentation: https://wordpress.org/documentation/
- Forums: https://wordpress.org/support/forums/

---

## 📞 Contact & Support

For issues specific to The WordPress Lab:

- **Project Name:** The WordPress Lab
- **Maintainer:** Ramanpreet Singh
- **Project Type:** Custom WordPress Development Lab
- **Status:** Active Development

---

## 🚦 Project Status

![Status](https://img.shields.io/badge/Status-Customized-yellow?style=flat-square)
![Version](https://img.shields.io/badge/WordPress-7.0--alpha--61450-blue?style=flat-square)
![License](https://img.shields.io/badge/License-GPL%20v2-green?style=flat-square)

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star!**

Made with ❤️ by Ramanpreet Singh

[Back to Top](#the-wordpress-lab)

</div>

---



**Project Name:** The WordPress Lab  
**Last Updated:** 2026-01-08  
**WordPress Version:** 7.0-alpha-61450  
**Project Size:** 172.27 MB
