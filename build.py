#!/usr/bin/env python

import os
from bincrafters import build_template_default

if __name__ == "__main__":
    docker_entry_script = None
    if os.getenv("CONAN_GCC_VERSIONS") == "4.9":
        docker_entry_script = "conan install ninja/1.10.0@ --build ninja"

    builder = build_template_default.get_builder(docker_entry_script=docker_entry_script)

    builder.run()
    
