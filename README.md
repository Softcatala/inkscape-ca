# Fitxers originals

* ca.upstream - fitxer original del Inkscape 1.3x
* ca.po - fitxer on hem llevat les fuzzy i hem retraduit tot el que quedava amb el traductor neuronal

# Fitxers a assignar

| Fitxer      | Cadenes a revisar | Persona  |
| ----------- | ----------- |----------- |
| [part-1.po](https://raw.githubusercontent.com/jordimas/inkscape-ca/main/part-1.po)   | 808         | Maite Guix
| [part-2.po](https://raw.githubusercontent.com/jordimas/inkscape-ca/main/part-2.po)   | 392         | Artur Vicedo
| [part-3.po](https://raw.githubusercontent.com/jordimas/inkscape-ca/main/part-3.po)   | 439         | ICS
| [part-4.po](https://raw.githubusercontent.com/jordimas/inkscape-ca/main/part-4.po)   | 372         | Xavi Ivars
| [part-5.po](https://raw.githubusercontent.com/jordimas/inkscape-ca/main/part-5.po)   | 605         | 
| [part-6.po](https://raw.githubusercontent.com/jordimas/inkscape-ca/main/part-6.po)   | 240         | Jordi Mas

# Scripts

Les actualitzacions de les traduccions de l'Inkscape acostumen a ser grans i es convenient poder dividir el fitxer PO en diverses parts per poder repartir la feina.

Els fitxers PO no es poden tallar arbritariament, per dos motius:

- La part tallada ha d'incloure msgid i msgstr i no pot quedar una part a un fitxer i un a un altre, perquè llavors el PO esdevé invàlid
- Les parts tallades han de començar amb un capçalera que cal afegir si no són invàlids

Hi ha dues eines molt senzilles:
* split.py - que divideix el fitxer en X parts per poder-les distribuir-les considerant els dos problemes anteriors
* join.py - que recrea el fitxer final ajuntant tots els fitxers dividits



