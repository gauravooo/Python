# This program determines the MIME type of a file based on its extension.
def main():
    i = input("Enter the file name: ").strip().lower()
    print(check(i))

def check(value):
        if value.endswith(".gif"):
            return "image/gif"
        elif value.endswith(".jpg"):
            return "image/jpeg"
        elif value.endswith(".jpeg"):
            return "image/jpeg"
        elif value.endswith(".png"):
            return "image/png"
        elif value.endswith(".pdf"):
            return "application/pdf"
        elif value.endswith(".txt"):
            return "text/plain"
        elif value.endswith(".zip"):
            return "application/zip"
        else:
            return "application/octet-stream"

main()