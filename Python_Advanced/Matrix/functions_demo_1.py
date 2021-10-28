def loop(index, max_index):
    print(f"starting index {index} , {max_index}")
    if index == max_index:
        print(f" ending loop {index} , {max_index}")
        return

    print(index)
    loop(index=index + 1, max_index=max_index)



loop(1, 3)