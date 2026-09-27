## Problem Statement
Most existing Naruto fan games are either graphical (requiring heavy assets and installation) or very limited in character roster and depth. Fans who want a lightweight, accessible, pure-text experience that still captures the feel of Naruto battles (unique jutsu, armor, status effects, timing-based reactions) currently lack a complete, single-file solution that runs on any terminal without external dependencies or images.

## Scope of the Project
- Single-player, turn-based text combat simulator focused exclusively on Naruto universe characters.
- Pure console application (no GUI, no images, no external libraries beyond Python standard library).
- Fixed roster of 28 playable characters with distinct stats, abilities, and playstyles.
- Core combat loop only (character selection → battle → results). No story mode, multiplayer, save system, or online features.
- Cross-platform support limited to Windows/Linux/macOS terminals (with optional timed keypress for reactions on Windows).

## Target Users
- Naruto anime/manga fans who enjoy turn-based or text-based games.
- Students and hobbyist programmers looking for a readable, self-contained Python game example.
- Players who prefer lightweight, no-installation, terminal-based entertainment.
- Users on low-resource devices or environments where graphical games are impractical.

## High-level Features
- 28 unique characters (Naruto, Sasuke, Itachi, Kakashi, Sakura, Madara, Obito, Minato, Hashirama, Tobirama, Gaara, Rock Lee, Might Guy, Killer Bee, Pain, Jiraiya, Tsunade, and others) each with custom health, armor, dodge bonus, and 4–6 abilities.
- Diverse ability types: direct attacks, heavy moves with cooldowns, heals, buffs (power-up), status effects (burn, stun, confuse), defensive armor (Susanoo-style), and projectiles.
- Reactive combat mechanics: timed Dodge (E) / Counter (C) windows on projectile attacks.
- Status and temporary effects system (armor duration, burn damage over time, stun, confuse, power-up).
- Clean terminal UI with screen clearing, turn-by-turn status display, and simple input handling.
- Fully self-contained pure-text experience – no images or external assets required.
