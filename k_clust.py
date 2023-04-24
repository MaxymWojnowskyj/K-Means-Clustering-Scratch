import numpy as np


test_data = np.zeros((40000, 4))
test_data[0:10000, :] = 30.0
test_data[10000:20000, :] = 60.0
test_data[20000:30000, :] = 90.0
test_data[30000:, :] = 120.0

np.random.shuffle(test_data)

k = 4

num_variations = 10
# variations_of_clusters  ex: [ [{clusters: [], variations: [] }], [{clusters: [], variations: [] }] ]
variations_of_clusters = []

# run a predefined number of k-means cluster runs saving the variation of each run
for var_i in range(num_variations):
    print('K means variation:', var_i+1)

    rand_rows = np.random.choice(test_data.shape[0], k, replace=False)
    # randomly selected cluster values
    k_clusters = test_data[rand_rows, 0]

    last_k_clusters = [0]*k
    # while the cluster values are changing (stop the loop when no change)
    while not (last_k_clusters == k_clusters).all():
        # create copy so when we modify k_clusters last_k_clusters wont be modified
        last_k_clusters = k_clusters.copy()

        # reset the points each time so we can reassign them to a new random cluster
        assigned_points = {}

        for i in range(len(test_data)): #row
            for j in range(len(test_data[0])): #col
                distances = []
                point = test_data[i][j]
                # for each point in the dataset calculate its distance from each cluster value
                for ki in k_clusters:
                    distances.append(abs(ki-point))

                # find the cluster with the minimum distance to the point (or the closest cluster to the point at row i column j)
                min_index = distances.index(min(distances))
                assigned_k = k_clusters[min_index]
        
                # either assign this cluster to have an array with the point in it or append the point to the clusters array
                if assigned_points.get(assigned_k):
                    assigned_points.get(assigned_k).append(point)
                else:
                    assigned_points[assigned_k] = [point]


        # for each of the clusters calculate the mean of its assigned points and change the cluster value to this mean
        for ki in range(len(k_clusters)):
            k_val = k_clusters[ki]
            mean_k = sum(assigned_points[k_val])/len(assigned_points[k_val])
            k_clusters[ki] = mean_k
        

    # calculate and save the variation for each of the clusters
    variances = []
    for ki in k_clusters:
        var = sum([(kpoint-ki)**2 for kpoint in assigned_points[ki]])/(len(assigned_points[ki])-1)
        variances.append(var)

    variations_of_clusters.append({'Clusters': k_clusters, 'Variances': variances}) 


# now get means of each array in dict, repeat process until there is no change in cluster key values. store variation after means no longer change

# get the version with the minimum sum of variation (meaning the smallest possible variation from the clusters)
min_clusters = None
min_vars = None
min_var_sum = 9999999999
for inst in variations_of_clusters:
    summed_var = sum(inst.get('Variances'))
    if summed_var < min_var_sum:
        min_var_sum = summed_var
        min_clusters = inst.get('Clusters')
        min_vars = inst.get('Variances') 

print(f'Optimal clusters found is {min_clusters}, at the following variances: {min_vars}') 




