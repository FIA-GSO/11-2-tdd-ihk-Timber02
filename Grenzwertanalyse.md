# Grenzwertanalyse

Tipp: benutzen Sie einen [Tabellengenerator für Markdown](https://www.tablesgenerator.com/markdown_tables)

## Muster

### percentage calculator

| #   | Punkte | Maximale Punkte | erwartetet Ergebnis |
| --- | ------ | --------------- | ------------------- |
| 1   | 100    | 100             | 100                 |
| 2   | 0      | 100             | 0                   |
| 3   | -1     | 100             | ValueError          |
| 4   | 101    | 100             | ValueError          |
| 5   | '50'   | 100             | TypeError           |
| 6   | 100    | 99              | ValueError          |
| 7   | 100    | 101             | ValueError          |
| 8   | 100    | '100'           | TypeError           |

### noten calculator

| #   | Prozentwert | erwartetet Ergebnis |
| --- | ----------- | ------------------- |
| 1   | 100         | 'sehr gut'          |
| 2   | 92          | 'sehr gut'          |
| 3   | 91          | 'gut'               |
| 4   | 81          | 'gut'               |
| 5   | 80          | 'befriedigend'      |
| 6   | 67          | 'befriedigend'      |
| 7   | 66          | 'ausreichend'       |
| 8   | 50          | 'ausreichend'       |
| 9   | 49          | 'mangelhaft'        |
| 10  | 30          | 'mangelhaft'        |
| 11  | 29          | 'ungenügend'        |
| 12  | 0           | 'ungenügend'        |
| 13  | -1          | ValueError          |
| 14  | 101         | ValueError          |
| 15  | 'text'      | TypeError           |
