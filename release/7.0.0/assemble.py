import hashlib
import json
import sys
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

root = Path(__file__).resolve().parent
old, target = map(Path, sys.argv[1:])
def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()

if digest(old) != "20b9e196a65ece25d42fffac11b493547a2d89d4c92b5fa2e3e5f7a07df8d537":
    sys.exit("Unexpected 6.5.0 archive")
timestamps = dict(json.loads((root / "times.json").read_text()))
with ZipFile(old) as base, ZipFile(root / "changes.zip") as changes, ZipFile(target, "w") as output:
    assert set(changes.namelist()) <= set(base.namelist())
    for index, member in enumerate(base.infolist()):
        if index in timestamps:
            stamp = tuple(timestamps[index])
        info = ZipInfo(member.filename, stamp)
        info.create_system = 0
        data = (changes if member.filename in changes.namelist() else base).read(member.filename)
        output.writestr(info, data, compress_type=ZIP_DEFLATED, compresslevel=4)
if digest(target) != "a1c84ab1d8b866fc89f32e3dc719a5a8f8d689900b8cb4dfc3e36df45ff28919":
    sys.exit("Archive differs from the tested and signed 7.0.0 build")
print("Archive matches the signed 7.0.0 release.")
