import sys

def main():
    if "--help" in sys.argv:
        print("Usage: python app1.py [options]")
        print("Options:")
        print("  --help        Show this help message")
        print("  --fast        Enable fast mode")
    elif "--fast" in sys.argv:
        print("Fast mode enabled")
    else:
        print("Slow mode enabled")

if __name__ == "__main__":
    main()
