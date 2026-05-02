# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Fixed

- **Backend: chat_submit background task executor error** — Fixed a server-side issue where tasks submitted via `chat_submit` would fail with `CurrentThreadExecutor already quit or is broken`. Tasks now execute reliably in the background. No client-side changes needed.

### Changed

- **Python 3.7+ support** — Added `from __future__ import annotations` to support Python 3.7 and above. Previously required Python 3.10+ due to `X | Y` type annotation syntax.
