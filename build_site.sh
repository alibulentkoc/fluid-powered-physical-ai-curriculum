#!/usr/bin/env bash
# Assemble the MkDocs docs/ tree from the authoring sources, then build.
# Sources of truth stay in modules/ and curriculum/; docs/ is generated.
set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

# Clean generated content (keep docs/ authoring files that are NOT generated)
rm -rf docs/modules docs/curriculum_pages
mkdir -p docs/modules docs/curriculum_pages

# Copy module lesson trees (lessons + summaries) into docs/
for d in modules/module*/; do
  mod="$(basename "$d")"
  mkdir -p "docs/modules/$mod/lessons"
  cp "$d"lessons/*.md "docs/modules/$mod/lessons/" 2>/dev/null || true
  [ -f "$d"summary.md ] && cp "$d"summary.md "docs/modules/$mod/summary.md"
done

# Copy the narrative page referenced in nav
cp curriculum/CURRICULUM_NARRATIVE.md docs/curriculum_pages/CURRICULUM_NARRATIVE.md 2>/dev/null || true

# Copy assets (figures) so image references resolve
if [ -d assets ]; then
  mkdir -p docs/assets
  cp -r assets/* docs/assets/ 2>/dev/null || true
fi

echo "docs/ assembled from authoring sources."
