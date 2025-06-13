# Contributing to AI Virtual Mouse

First off, thank you for considering contributing to AI Virtual Mouse! It's people like you that make this project a great tool for hands-free computing.

## 🤝 How to Contribute

### Reporting Bugs

Before creating bug reports, please check if the issue has already been reported. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**

#### Bug Report Template

```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:

1. Go to '...'
2. Make gesture '....'
3. See error

**Expected behavior**
A clear description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**

- OS: [e.g. Windows 10]
- Python Version: [e.g. 3.9]
- Camera: [e.g. Built-in webcam, USB camera]

**Additional context**
Add any other context about the problem here.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and explain which behavior you expected to see instead**
- **Explain why this enhancement would be useful**

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Make your changes**
4. **Add tests if applicable**
5. **Ensure your code follows the existing style**
6. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
7. **Push to the branch** (`git push origin feature/AmazingFeature`)
8. **Open a Pull Request**

#### Pull Request Guidelines

- **Follow the existing code style**
- **Write clear, concise commit messages**
- **Update documentation if needed**
- **Add tests for new functionality**
- **Ensure all tests pass**
- **Update the CHANGELOG.md**

## 🛠️ Development Setup

1. **Clone your fork:**

   ```bash
   git clone https://github.com/yourusername/AI-Virtual-Mouse.git
   cd AI-Virtual-Mouse
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Make your changes and test:**
   ```bash
   python AiVirtualMouseProject.py
   ```

## 📝 Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused
- Use type hints where appropriate

## 🧪 Testing

- Test your changes thoroughly with different lighting conditions
- Test with different hand positions and gestures
- Ensure backward compatibility
- Test on different camera setups if possible

## 💡 Ideas for Contributions

Here are some areas where contributions would be especially welcome:

### 🔮 New Features

- **Multi-hand support** for advanced gestures
- **Custom gesture creation** interface
- **Voice command integration**
- **MacOS/Linux support**
- **Mobile app companion**
- **Gesture sensitivity settings**

### 🐛 Bug Fixes

- Improve gesture detection accuracy
- Better error handling
- Performance optimizations
- Camera compatibility issues

### 📚 Documentation

- Tutorial videos
- Better installation guides
- API documentation
- Translation to other languages

### 🎨 UI/UX Improvements

- Better visual feedback
- Configuration interface
- Gesture training mode
- Real-time performance metrics

## 📋 Project Structure

```
AI-Virtual-Mouse/
├── AiVirtualMouseProject.py    # Main application
├── HandTrackingModule.py       # Hand detection module
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies
├── CHANGELOG.md               # Version history
├── CONTRIBUTING.md            # This file
└── LICENSE                    # MIT License
```

## 🎯 Coding Standards

### Python Best Practices

- Use virtual environments
- Follow PEP 8 style guide
- Write docstrings for functions and classes
- Handle exceptions gracefully
- Use meaningful variable names

### Git Best Practices

- Write clear commit messages
- Keep commits atomic (one logical change per commit)
- Use feature branches
- Rebase before submitting PR
- Update documentation with code changes

## ❓ Questions?

Don't hesitate to ask questions! You can:

1. **Open an issue** with the `question` label
2. **Start a discussion** in the GitHub Discussions tab
3. **Contact the maintainer** through GitHub

## 📜 License

By contributing to AI Virtual Mouse, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for making AI Virtual Mouse better!** 🙏
