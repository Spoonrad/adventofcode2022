from utils import read_day_input_file

DAY = 7


def subtree(tree, position):
    subtree = tree
    for k in position:
        subtree = subtree[k]
    return subtree


def parse_tree(input_str):
    tree = {}
    current_position = []
    for line in input_str.split('\n')[1:]:
        if line[0] == '$':
            if line[2:4] == 'cd':
                key = line[5:]
                if key == '..':
                    current_position.pop()
                else:
                    _subtree = subtree(tree, current_position)
                    if not _subtree.get(key):
                        _subtree[key] = {}
                    current_position.append(key)

        elif line[:3] == 'dir':
            key = line[4:]
            _subtree = subtree(tree, current_position)
            if not _subtree.get(key):
                _subtree[key] = {}
        else:
            size_str, key = tuple(line.split(' '))
            subtree(tree, current_position)[key] = int(size_str)

    return tree

def calc_dir_size(sizes, tree, position):
    _size = 0
    _subtree = subtree(tree, position)
    for key, value in _subtree.items():
        if isinstance(value, int):
            _size += value
        else:
            sizes, dir_size = calc_dir_size(sizes, tree, position + [key])
            _size += dir_size
    sizes['/'.join(position)] = _size
    return sizes, _size



def solve(input_str):
    tree = parse_tree(input_str)
    sizes, _ = calc_dir_size({}, tree, [])
    total_size = 0
    for path, size in sizes.items():
        if size < 100000:
            total_size += size
    return total_size

def solve_part_two(input_str):
    tree = parse_tree(input_str)
    sizes, _ = calc_dir_size({}, tree, [])
    total_size = sizes['']
    space_disk_left = 70000000 - total_size
    min_size_to_del = 30000000 - space_disk_left
    best = total_size

    for size in sizes.values():
        if size > min_size_to_del and size < best:
            best = size

    return best



if __name__ == '__main__':
    input_str = read_day_input_file(DAY)
    print(solve(input_str))
    print(solve_part_two(input_str))


