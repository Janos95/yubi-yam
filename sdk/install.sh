#!/usr/bin/env bash
# Add the yubi_4310 gripper type to an i2RT SDK checkout.
#
#   sdk/install.sh /path/to/i2rt
#
# Applies the 4-line code patch (enum entry + model path) and copies the gripper
# config, MuJoCo model and meshes into the checkout. Tested against i2rt 120c3c8.
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
target="${1:?usage: sdk/install.sh /path/to/i2rt}"

if [ ! -f "$target/i2rt/robots/utils.py" ]; then
  echo "error: $target does not look like an i2rt checkout (no i2rt/robots/utils.py)" >&2
  exit 1
fi

if grep -q 'YUBI_4310' "$target/i2rt/robots/utils.py"; then
  echo "patch already applied, updating files only"
else
  (cd "$target" && patch -p1 --forward --quiet < "$here/i2rt-yubi_4310.patch")
  echo "patched $target"
fi

cp -R "$here/overlay/i2rt/." "$target/i2rt/"
echo "installed config, model and meshes"
echo "use it with: get_yam_robot(..., gripper_type=GripperType.YUBI_4310)"
