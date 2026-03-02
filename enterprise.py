import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("\n---- ENTERPRISE RAG MEMORY GOVERNANCE SYSTEM ----\n")

policy_memory = {

"leave_policy": """
Employee Leave and Absence Management Policy

The organization believes that rest and personal time are essential
for employee wellbeing and productivity. Therefore, all full-time
employees are entitled to annual paid leave.

Each employee is eligible for 20 working days of paid leave every
calendar year. Leave may be used for vacation, personal commitments,
or health-related recovery.

Employees must submit leave requests through the HR management
portal at least three working days in advance. The request must
be approved by the reporting manager before the leave begins.

Emergency leave may be requested in urgent situations such as
medical emergencies, family emergencies, or unforeseen personal
events. The reporting manager has the authority to approve such
requests even if they are submitted on short notice.

Unused leave days may be carried forward to the next calendar year,
but only up to a maximum of ten days. Any remaining unused leave
beyond this limit will expire automatically.

Employees are expected to maintain clear communication with their
team members while planning leave so that project work continues
without interruption.
""",

"data_security_policy": """
Enterprise Data Security and Confidentiality Policy

The protection of company data is one of the highest priorities of
the organization. All employees are responsible for maintaining the
confidentiality and integrity of corporate information.

Employees must never share confidential company data with external
individuals or organizations without proper authorization.

All company devices including laptops, tablets, and mobile phones
must be protected using strong passwords and automatic screen locks.

Employees should only use company-approved software and secure
cloud storage platforms when handling company files.

Sensitive data such as financial information, employee records,
and customer databases must always be stored in encrypted systems.

Employees must immediately report any suspected data breach,
security vulnerability, or unauthorized system access to the
IT security team.

Failure to comply with data security guidelines may lead to
disciplinary action according to company policy.
""",

"remote_work_policy": """
Work From Home and Remote Work Policy

The organization supports flexible work arrangements to improve
employee productivity and work-life balance.

Employees may work remotely up to three days per week with prior
approval from their reporting manager.

During remote work days, employees must remain available online
during official working hours and must attend all scheduled
meetings and project discussions.

Employees are expected to maintain the same level of productivity
and responsibility as they would while working in the office.

Work progress should be updated daily using the organization's
project management system so that team members and supervisors
remain informed about ongoing tasks.

The company reserves the right to modify remote work permissions
based on project requirements or operational needs.
""",

"ai_usage_policy": """
Artificial Intelligence Usage and Responsible AI Policy

The organization encourages the responsible use of artificial
intelligence tools to improve productivity, research capability,
and innovation.

Employees may use AI tools for tasks such as documentation
assistance, code generation, knowledge summarization, and
data analysis.

However, employees must not input confidential company data
into public AI systems without prior authorization from the
data governance team.

All AI-generated outputs must be carefully reviewed and verified
before being used in official company documents or communications.

Employees are responsible for ensuring that AI-generated content
does not violate copyright laws, privacy regulations, or company
ethics policies.

The misuse of AI tools for unethical or illegal activities is
strictly prohibited.
"""
}


audit_log = []

def log_event(event):
    time = datetime.datetime.now()
    record = f"{time} : {event}"
    audit_log.append(record)


documents = list(policy_memory.values())
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

def retrieve(query):
    query_vector = vectorizer.transform([query])
    similarity = cosine_similarity(query_vector, tfidf_matrix)
    index = similarity.argmax()
    return documents[index]

def enterprise_rag(query):
    print("\nUser Query:", query)
    retrieved_policy = retrieve(query)
    print("\nRetrieved Policy:\n")
    print(retrieved_policy)
    log_event(f"Query executed: {query}")
    return retrieved_policy

def noise_injection_test():
    print("\nRunning Noise Injection Test...")
    noise = "asdf12345 !!! random text ####"
    keywords = ["policy", "employee", "data"]
    if not any(word in noise for word in keywords):
        print("Noise detected and rejected")
        log_event("Noise injection blocked")

def policy_filter(policy):
    banned_words = ["hack", "steal", "illegal", "attack"]
    for word in banned_words:
        if word in policy.lower():
            print("Unsafe policy detected")
            log_event("Policy rejected due to unsafe content")
            return False
    return True

def detect_conflict(new_policy):
    for existing in policy_memory.values():
        if "remote work not allowed" in new_policy.lower() and "remote" in existing.lower():
            print("Conflict detected with existing policy")
            log_event("Policy conflict detected")
            return True
    return False

def update_policy(name, new_policy):
    print("\nUpdating policy...")
    if detect_conflict(new_policy):
        print("Update rejected due to conflict")
        return
    if policy_filter(new_policy):
        policy_memory[name] = new_policy
        log_event(f"Policy '{name}' updated")
        print("Policy updated successfully")

def show_audit_log():
    print("\n---- MEMORY AUDIT LOG ----\n")
    for record in audit_log:
        print(record)

def run_tests():
    enterprise_rag("How many leave days do employees get")
    noise_injection_test()
    bad_policy = "Employees may hack company systems"
    policy_filter(bad_policy)
    conflict_policy = "Remote work not allowed for employees"
    detect_conflict(conflict_policy)
    new_leave_policy = """
                        Updated Leave Policy
                        Employees will now receive 25 days of annual leave.
                        Leave requests must be submitted at least five days in advance."""
    update_policy("leave_policy", new_leave_policy)
    show_audit_log()

if __name__ == "__main__":
    run_tests()
    while True:
        q = input("\nAsk policy question (type exit to stop): ")
        if q.lower() == "exit":
            break
        enterprise_rag(q)