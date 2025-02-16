import streamlit as st
from PIL import Image

# Toggle for language selection (True = English, False = Greek)
language_toggle = st.toggle("Switch to English", value=False)

# Define content in both languages
if language_toggle:
     language = "English"

     # Create layout with two columns
     col1, col2 = st.columns([3, 2])  # Adjust column width ratio if needed

     with col1:
        st.title("Cats vs Dogs")
        st.subheader("The eternal battle")
        st.write("Are you team purrs and toe beans or team wagging tails and puppy eyes? 🐾")
        st.subheader('Photos & Info')

     with col2:
        img = Image.open("main/Dog-and-Cat-Stress.png")
        st.image(img, width=1000)  # Adjust width as needed

    # radio button
    # first argument is the title of the radio button
    # second argument is the options for the radio button
     status = st.radio("Select a fur baby: ", ('Cat', 'Dog'))

    # conditional statement to print
    # Male if male is selected else print female
    # show the result using the success function
     if (status == 'Cat'):
        st.write("The cat (Felis catus), also referred to as the domestic cat, is a small domesticated carnivorous mammal. It is the only domesticated species of the family Felidae. Advances in archaeology and genetics have shown that the domestication of the cat occurred in the Near East around 7500 BC. It is commonly kept as a pet and farm cat, but also ranges freely as a feral cat avoiding human contact. ")
        # checkbox
        if st.checkbox("Show/Hide Image"):
            # display image
            img1 = Image.open(r"C:\Users\despoina.angelonidi\Documents\toy\cat-lying-down.jpg")
            st.image(img1, width=300)  # Adjust width as needed
        # selection box
        breed = st.selectbox("Breed: ", ['British Shorthair', 'Maine Coon', 'Sphynx cat','Persian cat','Siamese cat']) #options

        if breed=='British Shorthair':
            # print info about selected breed
            st.write("The British Shorthair is the pedigree version of the traditional British domestic cat, with a distinctively stocky body, thick coat, and broad face. The most familiar colour variant is the British Blue, with a solid grey-blue coat, pineapple eyes, and a medium-sized tail. The breed has also been bred in a wide range of other colours and patterns, including tabby and colourpoint.It is one of the most ancient cat breeds known. It remains the most popular pedigreed breed in its native country, as registered by the UK's Governing Council of the Cat Fancy (GCCF). A quarter of all kittens registered with the GCCF each year are British Shorthairs, making the British the most popular pedigree cat in the UK.[1]The breed's relatively calm temperament make it a frequent media star, notably as the inspiration for John Tenniel's famous illustration of the Cheshire Cat from Alice in Wonderland. ")

        elif breed=='Maine Coon':
            st.write("The Maine Coon is a large domesticated cat breed. One of the oldest natural breeds in North America, the breed originated in the U.S. state of Maine, where it is the official state cat.The Maine Coon is a large and social cat, commonly referred to as the gentle giant. The Maine Coon is predominantly known for its size and dense coat of fur which helps it survive in the harsh climate of Maine. The Maine Coon is often cited as having dog-like characteristics.")

        elif breed == 'Sphynx cat':
            st.write("The Sphynx cat (pronounced SFINKS, /ˈsfɪŋks/) also known as the Canadian Sphynx, is a breed of cat known for its lack of fur. Hairlessness in cats is a naturally occurring genetic mutation, and the Sphynx was developed through selective breeding of these animals, starting in the 1960s.[1]The skin has a texture of chamois leather,[2] as it has fine hairs, or the cat may be completely hairless. Whiskers may be present, either whole or broken, or may be totally absent. Per the breed standards, they have a somewhat wedge-shaped head with large eyes and ears, quite long legs and tail, and neat rounded paws. Their skin is the color that their fur would be, and all the usual cat markings (solid, point, van, tabby, tortie, etc.) may be found on the Sphynx cat's skin. Because they have no fur, Sphynx cats lose body heat more readily than coated cats, making them both warm to the touch and prone to seeking out warm places.")

        elif breed == 'Persian cat':
            st.write("The Persian cat, also known as the Persian Longhair, is a long-haired breed of cat characterised by a round face and short muzzle. The first documented ancestors of Persian cats might have been imported into Italy from Khorasan as early as around 1620, but this has not been proven. Instead, there is stronger evidence for a longhaired cat breed being exported from Afghanistan and Iran/Persia from the 19th century onwards. Persian cats have been widely recognised by the North-West European cat fancy since the 19th century, and after World War II by breeders from North America, Australia and New Zealand. Some cat fancier organisations' breed standards subsume the Himalayan and Exotic Shorthair as variants of this breed, while others generally treat them as separate breeds. The selective breeding carried out by breeders has allowed the development of a wide variety of coat colours, but has also led to the creation of increasingly flat-faced Persian cats. Favoured by fanciers, this head structure can bring with it several health problems. As is the case with the Siamese breed, there have been efforts by some breeders to preserve the older type of cat, the Traditional Persian, which has a more pronounced muzzle. Hereditary polycystic kidney disease (PKD) is prevalent in the breed, affecting almost half of the population in some countries. In 2021, Persian cats were ranked as the fourth-most popular cat breed in the world according to the Cat Fanciers' Association, an American international cat registry.")

        elif breed == 'Siamese cat':
            st.write("The Siamese cat is one of the first distinctly recognised breeds of Asian cat. It derives from the Wichianmat landrace. The Siamese cat is one of several varieties of cats native to Thailand (known as Siam before 1939). The original Siamese became one of the most popular breeds in Europe and North America in the 19th century.[1] Siamese cats have a distinctive colourpoint coat, resulting from a temperature-sensitive type of albinism.Distinct features like blue almond-shaped eyes, a triangular head shape, large ears, an elongated, slender, and muscular body, and various forms of point colouration characterise the modern-style Siamese. The modern-style Siamese's point-colouration resembles the old-style foundation stock. The old-style Siamese have a round head and body. They have been re-established by multiple registries as the Thai cat. Siamese and Thai cats are selectively bred and pedigreed in multiple cat fancier and breeder organisations. The terms Siamese or Thai are used for cats from this specific breed, which are by definition all purebred cats with a known and formally registered ancestry. ")

     else:
        st.write("The dog (Canis familiaris or Canis lupus familiaris) is a domesticated descendant of the gray wolf. Also called the domestic dog, it was selectively bred from an extinct population of wolves during the Late Pleistocene by hunter-gatherers. The dog was the first species to be domesticated by humans, over 14,000 years ago and before the development of agriculture. Experts estimate that due to their long association with humans, dogs have gained the ability to thrive on a starch-rich diet that would be inadequate for other canids.")
        if st.checkbox("Show/Hide Image"):
            img2 = Image.open(r"C:\Users\despoina.angelonidi\Documents\toy\dog-breed-temperaments-1240x640.jpg")
            st.image(img2, width=600)  # Adjust width as needed

            # selection box
        breed_dog = st.selectbox("Breed: ",['Azawakh', 'Labrador Retriever', 'Siberian Husky', 'Beagle', 'Dachshund'])  # options

        if breed_dog == 'Azawakh':
            # print info about selected breed
            st.write("The Azawakh is a breed of dog from West Africa. With ancient origins, it is raised throughout the Sahelian zone of Mali, Niger, and Burkina Faso. This region includes the Azawagh Valley for which the breed is named. While commonly associated with the nomadic Tuareg people, the dogs are also bred and owned by other ethnic groups, such as the Peulh, Bella, and Hausa. The Azawakh is more related to the Sloughi than it is to the Saluki.")
            img3 = Image.open(r"C:\Users\despoina.angelonidi\Documents\toy\Azawakh.jpg")
            st.image(img3, width=300)

        elif breed_dog == 'Labrador Retriever':
            st.write("The Labrador Retriever or simply Labrador is a British breed of retriever gun dog. It was developed in the United Kingdom from St. John's water dogs imported from the colony of Newfoundland (now a province of Canada), and was named after the Labrador region of that colony. It is among the most commonly kept dogs in several countries, particularly in the Western world.The Labrador is friendly, energetic, and playful.[2] It was bred as a sporting and hunting dog but is widely kept as a companion dog. It may also be trained as a guide or assistance dog, or for rescue or therapy work.[3]In the 1830s, the 10th Earl of Home and his nephews, the 5th Duke of Buccleuch and Lord John Scott,[4] imported progenitors of the breed from Newfoundland to Europe for use as gun dogs. Another early advocate of these Newfoundland fishing dogs was the 2nd Earl of Malmesbury, who bred them for their expertise in waterfowling.[4]During the 1880s, the 3rd Earl of Malmesbury, the 6th Duke of Buccleuch, and the 12th Earl of Home collaborated to develop and establish the Labrador Retriever breed. The dogs Buccleuch Avon and Buccleuch Ned, given by Malmesbury to Buccleuch, were mated with bitches carrying blood from those originally imported by the 5th Duke and the 10th Earl of Home. The offspring are the ancestors of all modern Labradors.[5]")

        elif breed_dog == 'Siberian Husky':
            st.write("The Siberian Husky is a breed of medium-sized working sled dog. The breed belongs to the Spitz genetic family. It is recognizable by its thickly furred double coat, erect triangular ears, and distinctive markings, and is smaller than the similar-looking Alaskan Malamute.Siberian Huskies originated in Northeast Asia where they are bred by the Chukchi people as well as the Koryak, Yukaghir and Kamchadal people of Siberia for sled pulling and companionship.[2][4] It is an active, energetic, resilient breed, whose ancestors lived in the extremely cold and harsh environment of the Siberian Arctic. William Goosak, a Russian fur trader, introduced them to Nome, Alaska, during the Nome Gold Rush, initially as sled dogs to work the mining fields and for expeditions through otherwise impassable terrain.[2] Today, the Siberian Husky is typically kept as a house pet, though they are still frequently used as sled dogs by competitive and recreational mushers.[5]")

        elif breed_dog == 'Beagle':
            st.write("The Beagle is a breed of small hound that is similar in appearance to the much larger foxhound. The beagle is a scent hound, developed primarily for hunting hare (beagling). Possessing a great sense of smell and superior tracking instincts, the beagle is the primary breed used as detection dogs for prohibited agricultural imports and foodstuffs in quarantine around the world. The beagle is intelligent but single-minded. It is a popular pet due to its size, good temper, and a lack of inherited health problems. Although beagle-type dogs have existed for over 2,000 years, the modern breed was developed in Great Britain around the 1830s from several breeds, including the Talbot Hound, the North Country Beagle, the Southern Hound, and possibly the Harrier.")

        elif breed_dog == 'Dachshund':
            st.write("The dachshund (UK: /ˈdækshʊnd, -ənd, -hʊnt/ DAKS-huund, -⁠ənd, -⁠huunt or US: /ˈdɑːkshʊnt, -hʊnd, -ənt/ DAHKS-huunt, -⁠huund, -⁠ənt;[1][2][3][4] German: 'badger dog'), also known as the wiener dog or sausage dog, badger dog and doxie, is a short-legged, long-bodied, hound-type dog breed. The dog may be smooth-haired, wire-haired, or long-haired, with varied coloration.The dachshund was bred to scent, chase, and flush out badgers and other burrow-dwelling animals. The miniature dachshund was bred to hunt small animals such as rabbits.[5]The dachshund was ranked 9th in registrations with the American Kennel Club in 2022.[6]")

