from __future__ import annotations

import hashlib
import json
import shutil
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
MANIFEST_PATH = ROOT / "update.json"
ALLOWED_RELEASE_PREFIX = "/faine-oss/butuoyan-app/releases/download/"


def release_asset_url(manifest: dict[str, object]) -> str:
    candidates: list[str] = []
    mirrors = manifest.get("downloadMirrors", [])
    if isinstance(mirrors, list):
        for mirror in mirrors:
            if isinstance(mirror, dict) and isinstance(mirror.get("url"), str):
                candidates.append(mirror["url"])
    download_url = manifest.get("downloadUrl")
    if isinstance(download_url, str):
        candidates.append(download_url)

    for candidate in candidates:
        parsed = urlparse(candidate)
        if (
            parsed.scheme == "https"
            and parsed.hostname == "github.com"
            and parsed.path.startswith(ALLOWED_RELEASE_PREFIX)
        ):
            return candidate
    raise RuntimeError("update.json does not contain an approved GitHub release asset")


def download_and_verify(source_url: str, destination: Path, expected_sha256: str) -> None:
    request = urllib.request.Request(
        source_url,
        headers={"User-Agent": "butuoyan-pages-builder/1.0"},
    )
    digest = hashlib.sha256()
    with urllib.request.urlopen(request, timeout=90) as response, destination.open("wb") as output:
        while chunk := response.read(1024 * 1024):
            output.write(chunk)
            digest.update(chunk)

    actual_sha256 = digest.hexdigest().upper()
    if actual_sha256 != expected_sha256.upper():
        destination.unlink(missing_ok=True)
        raise RuntimeError(
            f"APK checksum mismatch: expected {expected_sha256}, got {actual_sha256}"
        )


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    primary_url = manifest.get("downloadUrl")
    expected_sha256 = manifest.get("sha256")
    if not isinstance(primary_url, str) or not isinstance(expected_sha256, str):
        raise RuntimeError("update.json is missing downloadUrl or sha256")

    filename = Path(urlparse(primary_url).path).name
    if not filename.lower().endswith(".apk"):
        raise RuntimeError("downloadUrl must end with an APK filename")

    shutil.rmtree(SITE, ignore_errors=True)
    downloads = SITE / "downloads"
    downloads.mkdir(parents=True)
    shutil.copy2(ROOT / "index.html", SITE / "index.html")
    shutil.copy2(MANIFEST_PATH, SITE / "update.json")
    (SITE / ".nojekyll").touch()

    download_and_verify(
        release_asset_url(manifest),
        downloads / filename,
        expected_sha256,
    )


if __name__ == "__main__":
    main()
