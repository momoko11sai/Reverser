#!/usr/bin/env python3
import argparse, shutil, subprocess, sys
from pathlib import Path

def main():
    p = argparse.ArgumentParser(description="動画を逆再生にする(解像度は元のまま)")
    p.add_argument("input")
    p.add_argument("output", nargs="?")
    p.add_argument("--crf", type=int, default=18, help="画質(小さいほど高画質)")
    p.add_argument("--no-audio", action="store_true")
    a = p.parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("ffmpegが見つかりません。 brew install ffmpeg")

    src = Path(a.input)
    dst = Path(a.output) if a.output else src.with_name(src.stem + "_reversed.mp4")

    cmd = ["ffmpeg", "-i", str(src), "-vf", "reverse"]
    cmd += ["-an"] if a.no_audio else ["-af", "areverse"]
    cmd += ["-c:v", "libx264", "-crf", str(a.crf), "-pix_fmt", "yuv420p", str(dst)]
    subprocess.run(cmd, check=True)
    print(f"完了: {dst}")

if __name__ == "__main__":
    main()
