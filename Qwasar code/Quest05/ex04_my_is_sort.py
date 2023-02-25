def my_is_sort(intigers):
    if intigers == sorted(intigers) or intigers == sorted(intigers, reverse=True):
        return True
    elif intigers != sorted(intigers):
        return False