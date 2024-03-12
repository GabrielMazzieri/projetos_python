def getMinTime(cache_size, cache_time, server_time, urls):
    cache = {}
    result = []
    
    for url in urls:
        if url in cache:
            result.append(cache[url])
        else:
            if len(cache) >= cache_size:
                cache.pop(list(cache.keys())[0])  # Remove o URL mais antigo do cache
            cache[url] = min(cache_time, server_time)  # Adiciona o URL ao cache
            result.append(cache[url])
    
    return result

# Entrada de exemplo
cache_size = 2
cache_time = 2
server_time = 3
urls = ["www.google.com", "www.google.com", "www.yahoo.com", "www.coursera.com"]

# Chamada da função
print(getMinTime(cache_size, cache_time, server_time, urls))