import argparse
import pandas as pd

string_nodes = ""


def make_node(person):
    "Makes a node in DOT Format"
    # Arunachalam[label="Arunachalam",style=filled,fillcolor=lightblue];"

    ID = person.get('ID')
    PERSON = person.get('PERSON')
    GENDER = person.get('GENDER')
    if GENDER != "F":
        color = "lightskyblue"
    else:
        color = 'lightpink'

    format_string = "\t{0}[label=\"{1}\",style=filled,fillcolor={2}];\r\n".format(ID, PERSON, color)
    return format_string


def formatDOB_DOD(PERSON, DOB, DOD):
    if str(DOB) == "nan" and str(DOD) == "nan":
        label = PERSON
    elif str(DOD) == "nan":
        label = PERSON + "\\n" + DOB
    elif str(DOB) == "nan":
        label = PERSON + "\\n" + "NA" + "-" + DOD
    else:
        label = PERSON + "\\n" + DOB + " - " + DOD
    return label


def notes(s_notes):
    if str(s_notes) == 'nan':
        return ""
    else:
        return s_notes


def find_relation(node):
    "Find Spouse(s) and Child(ren)"


def readCSV(ancestor_id, input):
    "Read CSV here"
    df = pd.read_csv(input)
    family_list = df.to_dict('records')
    return find_ancestor(int(ancestor_id), family_list)


def find_ancestor(ancestor_id, family_list):
    filtered_dict = [d for d in family_list if d["ID"] in [ancestor_id]]
    # print(filtered_dict)
    for person in filtered_dict:
        global string_nodes
        string_nodes += make_node(person)
    find_spouses(ancestor_id, family_list)
    # for person in family_list:
    #     nodes += make_node(person)
    # return nodes


def find_spouses(current_node_id, family_list):
    filtered_dict = [d for d in family_list if d["SPOUSE"] in [current_node_id]]
    # print(filtered_dict)
    for person in filtered_dict:
        global string_nodes
        string_nodes += make_node(person)
        spouse_id = person.get("ID")
        string_nodes += "\n\t{\n\t\trank=same;\n\t\t" + str(current_node_id) + " -> h" + str(
            spouse_id) + " -> " + str(spouse_id) + ";\n\t\th" + str(
            spouse_id) + "[shape=circle,label=\"\",height=0.01,width=0.01];\n\t}\n\n"
        find_children(spouse_id, family_list)


def find_children(current_node_id, family_list):
    filtered_dict = [d for d in family_list if d["CHILD"] in [current_node_id]]
    # print(filtered_dict)
    # string_parent_child = "h_" + str(current_node_id) + "a -> "
    # string_child_union_nodes = "h_" + str(current_node_id) + "a" + \ "[shape=circle,label=\"\",height=0.01,width=0.01];\n\t\t"
    string_parent_child = ""
    string_child_union_nodes = ""
    global string_nodes
    if (len(filtered_dict) != 0):
        # string_nodes += "\th" + str(current_node_id) + " -> " + "h_" + str(current_node_id) + "a" + ";\n"
        for person in filtered_dict:
            string_parent_child += "h" + str(current_node_id) + "_" + str(person.get("ID")) + " -> "
            string_child_union_nodes += "h" + str(current_node_id) + "_" + str(
                person.get("ID")) + "[shape=circle,label=\"\",height=0.01,width=0.01];\n\t\t"
        string_nodes += "\t{\n\t\trank = same;\n\t\t" \
                        + string_parent_child[0:-4] + \
                        ";\n\t\t" + string_child_union_nodes + "\n\t}\n"
    for person in filtered_dict:
        if (person == filtered_dict[0]):
            string_nodes += "\th" + str(current_node_id) + " -> h" + str(current_node_id) + "_" + str(
                person.get("ID")) + ";\n\t"
        string_nodes += make_node(person)
        child_node_id = person.get("ID")
        string_nodes += "\th" + str(current_node_id) + "_" + str(child_node_id) + " -> " + str(child_node_id) + ";\n\t"
        find_spouses(child_node_id, family_list)
        find_children(child_node_id, family_list)


def main():
    "Entry point of the program when called as a script."

    parser = argparse.ArgumentParser(description=
                                     'Generates a family tree graph from a csv')
    parser.add_argument('-a', dest='ancestor_id',
                        help='Enter Ancestor ID from the csv')
    parser.add_argument('input', metavar='INPUTFILE', default='KumaraguruFamily.csv',
                        help='File Path of the formatted csv')
    args = parser.parse_args()

    dotText = "digraph {\n\tgraph [rankdir=LR, splines=ortho];\n\tnode [shape=plaintext, fontname=tahoma];\n\tedge [dir=none];\n\n"
    readCSV(args.ancestor_id, args.input)
    dotText += string_nodes + "\r\n}"
    print(dotText)


if __name__ == '__main__':
    main()
