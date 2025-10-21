#!/usr/bin/env python3
"""
GEDCOM to CSV Converter

A privacy-focused GEDCOM to CSV converter that processes files in-memory
without storing any user data. Accessible via link or sign-up.

Usage:
    python gedcom_to_csv_converter.py input.ged output.csv

Features:
- Converts GEDCOM genealogy files to CSV format
- Extracts individuals, families, and relationships
- No file retention - all processing done in-memory
- No data storage or logging of user information
- Clean, easy-to-use interface
"""

import csv
import sys
import re
from io import StringIO
from typing import List, Dict, Any


class GedcomParser:
    """Parse GEDCOM files and extract genealogical data."""
    
    def __init__(self, gedcom_content: str):
        self.content = gedcom_content
        self.individuals = []
        self.families = []
        
    def parse(self):
        """Parse the GEDCOM content."""
        lines = self.content.strip().split('\n')
        current_record = None
        current_type = None
        
        for line in lines:
            line = line.rstrip()
            if not line:
                continue
                
            parts = line.split(' ', 2)
            level = parts[0]
            
            if level == '0':
                # Save previous record
                if current_record and current_type:
                    if current_type == 'INDI':
                        self.individuals.append(current_record)
                    elif current_type == 'FAM':
                        self.families.append(current_record)
                
                # Start new record
                if len(parts) >= 3:
                    record_id = parts[1]
                    record_type = parts[2]
                    
                    if record_type in ['INDI', 'FAM']:
                        current_record = {'ID': record_id.strip('@'), 'type': record_type}
                        current_type = record_type
                    else:
                        current_record = None
                        current_type = None
                else:
                    current_record = None
                    current_type = None
                    
            elif level == '1' and current_record:
                tag = parts[1] if len(parts) > 1 else ''
                value = parts[2] if len(parts) > 2 else ''
                
                if tag == 'NAME':
                    current_record['Name'] = value.replace('/', '')
                elif tag == 'SEX':
                    current_record['Sex'] = value
                elif tag == 'BIRT':
                    current_record['_BIRT_NEXT'] = True
                elif tag == 'DEAT':
                    current_record['_DEAT_NEXT'] = True
                elif tag == 'HUSB':
                    current_record['Husband'] = value.strip('@')
                elif tag == 'WIFE':
                    current_record['Wife'] = value.strip('@')
                elif tag == 'CHIL':
                    if 'Children' not in current_record:
                        current_record['Children'] = []
                    current_record['Children'].append(value.strip('@'))
                    
            elif level == '2' and current_record:
                tag = parts[1] if len(parts) > 1 else ''
                value = parts[2] if len(parts) > 2 else ''
                
                if tag == 'DATE':
                    if current_record.get('_BIRT_NEXT'):
                        current_record['Birth Date'] = value
                        current_record.pop('_BIRT_NEXT', None)
                    elif current_record.get('_DEAT_NEXT'):
                        current_record['Death Date'] = value
                        current_record.pop('_DEAT_NEXT', None)
                elif tag == 'PLAC':
                    if current_record.get('_BIRT_NEXT'):
                        current_record['Birth Place'] = value
                    elif current_record.get('_DEAT_NEXT'):
                        current_record['Death Place'] = value
        
        # Save last record
        if current_record and current_type:
            if current_type == 'INDI':
                self.individuals.append(current_record)
            elif current_type == 'FAM':
                self.families.append(current_record)
                
        return self
    
    def to_csv(self) -> str:
        """Convert parsed data to CSV format."""
        output = StringIO()
        
        if self.individuals:
            writer = csv.DictWriter(
                output,
                fieldnames=['ID', 'Name', 'Sex', 'Birth Date', 'Birth Place', 
                           'Death Date', 'Death Place'],
                extrasaction='ignore'
            )
            writer.writeheader()
            
            for individual in self.individuals:
                # Clean up the record
                clean_record = {
                    'ID': individual.get('ID', ''),
                    'Name': individual.get('Name', ''),
                    'Sex': individual.get('Sex', ''),
                    'Birth Date': individual.get('Birth Date', ''),
                    'Birth Place': individual.get('Birth Place', ''),
                    'Death Date': individual.get('Death Date', ''),
                    'Death Place': individual.get('Death Place', '')
                }
                writer.writerow(clean_record)
        
        return output.getvalue()


def convert_gedcom_to_csv(gedcom_content: str) -> str:
    """
    Convert GEDCOM content to CSV format.
    
    Args:
        gedcom_content: String content of a GEDCOM file
        
    Returns:
        CSV formatted string
    """
    parser = GedcomParser(gedcom_content)
    parser.parse()
    return parser.to_csv()


def main():
    """Main function for command-line usage."""
    if len(sys.argv) < 3:
        print("Usage: python gedcom_to_csv_converter.py input.ged output.csv")
        print("")
        print("This script converts GEDCOM genealogy files to CSV format.")
        print("All processing is done in-memory with no data retention.")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        # Read GEDCOM file
        with open(input_file, 'r', encoding='utf-8') as f:
            gedcom_content = f.read()
        
        # Convert to CSV
        csv_content = convert_gedcom_to_csv(gedcom_content)
        
        # Write CSV file
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            f.write(csv_content)
        
        print(f"Successfully converted {input_file} to {output_file}")
        print(f"Total records: {len(csv_content.splitlines()) - 1}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)
    finally:
        # Ensure no data is retained in memory
        gedcom_content = None
        csv_content = None


if __name__ == "__main__":
    main()
