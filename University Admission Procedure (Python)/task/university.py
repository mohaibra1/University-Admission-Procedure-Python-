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
    app = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            first_name, last_name = parts[0], parts[1]
            scores = list(map(float, parts[2:6]))  # Convert the four scores to floats
            priorities = parts[6:]
            app.append((f"{first_name} {last_name}", scores, priorities))
    return app

def process_applicants(app, n):
    """Processes applicants for each department based on their priorities and scores."""
    departments1 = {
        'Biotech': [],
        'Chemistry': [],
        'Engineering': [],
        'Mathematics': [],
        'Physics': []
    }

    # Mapping departments to specific exam index
    department_exam_index = {
        'Physics': 0,
        'Chemistry': 1,
        'Mathematics': 2,
        'Engineering': 3,
        'Biotech': 1
    }

    # For each priority round (1st, 2nd, 3rd)
    for priority in range(3):
        # Sort applicants by relevant exam score and name
        app.sort(key=lambda x: (-x[1][department_exam_index[x[2][priority]]], x[0]))

        # Assign applicants based on the current priority
        remaining_applicants = []
        for name, scores, priorities in app:
            chosen_department = priorities[priority]
            relevant_score = scores[department_exam_index[chosen_department]]
            if len(departments1[chosen_department]) < n:
                departments1[chosen_department].append((name, relevant_score))
            else:
                remaining_applicants.append((name, scores, priorities))

        # Update applicants list with only those not yet accepted
        app = remaining_applicants

    return departments1


def print_departments(departments1):
    """Prints out the final accepted applicants for each department in the required format."""
    for department in sorted(departments.keys()):
        print(department)
        # Sort each department's accepted applicants by score descending, then by name ascending
        accepted_applicants = sorted(departments[department], key=lambda x: (-x[1], x[0]))
        for name, score in accepted_applicants:
            print(f"{name} {score:.1f}")
        print()

total_num_applicants = int(input('Number of applicants: '))
# max_num_applicants = int(input('Maximum number of applicants: '))
applicants = read_applicants('applicants.txt')

# sorted_applicants = acceptance(total_num_applicants, max_num_applicants, applicants)
# print('Successful applicants:')
# print(*sorted_applicants, sep='\n')
departments = process_applicants(applicants, total_num_applicants)
print_departments(departments)