"""
Export Engine

Exports evaluation results into JSON and CSV formats.
"""

import csv
import json
from pathlib import Path
from typing import Dict, List


class ExportEngine:

    def export_json(
        self,
        data: Dict,
        filename: str
    ) -> None:

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def export_csv(
        self,
        rows: List[Dict],
        filename: str
    ) -> None:

        if not rows:
            return

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=rows[0].keys()
            )

            writer.writeheader()

            writer.writerows(rows)

    def create_output_directory(
        self,
        directory: str
    ) -> Path:

        path = Path(directory)

        path.mkdir(
            parents=True,
            exist_ok=True
        )

        return path


if __name__ == "__main__":

    exporter = ExportEngine()

    sample = {

        "overall_score": 9.2,

        "confidence": 0.94

    }

    exporter.export_json(
        sample,
        "evaluation.json"
    )

    exporter.export_csv(

        [

            sample

        ],

        "evaluation.csv"

    )

    print("Export complete.")
