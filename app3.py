import argparse

def main():
    parser = argparse.ArgumentParser(description="Greet the user with details.")
    parser.add_argument('first_name', nargs='?', default='Larry', help='First name of the user')
    parser.add_argument('last_name', nargs='?', default='Hanson', help='Last name of the user')
    parser.add_argument('age', nargs='?', type=int, default=100, help='Age of the user')
    parser.add_argument('--fast', action='store_true', help='Enable fast mode')

    args = parser.parse_args()

    if args.fast:
        print("fast mode enabled")

    print(f"Hello {args.first_name} {args.last_name}! I see that you have had {args.age + 1} birthdays.")

if __name__ == "__main__":
    main()
