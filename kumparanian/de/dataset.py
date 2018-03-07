import os
import multiprocessing as mp
import numpy as np
import hashlib


def generate_partition(random_seed, output_file):
    """Generate partition given random seed and output file """
    print("[kumparanian]: Generating {} ...".format(output_file))

    # Set random seed to get a consistent output
    hex_digest = hashlib.sha1(random_seed.encode("utf-8")).hexdigest()
    random_seed_int = int(hex_digest, 16) % (2**32)
    np.random.seed(random_seed_int)

    # Create the output directory if not exist
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)

    # Generating the number
    m_val = 25000
    max_data = 6270700  # Will roughly generate 100MB of data

    # Using pareto distribution to represent wealth distribution
    num_list = (np.random.pareto(1.3, max_data) * m_val).astype(int)

    # Generating id
    max_id_int = 2**40-1
    random_ids = np.random.randint(low=0,
                                   high=max_id_int,
                                   size=max_data,
                                   dtype=np.int64)
    id_list = np.unique(random_ids)
    # Generating the pair of id and number
    max_data = min(len(id_list), max_data)
    rows = ["%010x,%d" % (id_list[i], num_list[i]) for i in range(0, max_data)]
    # Writing the result into output_file
    header = "account_id,account_balance"
    output = open(output_file, "w")
    output.write(header+"\n")
    output.write("\n".join(rows))
    output.close()
    print("[kumparanian]: Generating {} ... DONE".format(output_file))


def generate_data(candidate_name, output_dir, num_files, num_workers):
    """Generate assesment data given candidate_name and output_dir """
    random_seed_template = "{id}_{{num:02d}}".format(id=candidate_name)
    output_template = "{dir}/{id}_{{num:02d}}.csv".format(dir=output_dir,
                                                          id=candidate_name)
    # Generating NUM_FILES files that each have size of 100mb
    # We generate in parallel to speed up
    # We use up to 4 workers in parallel
    with mp.Pool(processes=num_workers) as pool:
        for i in range(0, num_files):
            random_seed = random_seed_template.format(num=i)
            output_file = output_template.format(num=i)
            pool.apply_async(generate_partition, (random_seed, output_file))
        pool.close()
        pool.join()
