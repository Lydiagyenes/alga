#!/bin/bash

# Tesztesetek száma
NUM_TESTS=10

# A jelszóellenőrző Python szkript neve
SCRIPT="password_cracker.py"

# Az elérési utak megadása az input és output fájlokhoz
INPUT_DIR="test_inputs"
OUTPUT_DIR="test_outputs"
EXPECTED_DIR="expected_outputs"

# Tesztek lefuttatása
for i in $(seq 1 $NUM_TESTS); do
    INPUT_FILE="$INPUT_DIR/test$i.txt"
    OUTPUT_FILE="$OUTPUT_DIR/output$i.txt"
    EXPECTED_FILE="$EXPECTED_DIR/expected$i.txt"
    
    echo "Teszteset $i futtatása..."
    
    # Python szkript futtatása a bemeneti fájl alapján
    python3 $SCRIPT < $INPUT_FILE > $OUTPUT_FILE
    
    # Az eredmények összehasonlítása az elvárt kimenettel
    if diff $OUTPUT_FILE $EXPECTED_FILE > /dev/null; then
        echo "Teszteset $i sikeres!"
    else
        echo "Teszteset $i sikertelen! Eltérés a kimenetben."
    fi
done
