import re
import pandas as pd


def find_good_names(excel_file, col_name, out_file):
    decoms = pd.read_excel(excel_file)
    print(decoms)
    good_names = []
    bad_names = []
    for ind, row in decoms.iterrows():
        # iterrows returns (index, values)
        print(row[col_name], end=" ")
        if re.search(r'\b[A-Z0-9]{11}-?[A-Z0-9]{,8}\b', row[col_name]):
            print("VALID DEVICE NAME!")
            good_names.append(pd.DataFrame([row]))
        else:
            print("yo joe, this is not working for me")
            # append non-valid device names to list
            bad_names.append(pd.DataFrame([row]))
    print("\nTHESE ARE FAILING THE NAME VALIDATION CHECK!\n")
    print(bad_names)
    passing_names = pd.concat(good_names)
    failed_names = pd.concat(bad_names)
    print("\nALL OF THE FAILED NAMES\n")
    print(failed_names)
    with pd.ExcelWriter(out_file) as writer:
        failed_names.to_excel(writer, sheet_name="BAD NAMES")
        passing_names.to_excel(writer, sheet_name="GOOD NAMES")


def valid_project(xl_file, xl2_file):
    # Opens xl_file, reads sheet "GOOD NAMES", iterates and checks for name in other xl2_file
    dev_names = pd.read_excel(xl_file, sheet_name="GOOD NAMES")
    print(dev_names)
    project = pd.read_excel(xl2_file)
    for ind, row in dev_names.iterrows():
        print(f"Verifying {row['NODENAME']} for file")
        if project["DEVICE"].str.contains(row["NODENAME"]).any():
            print(f"{row['NODENAME']} is valid!")
        else:
            print(f"{row['NODENAME']} is not valid!")


if __name__ == "__main__":
    # excel_file = "Example of DB of not completed Tasks.xlsx"
    # find_good_names(excel_file, 'DEVICES', "Devices needing renamed.xls")
    #excel_file = "Example Possible decom.xlsx"
    #find_good_names(excel_file, 'NODENAME', "Nodenames.xls")
    valid_project("Nodenames.xls", "Example of DB of not completed Tasks.xlsx")
