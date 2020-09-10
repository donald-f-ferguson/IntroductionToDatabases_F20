import csv
import time

tsv_data_dir = "../../../Data/IMDB/TSVFormat/"
name_basics_fn = "name_basics.tsv"
title_basics_fn = "title_basics.tsv"
title_principals_fn = "title_principals.tsv"


def load_csv_file(fn, delimiter="\t", quoting=csv.QUOTE_NONE):
    """
    Reads a CSV file and returns a list of dictionaries representing each row.

    :param fn: Fully qualified path to the file.
    :param delimiter: Field delimiter.
    :param quoting: Quoting value for strings.
    :return: Array of OrderedDict representing rows in file.
    """

    result = []

    with open(fn, "r") as in_file:

        # Create a DictReader with the options passed into this function.
        csv_rdr = csv.DictReader(in_file, delimiter=delimiter, quoting=quoting)
        for r in csv_rdr:
            result.append(dict(r))

    return result


def find_by_field(csv_table, field_name, value):

    result = []

    for r in csv_table:
        test_v = r.get(field_name, None)
        if test_v == value:
            result.append(r)

    return result


def find_person(name=None, id=None):

    fn = tsv_data_dir + name_basics_fn
    tbl = load_csv_file(fn)

    if name is None and id is None:
        raise ValueError("Must pass one non-null parameter.")

    if id is not None:
        field = 'nconst'
        v = id
    else:
        field = 'primaryName'
        v = name

    result = find_by_field(tbl, field, v)
    return result


def t1():

    name = "Tom Hanks"
    id = 'nm0000158'

    result = find_person(name=name)
    print("t1 result 1 = ", result)
    result = find_person(id=id)
    print("t1 result 2 = ", result)


def t2():

    name = "Tom Hanks"
    print("Finding all co_principals for ", name)
    print("Loading names_basics table")

    start_total_time = time.time()

    load1_start_time = time.time()
    names_tbl = load_csv_file(tsv_data_dir + name_basics_fn)
    load1_end_time = time.time()
    print("Loaded ", len(names_tbl), "rows in ", load1_end_time-load1_start_time, "seconds.")

    print("Starting lookup by name.")
    lookup1_start_time = time.time()
    p = find_by_field(names_tbl, "primaryName", name)
    lookup1_end_time = time.time()

    print("names_basics lookup returned ", p[0])
    print("Lookup time was ", lookup1_end_time-lookup1_start_time)

    nconst = p[0].get("nconst", None)

    print("Starting load of titles_principles table.")
    load2_start_time = time.time()
    titles_principals_tbl = load_csv_file(tsv_data_dir + title_principals_fn)
    load2_end_time = time.time()
    print("Loaded ", len(titles_principals_tbl), "rows.")
    print("Load time = ", load2_end_time-load2_start_time)

    print("Starting lookup for titles for ", nconst)
    lookup2_start_time = time.time()
    all_titles = find_by_field(titles_principals_tbl, "nconst", nconst)
    lookup2_end_time = time.time()
    print("Look titles elapsed time = ", lookup2_end_time - lookup2_start_time)
    print("Lookup returned ", len(all_titles), "titles.")

    all_co_artists = []
    for tt in all_titles:
        tc = tt.get("tconst", None)
        print("Looking up nconsts for tconst = ", tc)
        lookup_t_start_time = time.time()
        current_co_artists = find_by_field(titles_principals_tbl, "tconst", tc)
        lookup_t_end_time = time.time()
        print("Found ", len(current_co_artists), "co artists.")
        print("Lookup time = ", lookup_t_end_time-lookup_t_start_time)
        all_co_artists.extend(current_co_artists)

    total_end_time = time.time()

    print("All lookups done, found ", len(all_co_artists), "co artists.")
    print("Total time = ", total_end_time-start_total_time)


def t_all():
    #t1()
    t2()


t_all()




