def merge(results):
    i = 0
    while i < len(results):
        geo_key = results[i]['geo']
        j = i + 1
        while j < len(results):
            if geo_key == results[j]['geo']:
                for k in results[j]:
                    if k not in results[i]:
                        results[i][k] = results[j][k]
                results.remove(results[j])
            j += 1
        i += 1
    return results
