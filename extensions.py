# Approach 1: Using if-elif-else statements
# Read filename and identify the media type based on extension
file_name = input("Enter the filename: ")
file_name = file_name.strip().lower()
if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
  
# ----------------

# Approach 2: Using match-case blocks
def identify_media_type(file_name):
  file_name = file_name.strip().lower()

  match file_name.split(".")[-1]:
    case "gif":
      return "image/gif"
    case "jpg" | "jpeg":
      return "image/jpeg"
    case "png":
      return "image/png"
    case "pdf":
      return "application/pdf"
    case "txt":
      return "text/plain"
    case "zip":
      return "application/zip"
    case _:
      return "application/octet-stream"

# Example usage:
# file_name = input("Enter the filename: ")
# media_type = identify_media_type(file_name)
# print(media_type)