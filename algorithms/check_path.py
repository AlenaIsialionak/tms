
def check_path(path):
    if not path:
        return '/'
    new_path = path.replace('.//', '').split('/')
    result_path = []
    for i in new_path:
        if i != '..':
            result_path.append(i)
        else:
            if result_path:
                result_path.pop()
            else:
                result_path.append('')
    return '/'.join(result_path)


assert check_path('/foo/bar/../test/../test/../baz/.//bar') == '/foo/baz/bar'
assert check_path("") == '/'
assert check_path('../.././/../') == '/'




    

