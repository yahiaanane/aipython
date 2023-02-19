import openai
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

openai.api_key = "YOUR_API_KEY_HERE"

class ChatGptHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        prompt = data['prompt']
        completions = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"choices": completions.choices}
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=ChatGptHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Listening at: http://localhost:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
