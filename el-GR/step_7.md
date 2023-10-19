## Αναβάθμισε το έργο σου

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Εάν έχεις χρόνο, μπορείς να αναβαθμίσεις το έργο σου.
</div>
<div>

![Παράδειγμα διαστημικού έργου με ζωές.](images/example1.png){:width="300px"}

</div>
</div>

Εδώ είναι μερικές ιδέες που μπορείς να δοκιμάσεις:

### Συμπερίλαβε μια ποικιλία εμποδίων
Μπορείς να προσθέσεις ποικιλία στα εμπόδια σου με μερικούς τρόπους:
 - Επίλεξε τυχαία ανάμεσα σε διάφορες εικόνες, emoji ή σε συναρτήσεις σχεδίασης εμποδίων
 - Προσάρμοσε τυχαία το χρώμα, το σχήμα ή το μέγεθος των εμποδίων αλλάζοντας τις παραμέτρους που τα σχεδιάζουν
 - Δημιούργησε κίνηση στο εμπόδιο προσθέτοντας περιστροφή, αλλαγή χρώματος ή κάποια άλλη οπτική διαφορά που θα ελέγχεται από το `frame_count`

### Πρόσθεσε μια συνθήκη νίκης
Μπορείς να κάνεις τους παίκτες να κερδίσουν το παιχνίδι με μερικούς τρόπους:
 - Επίτευξη νικηφόρου σκορ
 - Φτάνοντας σε ένα συγκεκριμένο επίπεδο του παιχνιδιού

Μόλις κερδίσουν, θα πρέπει να τους το πεις με κάποιο τρόπο — ίσως χρησιμοποιώντας `print()` ή `text()` και μετά να σταματήσεις το παιχνίδι.

### Δώσε στους παίκτες περισσότερες από μία ζωές
Πρόσθεσε ζωές στο παιχνίδι σου, για να επιτρέψεις στους παίκτες να επιβιώσουν σε μερικές συγκρούσεις. This is a little trickier than just doing `lives -= 1` every time they collide with something:
 - Ο παίκτης μπορεί να περάσει πολλά καρέ σε επαφή με ένα αντικείμενο, και έτσι να χάσει περισσότερες από μία ζωές σε μία μόνο σύγκρουση — αυτό φρόντισε να μην συμβεί
 - Θα χρειαστείς επίσης έναν τρόπο για να γνωρίζουν οι παίκτες πόσες ζωές τους έχουν απομείνει και ίσως κάποιο είδος προειδοποίησης που θα τους λέει πότε βρίσκονται στην τελευταία τους ζωή
 - Θα μπορούσες να προσθέσεις ένα αντικείμενο που, όταν ο παίκτης συγκρούεται με αυτό, του δίνει μια επιπλέον ζωή. Θυμήσου ότι θα χρειαστεί να τροποποιήσεις τον κανονικό κώδικα σύγκρουσης, ώστε να μην αφαιρεί μια ζωή ταυτόχρονα!

Each example project in the Introduction allows you to look at the code, get ideas, and see how they work.

Ρίξε μια ματιά σε μερικά έργα Don't collide που δημιουργήθηκαν από μέλη της κοινότητας στο [Don't collide - Community Library](https://wke.lt/w/s/KobNfx){:target="_blank"} του Raspberry Pi Foundation.

**Dodge asteroids**:
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/dodge-asteroids-example" width="600" height="700" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>

You can find the Dodge asteroids project [here](https://editor.raspberrypi.org/en/projects/dodge-asteroids-example){:target="_blank"}

Take a look at some Don't collide projects created by community members in the Raspberry Pi Foundation’s [Don't collide - Community library](https://wke.lt/w/s/KobNfx){:target="_blank"}.

--- save ---
