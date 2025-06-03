# Teeko AI — `game.py`

A self-contained Python implementation of **Teeko**, a two-player abstract strategy game invented by John Scarne.  
This script provides:

* A **command-line playable** version of Teeko (human vs. AI).
* A **heuristic-based, α-β–pruned minimax AI** that chooses moves for one side.
* **Zero external dependencies** beyond the Python standard library.

---

## Table of Contents
1. [Game Rules](#game-rules)
2. [Quick Start](#quick-start)
3. [How the AI Works](#how-the-ai-works)
4. [File Walkthrough](#file-walkthrough)
5. [Customising or Re-using the AI](#customising-or-re-using-the-ai)
6. [Troubleshooting](#troubleshooting)
7. [License](#license)

---

## Game Rules
Teeko is played on a **5 × 5 board**.  
Each player has **four pieces** (Black `b` and Red `r`).

1. **Drop Phase** – Players alternate placing their four pieces on any empty square.
2. **Move Phase** – Pieces slide to any **adjacent** (orthogonal or diagonal) empty square.
3. **Win Conditions** – First to achieve **any one** of these with their four pieces wins:
   * **Line:** Four in a row horizontally, vertically, or diagonally.
   * **Box:** A 2 × 2 square anywhere on the board.

---

## Quick Start

### Prerequisites
* Python 3.8 or newer

### Run

```bash
python game.py
