#!/usr/bin/env python3
"""Build the project-local Sugaku Fourier Type 1 math-extension font.

The source font is Fourier-Math-Extension from TeX Live.  The generated
font keeps Fourier's metrics and glyph repertoire, changes the PostScript
font name, and replaces only summationtext and summationdisplay with
original outlines designed for this project.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
GENERATED = WORK / "generated"
TEXMF = ROOT / "texmf"

PFB_OUT = (
    TEXMF
    / "fonts"
    / "type1"
    / "public"
    / "sugaku-fourier"
    / "sugaku-fourier-mex.pfb"
)
AFM_OUT = (
    TEXMF
    / "fonts"
    / "afm"
    / "public"
    / "sugaku-fourier"
    / "sugaku-fourier-mex.afm"
)
TFM_OUT = (
    TEXMF
    / "fonts"
    / "tfm"
    / "public"
    / "sugaku-fourier"
    / "sugaku-fourier-mex.tfm"
)
MAP_OUT = (
    TEXMF
    / "fonts"
    / "map"
    / "dvips"
    / "sugaku-fourier"
    / "sugaku-fourier.map"
)
DISASM_OUT = GENERATED / "sugaku-fourier-mex.disasm"
PL_OUT = GENERATED / "sugaku-fourier-mex.pl"
BUILD_INFO_OUT = GENERATED / "BUILD-INFO.txt"

OLD_PS_NAME = "Fourier-Math-Extension"
NEW_PS_NAME = "SugakuFourier-Math-Extension"


SUMMATION_TEXT = r"""/summationtext {
	64 1048 hsbw
	-890 115 hstem
	-135 115 hstem
	0 -20 rmoveto
	920 hlineto
	8 0 -8 -115 -40 -115 rrcurveto
	-65 hlineto
	-5 60 -35 45 -80 10 rrcurveto
	-435 hlineto
	310 -295 rlineto
	15 -10 0 -30 -15 -10 rrcurveto
	-315 -295 rlineto
	440 hlineto
	70 0 45 45 5 70 rrcurveto
	65 hlineto
	40 -20 8 -180 -8 -30 rrcurveto
	-920 hlineto
	60 65 rlineto
	385 345 rlineto
	-15 10 0 30 15 10 rrcurveto
	-385 335 rlineto
	-60 75 rlineto
	closepath
	endchar
	} ND"""


SUMMATION_DISPLAY = r"""/summationdisplay {
	85 1450 hsbw
	-1240 155 hstem
	-185 165 hstem
	0 -20 rmoveto
	1280 hlineto
	10 0 -10 -160 -55 -165 rrcurveto
	-90 hlineto
	-10 85 -40 60 -115 15 rrcurveto
	-610 hlineto
	440 -420 rlineto
	20 -10 0 -30 -20 -10 rrcurveto
	-450 -430 rlineto
	620 hlineto
	90 0 65 65 10 95 rrcurveto
	90 hlineto
	55 -20 10 -250 -10 -45 rrcurveto
	-1280 hlineto
	80 80 rlineto
	540 505 rlineto
	-20 10 0 30 20 10 rrcurveto
	-540 475 rlineto
	-80 110 rlineto
	closepath
	endchar
	} ND"""


def run(*args: str) -> str:
    return subprocess.run(
        args,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    ).stdout


def kpsewhich(name: str) -> Path:
    resolved = run("kpsewhich", name).strip()
    if not resolved:
        raise FileNotFoundError(f"TeX Live file not found: {name}")
    return Path(resolved)


def replace_charstring(source: str, glyph_name: str, replacement: str) -> str:
    pattern = re.compile(
        rf"/{re.escape(glyph_name)} \{{.*?\n\t\}} ND",
        flags=re.DOTALL,
    )
    result, count = pattern.subn(lambda _: replacement, source)
    if count != 1:
        raise RuntimeError(
            f"Expected one /{glyph_name} charstring, replaced {count}"
        )
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    source_pfb = kpsewhich("fourier-mex.pfb")
    source_afm = kpsewhich("fourier-mex.afm")
    source_tfm = kpsewhich("fourier-mex.tfm")

    disassembled = run("t1disasm", str(source_pfb))
    disassembled = disassembled.replace(
        "%!PS-AdobeFont-1.0: Fourier-Math-Extension 001.004",
        "%!PS-AdobeFont-1.0: SugakuFourier-Math-Extension 001.000",
        1,
    )
    disassembled = disassembled.replace(
        "/version (001.004) readonly def",
        "/version (001.000) readonly def",
        1,
    )
    disassembled = disassembled.replace(
        "/Notice ((C) 2003, GUTenberg) readonly def",
        (
            "/Notice ((C) 2003, GUTenberg; SugakuFourier derived work "
            "2026) readonly def"
        ),
        1,
    )
    disassembled = disassembled.replace(OLD_PS_NAME, NEW_PS_NAME)
    disassembled = disassembled.replace(
        "/BlueScale 0.050000000000000 def",
        "/BlueScale 0.039625000000000 def",
        1,
    )
    disassembled = replace_charstring(
        disassembled, "summationtext", SUMMATION_TEXT
    )
    disassembled = replace_charstring(
        disassembled, "summationdisplay", SUMMATION_DISPLAY
    )

    for path in (PFB_OUT, AFM_OUT, TFM_OUT, MAP_OUT, DISASM_OUT, PL_OUT):
        path.parent.mkdir(parents=True, exist_ok=True)

    DISASM_OUT.write_text(disassembled, encoding="ascii")
    subprocess.run(
        ["t1asm", "-b", str(DISASM_OUT), str(PFB_OUT)],
        check=True,
    )

    afm = source_afm.read_text(encoding="latin-1")
    afm = afm.replace("FullName Fourier-Math-Extension", f"FullName {NEW_PS_NAME}")
    afm = afm.replace("FontName Fourier-Math-Extension", f"FontName {NEW_PS_NAME}")
    afm = afm.replace(
        "FamilyName Fourier-Math-Extension", f"FamilyName {NEW_PS_NAME}"
    )
    afm = afm.replace("Version 001.004", "Version 001.000")
    afm = afm.replace(
        "Notice (C) 2003, GUTenberg",
        "Notice (C) 2003, GUTenberg; SugakuFourier derived work 2026",
    )
    afm = re.sub(
        r"C 80 ; WX \d+ ; N summationtext ; B [^;]+;",
        "C 80 ; WX 1048 ; N summationtext ; B 64 -890 984 -20 ;",
        afm,
    )
    afm = re.sub(
        r"C 88 ; WX \d+ ; N summationdisplay ; B [^;]+;",
        "C 88 ; WX 1450 ; N summationdisplay ; B 85 -1240 1365 -20 ;",
        afm,
    )
    AFM_OUT.write_text(afm, encoding="latin-1")

    pl = run("tftopl", str(source_tfm))
    pl, text_width_count = re.subn(
        r"(\(CHARACTER O 120\s+\(CHARWD R )[^)]+(\))",
        r"\g<1>1.048\g<2>",
        pl,
        count=1,
    )
    pl, display_width_count = re.subn(
        r"(\(CHARACTER O 130\s+\(CHARWD R )[^)]+(\))",
        r"\g<1>1.45\g<2>",
        pl,
        count=1,
    )
    if text_width_count != 1 or display_width_count != 1:
        raise RuntimeError("Unable to update summation widths in TeX PL metrics")
    PL_OUT.write_text(pl, encoding="ascii")
    subprocess.run(["pltotf", str(PL_OUT), str(TFM_OUT)], check=True)
    MAP_OUT.write_text(
        (
            "sugaku-fourier-mex "
            "SugakuFourier-Math-Extension "
            "<sugaku-fourier-mex.pfb\n"
        ),
        encoding="ascii",
    )

    validation = run("t1disasm", str(PFB_OUT))
    for required in (
        "/FontName /SugakuFourier-Math-Extension def",
        "/summationtext {",
        "/summationdisplay {",
    ):
        if required not in validation:
            raise RuntimeError(f"Generated font validation failed: {required}")

    BUILD_INFO_OUT.write_text(
        "\n".join(
            (
                "SugakuFourier build manifest",
                "release: 1.0",
                f"source-pfb: {source_pfb}",
                f"source-pfb-sha256: {sha256(source_pfb)}",
                f"generated-pfb: {PFB_OUT}",
                f"generated-pfb-sha256: {sha256(PFB_OUT)}",
                f"generated-afm: {AFM_OUT}",
                f"generated-tfm: {TFM_OUT}",
                f"generated-pl: {PL_OUT}",
                "changed-glyphs: summationtext (code 80), summationdisplay (code 88)",
                "text-sum-width: 1.048 em",
                "display-sum-width: 1.450 em",
                "BlueScale: 0.039625 (derived-font validation fix)",
                "license: LPPL 1.3c; derived files use distinct names",
                "",
            )
        ),
        encoding="utf-8",
    )

    print(PFB_OUT)
    print(AFM_OUT)
    print(TFM_OUT)
    print(MAP_OUT)
    print(BUILD_INFO_OUT)


if __name__ == "__main__":
    main()
