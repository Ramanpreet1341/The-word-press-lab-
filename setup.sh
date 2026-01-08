#!/bin/bash

# The WordPress Lab - Setup Script
# This script helps set up The WordPress Lab for development

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Project information
PROJECT_NAME="The WordPress Lab"
VERSION="1.0.0"

echo -e "${BLUE}"
echo "======================================"
echo "  $PROJECT_NAME Setup Script"
echo "  Version: $VERSION"
echo "======================================"
echo -e "${NC}"

# Check if wp-config.php exists
if [ -f "wp-config.php" ]; then
    echo -e "${YELLOW}Warning: wp-config.php already exists.${NC}"
    read -p "Do you want to continue? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Setup cancelled."
        exit 1
    fi
fi

# Check PHP
echo -e "${BLUE}Checking PHP...${NC}"
if command -v php &> /dev/null; then
    PHP_VERSION=$(php -v | head -n 1 | cut -d " " -f 2 | cut -c 1-3)
    echo -e "${GREEN}✓ PHP found: $PHP_VERSION${NC}"
else
    echo -e "${RED}✗ PHP not found. Please install PHP 7.2+${NC}"
    exit 1
fi

# Check MySQL
echo -e "${BLUE}Checking MySQL...${NC}"
if command -v mysql &> /dev/null; then
    echo -e "${GREEN}✓ MySQL found${NC}"
else
    echo -e "${YELLOW}⚠ MySQL client not found (optional for setup)${NC}"
fi

# Copy wp-config-sample.php to wp-config.php
if [ ! -f "wp-config.php" ]; then
    echo -e "${BLUE}Creating wp-config.php...${NC}"
    cp wp-config-sample.php wp-config.php
    echo -e "${GREEN}✓ wp-config.php created${NC}"
    echo -e "${YELLOW}⚠ Please edit wp-config.php with your database credentials${NC}"
else
    echo -e "${GREEN}✓ wp-config.php already exists${NC}"
fi

# Create necessary directories
echo -e "${BLUE}Creating necessary directories...${NC}"
mkdir -p wp-content/uploads
mkdir -p wp-content/cache
mkdir -p wp-content/upgrade
mkdir -p screenshots

# Set permissions (basic)
if [ "$(uname)" != "Darwin" ]; then
    echo -e "${BLUE}Setting file permissions...${NC}"
    find . -type d -exec chmod 755 {} \;
    find . -type f -exec chmod 644 {} \;
    chmod 755 wp-content/uploads
    chmod 755 wp-content/cache
    chmod 755 wp-content/upgrade
    echo -e "${GREEN}✓ Permissions set${NC}"
fi

# Create .htaccess if it doesn't exist (for Apache)
if [ ! -f ".htaccess" ]; then
    echo -e "${BLUE}Creating .htaccess...${NC}"
    cat > .htaccess << 'EOF'
# BEGIN WordPress
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
# END WordPress
EOF
    echo -e "${GREEN}✓ .htaccess created${NC}"
fi

# Verify project structure
echo -e "${BLUE}Verifying project structure...${NC}"
REQUIRED_FILES=("index.php" "wp-config-sample.php" "wp-load.php" "wp-settings.php")
ALL_GOOD=true

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓ $file${NC}"
    else
        echo -e "${RED}✗ $file missing${NC}"
        ALL_GOOD=false
    fi
done

if [ "$ALL_GOOD" = true ]; then
    echo -e "${GREEN}✓ Project structure verified${NC}"
else
    echo -e "${RED}✗ Some required files are missing${NC}"
    exit 1
fi

# Summary
echo ""
echo -e "${GREEN}======================================"
echo "  Setup Complete!"
echo "======================================${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Edit wp-config.php with your database credentials"
echo "2. Create a MySQL database for WordPress"
echo "3. Visit http://localhost/wp-admin/install.php in your browser"
echo "4. Follow the WordPress installation wizard"
echo ""
echo -e "${YELLOW}For detailed instructions, see:${NC}"
echo "  - QUICKSTART.md - Quick start guide"
echo "  - README.md - Full documentation"
echo "  - CONTRIBUTING.md - Contribution guidelines"
echo ""
echo -e "${GREEN}Happy coding with The WordPress Lab!${NC}"

