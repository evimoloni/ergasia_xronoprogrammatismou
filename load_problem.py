import structure as st  # Κάνουμε import το βοηθητικό αρχείο
# structure.py το οποίο περιλαμβάνει το dictionary με όνομα students
# και το Graph με όνομα graph


def load_problem(filename):
    """
    Συνάρτηση load_problem η οποία δέχεται ως όρισμα ότι εισήχθει από
    τον χρήστη στην main ύστερα από το πάτημα της 1ης επιλογής.
    """
    st.init()
    sid = 1
    students = 0

    file = open(filename, 'r')  # Κάνουμε open το αρχείο που δόθηκε σαν όρισμα
    while(True):
        line = file.readline()  # Διαβάζουμε κάθε γραμμή του αρχείου αυτού
        students += 1   # Σε κάθε διάβασμα γραμμής αυξάνουμε τη μεταβλητή students
        # Για να βρούμε πόσοι είναι συνολικά οι φοιτητές

        if(line):  # Ελέγχουμε κάθε γραμμή που διαβάζεται
            exams = [int(x) for x in line.split(' ')[:-1]]  # Κάθε γραμμή που διαβάζεται
            # την μετατρέπει σε λίστα με περιεχόμενο τα μαθήματα ου κάθε φοιτητή.
            for exam in exams:  # Διατρέχει την κάθε λίστα η οποία δημιουργήθηκε παραπάνω
                """
                Το αποτέλεσμα αυτού του for είναι ότι εισάγει στο dictionary students
                του αρχείου structure.py ως key το μάθημα και ως values τους φοιτητές
                οι οποίοι το έχουνε επιλέξει.
                """
                try:
                    """ Τοποθέτηση των μαθημάτων στο dictionary του αρχείου
                    structure.py ως key και προσθήκη ως values του αριθμού του
                    φοιτητή. Αρχικά ο φοιτητής είναι ο νούμερο 1 και ύστερα το
                    sid αυξάνεται οπότε στο επόμενο run μπαίνει value το 2. """
                    st.students[exam].append(sid)  # Κάνει προσάρτιση του αριθμού
                    # του φοιτητή εφόσον το key του μαθήματος προυπάρχει
                except KeyError:
                    st.students[exam] = [sid]  # Δημιουργεί εφόσον δεν υπάρχει
                    # στο dictionary students key με το όνομα του μαθήματος και
                    # τοποθετεί ως αρχικό value τον αριθμό sid του φοιτητή
            sid += 1
        else:
            break


    len_exams = len(st.students)  # Βρίσκουμε το μέγεθος του dictionary students.
    # Δηλαδή ουσιαστικά το πόσα είναι τα keys οπότε επειδή τα keys είναι τα μαθήματα
    # μας επιστρέφεται το σύνολο μαθημάτων

    eggrafes = sum(map(len, st.students.values()))  # Υπολογισμός των εγγραφών
    # Επιστροφή του συνόλου των εγγραφών. Δηλαδή επιστροφή του συνόλου των μαθημάτων
    # που έχουν επιλέξει όλοι οι φοιτητές.

    collisions = 0

    """
    Για κάθε key στο dictionary students προσθέτει ένα node στο
    αντικείμενο graph του structure.py
    """
    for i in st.students:
        st.graph.add_node(i)

    """
    Διατρέχει το dictionary students με διπλή for και αν βρει κοινό στοιχείο
    σε λίστα διαφορετικών key τα προσθέτει μέσω add_edge στο αντικείμενο graph
    """
    for i in st.students:
        for j in st.students:
            if i == j:
                collisions += 1
            else:
                if set(st.students[i]) & set(st.students[j]):
                    collisions += 1
                    st.graph.add_edge(i, j)

    print("-"*10)
    print("DENSITY")
    print(collisions/len_exams**2)
    print("-"*10)
    print("EXAMS")
    print(len_exams)
    print("-"*10)
    print("STUDENTS")
    print(students)
    print("-"*10)
    print("EGGRAFES")
    print(eggrafes)
