##Sentence No. 16007 - fr-ud-dev_00022
 Il a fait partie de groupes musicaux comme Los Abuelos de la Nada et Los Rodríguez.
###Existing MWEs: 
1- **fait partie** (ID)
###Identified MWEs: 
1- **fait partie** ()

0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Il ,.. ]
1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Il]   -|||- [a ,.. ]
2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [a ,.. ]
3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[a]   -|||- [fait ,.. ]
4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [fait ,.. ]
5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[fait]   -|||- [partie ,.. ]
6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[fait, partie]   -|||- [de ,.. ]
7- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[[fait, partie]]   -|||- [de ,.. ]
8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [groupes ,.. ]
10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [groupes ,.. ]
11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[groupes]   -|||- [musicaux ,.. ]
12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [musicaux ,.. ]
13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[musicaux]   -|||- [comme ,.. ]
14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [comme ,.. ]
15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[comme]   -|||- [Los ,.. ]
16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Los ,.. ]
17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Los]   -|||- [Abuelos ,.. ]
18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Abuelos ,.. ]
19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Abuelos]   -|||- [de ,.. ]
20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [la ,.. ]
22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [la ,.. ]
23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[la]   -|||- [Nada ,.. ]
24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Nada ,.. ]
25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Nada]   -|||- [et ,.. ]
26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [et ,.. ]
27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[et]   -|||- [Los ,.. ]
28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Los ,.. ]
29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Los]   -|||- [Rodríguez ,.. ]
30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Rodríguez ,.. ]
31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Rodríguez]   -|||- [.]
32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [.]
33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[.]   -|||- [ ]
34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [ ]

###Features: 
0- 0 : {'B0Lemma': 'il', 'antepenultimateT': '_', 'B1POS': '_', 'B1Token': 'a', 'B0Token': 'Il', 'prevriousT': '_', 'B0POS': '_', 'B1Lemma': 'avoir'}
1- 2 : {'B0Lemma': 'avoir', 'antepenultimateT': '_', 'B1POS': '_', 'B1Token': 'fait', 'B0Token': 'a', 'prevriousT': 'None', 'S0Token': 'Il', 'S0Lemma': 'il', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'faire', 'distance': '1'}
2- 0 : {'B0Lemma': 'avoir', 'antepenultimateT': 'None', 'B1POS': '_', 'B1Token': 'fait', 'B0Token': 'a', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'faire'}
3- 2 : {'B0Lemma': 'faire', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'partie', 'B0Token': 'fait', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'a', 'S0Lemma': 'avoir', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'partie', 'distance': '1'}
4- 0 : {'B0Lemma': 'faire', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'partie', 'B0Token': 'fait', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'partie'}
5- 0 : {'B0Lemma': 'partie', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'partie', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'fait', 'S0Lemma': 'faire', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
6- 1 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'groupes', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'S0Token': 'fait', 'S1Token': 'partie', 'S1POS': '_', 'S0Lemma': 'faire', 'S1Lemma': 'partie', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'groupe', 'distance': '1'}
7- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'groupes', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'S0Token': 'fait-partie', 'S0Lemma': 'faire-partie', 'S0POS': '_-_', 'B0POS': '_', 'B1Lemma': 'groupe', 'distance': '1'}
8- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'groupes', 'B0Token': 'de', 'prevriousT': 'TransitionType.MERGE', 'B0POS': '_', 'B1Lemma': 'groupe'}
9- 2 : {'B0Lemma': 'groupe', 'antepenultimateT': 'TransitionType.MERGE', 'B1POS': '_', 'B1Token': 'musicaux', 'B0Token': 'groupes', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'musical', 'distance': '1'}
10- 0 : {'B0Lemma': 'groupe', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'musicaux', 'B0Token': 'groupes', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'musical'}
11- 2 : {'B0Lemma': 'musical', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'comme', 'B0Token': 'musicaux', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'groupes', 'S0Lemma': 'groupe', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'comme', 'distance': '1'}
12- 0 : {'B0Lemma': 'musical', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'comme', 'B0Token': 'musicaux', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'comme'}
13- 2 : {'B0Lemma': 'comme', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'Los', 'B0Token': 'comme', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'musicaux', 'S0Lemma': 'musical', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'el', 'distance': '1'}
14- 0 : {'B0Lemma': 'comme', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'Los', 'B0Token': 'comme', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'el'}
15- 2 : {'B0Lemma': 'el', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'Abuelos', 'B0Token': 'Los', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'comme', 'S0Lemma': 'comme', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'abuelo', 'distance': '1'}
16- 0 : {'B0Lemma': 'el', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'Abuelos', 'B0Token': 'Los', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'abuelo'}
17- 2 : {'B0Lemma': 'abuelo', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'Abuelos', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'Los', 'S0Lemma': 'el', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
18- 0 : {'B0Lemma': 'abuelo', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'Abuelos', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
19- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'Abuelos', 'S0Lemma': 'abuelo', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
20- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
21- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'Nada', 'B0Token': 'la', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'Nada', 'distance': '1'}
22- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'Nada', 'B0Token': 'la', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'Nada'}
23- 2 : {'B0Lemma': 'Nada', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'et', 'B0Token': 'Nada', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'la', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'et', 'distance': '1'}
24- 0 : {'B0Lemma': 'Nada', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'et', 'B0Token': 'Nada', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'et'}
25- 2 : {'B0Lemma': 'et', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'Los', 'B0Token': 'et', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'Nada', 'S0Lemma': 'Nada', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'Los', 'distance': '1'}
26- 0 : {'B0Lemma': 'et', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'Los', 'B0Token': 'et', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'Los'}
27- 2 : {'B0Lemma': 'Los', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'Rodr\xc3\xadguez', 'B0Token': 'Los', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'et', 'S0Lemma': 'et', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'Rodr\xc3\xadguez', 'distance': '1'}
28- 0 : {'B0Lemma': 'Los', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'Rodr\xc3\xadguez', 'B0Token': 'Los', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'Rodr\xc3\xadguez'}
29- 2 : {'B0Lemma': 'Rodr\xc3\xadguez', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '.', 'B0Token': 'Rodr\xc3\xadguez', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'Los', 'S0Lemma': 'Los', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '.', 'distance': '1'}
30- 0 : {'B0Lemma': 'Rodr\xc3\xadguez', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '.', 'B0Token': 'Rodr\xc3\xadguez', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '.'}
31- 2 : {'B0Lemma': '.', 'antepenultimateT': 'TransitionType.SHIFT', 'distance': '1', 'B0Token': '.', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'Rodr\xc3\xadguez', 'S0Lemma': 'Rodr\xc3\xadguez', 'S0POS': '_', 'B0POS': '_'}
32- 0 : {'B0Lemma': '.', 'B0Token': '.', 'prevriousT': 'TransitionType.SHIFT', 'antepenultimateT': 'TransitionType.COMPLETE', 'B0POS': '_'}
33- 2 : {'S0Lemma': '.', 'antepenultimateT': 'TransitionType.SHIFT', 'prevriousT': 'TransitionType.COMPLETE', 'S0POS': '_', 'S0Token': '.'}
##Sentence No. 16008 - fr-ud-dev_00023
 Les conventions signées entre l'UFE et les universités françaises partenaires garantissent que l'université est qualifiée selon les critères de l'Union européenne.
