"""Konvertierte Versnummern in Bibelstellen."""
import argparse
import csv
import pathlib


def init_mapping():
    mapping = {}
    verse_number = 0
    with open(pathlib.Path(__file__).parent / 'Versnummern.csv') as f:
        for book in csv.DictReader(f):
            for index, data in enumerate(book.values()):
                if not data:
                    break
                if index == 0:
                    book_name = data
                    continue
                else:
                    verses_in_chapter = int(data)
                    chapter = index
                for verse in range(1, verses_in_chapter + 2):
                    mapping[verse_number + verse] = (
                        f'{book_name} {chapter},{verse}')
                verse_number += verses_in_chapter
    return mapping


def to_bst(vn):
    bst = vn_bst_mapping.get(vn, None)
    return bst if bst else f'Keine Bibelstelle für {vn} bestimmbar.'


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('VN', nargs='+', type=int,
                    help='Versnummer(n), durch Leerzeichen getrennt')
args = parser.parse_args()

vn_bst_mapping = init_mapping()

for vn in args.VN:
    print(to_bst(vn))