else :
    # Create layout with two columns
    col3, col4 = st.columns([3, 2])  # Adjust column width ratio if needed

    with col3:
        st.title("Γάτες ή Σκύλοι;")
        st.subheader("Το αιώνιο δίλημμα")
        st.write("Προτιμάς τα γουργουριτά ή μήπως τις κουνιστές ουρές; 🐾")
        st.subheader('Φωτογραφίες και πληροφορίες')

    with col4:
        img = Image.open(r"C:\Users\despoina.angelonidi\Documents\toy\Dog-and-Cat-Stress.png")
        st.image(img, width=1000)

    status = st.radio("Επίλεξε την αγαπημένη σου χνουδόμπαλα: ", ('Γάτα', 'Σκύλος'))
    if (status == 'Γάτα'):
        st.write("Η γάτα (Felis catus – Αίλουρος η γαλή ή Felis silvestris catus) είναι ζώο που ανήκει στην οικογένεια των αιλουριδών. Πρόκειται για ένα από τα δημοφιλέστερα κατοικίδια ζώα και ίσως το μοναδικό οικόσιτο αιλουροειδές. Ζει στο περιβάλλον του ανθρώπου εδώ και τουλάχιστον 9.500 χρόνια.Δεινός θηρευτής, η γάτα κυνηγά πάνω από 1.000 είδη ζώων για τροφή. Μπορεί να εκπαιδευτεί ώστε να υπακούει σε ορισμένες απλές διαταγές, ενώ έχει διαπιστωθεί ότι μπορούν να μάθουν να χειρίζονται απλούς μηχανισμούς, όπως πόμολα πόρτας. Χρησιμοποιούν μια ποικιλία φωνών και ένα είδος γλώσσας του σώματος που τους χρησιμεύει στη μεταξύ τους επικοινωνία. Τα νιαουρίσματα, τα γουργουρίσματα και τα μουγκρίσματα είναι από τους πιο γνωστούς τρόπους επικοινωνίας.")
        # checkbox
        if st.checkbox("Εμφάνιση Εικόνας"):
            # display image
            img1 = Image.open(r"C:\Users\despoina.angelonidi\Documents\toy\cat-lying-down.jpg")
            st.image(img1, width=300)  # Adjust width as needed
        # selection box
        breed = st.selectbox("Ράτσα: ",
                             ['Βρετανική Κοντότριχη', 'Μέιν Κουν', 'Γάτα Σφιγξ', 'Γάτα Περσίας', 'Σιαμέζα Γάτα'])  # options

        if breed=='Βρετανική Κοντότριχη':
            # print info about selected breed
            st.write("Η Βρετανική Κοντότριχη είναι η καθαρόαιμη εκδοχή της παραδοσιακής βρετανικής οικόσιτης γάτας. Έχει γεροδεμένο σώμα, παχύ τρίχωμα και φαρδύ πρόσωπο. Η πιο γνωστή χρωματική ποικιλία είναι η Βρετανική Μπλε, με ομοιόμορφο γκρι-μπλε τρίχωμα, κεχριμπαρένια μάτια και μεσαίου μεγέθους ουρά. Η φυλή έχει εκτραφεί επίσης σε ποικιλία άλλων χρωμάτων και σχεδίων, συμπεριλαμβανομένων των ραβδωτών (tabby) και των colourpoint. Είναι μία από τις αρχαιότερες γνωστές φυλές γάτας και παραμένει η πιο δημοφιλής καθαρόαιμη φυλή στη Βρετανία, σύμφωνα με το Governing Council of the Cat Fancy (GCCF) του Ηνωμένου Βασιλείου.Το ένα τέταρτο όλων των γατιών που καταχωρούνται στο GCCF κάθε χρόνο είναι Βρετανικές Κοντότριχες, καθιστώντας τη φυλή την πιο δημοφιλή καθαρόαιμη γάτα στο Ηνωμένο Βασίλειο.Η σχετικά ήρεμη ιδιοσυγκρασία της φυλής την έχει κάνει διάσημη στα μέσα ενημέρωσης, με πιο γνωστή εμφάνιση την έμπνευση για την εικονογράφηση του Τσέσαϊρ Κατ (Cheshire Cat) από τον John Tenniel στο βιβλίο Η Αλίκη στη Χώρα των Θαυμάτων.")

        if breed=='Μέιν Κουν':
            # print info about selected breed
            st.write("Η Μέιν Κουν είναι αμερικανική ημιμακρύτριχη γάτα. Ως ξεχωριστή φυλή αναγνωρίστηκε για πρώτη φορά στο Μέιν, όπου τις είχαν σε μεγάλη εκτίμηση για τις κυνηγετικές τους ικανότητες. Με το πέρασμα των χρόνων αυτή η φυλή εξελίχθηκε σε μια στιβαρή γάτα, σχεδιασμένη να αντέχει τους σφοδρούς χειμώνες και τις εναλλαγές του καιρού της περιοχής. Οι Μέιν Κουν διακρίνονται ανάμεσα στις άλλες ράτσες για τον γλυκό τους χαρακτήρα, την καλοσυνάτη διάθεση και την εξυπνάδα τους.")

        if breed == 'Γάτα Σφιγξ':
            # print info about selected breed
            st.write("Η γάτα Σφίγγα (Sphynx, προφέρεται Σφινξ), γνωστή και ως Καναδική Σφίγγα, είναι μια φυλή γάτας που ξεχωρίζει για την έλλειψη τριχώματος. Η ατριχία στις γάτες είναι αποτέλεσμα μιας φυσικής γενετικής μετάλλαξης, και η φυλή Σφίγγα αναπτύχθηκε μέσα από επιλεκτική εκτροφή αυτών των γατών, ξεκινώντας από τη δεκαετία του 1960.Το δέρμα τους έχει την υφή του δέρματος σαμουά, καθώς διαθέτει πολύ λεπτές τρίχες, ή σε κάποιες περιπτώσεις μπορεί να είναι εντελώς άτριχο. Τα μουστάκια μπορεί να υπάρχουν ολόκληρα ή σπασμένα, ή να λείπουν εντελώς.Σύμφωνα με τα πρότυπα της φυλής, η Σφίγγα έχει σφηνοειδές κεφάλι, μεγάλα μάτια και αυτιά, μακριά πόδια και ουρά, και κομψά, στρογγυλεμένα πατουσάκια. Το χρώμα του δέρματός τους αντιστοιχεί στο χρώμα που θα είχε η γούνα τους και μπορεί να έχει όλα τα κλασικά μοτίβα των γατών, όπως μονόχρωμο, point, van, ριγέ (tabby) και ταρταρούγα (tortie).Λόγω της έλλειψης τριχώματος, οι γάτες Σφίγγα χάνουν θερμότητα πιο εύκολα από τις άλλες γάτες, γεγονός που τις κάνει να είναι ζεστές στην αφή αλλά και να αναζητούν συνεχώς ζεστά σημεία για να φωλιάσουν")

        if breed == 'Γάτα Περσίας':
            # print info about selected breed
            st.write("Η Περσική γάτα, γνωστή και ως Persian Longhair, είναι μια μακρύτριχη φυλή γάτας που ξεχωρίζει για το στρογγυλό πρόσωπο και το κοντό ρύγχος της.Οι πρώτοι καταγεγραμμένοι πρόγονοι των Περσικών γατών ίσως εισήχθησαν στην Ιταλία από το Χορασάν ήδη από το 1620, αλλά αυτό δεν έχει αποδειχθεί πλήρως. Αντίθετα, υπάρχουν ισχυρότερες ενδείξεις ότι μια φυλή μακρύτριχων γατών εξήχθη από το Αφγανιστάν και το Ιράν (Περσία) από τον 19ο αιώνα και μετά.Οι Περσικές γάτες αναγνωρίστηκαν ευρέως από τους Ευρωπαίους εκτροφείς της Βορειοδυτικής Ευρώπης τον 19ο αιώνα και μετά τον Β' Παγκόσμιο Πόλεμο, η εκτροφή τους εξαπλώθηκε στη Βόρεια Αμερική, την Αυστραλία και τη Νέα Ζηλανδία.Ορισμένοι οργανισμοί εκτροφέων θεωρούν τις φυλές Himalayan και Exotic Shorthair ως παραλλαγές της Περσικής, ενώ άλλοι τις αντιμετωπίζουν ως ξεχωριστές φυλές.Η επιλεκτική αναπαραγωγή από εκτροφείς οδήγησε στην ανάπτυξη μιας μεγάλης ποικιλίας χρωμάτων τριχώματος. Ωστόσο, αυτό είχε ως αποτέλεσμα τη δημιουργία όλο και πιο επίπεδων προσώπων στις Περσικές γάτες. Παρόλο που αυτή η εμφάνιση θεωρείται ελκυστική από πολλούς λάτρεις της φυλής, μπορεί να προκαλέσει διάφορα προβλήματα υγείας.Όπως συμβαίνει και με τη Σιαμέζικη γάτα, κάποιοι εκτροφείς προσπαθούν να διατηρήσουν τον πιο παραδοσιακό τύπο Περσικής γάτας, γνωστό ως Traditional Persian, που έχει πιο έντονο ρύγχος και λιγότερα αναπνευστικά προβλήματα. Ένα από τα σημαντικότερα προβλήματα της φυλής είναι η πολυκυστική νεφρική νόσος (PKD), η οποία επηρεάζει σχεδόν το 50% του πληθυσμού σε ορισμένες χώρες.Το 2021, οι Περσικές γάτες κατατάχθηκαν ως η τέταρτη πιο δημοφιλής φυλή γάτας στον κόσμο, σύμφωνα με την Cat Fanciers' Association, έναν διεθνή αμερικανικό οργανισμό καταγραφής γατών.")

        if breed == 'Σιαμέζα Γάτα':
            # print info about selected breed
            st.write("Η γάτα του Σιάμ ή Σιαμέζα γάτα είναι μια από της πιο αναγνωρισμένες φυλές της ανατολικής γάτας. Μία από τις πολλές ράτσες γάτας στην Ταϊλάνδη (παλαιότερα γνωστή ως Σιάμ), τον 20ο αιώνα, η σιαμέζα γάτα έγινε μια από τις πιο δημοφιλείς φυλές στην Ευρώπη και την Βόρεια Αμερική. Η σύγχρονη σιαμέζα γάτα χαρακτηρίζεται από τα μπλε αμυγδαλωτά μάτια, το τριγωνικό σχήμα του κεφαλιου της, τα μεγάλα μυτερά της αυτιά και το επίμηκες, λεπτό και μυώδες σώμα της. Το TICA (The international cat association) περιγράφει τη γάτα Σιαμ ως κοινωνικό, έξυπνο, παιχνιδιάρικο ζώο το οποίο συχνά συνεχίζει να απολαμβάνει το παιχνίδι και στην ενήλικη ζωή.")


    else:
        st.write("Ο σκύλος (Canis familiaris ή Canis lupus familiaris) είναι εξημερωμένος απόγονος του γκρίζου λύκου. Γνωστός και ως οικόσιτος σκύλος, προήλθε από επιλεκτική αναπαραγωγή μιας εξαφανισμένης πληθυσμιακής ομάδας λύκων κατά τη Ύστερη Πλειστόκαινο, από κυνηγούς-τροφοσυλλέκτες.Ο σκύλος ήταν το πρώτο είδος που εξημερώθηκε από τον άνθρωπο, περισσότερο από 14.000 χρόνια πριν, πολύ πριν από την ανάπτυξη της γεωργίας.Οι ειδικοί εκτιμούν ότι, λόγω της μακράς σχέσης τους με τον άνθρωπο, οι σκύλοι έχουν αναπτύξει την ικανότητα να επιβιώνουν με μια διατροφή πλούσια σε άμυλο, η οποία θα ήταν ακατάλληλη για άλλα είδη της οικογένειας των κυνίδων.")
        if st.checkbox("Εμφάνιση Εικόνας"):
            img2 = Image.open(r"C:\Users\despoina.angelonidi\Documents\toy\dog-breed-temperaments-1240x640.jpg")
            st.image(img2, width=600)  # Adjust width as needed

            # selection box
        breed_dog = st.selectbox("Ράτσα : ",['Αζαουάκ', 'Λαμπραντόρ Ριτρίβερ', 'Σιβηρικό Χάσκι', 'Μπίγκλ', 'Σκύλος Λουκάνικο'])  # options

        if breed_dog == 'Αζαουάκ':
            st.write("Ο Αζαουάκ (Azawakh) είναι μια φυλή σκύλου από τη Δυτική Αφρική. Με αρχαίες ρίζες, εκτρέφεται σε ολόκληρη τη σαχελιανή ζώνη του Μάλι, του Νίγηρα και της Μπουρκίνα Φάσο. Αυτή η περιοχή περιλαμβάνει την κοιλάδα Αζαγουάχ (Azawagh Valley), από όπου πήρε και το όνομά της η φυλή. Αν και συνδέεται κυρίως με τον νομαδικό λαό των Τουαρέγκ, οι σκύλοι Αζαουάκ εκτρέφονται και ανήκουν και σε άλλες εθνοτικές ομάδες, όπως οι Πέουλ (Peulh), Μπέλα (Bella) και Χάουσα (Hausa). Γενετικά, ο Αζαουάκ έχει περισσότερη συγγένεια με τον Σλούγκι (Sloughi) παρά με τον Σαλούκι (Saluki).")

        if breed_dog == 'Λαμπραντόρ Ριτρίβερ':
            st.write("Το Λαμπραντόρ Ριτρίβερ, ή απλά Λαμπραντόρ, είναι μια βρετανική φυλή σκύλου ριτρίβερ που αναπτύχθηκε στο Ηνωμένο Βασίλειο από τους σκύλους νερού του Αγίου Ιωάννη (St. John's water dogs), οι οποίοι είχαν εισαχθεί από την αποικία του Νιουφάουντλαντ (σημερινή επαρχία του Καναδά). Το όνομά του προέρχεται από την περιοχή Λαμπραντόρ αυτής της αποικίας.Σήμερα, το Λαμπραντόρ είναι μια από τις πιο δημοφιλείς ράτσες σε πολλές χώρες, ιδιαίτερα στον δυτικό κόσμο. Είναι ένας φιλικός, ενεργητικός και παιχνιδιάρης σκύλος. Αν και εκτράφηκε αρχικά ως κυνηγετικός και αθλητικός σκύλος, σήμερα είναι ιδιαίτερα αγαπητός ως σκύλος συντροφιάς. Επίσης, εκπαιδεύεται για να γίνει σκύλος-οδηγός, σκύλος βοήθειας, διάσωσης ή θεραπείας. Στη δεκαετία του 1830, ο 10ος Κόμης του Χομ (10th Earl of Home) και οι ανιψιοί του, ο 5ος Δούκας του Μπακλούχ (5th Duke of Buccleuch) και ο Λόρδος Τζον Σκοτ (Lord John Scott), εισήγαγαν προγόνους της φυλής από το Νιουφάουντλαντ στην Ευρώπη, για χρήση στο κυνήγι με όπλο.Ένας ακόμη υποστηρικτής των σκύλων αυτών ήταν ο 2ος Κόμης του Μάλσμπερι (2nd Earl of Malmesbury), ο οποίος τα εκτρέφει για το κυνήγι υδρόβιων πουλιών.Στη δεκαετία του 1880, ο 3ος Κόμης του Μάλσμπερι, ο 6ος Δούκας του Μπακλούχ και ο 12ος Κόμης του Χομ συνεργάστηκαν για να αναπτύξουν και να καθιερώσουν τη φυλή Λαμπραντόρ Ριτρίβερ. Οι σκύλοι Buccleuch Avon και Buccleuch Ned, που ο Μάλσμπερι χάρισε στον Μπακλούχ, διασταυρώθηκαν με θηλυκές σκύλες που είχαν καταγωγή από τους αρχικά εισαχθέντες σκύλους. Οι απόγονοί τους είναι οι πρόγονοι όλων των σύγχρονων Λαμπραντόρ Ριτρίβερ. ")

        if breed_dog == 'Σιβηρικό Χάσκι':
            st.write("Το Σιβηρικό Χάσκι (Siberian Husky) είναι μια μεσαίου μεγέθους φυλή σκύλων έλκηθρου. Ανήκει στη γενετική οικογένεια των Σπιτς, και ξεχωρίζει για το πυκνό διπλό τρίχωμά του, τα όρθια τριγωνικά αυτιά και τα χαρακτηριστικά σημάδια στο πρόσωπο. Είναι μικρότερος σε μέγεθος από τον Αλασκιανό Μαλαμούτ (Alaskan Malamute), με τον οποίο συχνά συγχέεται.Τα Σιβηρικά Χάσκι προέρχονται από τη Βορειοανατολική Ασία, όπου εκτρέφονταν από τους Τσούκτσι, καθώς και από άλλες Σιβηρικές φυλές όπως οι Κορυάκ, Γιουκαγίρ και Καμτσάνταλ. Χρησιμοποιούνταν κυρίως για την έλξη ελκήθρων και τη συντροφιά.Πρόκειται για μια δραστήρια, ενεργητική και ανθεκτική φυλή, οι πρόγονοι της οποίας επιβίωσαν στο σκληρό και ψυχρό περιβάλλον της Αρκτικής Σιβηρίας.")

        if breed_dog == 'Μπίγκλ':
            st.write("Το Μπιγκλ (αγγλικά: Beagle) είναι ράτσα σκύλου μεσαίου μεγέθους. Ανήκει στην κατηγορία των λαγωνικών (κυνηγόσκυλων), και έχει δηλαδή δημιουργηθεί αρχικά με σκοπό το κυνήγι λαγού. Χάρη στην πανίσχυρη αίσθηση της οσμής του, την οποία μόνο λίγες ράτσες σκύλου μπορούν να ανταγωνιστούν και παράλληλα το σπουδαίο ανιχνευτικό του ένστικτο, το Μπιγκλ χρησιμοποιείται στα τελωνεία πολλών χωρών για να ανιχνεύει απαγορευμένα προϊόντα ή ουσίες. Σωματικά το Μπιγκλ μπορεί να περιγραφεί ως γεροδεμένο και τυπικά ζυγίζει από 11 μέχρι 16 κιλά. Είναι πολύ ευφυές, αλλά πολλές φορές θρασύ, ανυπάκουο και μονόθυμο. Σήμερα είναι μία από τις πιο δημοφιλές ράτσες σκύλου κάτι το οποίο οφείλει στον καλό και ζωντανό του χαρακτήρα, στο βολικό του μέγεθος και στο γεγονός ότι -σε αντίθεση με τις περισσότερες σύγχρονες ράτσες- σπάνια έχει κληρονομικά προβλήματα υγείας. Δυστυχώς τα Μπιγκλ είναι από τις συνηθέστερες επιλογές σκύλων-πειραματόζωων ακριβώς λόγω της τεράστιας εμπιστοσύνης που έχουν στους ανθρώπους.")

        if breed_dog == 'Σκύλος Λουκάνικο':
            st.write(
                "Ο **Ντάτσχουντ (Dachshund)**, γνωστός επίσης ως **λουκάνικο σκύλος**, **σκύλος ασβοθήρας** ή **Doxie**, "
                "είναι μια φυλή σκύλου τύπου κυνηγόσκυλου με **κοντά πόδια** και **μακρύ σώμα**. "
                "Το όνομά του στα γερμανικά σημαίνει **σκύλος ασβών (badger dog)**, καθώς αρχικά εκτράφηκε για το "
                "**κυνήγι ασβών και άλλων ζώων που ζουν σε λαγούμια**.\n\n"

                " 🐾 Είδη τριχώματος:\n\n"
                "✔️ **Λείο (κοντότριχο)**\n\n"
                "✔️ **Συρμάτινο (τραχύτριχο)**\n\n"
                "✔️ **Μακρύτριχο**\n\n"

                "Επίσης, εμφανίζεται σε **ποικιλία χρωμάτων**.\n\n"

                "Ο **μικρόσωμος Ντάτσχουντ (miniature dachshund)** αναπτύχθηκε ειδικά για το "
                "**κυνήγι μικρότερων ζώων**, όπως οι **λαγοί**.\n\n"

                "📌 Σύμφωνα με το **American Kennel Club**, το **2022**, ο Ντάτσχουντ κατατάχθηκε "
                "στην **9η θέση** στις πιο δημοφιλείς φυλές σκύλων. 🐶🌭"
            )









