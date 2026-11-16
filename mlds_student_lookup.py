"""Search the saved MLDS alumni data from the command line."""
from pathlib import Path
import pandas as pd


class MLDSStudentLookup:
    """Keep the alumni table and search any of its four columns."""

    def __init__(self, df):
        required = ['Name', 'Year', 'Role', 'Company']
        if not all(column in df.columns for column in required):
            raise ValueError('The data must contain Name, Year, Role, and Company.')
        self.df = df[required].copy()

    def filter_by(self, field, value):
        """Return literal, partial matches without worrying about capitalization."""
        columns = {column.lower(): column for column in self.df.columns}
        field = str(field).strip().lower()
        if field not in columns:
            raise ValueError('Choose Name, Year, Role, or Company.')
        value = str(value).strip()
        if not value:
            raise ValueError('Please enter a search value.')
        column = columns[field]
        matches = self.df[column].astype('string').str.contains(
            value, case=False, regex=False, na=False
        )
        return self.df.loc[matches]


def main():
    """Load the pickle once, then keep searching until the user exits."""
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', 200)
    path = Path(__file__).resolve().parent / 'data' / 'alumni.pkl'
    try:
        # Only load a pickle that you created or trust.
        lookup = MLDSStudentLookup(pd.read_pickle(path))
    except Exception as error:
        print(f'Could not load alumni data: {error}')
        print('Run the scraping notebook first.')
        return
    while True:
        try:
            field = input('Field (Name, Year, Role, Company), or exit: ').strip()
            if field.lower() == 'exit':
                break
            value = input('Value, or exit: ').strip()
            if value.lower() == 'exit':
                break
            result = lookup.filter_by(field, value)
            if result.empty:
                print('No matches found.\n')
            else:
                print(result.to_string(index=False))
                print(f'{len(result)} match(es).\n')
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye!')
            break
        except Exception as error:
            print(f'Could not complete that search: {error}\n')


if __name__ == '__main__':
    main()
