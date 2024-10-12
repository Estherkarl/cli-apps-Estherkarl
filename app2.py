import argparse

def main():
    parser = argparse.ArgumentParser(description="Greet the user.")
    parser.add_argument('-n', '--name', type=str, help='Name of the user')

    args = parser.parse_args()

    if args.name:
        print(f"Good Morning {args.name}!")
    else:
        print("Good Morning folks!")

if __name__ == "__main__":
    main()
