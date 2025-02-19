"""
This file is kept for backwards compatibility with older pip versions.
The project configuration is in pyproject.toml
"""
from setuptools import setup
from setuptools.command.build_py import build_py as _build
import os.path
import subprocess
import shutil

PROTOC_EXEC = "protoc"
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

class ProtobufBuilder(_build):
    def run(self):
        # check if protobuf is installed
        exec_path = shutil.which(PROTOC_EXEC)
        if exec_path is None:
            raise Exception("You should install protobuf compiler")

        print("Building protobuf file")
        subprocess.run([exec_path,
            "--proto_path=" + CURRENT_DIR,
            "--python_out=" + CURRENT_DIR + "/gpapi/",
            CURRENT_DIR + "/googleplay.proto"])
        super().run()

if __name__ == "__main__":
    setup(
        cmdclass={'build_py': ProtobufBuilder}
    )
