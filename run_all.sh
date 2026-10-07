#!/usr/bin/env bash
# Rebuild everything from Toyota's CAD and re-run all checks.
#   git submodule update --init && pip install -r requirements.txt && ./run_all.sh
set -euo pipefail
cd "$(dirname "$0")"
python3 cad/build.py          # parts -> cad/out, interference check, sim meshes
python3 sim/finger_sweep.py   # finger travel from the exact meshes
python3 sim/build_model.py    # i2RT gripper model + config -> sdk/overlay
python3 sim/check_sim.py      # SDK path, grasp physics, reach vs stock gripper
python3 docs/make_figures.py
python3 cad/printed.py        # fully printed prototype parts -> cad/out/printed
python3 docs/make_printed_figure.py
