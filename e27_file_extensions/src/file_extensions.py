from collections import defaultdict

def file_extensions(filename):
    no_extension = []
    extension_dict = defaultdict(list)

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if '.' not in line:
                    no_extension.append(line)
                else:
                    parts = line.split('.')
                    ext = parts[-1]
                    extension_dict[ext].append(line)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

    return no_extension, dict(extension_dict)

def main():
    result = file_extensions("src/filenames.txt")

    if result:
        no_extension_count = len(result[0])
        print(f"{no_extension_count} files with no extension")

        sorted_extensions = sorted(result[1].items(), key=lambda x: x[0])
        for ext, filenames in sorted_extensions:
            print(f"{ext} {len(filenames)}")

if __name__ == "__main__":
    main()