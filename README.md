# Lipid / Ion Blockage (Cylinder Occupancy) Toolkit

This repository contains quick-and-practical scripts for detecting **lipid (POPC) or ion (K⁺) “blockage”** events in an MD trajectory by testing whether selected atoms enter a **moving cylinder** near the protein.

The workflow is intentionally *fast and dirty*: it assumes you know your system indexing and that you will adjust selections/parameters as needed.

## Contents

- `lipid_block.ipynb` — POPC cylinder-occupancy analysis (MDAnalysis)
- `lipid_block_ion.ipynb` — K⁺ cylinder-occupancy analysis (MDAnalysis)
- `do_lipidblockage.sh` — batch runner for replicate folders (copies scripts, runs analyses, plots with gnuplot, converts PS→PDF)

## Requirements

### Python / analysis
- Python 3
- `MDAnalysis`
- `numpy`

### Plotting / batch workflow
- `ipython` (to run `.py` scripts in the batch runner)
- `gnuplot`
- `ps2pdf` (Ghostscript)

## Expected input files

The notebooks (and your `.py` variants used by the batch script) expect:

- `v+centerilk.pdb` — structure/topology readable by MDAnalysis
- `v+center.xtc` — trajectory

## Method overview

1. Compute a **moving reference point**:
   - center of mass (COM) of a few user-chosen protein atoms (`atom_numbers`)
2. Define a **cylinder** centered on that point, optionally shifted along **z** (`cylinder_center_offset`)
3. For each sampled frame:
   - test whether each selected atom (lipid headgroup atoms or ions) lies inside the cylinder
4. Write a time series (`.xvg`) that can be plotted.

## Parameters you will likely edit

Inside the notebooks / scripts:

- `atom_numbers` — indices used for COM reference (system-dependent)
- `radius` (Å), `height` (Å) — cylinder geometry
- `cylinder_center_offset` (Å) — shifts the cylinder center in z
- Selection strings:
  - `popc_selection` for POPC atoms
  - `k_selection*` (index ranges) for K ions

## Outputs

The notebooks write `.xvg` files (e.g., `xxx2.xvg`, `xxx3.xvg`, `xxx4.xvg` in the current versions).
Columns contain:

- time
- cylinder center z
- per-atom value (either z relative to cylinder center, or radial distance, depending on the variant)

## Batch usage (replicates)

If your folders are arranged like:

```
lipid_block/
├── 1/   # “template” folder containing the analysis + gnuplot scripts
├── 3/
├── 4/
└── 5/
```

Run:

```bash
chmod +x do_lipidblockage.sh
./do_lipidblockage.sh
```

This will copy scripts from `../1/` into each replicate folder, run analyses, generate plots with gnuplot, and convert `.ps` files to `.pdf`.

