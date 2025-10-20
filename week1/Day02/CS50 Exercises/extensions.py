# Implement a program that prompts the user for the name of a file and 
# then outputs that file’s media type if the file’s name ends, case-insensitively,
#  in any of these suffixes: .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.


def main():
    filename = input("Enter your file name: ").strip().lower()

    # Get the extension from the filename
    if '.' in filename:
        ext = filename[filename.rfind('.'):]
    else:
        ext = ""

    # Use match statement to set media type
    match ext:
        case ".gif":
            media_type = "image/gif"
        case ".jpg" | ".jpeg":
            media_type = "image/jpeg"
        case ".png":
            media_type = "image/png"
        case ".pdf":
            media_type = "application/pdf"
        case ".txt":
            media_type = "text/plain"
        case ".zip":
            media_type = "application/zip"
        case _:
            media_type = "application/octet-stream"

    print("Media type:", media_type)

main()