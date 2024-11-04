# write your code here
def median(sub_1, sub_2, sub_3):
    med = (sub_1 + sub_2 + sub_3) / 3
    print(med)
    if med >= 60:
        return 'Congratulations, you are accepted!'
    else:
        return 'We regret to inform you that we will not be able to offer you admission.'
def acceptance(total, max_app, app):
    app = [[j[0], float(j[1])] for j in app]
    sorted_applicants = sort_ascending(app)
    accepted_applicants = sorted_applicants[:max_app]
    names_applicants = [i[0] for i in accepted_applicants]
    return names_applicants
def sort_ascending(applicants):
    sorted_list = sorted(applicants, key=lambda x: (-x[1], x[0]))
    return sorted_list
    
def sort_high_low(applicants):
    sorted_list = sorted(applicants, key=lambda x: (x[0], [1]))
    sorted_list = sorted(applicants, reverse=True, key=lambda x: (x[0], x[1]))
    return sorted_list
    
total_num_applicants = int(input('Number of applicants: '))
max_num_applicants = int(input('Maximum number of applicants: '))
applicants = [input().rsplit(' ', 1) for i in range(total_num_applicants)]

sorted_applicants = acceptance(total_num_applicants, max_num_applicants, applicants)
print('Successful applicants:')
print(*sorted_applicants, sep='\n')