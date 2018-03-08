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
