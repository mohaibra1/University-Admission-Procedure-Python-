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
    applicants = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            first_name, last_name = parts[0], parts[1]
            scores = list(map(float, parts[2:6]))  # Convert the four scores to floats
            priorities = parts[6:]
            applicants.append((f"{first_name} {last_name}", scores, priorities))
    return applicants

def get_department_score(department, scores):
    """Returns the relevant score or mean score for a department."""
    department_exam_indices = {
        'Physics': [0, 2],         # Physics and Math
        'Chemistry': [1],          # Chemistry
        'Mathematics': [2],        # Math
        'Engineering': [3, 2],     # Computer Science and Math
        'Biotech': [1, 0]          # Chemistry and Physics
    }
    exams = department_exam_indices[department]
    return sum(scores[i] for i in exams) / len(exams)


def process_applicants(applicants, n):
    """Processes applicants for each department based on their priorities and scores."""
    departments = {
        'Biotech': [],
        'Chemistry': [],
        'Engineering': [],
        'Mathematics': [],
        'Physics': []
    }

    # For each priority round (1st, 2nd, 3rd)
    for priority in range(3):
        # Sort applicants by relevant score and name
        applicants.sort(
            key=lambda x: (-get_department_score(x[2][priority], x[1]), x[0])
        )

        # Assign applicants based on the current priority
        remaining_applicants = []
        for name, scores, priorities in applicants:
            chosen_department = priorities[priority]
            relevant_score = get_department_score(chosen_department, scores)
            if len(departments[chosen_department]) < n:
                departments[chosen_department].append((name, relevant_score))
            else:
                remaining_applicants.append((name, scores, priorities))

        # Update applicants list with only those not yet accepted
        applicants = remaining_applicants

    return departments

def write_departments_to_files(departments):
    """Writes the final accepted applicants for each department to separate files."""
    for department, accepted_applicants in departments.items():
        # Sort each department's accepted applicants by score descending, then by name ascending
        accepted_applicants = sorted(accepted_applicants, key=lambda x: (-x[1], x[0]))
        with open(f"{department.lower()}.txt", 'w') as file:
            for name, score in accepted_applicants:
                file.write(f"{name} {score:.1f}\n")


total_num_applicants = int(input('Number of applicants: '))
# max_num_applicants = int(input('Maximum number of applicants: '))
app = read_applicants('applicants.txt')

# sorted_applicants = acceptance(total_num_applicants, max_num_applicants, applicants)
# print('Successful applicants:')
# print(*sorted_applicants, sep='\n')
departments1 = process_applicants(app, total_num_applicants)
write_departments_to_files(departments1)