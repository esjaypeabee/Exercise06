scores_dict = {}

scores = open('scores.txt')

for line in scores:
    line = line.rstrip()
    rest_data = line.split(':')
    scores_dict[rest_data[0]] = rest_data[1] 

for resto in sorted(scores_dict):
    print "Restaurant %s is rated %s" % (resto, scores_dict[resto])