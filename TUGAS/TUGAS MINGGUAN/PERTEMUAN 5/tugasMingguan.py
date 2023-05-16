import sys

# system exit 


try:
    # Kode yang mungkin menimbulkan SystemExit exception
    sys.exit("Program dihentikan oleh SystemExit exception")
except SystemExit as e:
    print("Exception SystemExit terjadi:", e)
    print("Output: Program berhenti")
