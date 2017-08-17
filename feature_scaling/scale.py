""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
### x - x_min / x_max - x_min
def featureScaling(arr):
    result = []
    for x in arr:
        x_min = min(arr)
        x_max =  max(arr)
        scaling = float(x - x_min) / float(x_max - x_min)
        result.append(round(scaling, 3))
    return result

# tests of your feature scaler--line below is input data
# data = [115, 140, 175]
data = [200000, 100000]
print (featureScaling(data))

