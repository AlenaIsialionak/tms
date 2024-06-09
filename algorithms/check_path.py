
def check_path(path):
    new_path = path.split('/')
    result_path = []
    for i in new_path:
        if i == '' or i =='.':
            continue
        if i == '..':
            if result_path:
                result_path.pop()
        else:
            result_path.append(i)
    return '/' + '/'.join(result_path)



# print(check_path('/foo/bar/../test/../test/../baz/.//bar') )
# print(check_path(""))
# print(check_path('../.././/../'))


assert check_path('/foo/bar/../test/../test/../baz/.//bar') == '/foo/baz/bar'
assert check_path("") == '/'
assert check_path('../.././/../') == '/'




    

