# Contributing to The WordPress Lab

Thank you for your interest in contributing to **The WordPress Lab**! This document provides guidelines and instructions for contributing to this project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Process](#development-process)
- [Coding Standards](#coding-standards)
- [Submission Guidelines](#submission-guidelines)
- [Questions?](#questions)

## 🤝 Code of Conduct

By participating in this project, you agree to:

- Be respectful and considerate of others
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect differing viewpoints and experiences
- Show empathy towards other community members

## 🚀 Getting Started

### Prerequisites

- WordPress 7.0+ (alpha)
- PHP 7.2.24+ (8.3+ recommended)
- MySQL 5.5.5+ (8.0+ recommended)
- Basic knowledge of WordPress development
- Git for version control

### Setting Up Development Environment

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/the-wordpress-lab.git
   cd the-wordpress-lab
   ```

2. **Set Up WordPress**
   - Copy `wp-config-sample.php` to `wp-config.php`
   - Configure your database settings
   - Run the WordPress installation

3. **Configure Development Environment**
   - Enable `WP_DEBUG` in `wp-config.php`
   - Set up local development server
   - Install recommended tools

## 📝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

- **Clear description** of the bug
- **Steps to reproduce** the issue
- **Expected behavior** vs **Actual behavior**
- **Environment details** (PHP version, WordPress version, etc.)
- **Screenshots** if applicable
- **Error messages** or logs

### Suggesting Enhancements

For feature requests or enhancements:

- **Clear description** of the enhancement
- **Use case** or problem it solves
- **Proposed solution** (optional)
- **Examples** or mockups (if applicable)

### Contributing Code

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Make Your Changes**
   - Follow coding standards
   - Write clean, documented code
   - Test your changes thoroughly

3. **Commit Your Changes**
   ```bash
   git commit -m "Description of your changes"
   ```
   Use clear, descriptive commit messages.

4. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## 🔨 Development Process

### Branch Naming Convention

- `feature/feature-name` - New features
- `fix/bug-description` - Bug fixes
- `docs/documentation-update` - Documentation changes
- `refactor/component-name` - Code refactoring
- `test/test-name` - Testing improvements

### Commit Message Format

Use clear, descriptive commit messages:

```
type: brief description (max 50 chars)

Optional detailed explanation if needed
```

Types:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Example:
```
feat: add custom theme configuration wizard

Implemented a step-by-step wizard for configuring custom themes
with validation and preview functionality.
```

## 📐 Coding Standards

### PHP Standards

- Follow [WordPress PHP Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/)
- Use meaningful variable and function names
- Comment complex logic
- Keep functions focused and small

### JavaScript Standards

- Follow [WordPress JavaScript Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/javascript/)
- Use ES6+ features appropriately
- Comment complex logic
- Ensure browser compatibility

### CSS Standards

- Follow [WordPress CSS Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/css/)
- Use meaningful class names
- Keep specificity low
- Use consistent formatting

### File Organization

- Keep related files together
- Use descriptive file names
- Follow WordPress file structure conventions
- Document custom structures

## ✅ Submission Guidelines

### Pull Request Checklist

Before submitting a pull request, ensure:

- [ ] Code follows project coding standards
- [ ] Code is tested and working
- [ ] Documentation is updated (if needed)
- [ ] No console errors or warnings
- [ ] Code is properly formatted
- [ ] Commit messages are clear and descriptive
- [ ] Branch is up to date with main branch
- [ ] All tests pass (if applicable)

### Pull Request Template

When creating a pull request, include:

1. **Description** - What does this PR do?
2. **Type** - Feature, Bug Fix, Documentation, etc.
3. **Testing** - How was this tested?
4. **Screenshots** - If UI changes are involved
5. **Related Issues** - Link to related issues

## 🧪 Testing

- Test your changes in a development environment
- Test across different browsers (if UI changes)
- Test edge cases and error conditions
- Document any known limitations

## 📚 Documentation

- Update README.md if adding new features
- Document new functions/classes
- Update CHANGELOG.md for significant changes
- Add inline comments for complex code

## ❓ Questions?

If you have questions:

- Open an issue with the `question` label
- Check existing documentation
- Review closed issues and PRs
- Contact the maintainer: Ramanpreet Singh

## 🙏 Thank You!

Thank you for taking the time to contribute to The WordPress Lab! Every contribution, no matter how small, is appreciated and helps make this project better.

---

**Maintainer:** Ramanpreet Singh  
**Project:** The WordPress Lab  
**License:** GPL v2

