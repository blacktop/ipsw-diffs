#!/usr/bin/env python3
"""Update the root README diff index after an automated diff run."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readme", default="README.md")
    parser.add_argument("--os", required=True)
    parser.add_argument("--prev-version", required=True)
    parser.add_argument("--prev-build", required=True)
    parser.add_argument("--next-version", required=True)
    parser.add_argument("--next-build", required=True)
    parser.add_argument("--ai-json", default="")
    return parser.parse_args()


def anchor_for(label: str) -> str:
    anchor = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
    return re.sub(r"-+", "-", anchor)


def section_label(os_name: str, version: str) -> str:
    if " beta" in version.lower():
        match = re.search(r"^(\d+(?:\.\d+)?)\s+beta", version, re.IGNORECASE)
        if match:
            return f"{os_name} {match.group(1)} beta"

    match = re.search(r"^(\d+\.\d+)", version)
    if match:
        return f"{os_name} {match.group(1)}"

    raise ValueError(f"cannot derive README section from version {version!r}")


def display_label(version: str, build: str, other_version: str) -> str:
    label = version
    beta_base = re.match(r"^(.+ beta)$", version, re.IGNORECASE)
    if beta_base and re.match(
        rf"^{re.escape(beta_base.group(1))}\s+2$", other_version, re.IGNORECASE
    ):
        label = f"{version} 1"
    return f"{label} ({build})"


def strip_code_fence(text: str) -> str:
    text = text.strip()
    if not text.startswith("```"):
        return text

    lines = text.splitlines()
    if len(lines) >= 3 and lines[-1].strip() == "```":
        return "\n".join(lines[1:-1]).strip()
    return text


def ai_labels(
    args: argparse.Namespace, expected_section: str
) -> tuple[str, str, str] | None:
    if not args.ai_json.strip():
        return None

    try:
        payload = json.loads(strip_code_fence(args.ai_json))
    except json.JSONDecodeError:
        return None

    got_section = payload.get("section_label")
    previous = payload.get("previous_label")
    next_label = payload.get("next_label")
    if not all(isinstance(value, str) for value in (got_section, previous, next_label)):
        return None
    if got_section != expected_section:
        return None
    if args.prev_build not in previous or args.next_build not in next_label:
        return None

    return got_section, previous, next_label


def discover_diff_dir(prev_build: str, next_build: str) -> str:
    matches: list[Path] = []
    for readme in Path(".").glob("*/README.md"):
        diff_dir = readme.parent
        name = diff_dir.name
        if prev_build in name and next_build in name:
            matches.append(diff_dir)

    if not matches:
        raise FileNotFoundError(
            f"no diff README found for {prev_build} -> {next_build}"
        )
    if len(matches) > 1:
        names = ", ".join(sorted(path.name for path in matches))
        raise RuntimeError(
            f"multiple diff directories match {prev_build} -> {next_build}: {names}"
        )

    return matches[0].as_posix()


def replace_quick_nav(readme: str, label: str, anchor: str, os_name: str) -> str:
    pattern = re.compile(
        r"<p><strong>Quick Nav:</strong>\n(?P<body>.*?)\n</p>", re.DOTALL
    )
    match = pattern.search(readme)
    if not match:
        raise ValueError("README Quick Nav block not found")

    anchors = re.findall(r'<a href="#([^"]+)">([^<]+)</a>', match.group("body"))
    if anchor not in {item[0] for item in anchors}:
        insert_at = len(anchors)
        for index, (_, existing_label) in enumerate(anchors):
            if existing_label.startswith(f"{os_name} "):
                insert_at = index
                break
        anchors.insert(insert_at, (anchor, label))

    lines = []
    for index, (href, text) in enumerate(anchors):
        suffix = " \u00b7" if index < len(anchors) - 1 else ""
        lines.append(f'<a href="#{href}">{text}</a>{suffix}')

    replacement = "<p><strong>Quick Nav:</strong>\n" + "\n".join(lines) + "\n</p>"
    return readme[: match.start()] + replacement + readme[match.end() :]


def section_bounds(readme: str, anchor: str) -> tuple[int, int] | None:
    marker = f'<a id="{anchor}"></a>'
    start = readme.find(marker)
    if start == -1:
        return None

    next_anchor = readme.find("\n<a id=", start + len(marker))
    generating = readme.find("\n### Generating Diffs", start + len(marker))
    candidates = [index for index in (next_anchor, generating) if index != -1]
    end = min(candidates) if candidates else len(readme)
    return start, end


def insert_section(readme: str, os_name: str, section: str) -> str:
    for match in re.finditer(
        rf'\n<a id="[^"]+"></a>\n### {re.escape(os_name)} ', readme
    ):
        return (
            readme[: match.start() + 1] + section + "\n" + readme[match.start() + 1 :]
        )

    marker = "\n### Generating Diffs"
    index = readme.find(marker)
    if index == -1:
        raise ValueError("README insertion point not found")
    return readme[: index + 1] + section + "\n" + readme[index + 1 :]


def replace_or_insert_diff(
    readme: str, args: argparse.Namespace, label: str, anchor: str, link_line: str
) -> str:
    bounds = section_bounds(readme, anchor)
    if bounds is None:
        section = (
            f'<a id="{anchor}"></a>\n'
            f"### {label}\n"
            "<details open>\n"
            "  <summary>View diffs</summary>\n\n"
            f"{link_line}\n\n"
            "</details>\n"
        )
        return insert_section(readme, args.os, section)

    start, end = bounds
    section = readme[start:end]
    link_target = link_line[link_line.rfind("(") + 1 : link_line.rfind(")")]
    if link_target in section:
        return readme

    insert_after = "  <summary>View diffs</summary>\n\n"
    summary_index = section.find(insert_after)
    if summary_index == -1:
        raise ValueError(f"README section {label!r} has no View diffs summary")

    point = summary_index + len(insert_after)
    section = section[:point] + f"{link_line}\n" + section[point:]
    return readme[:start] + section + readme[end:]


def main() -> None:
    args = parse_args()
    expected_section = section_label(args.os, args.next_version)
    labels = ai_labels(args, expected_section)
    if labels is None:
        _, previous, next_label = (
            expected_section,
            display_label(args.prev_version, args.prev_build, args.next_version),
            display_label(args.next_version, args.next_build, args.prev_version),
        )
    else:
        _, previous, next_label = labels

    anchor = anchor_for(expected_section)
    diff_dir = discover_diff_dir(args.prev_build, args.next_build)
    link_line = f"- [{previous} .vs {next_label}]({diff_dir}/README.md)"

    readme_path = Path(args.readme)
    readme = readme_path.read_text()
    updated = replace_quick_nav(readme, expected_section, anchor, args.os)
    updated = replace_or_insert_diff(updated, args, expected_section, anchor, link_line)

    if updated != readme:
        readme_path.write_text(updated)
        print(f"Updated {readme_path} with {link_line}")
    else:
        print(f"{readme_path} already includes {diff_dir}/README.md")


if __name__ == "__main__":
    main()
