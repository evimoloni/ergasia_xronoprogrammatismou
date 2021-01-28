import structure as st  # Κάνουμε import το βοηθητικό αρχείο
# structure.py το οποίο περιλαμβάνει το dictionary με όνομα students
# και το Graph με όνομα graph
import networkx as nx  # Κάνουμε import το package networkx
from load_problem import load_problem


def solve_problem(filename):
    """
    H συνάρτηση αυτή επιλύει το αρχείο stu το οποίο του
    υποδεικνύουμε.
    Στην μεταβλητή greedy αποθηκεύουμε το αποτέλεσμα
    του coloring.greedy_color σύμφωνα με τις οδηγίες
    από το site του networkx.
    Το αποτέλεσμα του coloring είναι ένα dictionary το
    οποίο έχει ως key την εξέταση και ως value την περίοδο.
    """
    greedy = nx.coloring.greedy_color(
        st.graph, strategy=nx.coloring.strategy_saturation_largest_first)


    """
    Διατρέχει το dictionary greedy το τελικό dictionary
    που επιστρέφεται περιλαμβάνει ως key την περίοδο
    και ως values τις εξετάσεις των μαθημάτων.
    """
    period_exams = {}
    for exam in greedy:
        period = greedy[exam]
        try:
            period_exams[period].append(exam)
        except KeyError:
            period_exams[period] = [exam]

    # print(period_exams)

    """
    Δημιουργούμε αρχείο που έχει το όνομα του εκάστοτε
    filename και προσθέτουμε ως κατάληξη .sol
    Διατρέχει το dictionary period_exams και εξάγει σε
    αρχείο τις εξής δύο στήλες. Πρώτη στήλη περιλαμβάνει
    το μάθημα και δεύτερη στήλη περιλαμβάνει την περίοδο
    που ορίστηκε.
    """
    with open(filename[0:8]+'.sol', 'w') as f:
        for key in period_exams:
            for items in period_exams[key]:
                f.write('{}\t{}\n'.format(items, key))
    cost(period_exams)


def cost(period_exams):
    """
    Συνάρτηση η οποία μας επιστρέφει το κόστος
    Διατρέχουμε τα δύο dictionaries period_exams
    και st.students που υπάρχει στο structure.py
    και αποθηκεύουμε τα αποτελέσματα σε νέο dictionary
    με όνομα student_periods.
    To dictionary έχει κλειδί τον κάθε φοιτητή και ως
    values τις περιόδους που θα συμμετάσχουν.
    """
    student_periods = {}
    for aperiod in period_exams:        # Διατρέχουμε τα keys
        for e in period_exams[aperiod]: # Διατρέχουμε τα values
            for s in st.students[e]:    # Διατρέχουμε τα values
                                        # μέσω των values του period_exams
                try:
                    student_periods[s].append(aperiod)
                except KeyError:
                    student_periods[s] = [aperiod]

    numofstudents = len(student_periods) # Τον αριθμό των μαθητών


    """
    Διατρέχουμε με την for το dictionary student_periods. Αποθηκεύουμε σε λίστα
    ονόματι mycal τα σορταρισμένα values του key student_periods[s]

    Ελέγχει αν η απόσταση των περιόδων που δίνει ο φοιτητής είναι στο εύρος 6
    Κάνει κλήση της συνάρτησης costoftwo και προσθέτει τον αριθμό που επιστρέφεται
    στη μεταβλητή cost
    """
    cost = 0
    for s in student_periods: # Διατρέχει τα keys του student_periods
        mycal = sorted(student_periods[s]) # Λίστα που περιλαμβάνει
                        # τις περιόδους που θα δώσει ο κάθε φοιητής
        # print("My cal")
        # print(mycal)
        for (i, eachexam) in enumerate(sorted(mycal)): # Επιστρέφει διατεταγμένα
                                # από 0 και πάνω σε αντιστοιχία της κάθε περιόδου
            for j in range(i+1, i+6): # Για κάθε j σε εύρος έως 6 μονάδες
                if j < len(mycal): # Αν το j μικρότερο του μήκους λίστας mycal
                    cost += costoftwo(mycal[i], mycal[j]) # Κλήση της συνάρητησης
                                            # και προσθήκη τιμής. 0 ή αντίστοιχο κόστος
    print("-"*10)
    print("COST:")
    print(cost/numofstudents)
    print("-"*10)


def costoftwo(exam1, exam2):
    """
    Εάν η απόσταση είναι λιγότερο από πέντε επέστρεψε
    τα αντίστοιχα κόστη.
    Το κόστος καθορίζεται αναλόγως την απόσταση. Απόσταση
    ένα έχει κόστος 16, απόσταση 2 έχει κόστος 8 κ.λ.π
    """
    d = exam2-exam1
    if d > 5:
        return(0)
    else:
        return([16, 8, 4, 2, 1][d-1])

def mass_solve():
    """ Η mass_solve είναι μία συνάρτηση η οποία φορτώνει και λύνει
    το πρόβλημα για καθένα από τα περιεχόμενα της λίστας filename.
    Δηλαδή για καθένα από τα 13 αρχεία. """
    fileNames = ["car-f-92.stu",
                 "car-s-91.stu",
                 "ear-f-83.stu",
                 "hec-s-92.stu",
                 "kfu-s-93.stu",
                 "lse-f-91.stu",
                 "pur-s-93.stu",
                 "rye-s-93.stu",
                 "sta-f-83.stu",
                 "tre-s-92.stu",
                 "uta-s-92.stu",
                 "ute-s-92.stu",
                 "yor-f-83.stu"]

    '''
    Σε κάθε run της for γίνεται η αρχικοποίηση στο αρχείο structure.py
    φορτώνονται μέσω του load_problem στο dictionary και στο Graph
    τα στοιχεία του αντίστοιχουπροβλήματος και αυτά τα στοιχεία
    χρησιμοποιούνται από το solve_problem για την επίλυση.
    '''
    for x in range(len(fileNames)): # Η for τρέχει τόσες φορές όσο το length
                                    # της λίστας fileNames
        st.init()
        load_problem(fileNames[x])
        solve_problem(fileNames[x])
