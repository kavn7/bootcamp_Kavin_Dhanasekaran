#!/usr/bin/env python3
import argparse
import json
import logging
from pathlib import Path
from datetime import datetime

def clean_task(input_path: str, output_path: str) -> None:
    """Reads raw JSON, applies simple transform, writes cleaned JSON."""
    logging.info('[clean_task] start: %s → %s', input_path, output_path)
    raw = json.loads(Path(input_path).read_text())
    # Example transform: filter out null prices
    cleaned = [r for r in raw if r.get('price') is not None]
    result = {
        'run_at': datetime.utcnow().isoformat(),
        'rows_in': len(raw),
        'rows_out': len(cleaned),
        'data': cleaned,
    }
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(json.dumps(result, indent=2))
    logging.info('[clean_task] wrote %d records to %s', len(cleaned), output_path)

def main():
    parser = argparse.ArgumentParser(description='Clean raw prices JSON')
    parser.add_argument('--input',  required=True, help='Path to raw JSON')
    parser.add_argument('--output', required=True, help='Path to cleaned JSON')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    clean_task(args.input, args.output)


if __name__ == '__main__':
    main()
