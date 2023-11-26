def my_function(liste):
    doublons = []
    for _ in liste:
        if _ not in doublons:
            doublons.append(_)
    return doublons

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print("liste avant supression des doublons :", L)

doublons = my_function(L)
print("liste après supression des doublons :", doublons)