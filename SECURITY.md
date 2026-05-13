# Security Policy

## Reporting Security Issues

Please do not report security issues publicly in GitHub Issues.

If you discover:

- unsafe robot behavior
- exposed credentials
- unsafe simulation configuration
- dangerous deployment practices
- ROS2 security issues

please contact the maintainers privately:

botshare.ai@gmail.com

Include:

- repository name
- affected component
- description
- reproduction steps
- possible impact
- suggested fix if known

## Scope

This policy applies to:

- ROS2 packages
- Gazebo integration
- launch files
- simulation files
- robot description files
- documentation
- CI configuration

## Robotics Safety Notice

This repository may be used with real autonomous mobile robots.

Before deploying on hardware:

- validate in simulation first
- verify emergency stop behavior
- verify TF frames
- verify sensor topics
- verify speed limits
- test in controlled environments

Unsafe contributions may be rejected or removed.