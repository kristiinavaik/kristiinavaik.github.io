#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ -x /opt/homebrew/opt/ruby/bin/ruby ]]; then
  ruby_bin=/opt/homebrew/opt/ruby/bin/ruby
  bundle_bin=/opt/homebrew/opt/ruby/bin/bundle
else
  ruby_bin="$(command -v ruby)"
  bundle_bin="$(command -v bundle)"
fi
export BUNDLE_PATH=vendor/bundle
if [[ "${1:-}" == install ]]; then
  exec "$ruby_bin" "$bundle_bin" install
fi
exec "$ruby_bin" "$bundle_bin" exec jekyll "$@"
