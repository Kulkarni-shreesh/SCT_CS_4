def main():
    with open("key_log.txt", "a") as log_file:
        print("Type your input (Ctrl+C to stop):")
        try:
            while True:
                user_input = input()
                log_file.write(user_input + "\n")
                log_file.flush()
        except KeyboardInterrupt:
            print("\nExiting and saving log.")

if _name_ == "_main_":
    main()