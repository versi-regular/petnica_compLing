# Dodelite varijabli recenica vrednost: "Mislim da je seminar lingvistike kul." Indeksacijom varijable recenica dodelite vrednost varijabli sintagma_1 vrednost "seminar lingvistike".

recenica = "Mislim da je seminar lingvistike kul."
sintagma_1 = recenica[13:32]

# Varijabli sintagma_2 takođe dodelite vrednost "seminar lingvistike", ali ovoga puta koristeći metodu .split(), indeksaciju i operaciju konkatenacije elemenata liste. Tip varijable sintagma_2 na kraju treba da bude niska.

# Rešenje 1
reci = recenica.split()
prva_rec = reci[3]
druga_rec = reci[4]
sintagma_2 = prva_rec + druga_rec

# Rešenje 2
reci = recenica.split()
dve_reci = reci[3:5]
sintagma_2 = dve_reci[0] + dve_reci[1]

# Rešenje 3
reci = recenica.split()
sintagma_2 = reci[3] + reci[4]

# Rešenje 4 (samo za hrabre)
sintagma_2 = " ".join(recenica.split()[3:5]) # https://www.tutorialspoint.com/python/string_join.htm
