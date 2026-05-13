# Contributing to OpenAMRobot Simulation

Thank you for your interest in contributing to OpenAMRobot simulation development.

This repository contains ROS2 simulation, robot description, Gazebo integration, and educational robotics infrastructure.

## Contribution Workflow

1. Fork the repository.
2. Create a feature branch.
3. Make focused changes.
4. Commit using DCO sign-off.
5. Push your branch.
6. Open a Pull Request.
7. Complete the Pull Request checklist.
8. Wait for maintainer review.

Example:

```bash
git checkout -b feature/add-gazebo-world
git commit -s -m "Add Gazebo Harmonic world"
```

## DCO Requirement

This repository uses the Developer Certificate of Origin (DCO).

Each commit must include sign-off:

```text
Signed-off-by: Your Name <your.email@example.com>
```

Use:

```bash
git commit -s -m "Your commit message"
```

## Contribution Rules

Do not commit:

```text
build/
install/
log/
```

Do not add third-party assets unless their license is documented.

Document changes affecting:

- launch files
- topics
- services
- TF frames
- simulation behavior
- parameters
- Gazebo integration

## Simulation Contributions

Simulation contributions should include:

- launch instructions
- ROS2 distro
- Gazebo version
- expected behavior
- known limitations
- screenshots or logs if useful

## Documentation Standards

Documentation should be:

- concise
- technically accurate
- beginner-friendly where appropriate
- useful for real robotics engineering
- connected to actual package structure

## Contribution Ownership, Licensing, and Governance

By submitting contributions to this repository, contributors agree that:

- contributions are provided under the repository license;
- the OpenAMRobot organization may use, modify, sublicense, distribute, commercialize, or integrate contributions into commercial or non-commercial systems;
- repository governance remains under the OpenAMRobot organization;
- trademarks, branding, and project identity remain controlled by the OpenAMRobot organization.

Contributors retain attribution through Git history and repository records.

## Contributor Roles

Contributors may participate as:

- contributors;
- reviewers;
- maintainers of individual packages;
- simulation maintainers;
- documentation maintainers.

Role assignments are determined by repository maintainers and may evolve over time based on contribution quality and project needs.