#!/usr/bin/env python3
"""Validate local links in the workshop static HTML hub.

The checker intentionally ignores external URLs and approval-gated publishing
concerns. It verifies only same-repository HTML/document references so the hub
can be previewed safely before it is made public.
"""

from __future__ import annotations

import html.parser
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
HTML_GLOBS = ("*.html", "resources/*.html")
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "sms", "javascript"}


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        element_id = attrs_dict.get("id")
        if element_id:
            self.ids.add(element_id)

        for attr in ("href", "src"):
            value = attrs_dict.get(attr)
            if value:
                self.links.append((attr, value))


def html_files() -> list[Path]:
    files: list[Path] = []
    for pattern in HTML_GLOBS:
        files.extend(ROOT.glob(pattern))
    return sorted(set(files))


def parse_file(path: Path) -> LinkParser:
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def local_target(source: Path, raw_link: str) -> tuple[Path, str] | None:
    parsed = urlparse(raw_link)
    if parsed.scheme in IGNORED_SCHEMES or parsed.netloc:
        return None

    # Pure page-local fragment: only verify the id on this page.
    if not parsed.path and parsed.fragment:
        return (source, unquote(parsed.fragment))

    if not parsed.path:
        return None

    target = (source.parent / unquote(parsed.path)).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return None
    return (target, unquote(parsed.fragment))


def main() -> int:
    parsers = {path: parse_file(path) for path in html_files()}
    errors: list[str] = []

    for source, parser in parsers.items():
        for attr, raw_link in parser.links:
            target_info = local_target(source, raw_link)
            if target_info is None:
                continue

            target, fragment = target_info
            display_source = source.relative_to(ROOT)
            display_target = target.relative_to(ROOT) if target.exists() else target

            if not target.exists():
                errors.append(f"{display_source}: {attr}='{raw_link}' points to missing file {display_target}")
                continue

            if fragment and target.suffix.lower() in {".html", ".htm"}:
                target_parser = parsers.get(target) or parse_file(target)
                if fragment not in target_parser.ids:
                    errors.append(f"{display_source}: {attr}='{raw_link}' points to missing fragment #{fragment}")

    if errors:
        print("Static link check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Static link check passed for {len(parsers)} HTML files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
