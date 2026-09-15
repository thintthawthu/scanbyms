#!/usr/bin/env python3
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    import ms
    ms.entry_point()
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Make sure ms.so is in the same folder")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
