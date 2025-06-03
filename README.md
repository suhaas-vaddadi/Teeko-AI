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
3. [How the AI works](#How the Heuristic Works — heuristic_game_value())

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

### How the Heuristic Works — heuristic_game_value()

The AI evaluates every **non-terminal** board position and returns a value in **(-1 … +1)**:
- **+1** → a near-certain win for the AI (`self.my_piece`)
- **–1** → a near-certain win for the opponent (`self.opp`)
- **0**  → a balanced or unclear position

---

#### 1. What Patterns Are Counted

The function examines every possible “window” on the 5×5 board that could contribute to a four-in-a-row or a 2×2 box. Each pattern has a **base weight**:

| Pattern                     | Windows considered                                                                        | Base weight           |
|-----------------------------|-------------------------------------------------------------------------------------------|-----------------------|
| **Rows (length-4)**         | For each of the 5 rows, the 4-cell segments at columns 0–3 and 1–4                        | `ROW_WEIGHT = 1.0`    |
| **Columns (length-4)**      | For each of the 5 columns, the 4-cell segments at rows 0–3 and 1–4                         | `COL_WEIGHT = 1.0`    |
| **Main diagonals (\\)**     | Two length-4 diagonals (positions [0,0]→[3,3] and [1,1]→[4,4])                             | `MAIN_DIAG_WEIGHT = 2.5` |
| **Secondary diagonals (/)** | Two length-4 diagonals (positions [0,4]→[3,1] and [1,3]→[4,0])                             | `MAIN_DIAG_WEIGHT = 2.5` |
| **Support diagonals**       | Four “off-by-one” diagonals that lead into main/secondary diagonals (see code loops)       | `SUPP_DIAG_WEIGHT = 2.5` |
| **2×2 boxes**               | All 16 possible 2×2 squares                                                                 | `BOX_WEIGHT = 5.0`    |

---

#### 2. Contested vs. Uncontested Scaling

For each window, the evaluation counts how many of the AI’s pieces and how many of the opponent’s pieces appear. Then it multiplies those counts by different **contest factors** depending on whether the window is “pure” (only one side’s pieces) or “contested” (both sides have at least one piece):

| Scenario                                | AI factor                | Opponent factor         |
|-----------------------------------------|---------------------------|-------------------------|
| Window contains **only AI’s pieces**      | `MY_UNCONTESTED_WEIGHT  = 15.0` | N/A (opponent has none) |
| Window contains **only Opponent’s pieces** | N/A (AI has none)             | `OPP_UNCONTESTED_WEIGHT = 20.0` |
| Window contains **both AI & Opponent**     | `MY_CONTESTED_WEIGHT    = 1.0`  | `OPP_CONTESTED_WEIGHT   = 4.0`  |

- **Uncontested** windows get a large multiplier (15× for the AI, 20× for the opponent), reflecting that an open line/box is a major threat.
- **Contested** windows receive a small multiplier (1× for the AI, 4× for the opponent), since any mixed window is far less valuable than an open one.
- The asymmetry (20 vs 15, 4 vs 1) biases the AI towards **blocking opponent threats** before advancing its own.

---

#### 3. Computing the Total Score

1. **Compute “raw” totals** for each pattern type:
   - For each window, sum `BASE_WEIGHT` for each piece belonging to a side.
   - Multiply that sum by the appropriate contest factor.
   - Add to running totals:  
     ```python
     my_tot_score  += weighted_my_sum
     opp_tot_score += weighted_opp_sum
     ```
2. **Combine all pattern scores**:
   ```python
   my_tot_score  = my_row_score + my_col_score + my_main_diag_score + my_sec_diag_score + my_support_diag_score + my_box_score
   opp_tot_score = opp_row_score + opp_col_score + opp_main_diag_score + opp_sec_diag_score + opp_support_diag_score + opp_box_score

## Quick Start

### Prerequisites
* Python 3.8 or newer

### Run

```bash
python game.py
