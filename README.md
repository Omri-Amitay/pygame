# 2D Arcade Game Engine

A clean, modular 2D arcade game built in Python using the Pygame library. This repository showcases an object-oriented approach to game loops, entity management, and state mechanics, including character movement, projectile tracking, collision logic, and dynamic obstacle spawning.

## Repository Architecture

The codebase is split into specific modules to handle game logic cleanly and prevent monolith scripts:

* main.py - The central entry point. Manages the core game loop, event handling (keyboard inputs), screen rendering updates, framerate capping, and overall game state conditions.
* Player.py - Contains the Player class, defining user-controlled movement, boundary restrictions, positioning, and rendering states.
* Bullet.py - Manages projectile properties, linear motion vectors, rendering, and off-screen lifetime disposal loops.
* Egg.py - Controls enemy, collectible, or dropping obstacle entities, defining spawn metrics, vertical velocity movement, and dynamic positional updates.
* Constants.py - Holds globally shared configurations, including screen dimensions, rendering colors, object velocities, and framerate caps.
* Utils.py - Provides helper functions for reusable math, asset scaling, or text rendering overlays.

## Getting Started

### Prerequisites

You need Python 3.x and pygame installed on your system.

### Installation & Environment Setup

1. Clone the repository:
   git clone https://github.com/Omri-Amitay/pygame.git
   cd pygame

2. Create and activate a virtual environment (recommended):
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

3. Install the required packages:
   pip install pygame

### Running the Game

Launch the application using the main entry point:
python main.py

## Implementation Highlights

* Object-Oriented Design: Separate classes for game elements ensure that logic like collision boxes and custom behaviors are isolated to their respective instances.
* Asset Loading Management: The engine references sprite files from the assets/ directory, employing optimization practices to ensure smooth visual rendering.
* Consistent Framerate Capping: Utilizes Pygame clocks to stabilize logic execution regardless of the host hardware's compute speeds.
