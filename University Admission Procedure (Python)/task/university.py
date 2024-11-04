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
    sorted_app = sort_ascending(app)
    accepted_applicants = sorted_app[:max_app]
    names_applicants = [i[0] for i in accepted_applicants]
    return names_applicants
def sort_ascending(app):
    sorted_list = sorted(app, key=lambda x: (-x[1], x[0]))
    return sorted_list
    
def sort_high_low(app):
    sorted_list = sorted(app, key=lambda x: (x[0], [1]))
    sorted_list = sorted(app, reverse=True, key=lambda x: (x[0], x[1]))
    return sorted_list

def read_applicants(filename):
    """Reads applicants from a file and parses them into a structured list."""
    applicants_in = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            first_name, last_name = parts[0], parts[1]
            gpa = float(parts[2])
            priorities = parts[3:]
            applicants_in.append((f"{first_name} {last_name}", gpa, priorities))
    return applicants_in

def process_applicants(app, n):
    """Processes applicants for each department based on their priorities and GPAs."""
    departments = {
        'Biotech' : [],
        'Chemistry': [],
        'Engineering': [],
        'Mathematics': [],
        'Physics': []
    }

    for priority in range(3):
        app.sort(key=lambda x: (-x[1], x[0]))

        remaining_applicants = []
        for name, gpa, priorities in app:
            chosen_department = priorities[priority]
            if len(departments[chosen_department]) < n:
                departments[chosen_department].append((name, gpa))
            else:
                remaining_applicants.append((name, gpa, priorities))
        app = remaining_applicants

    return departments

def print_departments(departments1):
    """Prints out the final accepted applicants for each department in the required format."""
    for department in sorted(departments1.keys()):
        print(department)

        accepted_applicants = sorted(departments1[department], key=lambda x: (-x[1], x[0]))
        for name, gpa, in accepted_applicants:
            print(f'{name} {gpa:.2f}')
        print()
total_num_applicants = int(input('Number of applicants: '))
# max_num_applicants = int(input('Maximum number of applicants: '))
applicants = read_applicants('applicants.txt')

# sorted_applicants = acceptance(total_num_applicants, max_num_applicants, applicants)
# print('Successful applicants:')
# print(*sorted_applicants, sep='\n')
departments = process_applicants(applicants, total_num_applicants)
print_departments(departments)