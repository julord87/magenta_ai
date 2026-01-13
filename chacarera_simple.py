import note_seq
from note_seq.protobuf import music_pb2

print("Generando MIDI de chacarera...")

# Crear secuenciaa
sequence = music_pb2.NoteSequence()
sequence.tempos.add().qpm = 110
sequence.time_signatures.add(numerator=4, denominator=4)

beat_length = 60.0 / 110

# Patrón de rasgueo de chacarera (corcheas con acentos)
# En chacarera típicamente: fuerte-débil-débil-fuerte-débil-débil-fuerte-débil
velocities = [90, 60, 60, 85, 60, 60, 80, 60]
rasgueo_beats = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]

# Am (compás 1: beats 0-4)
am_notes = [57, 60, 64, 69]  # A, C, E, A (más fullness)
for i, beat in enumerate(rasgueo_beats):
    for pitch in am_notes:
        sequence.notes.add(
            pitch=pitch,
            start_time=(0 + beat) * beat_length,
            end_time=(0 + beat + 0.35) * beat_length,
            velocity=velocities[i],
            instrument=0,
            program=25  # Steel Guitar
        )

# Bm (compás 2: beats 4-8)
bm_notes = [59, 62, 66, 71]  # B, D, F#, B
for i, beat in enumerate(rasgueo_beats):
    for pitch in bm_notes:
        sequence.notes.add(
            pitch=pitch,
            start_time=(4 + beat) * beat_length,
            end_time=(4 + beat + 0.35) * beat_length,
            velocity=velocities[i],
            instrument=0,
            program=25
        )

# Em (compás 3: beats 8-12)
em_notes = [64, 67, 71, 76]  # E, G, B, E
for i, beat in enumerate(rasgueo_beats):
    for pitch in em_notes:
        sequence.notes.add(
            pitch=pitch,
            start_time=(8 + beat) * beat_length,
            end_time=(8 + beat + 0.35) * beat_length,
            velocity=velocities[i],
            instrument=0,
            program=25
        )

# E7 (compás 4: beats 12-16)
e7_notes = [64, 68, 71, 74]  # E, G#, B, D
for i, beat in enumerate(rasgueo_beats):
    for pitch in e7_notes:
        sequence.notes.add(
            pitch=pitch,
            start_time=(12 + beat) * beat_length,
            end_time=(12 + beat + 0.35) * beat_length,
            velocity=velocities[i],
            instrument=0,
            program=25
        )

sequence.total_time = 16 * beat_length

# Guardar
filename = 'chacarera_guitarra.mid'
note_seq.sequence_proto_to_midi_file(sequence, filename)
print(f"✓ Archivo creado: {filename}")
print("\nImporta este MIDI a Cubase y carga tu VST de guitarra favorito")