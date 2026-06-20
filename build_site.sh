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

# Copy the authoritative curriculum overview into the site (primary overview doc).
# Governance artifacts (methodology, completion report) are intentionally NOT copied
# into the student site. Rewrite its repo-root links to site-relative paths.
if [ -f CURRICULUM_OVERVIEW.md ]; then
  sed -e 's|(docs/MACHINE_STORY.md)|(MACHINE_STORY.md)|g' \
      -e 's|(docs/BENCHMARK_TASKS.md)|(BENCHMARK_TASKS.md)|g' \
      -e 's|(docs/MODULE_ARTIFACT_MAP.md)|(MODULE_ARTIFACT_MAP.md)|g' \
      -e 's|(curriculum/CURRICULUM_NARRATIVE.md)|(curriculum_pages/CURRICULUM_NARRATIVE.md)|g' \
      -e 's|(curriculum/CAPABILITY_GROWTH_MAP.md)|(https://github.com/alibulentkoc/fluid-powered-physical-ai-curriculum/blob/main/curriculum/CAPABILITY_GROWTH_MAP.md)|g' \
      -e 's|(curriculum/CURRICULUM_ENGINEERING_METHODOLOGY.md)|(https://github.com/alibulentkoc/fluid-powered-physical-ai-curriculum/blob/main/curriculum/CURRICULUM_ENGINEERING_METHODOLOGY.md)|g' \
      -e 's|(curriculum/FINAL_COMPLETION_REPORT.md)|(https://github.com/alibulentkoc/fluid-powered-physical-ai-curriculum/blob/main/curriculum/FINAL_COMPLETION_REPORT.md)|g' \
      CURRICULUM_OVERVIEW.md > docs/CURRICULUM_OVERVIEW.md
fi

# Copy assets (figures) so image references resolve
if [ -d assets ]; then
  mkdir -p docs/assets
  cp -r assets/* docs/assets/ 2>/dev/null || true
fi

# Copy the standalone interactive demos and quizzes into the site so the
# lesson links resolve (they open in a new tab, like the sister site).
rm -rf docs/demos docs/quizzes
if [ -d demos ]; then
  mkdir -p docs/demos
  # only the per-module html widgets (skip PLAN.md / _shared.css)
  for d in demos/module*/; do
    cp -r "$d" "docs/demos/" 2>/dev/null || true
  done
fi
if [ -d quizzes ]; then
  mkdir -p docs/quizzes
  for d in quizzes/module*/; do
    cp -r "$d" "docs/quizzes/" 2>/dev/null || true
  done
fi

echo "docs/ assembled from authoring sources."
