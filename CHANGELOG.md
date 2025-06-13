# Changelog

All notable changes to the AI Virtual Mouse project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-06-13

### Added

- **Core Features**:

  - Hand gesture recognition using MediaPipe
  - Mouse movement control with index finger
  - Left click with index + middle finger gesture
  - Right click with index + middle + ring finger gesture
  - Double click detection within 0.5 seconds
  - Drag and drop functionality with thumb + index finger
  - Scroll control with index + pinky finger
  - System volume control with thumb + pinky gesture

- **Smart Features**:

  - Real-time hand tracking and landmark detection
  - Smooth cursor movement with configurable smoothening
  - Visual feedback with on-screen mode indicators
  - Finger status display (UP/DOWN for each finger)
  - FPS counter for performance monitoring
  - Purple boundary frame for mouse control area
  - Volume bar visualization during volume control

- **Technical Implementation**:

  - Multi-camera support with automatic detection
  - Error handling for missing dependencies
  - Graceful fallbacks when features aren't available
  - Windows API integration for scrolling
  - COM interface for audio control
  - Configurable parameters for customization

- **Documentation**:
  - Comprehensive README with installation guide
  - Hand gesture reference table
  - Usage tips and troubleshooting section
  - Requirements.txt for easy dependency management

### Technical Details

- **Dependencies**: OpenCV, MediaPipe, NumPy, AutoPy, PyCaw, ComTypes, PyWin32
- **Platform**: Windows (primary), with cross-platform mouse control
- **Python**: 3.7+ compatibility
- **Performance**: 15-30 FPS real-time processing

### Known Issues

- Volume control requires Windows administrator privileges in some cases
- Camera access may conflict with other applications
- Gesture detection sensitive to lighting conditions

## [Unreleased]

### Planned Features

- [ ] Multi-hand support for advanced gestures
- [ ] Custom gesture creation and training
- [ ] Voice command integration
- [ ] MacOS and Linux platform support
- [ ] Mobile app companion
- [ ] AI-powered gesture learning
- [ ] Gesture sensitivity configuration
- [ ] Multiple monitor support
- [ ] Gesture macros and shortcuts
