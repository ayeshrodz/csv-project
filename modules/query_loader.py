def load_query(file_path, query_name, limit):
    with open(file_path, 'r') as file:
        content = file.read()

    queries = {}
    current_query = None

    for line in content.splitlines():
        line = line.strip()
        if line.startswith('[') and line.endswith(']'):
            current_query = line[1:-1]
            queries[current_query] = []
        elif current_query:
            queries[current_query].append(line)

    if query_name not in queries:
        raise ValueError(f"Query '{query_name}' not found in the SQL file.")

    query = "\n".join(queries[query_name])
    return query.replace('{limit}', str(limit))