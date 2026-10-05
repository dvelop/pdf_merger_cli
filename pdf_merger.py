import os
from pathlib import Path
import sys
from pypdf import PdfWriter
import questionary

# Aktiviert ANSI-Escape-Sequenzen in Windows-Konsolen für korrekte Farben/Pfeile
if sys.platform == "win32":
    os.system("color")


def find_pdf_files(search_dir="."):
    """Sucht rekursiv nach allen PDF-Dateien im angegebenen Ordner."""
    path = Path(search_dir)
    return sorted([str(p.resolve()) for p in path.rglob("*.pdf")])


def main():
    print("\n=== Interaktiver PDF Merger ===\n")

    try:
        # 1. Suchverzeichnis festlegen
        start_dir = questionary.text(
            "In welchem Ordner soll nach PDFs gesucht werden?",
            default=".",
        ).ask()

        if start_dir is None:
            print("\n👋 Vorgang abgebrochen.")
            return

        if not os.path.exists(start_dir):
            print("🔴 Der angegebene Pfad existiert nicht.")
            return

        print("🔎 Suche nach PDF-Dateien...")
        pdf_files = find_pdf_files(start_dir)

        if not pdf_files:
            print("❌ Keine PDF-Dateien im angegebenen Ordner gefunden.")
            return

        # Relative Pfade für die Anzeige im Menü erstellen
        display_map = {}
        for full_path in pdf_files:
            try:
                rel_path = os.path.relpath(full_path, start_dir)
            except ValueError:
                rel_path = full_path
            display_map[rel_path] = full_path

        # 2. Mehrfachauswahl der PDFs
        selected_display_names = questionary.checkbox(
            "Wähle die PDF-Dateien aus (Leertaste = Auswählen, Eingabe = Bestätigen):",
            choices=list(display_map.keys()),
        ).ask()

        if not selected_display_names:
            print("\n⚠️ Keine Dateien ausgewählt. Vorgang abgebrochen.")
            return

        selected_files = [display_map[name] for name in selected_display_names]

        # 3. Reihenfolge anpassen
        print("\n--- Reihenfolge anpassen ---")
        ordered_files = []
        remaining_files = selected_files.copy()

        while remaining_files:
            if len(remaining_files) == 1:
                ordered_files.append(remaining_files.pop(0))
                break

            choices = [
                f
                for display, full in display_map.items()
                if full in remaining_files
            ]

            chosen_display = questionary.select(
                f"Wähle die Datei für Position #{len(ordered_files) + 1}:",
                choices=choices,
            ).ask()

            if chosen_display is None:
                print("\n👋 Vorgang abgebrochen.")
                return

            chosen_full = display_map[chosen_display]
            ordered_files.append(chosen_full)
            remaining_files.remove(chosen_full)

        # 4. Zusammenfassung & Bestätigung
        print("\n📋 Finale Reihenfolge der Dokumente:")
        for idx, filepath in enumerate(ordered_files, start=1):
            print(f"  {idx}. {os.path.basename(filepath)}")

        output_filename = questionary.text(
            "\nWie soll die zusammengeführte Datei heißen?",
            default="zusammengefuehrt.pdf",
        ).ask()

        if output_filename is None:
            print("\n👋 Vorgang abgebrochen.")
            return

        if not output_filename.endswith(".pdf"):
            output_filename += ".pdf"

        # 5. PDFs zusammenführen
        merger = PdfWriter()
        try:
            for filepath in ordered_files:
                merger.append(filepath)

            merger.write(output_filename)
            merger.close()

            print(
                f"\n✅ Erfolg! Datei wurde gespeichert als: {os.path.abspath(output_filename)}\n"
            )
        except Exception as e:
            print(f"\n🔴 Fehler beim Zusammenführen der PDFs: {e}\n")

    except KeyboardInterrupt:
        print("\n\n👋 Programm durch Tastenkombination (Strg+C) beendet.")


if __name__ == "__main__":
    main()