###Existing MWEs: 
1- **conventions signées** (LVC)

0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Les ,.. ]
1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Les]   -|||- [conventions ,.. ]
2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [conventions ,.. ]
3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[conventions]   -|||- [signées ,.. ]
4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [signées ,.. ]
5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[signées]   -|||- [entre ,.. ]
6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [entre ,.. ]
7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[entre]   -|||- [l' ,.. ]
8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [l' ,.. ]
9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[l']   -|||- [UFE ,.. ]
10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [UFE ,.. ]
11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[UFE]   -|||- [et ,.. ]
12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [et ,.. ]
13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[et]   -|||- [les ,.. ]
14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [les ,.. ]
15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[les]   -|||- [universités ,.. ]
16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [universités ,.. ]
17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[universités]   -|||- [françaises ,.. ]
18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [françaises ,.. ]
19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[françaises]   -|||- [partenaires ,.. ]
20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [partenaires ,.. ]
21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[partenaires]   -|||- [garantissent ,.. ]
22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [garantissent ,.. ]
23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[garantissent]   -|||- [que ,.. ]
24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [que ,.. ]
25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[que]   -|||- [l' ,.. ]
26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [l' ,.. ]
27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[l']   -|||- [université ,.. ]
28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [université ,.. ]
29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[université]   -|||- [est ,.. ]
30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [est ,.. ]
31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[est]   -|||- [qualifiée ,.. ]
32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [qualifiée ,.. ]
33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[qualifiée]   -|||- [selon ,.. ]
34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [selon ,.. ]
35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[selon]   -|||- [les ,.. ]
36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [les ,.. ]
37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[les]   -|||- [critères ,.. ]
38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [critères ,.. ]
39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[critères]   -|||- [de ,.. ]
40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [l' ,.. ]
42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [l' ,.. ]
43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[l']   -|||- [Union ,.. ]
44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Union ,.. ]
45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Union]   -|||- [européenne ,.. ]
46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [européenne ,.. ]
47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[européenne]   -|||- [.]
48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [.]
49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[.]   -|||- [ ]
50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [ ]

###Features: 
0- 0 : {'B0Lemma': 'le', 'antepenultimateT': '_', 'B1POS': '_', 'B1Token': 'conventions', 'B0Token': 'Les', 'prevriousT': '_', 'B0POS': '_', 'B1Lemma': 'convention'}
1- 2 : {'B0Lemma': 'convention', 'antepenultimateT': '_', 'B1POS': '_', 'B1Token': 'sign\xc3\xa9es', 'B0Token': 'conventions', 'prevriousT': 'None', 'S0Token': 'Les', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'signer', 'distance': '1'}
2- 0 : {'B0Lemma': 'convention', 'antepenultimateT': 'None', 'B1POS': '_', 'B1Token': 'sign\xc3\xa9es', 'B0Token': 'conventions', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'signer'}
3- 2 : {'B0Lemma': 'signer', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'entre', 'B0Token': 'sign\xc3\xa9es', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'conventions', 'S0Lemma': 'convention', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'entre', 'distance': '1'}
4- 0 : {'B0Lemma': 'signer', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'entre', 'B0Token': 'sign\xc3\xa9es', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'entre'}
5- 2 : {'B0Lemma': 'entre', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': "l'", 'B0Token': 'entre', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'sign\xc3\xa9es', 'S0Lemma': 'signer', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
6- 0 : {'B0Lemma': 'entre', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': "l'", 'B0Token': 'entre', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
7- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'UFE', 'B0Token': "l'", 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'entre', 'S0Lemma': 'entre', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'UFE', 'distance': '1'}
8- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'UFE', 'B0Token': "l'", 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'UFE'}
9- 2 : {'B0Lemma': 'UFE', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'et', 'B0Token': 'UFE', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': "l'", 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'et', 'distance': '1'}
10- 0 : {'B0Lemma': 'UFE', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'et', 'B0Token': 'UFE', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'et'}
11- 2 : {'B0Lemma': 'et', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'les', 'B0Token': 'et', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'UFE', 'S0Lemma': 'UFE', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
12- 0 : {'B0Lemma': 'et', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'les', 'B0Token': 'et', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
13- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'universit\xc3\xa9s', 'B0Token': 'les', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'et', 'S0Lemma': 'et', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'universit\xc3\xa9', 'distance': '1'}
14- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'universit\xc3\xa9s', 'B0Token': 'les', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'universit\xc3\xa9'}
15- 2 : {'B0Lemma': 'universit\xc3\xa9', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'fran\xc3\xa7aises', 'B0Token': 'universit\xc3\xa9s', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'les', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'fran\xc3\xa7ais', 'distance': '1'}
16- 0 : {'B0Lemma': 'universit\xc3\xa9', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'fran\xc3\xa7aises', 'B0Token': 'universit\xc3\xa9s', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'fran\xc3\xa7ais'}
17- 2 : {'B0Lemma': 'fran\xc3\xa7ais', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'partenaires', 'B0Token': 'fran\xc3\xa7aises', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'universit\xc3\xa9s', 'S0Lemma': 'universit\xc3\xa9', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'partenaire', 'distance': '1'}
18- 0 : {'B0Lemma': 'fran\xc3\xa7ais', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'partenaires', 'B0Token': 'fran\xc3\xa7aises', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'partenaire'}
19- 2 : {'B0Lemma': 'partenaire', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'garantissent', 'B0Token': 'partenaires', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'fran\xc3\xa7aises', 'S0Lemma': 'fran\xc3\xa7ais', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'garantir', 'distance': '1'}
20- 0 : {'B0Lemma': 'partenaire', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'garantissent', 'B0Token': 'partenaires', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'garantir'}
21- 2 : {'B0Lemma': 'garantir', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'que', 'B0Token': 'garantissent', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'partenaires', 'S0Lemma': 'partenaire', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'que', 'distance': '1'}
22- 0 : {'B0Lemma': 'garantir', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'que', 'B0Token': 'garantissent', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'que'}
23- 2 : {'B0Lemma': 'que', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': "l'", 'B0Token': 'que', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'garantissent', 'S0Lemma': 'garantir', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
24- 0 : {'B0Lemma': 'que', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': "l'", 'B0Token': 'que', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
25- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'universit\xc3\xa9', 'B0Token': "l'", 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'que', 'S0Lemma': 'que', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'universit\xc3\xa9', 'distance': '1'}
26- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'universit\xc3\xa9', 'B0Token': "l'", 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'universit\xc3\xa9'}
27- 2 : {'B0Lemma': 'universit\xc3\xa9', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'est', 'B0Token': 'universit\xc3\xa9', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': "l'", 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '\xc3\xaatre', 'distance': '1'}
28- 0 : {'B0Lemma': 'universit\xc3\xa9', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'est', 'B0Token': 'universit\xc3\xa9', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '\xc3\xaatre'}
29- 2 : {'B0Lemma': '\xc3\xaatre', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'qualifi\xc3\xa9e', 'B0Token': 'est', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'universit\xc3\xa9', 'S0Lemma': 'universit\xc3\xa9', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'qualifier', 'distance': '1'}
30- 0 : {'B0Lemma': '\xc3\xaatre', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'qualifi\xc3\xa9e', 'B0Token': 'est', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'qualifier'}
31- 2 : {'B0Lemma': 'qualifier', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'selon', 'B0Token': 'qualifi\xc3\xa9e', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'est', 'S0Lemma': '\xc3\xaatre', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'selon', 'distance': '1'}
32- 0 : {'B0Lemma': 'qualifier', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'selon', 'B0Token': 'qualifi\xc3\xa9e', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'selon'}
33- 2 : {'B0Lemma': 'selon', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'les', 'B0Token': 'selon', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'qualifi\xc3\xa9e', 'S0Lemma': 'qualifier', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
34- 0 : {'B0Lemma': 'selon', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'les', 'B0Token': 'selon', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
35- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'crit\xc3\xa8res', 'B0Token': 'les', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'selon', 'S0Lemma': 'selon', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'crit\xc3\xa8re', 'distance': '1'}
36- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'crit\xc3\xa8res', 'B0Token': 'les', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'crit\xc3\xa8re'}
37- 2 : {'B0Lemma': 'crit\xc3\xa8re', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'crit\xc3\xa8res', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'les', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
38- 0 : {'B0Lemma': 'crit\xc3\xa8re', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'crit\xc3\xa8res', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
39- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': "l'", 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'crit\xc3\xa8res', 'S0Lemma': 'crit\xc3\xa8re', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
40- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': "l'", 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
41- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'Union', 'B0Token': "l'", 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'union', 'distance': '1'}
42- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'Union', 'B0Token': "l'", 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'union'}
43- 2 : {'B0Lemma': 'union', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'europ\xc3\xa9enne', 'B0Token': 'Union', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': "l'", 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'europ\xc3\xa9en', 'distance': '1'}
44- 0 : {'B0Lemma': 'union', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'europ\xc3\xa9enne', 'B0Token': 'Union', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'europ\xc3\xa9en'}
45- 2 : {'B0Lemma': 'europ\xc3\xa9en', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '.', 'B0Token': 'europ\xc3\xa9enne', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'Union', 'S0Lemma': 'union', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '.', 'distance': '1'}
46- 0 : {'B0Lemma': 'europ\xc3\xa9en', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '.', 'B0Token': 'europ\xc3\xa9enne', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '.'}
47- 2 : {'B0Lemma': '.', 'antepenultimateT': 'TransitionType.SHIFT', 'distance': '1', 'B0Token': '.', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'europ\xc3\xa9enne', 'S0Lemma': 'europ\xc3\xa9en', 'S0POS': '_', 'B0POS': '_'}
48- 0 : {'B0Lemma': '.', 'B0Token': '.', 'prevriousT': 'TransitionType.SHIFT', 'antepenultimateT': 'TransitionType.COMPLETE', 'B0POS': '_'}
49- 2 : {'S0Lemma': '.', 'antepenultimateT': 'TransitionType.SHIFT', 'prevriousT': 'TransitionType.COMPLETE', 'S0POS': '_', 'S0Token': '.'}
##Sentence No. 16020 - fr-ud-dev_00035
 Cette force résulte de la faible poussée exercée par la restitution sous forme de rayonnement infrarouge de l'énergie solaire absorbée.
###Existing MWEs: 
1- **poussée exercée** (LVC)

0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Cette ,.. ]
1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Cette]   -|||- [force ,.. ]
2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [force ,.. ]
3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[force]   -|||- [résulte ,.. ]
4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [résulte ,.. ]
5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[résulte]   -|||- [de ,.. ]
6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [la ,.. ]
8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [la ,.. ]
9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[la]   -|||- [faible ,.. ]
10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [faible ,.. ]
11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[faible]   -|||- [poussée ,.. ]
12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [poussée ,.. ]
13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[poussée]   -|||- [exercée ,.. ]
14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [exercée ,.. ]
15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[exercée]   -|||- [par ,.. ]
16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [par ,.. ]
17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[par]   -|||- [la ,.. ]
18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [la ,.. ]
19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[la]   -|||- [restitution ,.. ]
20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [restitution ,.. ]
21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[restitution]   -|||- [sous ,.. ]
22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [sous ,.. ]
23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[sous]   -|||- [forme ,.. ]
24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [forme ,.. ]
25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[forme]   -|||- [de ,.. ]
26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [rayonnement ,.. ]
28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [rayonnement ,.. ]
29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[rayonnement]   -|||- [infrarouge ,.. ]
30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [infrarouge ,.. ]
31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[infrarouge]   -|||- [de ,.. ]
32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [l' ,.. ]
34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [l' ,.. ]
35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[l']   -|||- [énergie ,.. ]
36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [énergie ,.. ]
37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[énergie]   -|||- [solaire ,.. ]
38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [solaire ,.. ]
39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[solaire]   -|||- [absorbée ,.. ]
40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [absorbée ,.. ]
41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[absorbée]   -|||- [.]
42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [.]
43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[.]   -|||- [ ]
44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [ ]

###Features: 
0- 0 : {'B0Lemma': 'ce', 'antepenultimateT': '_', 'B1POS': '_', 'B1Token': 'force', 'B0Token': 'Cette', 'prevriousT': '_', 'B0POS': '_', 'B1Lemma': 'force'}
1- 2 : {'B0Lemma': 'force', 'antepenultimateT': '_', 'B1POS': '_', 'B1Token': 'r\xc3\xa9sulte', 'B0Token': 'force', 'prevriousT': 'None', 'S0Token': 'Cette', 'S0Lemma': 'ce', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'r\xc3\xa9sulter', 'distance': '1'}
2- 0 : {'B0Lemma': 'force', 'antepenultimateT': 'None', 'B1POS': '_', 'B1Token': 'r\xc3\xa9sulte', 'B0Token': 'force', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'r\xc3\xa9sulter'}
3- 2 : {'B0Lemma': 'r\xc3\xa9sulter', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'r\xc3\xa9sulte', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'force', 'S0Lemma': 'force', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
4- 0 : {'B0Lemma': 'r\xc3\xa9sulter', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'r\xc3\xa9sulte', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
5- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'r\xc3\xa9sulte', 'S0Lemma': 'r\xc3\xa9sulter', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
6- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
7- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'faible', 'B0Token': 'la', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'faible', 'distance': '1'}
8- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'faible', 'B0Token': 'la', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'faible'}
9- 2 : {'B0Lemma': 'faible', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'pouss\xc3\xa9e', 'B0Token': 'faible', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'la', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'pouss\xc3\xa9e', 'distance': '1'}
10- 0 : {'B0Lemma': 'faible', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'pouss\xc3\xa9e', 'B0Token': 'faible', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'pouss\xc3\xa9e'}
11- 2 : {'B0Lemma': 'pouss\xc3\xa9e', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'exerc\xc3\xa9e', 'B0Token': 'pouss\xc3\xa9e', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'faible', 'S0Lemma': 'faible', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'exercer', 'distance': '1'}
12- 0 : {'B0Lemma': 'pouss\xc3\xa9e', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'exerc\xc3\xa9e', 'B0Token': 'pouss\xc3\xa9e', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'exercer'}
13- 2 : {'B0Lemma': 'exercer', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'par', 'B0Token': 'exerc\xc3\xa9e', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'pouss\xc3\xa9e', 'S0Lemma': 'pouss\xc3\xa9e', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'par', 'distance': '1'}
14- 0 : {'B0Lemma': 'exercer', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'par', 'B0Token': 'exerc\xc3\xa9e', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'par'}
15- 2 : {'B0Lemma': 'par', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'par', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'exerc\xc3\xa9e', 'S0Lemma': 'exercer', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
16- 0 : {'B0Lemma': 'par', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'par', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
17- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'restitution', 'B0Token': 'la', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'par', 'S0Lemma': 'par', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'restitution', 'distance': '1'}
18- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'restitution', 'B0Token': 'la', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'restitution'}
19- 2 : {'B0Lemma': 'restitution', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'sous', 'B0Token': 'restitution', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'la', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'sous', 'distance': '1'}
20- 0 : {'B0Lemma': 'restitution', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'sous', 'B0Token': 'restitution', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'sous'}
21- 2 : {'B0Lemma': 'sous', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'forme', 'B0Token': 'sous', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'restitution', 'S0Lemma': 'restitution', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'forme', 'distance': '1'}
22- 0 : {'B0Lemma': 'sous', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'forme', 'B0Token': 'sous', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'forme'}
23- 2 : {'B0Lemma': 'forme', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'forme', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'sous', 'S0Lemma': 'sous', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
24- 0 : {'B0Lemma': 'forme', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'forme', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
25- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'rayonnement', 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'forme', 'S0Lemma': 'forme', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'rayonnement', 'distance': '1'}
26- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'rayonnement', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'rayonnement'}
27- 2 : {'B0Lemma': 'rayonnement', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'infrarouge', 'B0Token': 'rayonnement', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'infrarouge', 'distance': '1'}
28- 0 : {'B0Lemma': 'rayonnement', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'infrarouge', 'B0Token': 'rayonnement', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'infrarouge'}
29- 2 : {'B0Lemma': 'infrarouge', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'infrarouge', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'rayonnement', 'S0Lemma': 'rayonnement', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
30- 0 : {'B0Lemma': 'infrarouge', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'infrarouge', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
31- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': "l'", 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'infrarouge', 'S0Lemma': 'infrarouge', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
32- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': "l'", 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
33- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '\xc3\xa9nergie', 'B0Token': "l'", 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '\xc3\xa9nergie', 'distance': '1'}
34- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '\xc3\xa9nergie', 'B0Token': "l'", 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '\xc3\xa9nergie'}
35- 2 : {'B0Lemma': '\xc3\xa9nergie', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'solaire', 'B0Token': '\xc3\xa9nergie', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': "l'", 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'solaire', 'distance': '1'}
36- 0 : {'B0Lemma': '\xc3\xa9nergie', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'solaire', 'B0Token': '\xc3\xa9nergie', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'solaire'}
37- 2 : {'B0Lemma': 'solaire', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'absorb\xc3\xa9e', 'B0Token': 'solaire', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': '\xc3\xa9nergie', 'S0Lemma': '\xc3\xa9nergie', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'absorber', 'distance': '1'}
38- 0 : {'B0Lemma': 'solaire', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'absorb\xc3\xa9e', 'B0Token': 'solaire', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'absorber'}
39- 2 : {'B0Lemma': 'absorber', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '.', 'B0Token': 'absorb\xc3\xa9e', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'solaire', 'S0Lemma': 'solaire', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '.', 'distance': '1'}
40- 0 : {'B0Lemma': 'absorber', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '.', 'B0Token': 'absorb\xc3\xa9e', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '.'}
41- 2 : {'B0Lemma': '.', 'antepenultimateT': 'TransitionType.SHIFT', 'distance': '1', 'B0Token': '.', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'absorb\xc3\xa9e', 'S0Lemma': 'absorber', 'S0POS': '_', 'B0POS': '_'}
42- 0 : {'B0Lemma': '.', 'B0Token': '.', 'prevriousT': 'TransitionType.SHIFT', 'antepenultimateT': 'TransitionType.COMPLETE', 'B0POS': '_'}
43- 2 : {'S0Lemma': '.', 'antepenultimateT': 'TransitionType.SHIFT', 'prevriousT': 'TransitionType.COMPLETE', 'S0POS': '_', 'S0Token': '.'}
##Sentence No. 16021 - fr-ud-dev_00036
 Elle est traditionnellement divisée en deux parties : la zone de Sorgenfrei-Tornquist au nord-ouest, et la zone de Teisseyre-Tornquist au sud-est, la jonction s'effectuant au niveau de Bornholm.
###Existing MWEs: 
1- **jonction effectuant** (LVC)
###Identified MWEs: 
1- **s' effectuant** ()

0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Elle ,.. ]
1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Elle]   -|||- [est ,.. ]
2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [est ,.. ]
3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[est]   -|||- [traditionnellement ,.. ]
4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [traditionnellement ,.. ]
5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[traditionnellement]   -|||- [divisée ,.. ]
6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [divisée ,.. ]
7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[divisée]   -|||- [en ,.. ]
8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [en ,.. ]
9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[en]   -|||- [deux ,.. ]
10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [deux ,.. ]
11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[deux]   -|||- [parties ,.. ]
12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [parties ,.. ]
13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[parties]   -|||- [: ,.. ]
14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [: ,.. ]
15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[:]   -|||- [la ,.. ]
16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [la ,.. ]
17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[la]   -|||- [zone ,.. ]
18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [zone ,.. ]
19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[zone]   -|||- [de ,.. ]
20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [Sorgenfrei-Tornquist ,.. ]
22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Sorgenfrei-Tornquist ,.. ]
23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Sorgenfrei-Tornquist]   -|||- [à ,.. ]
24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [à ,.. ]
25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[à]   -|||- [le ,.. ]
26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [le ,.. ]
27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[le]   -|||- [nord-ouest ,.. ]
28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [nord-ouest ,.. ]
29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[nord-ouest]   -|||- [, ,.. ]
30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [, ,.. ]
31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[,]   -|||- [et ,.. ]
32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [et ,.. ]
33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[et]   -|||- [la ,.. ]
34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [la ,.. ]
35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[la]   -|||- [zone ,.. ]
36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [zone ,.. ]
37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[zone]   -|||- [de ,.. ]
38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [Teisseyre-Tornquist ,.. ]
40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Teisseyre-Tornquist ,.. ]
41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Teisseyre-Tornquist]   -|||- [à ,.. ]
42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [à ,.. ]
43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[à]   -|||- [le ,.. ]
44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [le ,.. ]
45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[le]   -|||- [sud-est ,.. ]
46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [sud-est ,.. ]
47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[sud-est]   -|||- [, ,.. ]
48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [, ,.. ]
49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[,]   -|||- [la ,.. ]
50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [la ,.. ]
51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[la]   -|||- [jonction ,.. ]
52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [jonction ,.. ]
53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[jonction]   -|||- [s' ,.. ]
54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [s' ,.. ]
55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[s']   -|||- [effectuant ,.. ]
56- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[s', effectuant]   -|||- [à ,.. ]
57- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[[s', effectuant]]   -|||- [à ,.. ]
58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [à ,.. ]
59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[à]   -|||- [le ,.. ]
60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [le ,.. ]
61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[le]   -|||- [niveau ,.. ]
62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [niveau ,.. ]
63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[niveau]   -|||- [de ,.. ]
64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [Bornholm ,.. ]
66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Bornholm ,.. ]
67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Bornholm]   -|||- [.]
68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [.]
69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[.]   -|||- [ ]
70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [ ]

###Features: 
0- 0 : {'B0Lemma': 'elle', 'antepenultimateT': '_', 'B1POS': '_', 'B1Token': 'est', 'B0Token': 'Elle', 'prevriousT': '_', 'B0POS': '_', 'B1Lemma': '\xc3\xaatre'}
1- 2 : {'B0Lemma': '\xc3\xaatre', 'antepenultimateT': '_', 'B1POS': '_', 'B1Token': 'traditionnellement', 'B0Token': 'est', 'prevriousT': 'None', 'S0Token': 'Elle', 'S0Lemma': 'elle', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'traditionnellement', 'distance': '1'}
2- 0 : {'B0Lemma': '\xc3\xaatre', 'antepenultimateT': 'None', 'B1POS': '_', 'B1Token': 'traditionnellement', 'B0Token': 'est', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'traditionnellement'}
3- 2 : {'B0Lemma': 'traditionnellement', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'divis\xc3\xa9e', 'B0Token': 'traditionnellement', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'est', 'S0Lemma': '\xc3\xaatre', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'diviser', 'distance': '1'}
4- 0 : {'B0Lemma': 'traditionnellement', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'divis\xc3\xa9e', 'B0Token': 'traditionnellement', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'diviser'}
5- 2 : {'B0Lemma': 'diviser', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'en', 'B0Token': 'divis\xc3\xa9e', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'traditionnellement', 'S0Lemma': 'traditionnellement', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'en', 'distance': '1'}
6- 0 : {'B0Lemma': 'diviser', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'en', 'B0Token': 'divis\xc3\xa9e', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'en'}
7- 2 : {'B0Lemma': 'en', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'deux', 'B0Token': 'en', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'divis\xc3\xa9e', 'S0Lemma': 'diviser', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'deux', 'distance': '1'}
8- 0 : {'B0Lemma': 'en', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'deux', 'B0Token': 'en', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'deux'}
9- 2 : {'B0Lemma': 'deux', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'parties', 'B0Token': 'deux', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'en', 'S0Lemma': 'en', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'partie', 'distance': '1'}
10- 0 : {'B0Lemma': 'deux', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'parties', 'B0Token': 'deux', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'partie'}
11- 2 : {'B0Lemma': 'partie', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': ':', 'B0Token': 'parties', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'deux', 'S0Lemma': 'deux', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': ':', 'distance': '1'}
12- 0 : {'B0Lemma': 'partie', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': ':', 'B0Token': 'parties', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': ':'}
13- 2 : {'B0Lemma': ':', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'la', 'B0Token': ':', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'parties', 'S0Lemma': 'partie', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
14- 0 : {'B0Lemma': ':', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'la', 'B0Token': ':', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
15- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'zone', 'B0Token': 'la', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': ':', 'S0Lemma': ':', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'zone', 'distance': '1'}
16- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'zone', 'B0Token': 'la', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'zone'}
17- 2 : {'B0Lemma': 'zone', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'zone', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'la', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
18- 0 : {'B0Lemma': 'zone', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'zone', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
19- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'Sorgenfrei-Tornquist', 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'zone', 'S0Lemma': 'zone', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'Sorgenfrei-Tornquist', 'distance': '1'}
20- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'Sorgenfrei-Tornquist', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'Sorgenfrei-Tornquist'}
21- 2 : {'B0Lemma': 'Sorgenfrei-Tornquist', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': 'Sorgenfrei-Tornquist', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '\xc3\xa0', 'distance': '1'}
22- 0 : {'B0Lemma': 'Sorgenfrei-Tornquist', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': 'Sorgenfrei-Tornquist', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '\xc3\xa0'}
23- 2 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'Sorgenfrei-Tornquist', 'S0Lemma': 'Sorgenfrei-Tornquist', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
24- 0 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
25- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'nord-ouest', 'B0Token': 'le', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': '\xc3\xa0', 'S0Lemma': '\xc3\xa0', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'nord-ouest', 'distance': '1'}
26- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'nord-ouest', 'B0Token': 'le', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'nord-ouest'}
27- 2 : {'B0Lemma': 'nord-ouest', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': ',', 'B0Token': 'nord-ouest', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'le', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': ',', 'distance': '1'}
28- 0 : {'B0Lemma': 'nord-ouest', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': ',', 'B0Token': 'nord-ouest', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': ','}
29- 2 : {'B0Lemma': ',', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'et', 'B0Token': ',', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'nord-ouest', 'S0Lemma': 'nord-ouest', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'et', 'distance': '1'}
30- 0 : {'B0Lemma': ',', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'et', 'B0Token': ',', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'et'}
31- 2 : {'B0Lemma': 'et', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'et', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': ',', 'S0Lemma': ',', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
32- 0 : {'B0Lemma': 'et', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'et', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
33- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'zone', 'B0Token': 'la', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'et', 'S0Lemma': 'et', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'zone', 'distance': '1'}
34- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'zone', 'B0Token': 'la', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'zone'}
35- 2 : {'B0Lemma': 'zone', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'zone', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'la', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
36- 0 : {'B0Lemma': 'zone', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'zone', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
37- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'Teisseyre-Tornquist', 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'zone', 'S0Lemma': 'zone', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'Teisseyre-Tornquist', 'distance': '1'}
38- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'Teisseyre-Tornquist', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'Teisseyre-Tornquist'}
39- 2 : {'B0Lemma': 'Teisseyre-Tornquist', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': 'Teisseyre-Tornquist', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '\xc3\xa0', 'distance': '1'}
40- 0 : {'B0Lemma': 'Teisseyre-Tornquist', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': 'Teisseyre-Tornquist', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '\xc3\xa0'}
41- 2 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'Teisseyre-Tornquist', 'S0Lemma': 'Teisseyre-Tornquist', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
42- 0 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
43- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'sud-est', 'B0Token': 'le', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': '\xc3\xa0', 'S0Lemma': '\xc3\xa0', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'sud-est', 'distance': '1'}
44- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'sud-est', 'B0Token': 'le', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'sud-est'}
45- 2 : {'B0Lemma': 'sud-est', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': ',', 'B0Token': 'sud-est', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'le', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': ',', 'distance': '1'}
46- 0 : {'B0Lemma': 'sud-est', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': ',', 'B0Token': 'sud-est', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': ','}
47- 2 : {'B0Lemma': ',', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'la', 'B0Token': ',', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'sud-est', 'S0Lemma': 'sud-est', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
48- 0 : {'B0Lemma': ',', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'la', 'B0Token': ',', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
49- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'jonction', 'B0Token': 'la', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': ',', 'S0Lemma': ',', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'jonction', 'distance': '1'}
50- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'jonction', 'B0Token': 'la', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'jonction'}
51- 2 : {'B0Lemma': 'jonction', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': "s'", 'B0Token': 'jonction', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'la', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'se', 'distance': '1'}
52- 0 : {'B0Lemma': 'jonction', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': "s'", 'B0Token': 'jonction', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'se'}
53- 2 : {'B0Lemma': 'se', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'effectuant', 'B0Token': "s'", 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'jonction', 'S0Lemma': 'jonction', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'effectuer', 'distance': '1'}
54- 0 : {'B0Lemma': 'se', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'effectuant', 'B0Token': "s'", 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'effectuer'}
55- 0 : {'B0Lemma': 'effectuer', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': 'effectuant', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': "s'", 'S0Lemma': 'se', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '\xc3\xa0', 'distance': '1'}
56- 1 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.SHIFT', 'S0Token': "s'", 'S1Token': 'effectuant', 'S1POS': '_', 'S0Lemma': 'se', 'S1Lemma': 'effectuer', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
57- 2 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.SHIFT', 'S0Token': "s'-effectuant", 'S0Lemma': 'se-effectuer', 'S0POS': '_-_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
58- 0 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.MERGE', 'B0POS': '_', 'B1Lemma': 'le'}
59- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.MERGE', 'B1POS': '_', 'B1Token': 'niveau', 'B0Token': 'le', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': '\xc3\xa0', 'S0Lemma': '\xc3\xa0', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'niveau', 'distance': '1'}
60- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'niveau', 'B0Token': 'le', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'niveau'}
61- 2 : {'B0Lemma': 'niveau', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'niveau', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'le', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
62- 0 : {'B0Lemma': 'niveau', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'niveau', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
63- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'Bornholm', 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'niveau', 'S0Lemma': 'niveau', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'Bornholm', 'distance': '1'}
64- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'Bornholm', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'Bornholm'}
65- 2 : {'B0Lemma': 'Bornholm', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '.', 'B0Token': 'Bornholm', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '.', 'distance': '1'}
66- 0 : {'B0Lemma': 'Bornholm', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '.', 'B0Token': 'Bornholm', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '.'}
67- 2 : {'B0Lemma': '.', 'antepenultimateT': 'TransitionType.SHIFT', 'distance': '1', 'B0Token': '.', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'Bornholm', 'S0Lemma': 'Bornholm', 'S0POS': '_', 'B0POS': '_'}
68- 0 : {'B0Lemma': '.', 'B0Token': '.', 'prevriousT': 'TransitionType.SHIFT', 'antepenultimateT': 'TransitionType.COMPLETE', 'B0POS': '_'}
69- 2 : {'S0Lemma': '.', 'antepenultimateT': 'TransitionType.SHIFT', 'prevriousT': 'TransitionType.COMPLETE', 'S0POS': '_', 'S0Token': '.'}
##Sentence No. 16026 - fr-ud-dev_00041
 Le solde naturel annuel, qui est la différence entre le nombre de naissances et le nombre de décès enregistrés au cours d'une même année, connaît une forte augmentation, puisque la variation annuelle due au solde naturel passe de-1 à-0,8.
###Existing MWEs: 
1- **connaît augmentation** (LVC)

0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [Le ,.. ]
1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[Le]   -|||- [solde ,.. ]
2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [solde ,.. ]
3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[solde]   -|||- [naturel ,.. ]
4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [naturel ,.. ]
5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[naturel]   -|||- [annuel ,.. ]
6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [annuel ,.. ]
7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[annuel]   -|||- [, ,.. ]
8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [, ,.. ]
9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[,]   -|||- [qui ,.. ]
10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [qui ,.. ]
11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[qui]   -|||- [est ,.. ]
12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [est ,.. ]
13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[est]   -|||- [la ,.. ]
14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [la ,.. ]
15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[la]   -|||- [différence ,.. ]
16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [différence ,.. ]
17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[différence]   -|||- [entre ,.. ]
18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [entre ,.. ]
19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[entre]   -|||- [le ,.. ]
20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [le ,.. ]
21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[le]   -|||- [nombre ,.. ]
22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [nombre ,.. ]
23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[nombre]   -|||- [de ,.. ]
24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [naissances ,.. ]
26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [naissances ,.. ]
27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[naissances]   -|||- [et ,.. ]
28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [et ,.. ]
29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[et]   -|||- [le ,.. ]
30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [le ,.. ]
31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[le]   -|||- [nombre ,.. ]
32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [nombre ,.. ]
33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[nombre]   -|||- [de ,.. ]
34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [décès ,.. ]
36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [décès ,.. ]
37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[décès]   -|||- [enregistrés ,.. ]
38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [enregistrés ,.. ]
39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[enregistrés]   -|||- [à ,.. ]
40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [à ,.. ]
41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[à]   -|||- [le ,.. ]
42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [le ,.. ]
43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[le]   -|||- [cours ,.. ]
44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [cours ,.. ]
45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[cours]   -|||- [d' ,.. ]
46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [d' ,.. ]
47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[d']   -|||- [une ,.. ]
48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [une ,.. ]
49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[une]   -|||- [même ,.. ]
50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [même ,.. ]
51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[même]   -|||- [année ,.. ]
52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [année ,.. ]
53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[année]   -|||- [, ,.. ]
54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [, ,.. ]
55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[,]   -|||- [connaît ,.. ]
56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [connaît ,.. ]
57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[connaît]   -|||- [une ,.. ]
58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [une ,.. ]
59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[une]   -|||- [forte ,.. ]
60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [forte ,.. ]
61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[forte]   -|||- [augmentation ,.. ]
62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [augmentation ,.. ]
63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[augmentation]   -|||- [, ,.. ]
64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [, ,.. ]
65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[,]   -|||- [puisque ,.. ]
66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [puisque ,.. ]
67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[puisque]   -|||- [la ,.. ]
68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [la ,.. ]
69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[la]   -|||- [variation ,.. ]
70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [variation ,.. ]
71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[variation]   -|||- [annuelle ,.. ]
72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [annuelle ,.. ]
73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[annuelle]   -|||- [due ,.. ]
74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [due ,.. ]
75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[due]   -|||- [à ,.. ]
76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [à ,.. ]
77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[à]   -|||- [le ,.. ]
78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [le ,.. ]
79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[le]   -|||- [solde ,.. ]
80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [solde ,.. ]
81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[solde]   -|||- [naturel ,.. ]
82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [naturel ,.. ]
83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[naturel]   -|||- [passe ,.. ]
84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [passe ,.. ]
85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[passe]   -|||- [de ,.. ]
86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [de ,.. ]
87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[de]   -|||- [-1 ,.. ]
88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [-1 ,.. ]
89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[-1]   -|||- [à ,.. ]
90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [à ,.. ]
91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[à]   -|||- [-0,8 ,.. ]
92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [-0,8 ,.. ]
93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[-0,8]   -|||- [.]
94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [.]
95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[.]   -|||- [ ]
96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;[]   -|||- [ ]

###Features: 
0- 0 : {'B0Lemma': 'le', 'antepenultimateT': '_', 'B1POS': '_', 'B1Token': 'solde', 'B0Token': 'Le', 'prevriousT': '_', 'B0POS': '_', 'B1Lemma': 'solde'}
1- 2 : {'B0Lemma': 'solde', 'antepenultimateT': '_', 'B1POS': '_', 'B1Token': 'naturel', 'B0Token': 'solde', 'prevriousT': 'None', 'S0Token': 'Le', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'naturel', 'distance': '1'}
2- 0 : {'B0Lemma': 'solde', 'antepenultimateT': 'None', 'B1POS': '_', 'B1Token': 'naturel', 'B0Token': 'solde', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'naturel'}
3- 2 : {'B0Lemma': 'naturel', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'annuel', 'B0Token': 'naturel', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'solde', 'S0Lemma': 'solde', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'annuel', 'distance': '1'}
4- 0 : {'B0Lemma': 'naturel', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'annuel', 'B0Token': 'naturel', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'annuel'}
5- 2 : {'B0Lemma': 'annuel', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': ',', 'B0Token': 'annuel', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'naturel', 'S0Lemma': 'naturel', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': ',', 'distance': '1'}
6- 0 : {'B0Lemma': 'annuel', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': ',', 'B0Token': 'annuel', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': ','}
7- 2 : {'B0Lemma': ',', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'qui', 'B0Token': ',', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'annuel', 'S0Lemma': 'annuel', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'qui', 'distance': '1'}
8- 0 : {'B0Lemma': ',', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'qui', 'B0Token': ',', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'qui'}
9- 2 : {'B0Lemma': 'qui', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'est', 'B0Token': 'qui', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': ',', 'S0Lemma': ',', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '\xc3\xaatre', 'distance': '1'}
10- 0 : {'B0Lemma': 'qui', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'est', 'B0Token': 'qui', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '\xc3\xaatre'}
11- 2 : {'B0Lemma': '\xc3\xaatre', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'est', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'qui', 'S0Lemma': 'qui', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
12- 0 : {'B0Lemma': '\xc3\xaatre', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'est', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
13- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'diff\xc3\xa9rence', 'B0Token': 'la', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'est', 'S0Lemma': '\xc3\xaatre', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'diff\xc3\xa9rence', 'distance': '1'}
14- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'diff\xc3\xa9rence', 'B0Token': 'la', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'diff\xc3\xa9rence'}
15- 2 : {'B0Lemma': 'diff\xc3\xa9rence', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'entre', 'B0Token': 'diff\xc3\xa9rence', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'la', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'entre', 'distance': '1'}
16- 0 : {'B0Lemma': 'diff\xc3\xa9rence', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'entre', 'B0Token': 'diff\xc3\xa9rence', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'entre'}
17- 2 : {'B0Lemma': 'entre', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'le', 'B0Token': 'entre', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'diff\xc3\xa9rence', 'S0Lemma': 'diff\xc3\xa9rence', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
18- 0 : {'B0Lemma': 'entre', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'le', 'B0Token': 'entre', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
19- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'nombre', 'B0Token': 'le', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'entre', 'S0Lemma': 'entre', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'nombre', 'distance': '1'}
20- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'nombre', 'B0Token': 'le', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'nombre'}
21- 2 : {'B0Lemma': 'nombre', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'nombre', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'le', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
22- 0 : {'B0Lemma': 'nombre', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'nombre', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
23- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'naissances', 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'nombre', 'S0Lemma': 'nombre', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'naissance', 'distance': '1'}
24- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'naissances', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'naissance'}
25- 2 : {'B0Lemma': 'naissance', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'et', 'B0Token': 'naissances', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'et', 'distance': '1'}
26- 0 : {'B0Lemma': 'naissance', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'et', 'B0Token': 'naissances', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'et'}
27- 2 : {'B0Lemma': 'et', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'le', 'B0Token': 'et', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'naissances', 'S0Lemma': 'naissance', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
28- 0 : {'B0Lemma': 'et', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'le', 'B0Token': 'et', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
29- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'nombre', 'B0Token': 'le', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'et', 'S0Lemma': 'et', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'nombre', 'distance': '1'}
30- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'nombre', 'B0Token': 'le', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'nombre'}
31- 2 : {'B0Lemma': 'nombre', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'nombre', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'le', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
32- 0 : {'B0Lemma': 'nombre', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'nombre', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
33- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'd\xc3\xa9c\xc3\xa8s', 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'nombre', 'S0Lemma': 'nombre', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'd\xc3\xa9c\xc3\xa8s', 'distance': '1'}
34- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'd\xc3\xa9c\xc3\xa8s', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'd\xc3\xa9c\xc3\xa8s'}
35- 2 : {'B0Lemma': 'd\xc3\xa9c\xc3\xa8s', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'enregistr\xc3\xa9s', 'B0Token': 'd\xc3\xa9c\xc3\xa8s', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'enregistrer', 'distance': '1'}
36- 0 : {'B0Lemma': 'd\xc3\xa9c\xc3\xa8s', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'enregistr\xc3\xa9s', 'B0Token': 'd\xc3\xa9c\xc3\xa8s', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'enregistrer'}
37- 2 : {'B0Lemma': 'enregistrer', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': 'enregistr\xc3\xa9s', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'd\xc3\xa9c\xc3\xa8s', 'S0Lemma': 'd\xc3\xa9c\xc3\xa8s', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '\xc3\xa0', 'distance': '1'}
38- 0 : {'B0Lemma': 'enregistrer', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': 'enregistr\xc3\xa9s', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '\xc3\xa0'}
39- 2 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'enregistr\xc3\xa9s', 'S0Lemma': 'enregistrer', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
40- 0 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
41- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'cours', 'B0Token': 'le', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': '\xc3\xa0', 'S0Lemma': '\xc3\xa0', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'cours', 'distance': '1'}
42- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'cours', 'B0Token': 'le', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'cours'}
43- 2 : {'B0Lemma': 'cours', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': "d'", 'B0Token': 'cours', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'le', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
44- 0 : {'B0Lemma': 'cours', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': "d'", 'B0Token': 'cours', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
45- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'une', 'B0Token': "d'", 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'cours', 'S0Lemma': 'cours', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'un', 'distance': '1'}
46- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'une', 'B0Token': "d'", 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'un'}
47- 2 : {'B0Lemma': 'un', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'm\xc3\xaame', 'B0Token': 'une', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': "d'", 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'm\xc3\xaame', 'distance': '1'}
48- 0 : {'B0Lemma': 'un', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'm\xc3\xaame', 'B0Token': 'une', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'm\xc3\xaame'}
49- 2 : {'B0Lemma': 'm\xc3\xaame', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'ann\xc3\xa9e', 'B0Token': 'm\xc3\xaame', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'une', 'S0Lemma': 'un', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'ann\xc3\xa9e', 'distance': '1'}
50- 0 : {'B0Lemma': 'm\xc3\xaame', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'ann\xc3\xa9e', 'B0Token': 'm\xc3\xaame', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'ann\xc3\xa9e'}
51- 2 : {'B0Lemma': 'ann\xc3\xa9e', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': ',', 'B0Token': 'ann\xc3\xa9e', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'm\xc3\xaame', 'S0Lemma': 'm\xc3\xaame', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': ',', 'distance': '1'}
52- 0 : {'B0Lemma': 'ann\xc3\xa9e', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': ',', 'B0Token': 'ann\xc3\xa9e', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': ','}
53- 2 : {'B0Lemma': ',', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'conna\xc3\xaet', 'B0Token': ',', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'ann\xc3\xa9e', 'S0Lemma': 'ann\xc3\xa9e', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'conna\xc3\xaetre', 'distance': '1'}
54- 0 : {'B0Lemma': ',', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'conna\xc3\xaet', 'B0Token': ',', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'conna\xc3\xaetre'}
55- 2 : {'B0Lemma': 'conna\xc3\xaetre', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'une', 'B0Token': 'conna\xc3\xaet', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': ',', 'S0Lemma': ',', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'un', 'distance': '1'}
56- 0 : {'B0Lemma': 'conna\xc3\xaetre', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'une', 'B0Token': 'conna\xc3\xaet', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'un'}
57- 2 : {'B0Lemma': 'un', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'forte', 'B0Token': 'une', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'conna\xc3\xaet', 'S0Lemma': 'conna\xc3\xaetre', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'fort', 'distance': '1'}
58- 0 : {'B0Lemma': 'un', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'forte', 'B0Token': 'une', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'fort'}
59- 2 : {'B0Lemma': 'fort', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'augmentation', 'B0Token': 'forte', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'une', 'S0Lemma': 'un', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'augmentation', 'distance': '1'}
60- 0 : {'B0Lemma': 'fort', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'augmentation', 'B0Token': 'forte', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'augmentation'}
61- 2 : {'B0Lemma': 'augmentation', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': ',', 'B0Token': 'augmentation', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'forte', 'S0Lemma': 'fort', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': ',', 'distance': '1'}
62- 0 : {'B0Lemma': 'augmentation', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': ',', 'B0Token': 'augmentation', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': ','}
63- 2 : {'B0Lemma': ',', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'puisque', 'B0Token': ',', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'augmentation', 'S0Lemma': 'augmentation', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'puisque', 'distance': '1'}
64- 0 : {'B0Lemma': ',', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'puisque', 'B0Token': ',', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'puisque'}
65- 2 : {'B0Lemma': 'puisque', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'puisque', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': ',', 'S0Lemma': ',', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
66- 0 : {'B0Lemma': 'puisque', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'la', 'B0Token': 'puisque', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
67- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'variation', 'B0Token': 'la', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'puisque', 'S0Lemma': 'puisque', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'variation', 'distance': '1'}
68- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'variation', 'B0Token': 'la', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'variation'}
69- 2 : {'B0Lemma': 'variation', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'annuelle', 'B0Token': 'variation', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'la', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'annuel', 'distance': '1'}
70- 0 : {'B0Lemma': 'variation', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'annuelle', 'B0Token': 'variation', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'annuel'}
71- 2 : {'B0Lemma': 'annuel', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'due', 'B0Token': 'annuelle', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'variation', 'S0Lemma': 'variation', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'devoir', 'distance': '1'}
72- 0 : {'B0Lemma': 'annuel', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'due', 'B0Token': 'annuelle', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'devoir'}
73- 2 : {'B0Lemma': 'devoir', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': 'due', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'annuelle', 'S0Lemma': 'annuel', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '\xc3\xa0', 'distance': '1'}
74- 0 : {'B0Lemma': 'devoir', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': 'due', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '\xc3\xa0'}
75- 2 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'due', 'S0Lemma': 'devoir', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'le', 'distance': '1'}
76- 0 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'le', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'le'}
77- 2 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'solde', 'B0Token': 'le', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': '\xc3\xa0', 'S0Lemma': '\xc3\xa0', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'solde', 'distance': '1'}
78- 0 : {'B0Lemma': 'le', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'solde', 'B0Token': 'le', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'solde'}
79- 2 : {'B0Lemma': 'solde', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'naturel', 'B0Token': 'solde', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'le', 'S0Lemma': 'le', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'naturel', 'distance': '1'}
80- 0 : {'B0Lemma': 'solde', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'naturel', 'B0Token': 'solde', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'naturel'}
81- 2 : {'B0Lemma': 'naturel', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'passe', 'B0Token': 'naturel', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'solde', 'S0Lemma': 'solde', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'passer', 'distance': '1'}
82- 0 : {'B0Lemma': 'naturel', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'passe', 'B0Token': 'naturel', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'passer'}
83- 2 : {'B0Lemma': 'passer', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'passe', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'naturel', 'S0Lemma': 'naturel', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': 'de', 'distance': '1'}
84- 0 : {'B0Lemma': 'passer', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': 'de', 'B0Token': 'passe', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': 'de'}
85- 2 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '-1', 'B0Token': 'de', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'passe', 'S0Lemma': 'passer', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '-1', 'distance': '1'}
86- 0 : {'B0Lemma': 'de', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '-1', 'B0Token': 'de', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '-1'}
87- 2 : {'B0Lemma': '-1', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': '-1', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': 'de', 'S0Lemma': 'de', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '\xc3\xa0', 'distance': '1'}
88- 0 : {'B0Lemma': '-1', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '\xc3\xa0', 'B0Token': '-1', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '\xc3\xa0'}
89- 2 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '-0,8', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': '-1', 'S0Lemma': '-1', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '-0,8', 'distance': '1'}
90- 0 : {'B0Lemma': '\xc3\xa0', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '-0,8', 'B0Token': '\xc3\xa0', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '-0,8'}
91- 2 : {'B0Lemma': '-0,8', 'antepenultimateT': 'TransitionType.SHIFT', 'B1POS': '_', 'B1Token': '.', 'B0Token': '-0,8', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': '\xc3\xa0', 'S0Lemma': '\xc3\xa0', 'S0POS': '_', 'B0POS': '_', 'B1Lemma': '.', 'distance': '1'}
92- 0 : {'B0Lemma': '-0,8', 'antepenultimateT': 'TransitionType.COMPLETE', 'B1POS': '_', 'B1Token': '.', 'B0Token': '-0,8', 'prevriousT': 'TransitionType.SHIFT', 'B0POS': '_', 'B1Lemma': '.'}
93- 2 : {'B0Lemma': '.', 'antepenultimateT': 'TransitionType.SHIFT', 'distance': '1', 'B0Token': '.', 'prevriousT': 'TransitionType.COMPLETE', 'S0Token': '-0,8', 'S0Lemma': '-0,8', 'S0POS': '_', 'B0POS': '_'}
94- 0 : {'B0Lemma': '.', 'B0Token': '.', 'prevriousT': 'TransitionType.SHIFT', 'antepenultimateT': 'TransitionType.COMPLETE', 'B0POS': '_'}
95- 2 : {'S0Lemma': '.', 'antepenultimateT': 'TransitionType.SHIFT', 'prevriousT': 'TransitionType.COMPLETE', 'S0POS': '_', 'S0Token': '.'}
