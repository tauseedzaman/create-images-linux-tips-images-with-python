text = "Zstdmt is a multi-threaded version of the Zstandard compression algorithm, which is available in Kali Linux. It is designed to provide faster compression and decompression speeds than the single-threaded version of Zstandard. Zstdmt is especially useful for compressing large files, as it can take advantage of multiple CPU cores to speed up the process.For example, to compress a file named example.txt using Zstdmt in Kali Linux, you can use the following command:zstdmt -T4 -o example.zst example.txt"

# Split the text into words
words = text.split(" ")

# Initialize a counter
counter = 0

message=""
# Loop through the words
for word in words:
    # Print the word
    message += word+" "
    counter += 1
    # Check if the counter is divisible by 9
    if counter % 9 == 0:
        # If so, add a newline character
        message += "\n"
print(message)