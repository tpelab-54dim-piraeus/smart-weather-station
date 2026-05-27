"""
Δημιουργία ελληνικών MP3 αρχείων για DFPlayer Mini
Φωνή: Microsoft el-GR-AthinaNeural (φυσική ελληνική)

Εγκατάσταση:
    pip install edge-tts

Εκτέλεση:
    python generate_greek_mp3.py

Τα αρχεία αποθηκεύονται στον φάκελο mp3_output/
Αντέγραψέ τα στην κάρτα SD ΜΕ ΤΗ ΣΕΙΡΑ αρίθμησής τους.
"""

import asyncio
import edge_tts
import os

OUTPUT_DIR = "mp3_output"
VOICE      = "el-GR-AthinaNeural"   # Αλλαγή σε "el-GR-NestorasNeural" για ανδρική φωνή

files = {
    # 1–10
    "0001": "ένα",
    "0002": "δύο",
    "0003": "τρία",
    "0004": "τέσσερα",
    "0005": "πέντε",
    "0006": "έξι",
    "0007": "επτά",
    "0008": "οκτώ",
    "0009": "εννέα",
    "0010": "δέκα",
    # Ειδικοί (δεν φτιάχνονται από δεκάδα + μονάδα)
    "0011": "έντεκα",
    "0012": "δώδεκα",
    # Υπόλοιπες Δεκάδες
    "0020": "είκοσι",
    "0030": "τριάντα",
    "0040": "σαράντα",
    "0050": "πενήντα",
    "0060": "εξήντα",
    "0070": "εβδομήντα",
    "0080": "ογδόντα",
    "0090": "ενενήντα",
    # Εκατοντάδες
    "0100": "εκατό",
    "0101": "εκατόν",
    # Μονάδες μέτρησης
    "0120": "b p m",
    "0121": "τοις εκατό",
    "0122": "παλμοί",
    "0123": "οξυγόνο",
    # Μηνύματα
    "0124": "φυσιολογικό",
    "0125": "υψηλό",
    "0126": "χαμηλό",
    "0127": "προσοχή",
}

async def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total = len(files)
    for i, (filename, text) in enumerate(files.items(), 1):
        path = os.path.join(OUTPUT_DIR, f"{filename}.mp3")
        try:
            communicate = edge_tts.Communicate(text, voice=VOICE)
            await communicate.save(path)
            print(f"[{i:2}/{total}] ✓ {filename}.mp3 = «{text}»")
        except Exception as e:
            print(f"[{i:2}/{total}] ✗ {filename}.mp3 ΣΦΑΛΜΑ: {e}")

    print(f"\n✅ Ολοκληρώθηκε! {total} αρχεία στον φάκελο '{OUTPUT_DIR}/'")
    print("\n📋 Επόμενο βήμα:")
    print("   Αντέγραψε τα αρχεία στην κάρτα SD ΜΕ ΤΗ ΣΕΙΡΑ αρίθμησής τους.")
    print("   Φορμάτ κάρτας: FAT32, μέγεθος ≤ 32GB")

if __name__ == "__main__":
    asyncio.run(generate())
