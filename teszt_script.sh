#!/bin/bash

# Tesztelési fájlok könyvtára
INPUT_DIR="test_cases"
OUTPUT_DIR="test_cases"

# Python program fájl
PROGRAM="main.py"

# Ellenőrizzük, hogy minden szükséges fájl létezik-e
if [ ! -f "$PROGRAM" ]; then
  echo "Python program fájl ($PROGRAM) nem található!"
  exit 1
fi

# Ellenőrizzük a bemeneti fájlokat
for i in {1..10}; do
  INPUT_FILE="$INPUT_DIR/input$i.txt"
  OUTPUT_FILE="$OUTPUT_DIR/output$i.txt"
  
  if [ ! -f "$INPUT_FILE" ]; then
    echo "Bemeneti fájl ($INPUT_FILE) hiányzik!"
    exit 1
  fi

  if [ ! -f "$OUTPUT_FILE" ]; then
    echo "Elvárt kimeneti fájl ($OUTPUT_FILE) hiányzik!"
    exit 1
  fi
done

# Minden teszteset ellenőrzése
echo "Tesztelés indítása..."
for i in {1..10}; do
  INPUT_FILE="$INPUT_DIR/input$i.txt"
  OUTPUT_FILE="$OUTPUT_DIR/output$i.txt"

  # Futtassuk a Python programot az adott bemenettel
  ACTUAL_OUTPUT=$(python3 "$PROGRAM" < "$INPUT_FILE")

  # Hasonlítsuk össze a kimenetet az elvárt eredménnyel
  EXPECTED_OUTPUT=$(cat "$OUTPUT_FILE")

  if [ "$ACTUAL_OUTPUT" == "$EXPECTED_OUTPUT" ]; then
    echo "Teszt $i: Sikeres"
  else
    echo "Teszt $i: Sikertelen"
    echo "Várt eredmény: $EXPECTED_OUTPUT"
    echo "Kapott eredmény: $ACTUAL_OUTPUT"
  fi
done
