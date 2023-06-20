# homework23
Supported Commands
1. Filter Command (filter)
The filter command filters the lines of the file based on the provided value. Only the lines containing the value will be included in the result.

Example query: cmd1=filter&value1=POST

2. Limit Command (limit)
The limit command limits the number of lines returned in the result to the specified value.

Example query: cmd2=limit&value2=5

Response Format
The server responds with JSON objects containing the result of the file processing or error messages.

Success Response
json
Copy code
{
  "result": [
    "Line 1",
    "Line 2",
    "Line 3"
  ]
}
Error Response
json
Copy code
{
  "error": "File not found"
}
Notes
Make sure to place the files you want to process inside the data directory in the same folder as the web server.
The server supports the processing of text files.
Feel free to customize the server and add additional functionality as per your requirements.
