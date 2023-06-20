from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/perform_query', methods=['POST'])
def perform_query():
    query1 = request.form.get('cmd1')
    value1 = request.form.get('value1')
    query2 = request.form.get('cmd2')
    value2 = request.form.get('value2')
    filename = request.form.get('filename')

    file_path = os.path.join('data', filename)

    if not os.path.isfile(file_path):
        return jsonify({'error': f'File {filename} not found'})

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        result = apply_queries(lines, query1, value1, query2, value2)

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)})


def apply_queries(lines, query1, value1, query2, value2):
    # Apply the queries to the lines of the file content

    if query1 == 'filter':
        lines = filter(lambda line: value1 in line, lines)

    if query2 == 'limit':
        try:
            limit = int(value2)
            lines = lines[:limit]
        except ValueError:
            pass

    result = list(lines)

    return result


if __name__ == '__main__':
    app.run()
