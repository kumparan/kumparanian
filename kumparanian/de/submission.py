import os
import csv


def verify(submission_dir):
    """Verify the submission.
    - task_1_result.txt should have a single line of number
      representing the total sum of money from all account.
    - task_2_result.csv should have 2 columns: account_group and sum.
    - task_3_result.csv should have 2 columns: account_id and account_balance.
    - task_4_result.txt should have 2 lines which show the sum and
      ratio percentage of the richest.
    """
    # Task 1
    task_1_file = os.path.join(submission_dir, "task_1_result.txt")
    # Make sure the file is exists
    if not os.path.isfile(task_1_file):
        raise ValueError("{} is not exists".format(task_1_file))
    # Check the content
    with open(task_1_file, "r") as f:
        content = f.read().strip()
        lines = content.split("\n")
        assertion_err = "task_1_result.txt should contains a single line"
        assert len(lines) == 1, assertion_err
        assert content.isdigit(), "task_1_result.txt should contains a number"

    # Task 2
    task_2_file = os.path.join(submission_dir, "task_2_result.csv")
    # Make sure the file is exists
    if not os.path.isfile(task_2_file):
        raise ValueError("{} is not exists".format(task_2_file))
    # Check the content
    with open(task_2_file, "r") as f:
        rows = csv.DictReader(f)
        row = None
        for r in rows:
            row = r
            break
        acc_group = row.get("account_group", None)
        if acc_group is None:
            err_msg = "task_2_result.csv should contains account_group column"
            raise ValueError(err_msg)
        sum_col = row.get("sum", None)
        if sum_col is None:
            err_msg = "task_2_result.csv should contains sum column"
            raise ValueError(err_msg)

    # Task 3
    task_3_file = os.path.join(submission_dir, "task_3_result.csv")
    # Make sure the file is exists
    if not os.path.isfile(task_3_file):
        raise ValueError("{} is not exists".format(task_3_file))
    # Check the content
    with open(task_3_file, "r") as f:
        rows = csv.DictReader(f)
        row = None
        for r in rows:
            row = r
            break
        acc_group = row.get("account_id", None)
        if acc_group is None:
            err_msg = "task_3_result.csv should contains account_id column"
            raise ValueError(err_msg)
        sum_col = row.get("account_balance", None)
        if sum_col is None:
            err_msg = ("task_3_result.csv should contains account_balance "
                       "column")
            raise ValueError(err_msg)

    # Task 4
    task_4_file = os.path.join(submission_dir, "task_4_result.txt")
    # Make sure the file is exists
    if not os.path.isfile(task_4_file):
        raise ValueError("{} is not exists".format(task_4_file))
    # Check the content
    with open(task_4_file, "r") as f:
        content = f.read().strip()
        lines = content.split("\n")
        assertion_err = "task_4_result.txt should contains 2 lines"
        assert len(lines) == 2, assertion_err
        for line in lines:
            assert line.isdigit(), "task_4_result.txt should contains a number"


def evaluate(submission_dir, solution_dir):
    """Evaluate the results"""
    # Task 1
    task1 = True
    submission_path = os.path.join(submission_dir, "task_1_result.txt")
    solution_path = os.path.join(solution_dir, "task_1", "total_wealth.txt")
    with open(submission_path, "r") as su, open(solution_path, "r") as so:
        submission_value = int(su.read().strip())
        solution_value = int(so.read().strip())
        if submission_value != solution_value:
            task1 = False
    if task1:
        print("[kumparanian] Task 1: OK")
    else:
        print("[kumparanian] Task 1: Wrong")

    # Task 2
    task2 = True
    submission_path = os.path.join(submission_dir, "task_2_result.csv")
    solution_path = os.path.join(solution_dir, "task_2", "grouped_wealth.csv")
    with open(submission_path, "r") as su, open(solution_path, "r") as so:
        surows = csv.DictReader(su)
        sorows = csv.DictReader(so)
        for surow, sorow in zip(surows, sorows):
            if surow != sorow:
                task2 = False
                break
    if task2:
        print("[kumparanian] Task 2: OK")
    else:
        print("[kumparanian] Task 2: Wrong")

    # Task 3
    task3 = True
    submission_path = os.path.join(submission_dir, "task_3_result.csv")
    solution_path = os.path.join(solution_dir, "task_3", "richest.csv")
    with open(submission_path, "r") as su, open(solution_path, "r") as so:
        surows = csv.DictReader(su)
        sorows = csv.DictReader(so)
        for surow, sorow in zip(surows, sorows):
            if surow != sorow:
                task3 = False
                break
    if task3:
        print("[kumparanian] Task 3: OK")
    else:
        print("[kumparanian] Task 3: Wrong")

    # Task 4
    task4 = True
    submission_path = os.path.join(submission_dir, "task_4_result.txt")
    solution_path = os.path.join(solution_dir, "task_3", "richest_stats.txt")
    with open(submission_path, "r") as su, open(solution_path, "r") as so:
        submission_value = su.read().strip().split()
        solution_value = so.read().strip().split()
        if submission_value != solution_value:
            task4 = False
    if task4:
        print("[kumparanian] Task 4: OK")
    else:
        print("[kumparanian] Task 4: Wrong")
