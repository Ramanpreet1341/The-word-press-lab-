# Quick Start Guide - The WordPress Lab

Get up and running with **The WordPress Lab** in minutes!

## 🚀 Quick Setup (5 Minutes)

### Step 1: Prerequisites Check

Ensure you have:
- ✅ PHP 7.2.24+ (8.3+ recommended)
- ✅ MySQL 5.5.5+ (8.0+ recommended)
- ✅ Web server (Apache/Nginx) or PHP built-in server
- ✅ A database ready for WordPress

### Step 2: Extract and Navigate

```bash
# Extract the project
unzip the-wordpress-lab.zip

# Navigate to project directory
cd the-wordpress-lab
```

### Step 3: Database Setup

Create a MySQL database:

```sql
CREATE DATABASE wordpress_lab CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'wp_user'@'localhost' IDENTIFIED BY 'secure_password_here';
GRANT ALL PRIVILEGES ON wordpress_lab.* TO 'wp_user'@'localhost';
FLUSH PRIVILEGES;
```

### Step 4: Configure WordPress

```bash
# Copy configuration template
cp wp-config-sample.php wp-config.php

# Edit wp-config.php with your database details
```

Edit `wp-config.php`:

```php
define( 'DB_NAME', 'wordpress_lab' );
define( 'DB_USER', 'wp_user' );
define( 'DB_PASSWORD', 'secure_password_here' );
define( 'DB_HOST', 'localhost' );
```

### Step 5: Run Installation

**Option A: Using PHP Built-in Server (Development)**

```bash
php -S localhost:8000
```

Then visit: `http://localhost:8000/wp-admin/install.php`

**Option B: Using Web Server**

Navigate to: `http://yourdomain.com/wp-admin/install.php`

### Step 6: Complete Installation

Follow the WordPress installation wizard:
1. Select language
2. Enter site information:
   - Site Title: The WordPress Lab
   - Username: (choose your admin username)
   - Password: (choose a strong password)
   - Email: (your email address)
3. Click "Install WordPress"
4. Login with your credentials

## ✅ You're Done!

You now have **The WordPress Lab** installed and ready to use!

## 🎯 Next Steps

### Customize Your Site

1. **Choose a Theme**
   - Go to: `Appearance → Themes`
   - Activate your preferred theme
   - Customize: `Appearance → Customize`

2. **Configure Settings**
   - General: `Settings → General`
   - Permalinks: `Settings → Permalinks` (recommended: Post name)
   - Reading: `Settings → Reading`

3. **Install Plugins** (optional)
   - Go to: `Plugins → Add New`
   - Search and install needed plugins

### Development Setup

For development work:

1. **Enable Debug Mode**
   Edit `wp-config.php`:
   ```php
   define( 'WP_DEBUG', true );
   define( 'WP_DEBUG_LOG', true );
   define( 'WP_DEBUG_DISPLAY', false );
   ```

2. **Set Up Version Control**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: The WordPress Lab setup"
   ```

3. **Configure .gitignore**
   - Already included in the project
   - Ensures sensitive files aren't tracked

## 📚 Common Tasks

### Create Your First Post

1. Go to: `Posts → Add New`
2. Enter title and content
3. Click "Publish"

### Add a Page

1. Go to: `Pages → Add New`
2. Enter title and content
3. Click "Publish"

### Upload Media

1. Go to: `Media → Add New`
2. Drag and drop files or click "Select Files"
3. Files are automatically uploaded

## 🔧 Troubleshooting

### Can't Connect to Database?

- ✅ Check database credentials in `wp-config.php`
- ✅ Verify database server is running
- ✅ Ensure database user has correct permissions

### White Screen?

- ✅ Enable `WP_DEBUG` in `wp-config.php`
- ✅ Check PHP error logs
- ✅ Verify file permissions (755 for directories, 644 for files)

### Permalinks Not Working?

- ✅ Enable mod_rewrite in Apache
- ✅ Ensure `.htaccess` is writable
- ✅ Set permalink structure: `Settings → Permalinks`

## 📖 More Information

- **Full Documentation:** See [README.md](README.md)
- **Configuration Guide:** See [README.md#configuration](README.md#-configuration)
- **Troubleshooting:** See [README.md#troubleshooting](README.md#-troubleshooting)

## 💡 Tips

- 🔐 **Security:** Change default admin username, use strong passwords
- 🚀 **Performance:** Use caching plugins for production
- 📱 **Mobile:** Test your site on mobile devices
- 🔄 **Backups:** Regularly backup your database and files

## 🆘 Need Help?

- Check the [README.md](README.md) for detailed information
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
- Check WordPress documentation: https://wordpress.org/documentation/

---

**Happy Coding with The WordPress Lab!** 🎉

*Maintained by Ramanpreet Singh*

