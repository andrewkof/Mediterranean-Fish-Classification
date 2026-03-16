#!/usr/bin/env python3
import csv
import sys
from pathlib import Path


USED_CLASS_NAMES = [
    "Aidablennius sphynx",
    "Apogon imberbis",
    "Arnoglossus laterna",
    "Atherina boyeri",
    "Atherina hepsetus",
    "Boops boops",
    "Bothus podas",
    "Callionymus pusillus",
    "Callionymus risso",
    "Caranx crysos",
    "Chelidonichthys lucerna",
    "Chromis chromis",
    "Coris julis",
    "Dactylopterus volitans",
    "Dasyatis pastinaca",
    "Diplodus annularis",
    "Diplodus puntazzo",
    "Diplodus sargus",
    "Diplodus vulgaris",
    "Echiichthys vipera",
    "Epinephelus costae",
    "Epinephelus marginatus",
    "Fistularia commersonii",
    "Gobius auratus",
    "Gobius bucchichi",
    "Gobius cobitis",
    "Gobius cruentatus",
    "Gobius geniporus",
    "Gobius incognitus",
    "Gobius niger",
    "Gobius paganellus",
    "Gobius vittatus",
    "Hippocampus guttulatus",
    "Hippocampus hippocampus",
    "Labrus bergylta",
    "Labrus merula",
    "Labrus mixtus",
    "Labrus viridis",
    "Lagocephalus sceleratus",
    "Lithognathus mormyrus",
    "Microlipophrys nigriceps",
    "Mugil auratus",
    "Mugil cephalus",
    "Mullus barbatus",
    "Mullus surmuletus",
    "Muraena helena",
    "Oblada melanura",
    "Pagrus pagrus",
    "Parablennius gattorugine",
    "Parablennius incognitus",
    "Parablennius pilicornis",
    "Parablennius rouxi",
    "Parablennius sanguinolentus",
    "Parablennius tentacularis",
    "Parablennius zvonimiri",
    "Parupeneus forsskali",
    "Phycis phycis",
    "Plotosus lineatus",
    "Pomatoschistus marmoratus",
    "Pterois miles",
    "Salaria pavo",
    "Sargocentron rubrum",
    "Sarpa salpa",
    "Sciaena umbra",
    "Scorpaena maderensis",
    "Scorpaena notata",
    "Scorpaena scrofa",
    "Serranus cabrilla",
    "Serranus hepatus",
    "Serranus scriba",
    "Siganus luridus",
    "Siganus rivulatus",
    "Solea solea",
    "Sparisoma cretense",
    "Sparus aurata",
    "Spicara maena",
    "Spicara smaris",
    "Spondyliosoma cantharus",
    "Stephanolepis diaspros",
    "Symphodus cinereus",
    "Symphodus mediterraneus",
    "Symphodus melanocercus",
    "Symphodus ocellatus",
    "Symphodus roissali",
    "Symphodus rostratus",
    "Symphodus tinca",
    "Syngnathus abaster",
    "Syngnathus tenuirostris",
    "Syngnathus typhle",
    "Thalassoma pavo",
    "Thorogobius ephippiatus",
    "Torpedo marmorata",
    "Torquigener flavimaculosus",
    "Trachinus araneus",
    "Trachinus draco",
    "Trachinus radiatus",
    "Tripterygion delaisi",
    "Tripterygion melanurus",
    "Tripterygion tripteronotus",
    "Uranoscopus scaber",
    "Xyrichtys novacula",
]


MAX_LINKS_PER_CLASS = 1000


def main() -> int:
    csv_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if not csv_dir.is_dir():
        print(f"Error: directory not found: {csv_dir}")
        return 1

    output_path = csv_dir / "all_image_links_101.csv"
    total_rows = 0

    with output_path.open("w", encoding="utf-8", newline="") as out_f:
        writer = csv.writer(out_f)
        writer.writerow(["image_id", "class_name", "image_link"])

        total_classes = len(USED_CLASS_NAMES)
        for idx, class_name in enumerate(USED_CLASS_NAMES, start=1):
            print(f"[{idx}/{total_classes}] Processing: {class_name}")
            csv_path = csv_dir / f"{class_name}.csv"

            if not csv_path.is_file():
                print(f"  Missing file: {csv_path.name}")
                continue

            class_rows = 0
            try:
                with csv_path.open("r", encoding="utf-8", newline="") as f:
                    reader = csv.DictReader(f)
                    fieldnames = reader.fieldnames or []
                    if "image_url" not in fieldnames:
                        print(f"  Skipping {csv_path.name}: missing image_url column")
                        continue
                    if "id" not in fieldnames:
                        print(f"  Skipping {csv_path.name}: missing id column")
                        continue

                    for row in reader:
                        if class_rows >= MAX_LINKS_PER_CLASS:
                            break

                        image_id = (row.get("id") or "").strip()
                        image_link = (row.get("image_url") or "").strip()
                        if not image_link:
                            continue

                        writer.writerow([image_id, class_name, image_link])
                        class_rows += 1
                        total_rows += 1
            except Exception as e:
                print(f"  Error while reading {csv_path.name}: {e}")
                continue

            print(f"  Saved {class_rows} links (max {MAX_LINKS_PER_CLASS})")

    print(f"\nSaved combined file to: {output_path}")
    print(f"Total image links saved: {total_rows}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
