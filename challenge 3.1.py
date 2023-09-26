def linearSearchProduct(productList, 
targetProduct):
    indices=[]
    for index, product in enumerate(productList):
        if product==targetProduct:
            indices.append(index)
    return indices 
#Example usage:
products=["pen","pencil","Eraser","pen","note","pen"]
target="pen"
target2="paper "
result=linearSearchProduct (products, target)
print(result)