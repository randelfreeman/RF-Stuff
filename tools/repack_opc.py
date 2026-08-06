#!/usr/bin/env python3
"""Repack a .docx/.xlsx/.pptx so the package is strictly OPC-conformant.

Two things some writers get wrong and strict readers (notably Word) dislike:
  1. [Content_Types].xml must be the FIRST part in the archive.
  2. Directory entries have no place in an OPC package.

Usage: python tools/repack_opc.py in.docx out.docx
"""
import shutil
import sys
import zipfile

CT = "[Content_Types].xml"


def repack(src: str, dst: str) -> None:
    with zipfile.ZipFile(src) as zin:
        names = [n for n in zin.namelist() if not n.endswith("/")]
        if CT not in names:
            raise SystemExit(f"{src}: no {CT} — not an OPC package")
        ordered = [CT] + [n for n in names if n != CT]
        data = {n: zin.read(n) for n in ordered}
        infos = {n: zin.getinfo(n) for n in ordered}

    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for n in ordered:
            zi = zipfile.ZipInfo(n, date_time=infos[n].date_time)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o600 << 16
            zout.writestr(zi, data[n])

    with zipfile.ZipFile(dst) as z:
        got = z.namelist()
        assert got[0] == CT, f"repack failed: first entry is {got[0]}"
        assert not any(n.endswith("/") for n in got), "repack failed: directory entries remain"
        assert z.testzip() is None, "repack failed: CRC error"
    print(f"repacked {dst}: {len(ordered)} parts, {CT} first, no directory entries")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    src, dst = sys.argv[1], sys.argv[2]
    if src == dst:
        shutil.copyfile(src, src + ".tmp")
        src = src + ".tmp"
    repack(src, dst)
