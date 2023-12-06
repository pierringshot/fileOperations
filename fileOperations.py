import os
import shutil

# Function to check if an image exists in the directory


def check_image_existence(directory, image):
    return os.path.exists(os.path.join(directory, image))

# Function to set default paths for filenames.txt, source directory, and target directories


def configure_paths():
    global txt_file, image_directory, copy_directory, move_directory

    print("\nSet Default Paths:")
    txt_file = input(
        "Enter the path of filenames.txt (default: " + txt_file + "): ") or txt_file
    image_directory = input(
        "Enter the source directory path (default: " + image_directory + "): ") or image_directory
    copy_directory = input(
        "Enter the copy destination directory path (default: " + copy_directory + "): ") or copy_directory
    move_directory = input(
        "Enter the move destination directory path (default: " + move_directory + "): ") or move_directory
    print("\nDefault paths configured successfully.")

# Function to display counts of successful and unsuccessful operations


def display_counts(successful_count, unsuccessful_count):
    total_images = successful_count + unsuccessful_count
    print(
        f"\nSuccessful: {successful_count}, Unsuccessful: {unsuccessful_count}. Total Images: {total_images}")

# Function to operate on images in a directory


def process_images(option):
    global txt_file, image_directory, copy_directory, move_directory

    with open(txt_file, 'r') as file:
        image_list = file.read().splitlines()

    if option == "1":
        # Check existence of images
        found_images = []
        missing_images = []

        for image in image_list:
            if check_image_existence(image_directory, image):
                found_images.append(image)
                print(f'\033[92mFound: {image}\033[0m')  # Print in green
            else:
                missing_images.append(image)
                print(f'\033[91mNot Found: {image}\033[0m')  # Print in red

        with open('output/missing_images.txt', 'w') as file:
            for image in missing_images:
                file.write(image + '\n')

        display_counts(len(found_images), len(missing_images))

    elif option == "2":
        # Copy files to directory
        successful_copies = []
        unsuccessful_copies = []

        for image in image_list:
            source_path = os.path.join(image_directory, image)
            target_path = os.path.join(copy_directory, image)
            try:
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copy(source_path, target_path)
                successful_copies.append(image)
                print(f'\033[92mCopied: {image}\033[0m')  # Print in green
            except Exception as e:
                unsuccessful_copies.append(image)
                # Print in red
                print(f'\033[91mFailed to Copy: {image} - {e}\033[0m')

        with open('output/unsuccessful_copies.txt', 'w') as file:
            for image in unsuccessful_copies:
                file.write(image + '\n')

        display_counts(len(successful_copies), len(unsuccessful_copies))

    elif option == "3":
        # Move files to directory
        successful_moves = []
        unsuccessful_moves = []

        for image in image_list:
            source_path = os.path.join(image_directory, image)
            target_path = os.path.join(move_directory, image)
            try:
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.move(source_path, target_path)
                successful_moves.append(image)
                print(f'\033[92mMoved: {image}\033[0m')  # Print in green
            except Exception as e:
                unsuccessful_moves.append(image)
                # Print in red
                print(f'\033[91mFailed to Move: {image} - {e}\033[0m')

        with open('output/unsuccessful_moves.txt', 'w') as file:
            for image in unsuccessful_moves:
                file.write(image + '\n')

        display_counts(len(successful_moves), len(unsuccessful_moves))


# Default paths
txt_file = "/default/filenames.txt"
image_directory = "/default/source_directory"
copy_directory = "/default/copy_destination"
move_directory = "/default/move_destination"

# Load last configured paths (if available)
try:
    with open('config/last_config.txt', 'r') as file:
        txt_file, image_directory, copy_directory, move_directory = file.read().splitlines()
except FileNotFoundError:
    pass

# Main menu with options
while True:
    print("\nOptions:")
    print("1. Check existence of images in directory and subdirectories")
    print("2. Copy given filenames from txt file to directory")
    print("3. Move files from txt file to directory")
    print("4. Configuration (Set default paths)")
    print("5. Exit")

    option = input("Enter your choice (1-5): ")

    if option == "1" or option == "2" or option == "3":
        process_images(option)

    elif option == "4":
        # Configuration to set default paths
        configure_paths()
        with open('config/last_config.txt', 'w') as file:
            file.write(
                f"{txt_file}\n{image_directory}\n{copy_directory}\n{move_directory}")

    elif option == "5":
        # Exit the script
        break

    else:
        print("Invalid option. Please select a valid option (1-5).")
