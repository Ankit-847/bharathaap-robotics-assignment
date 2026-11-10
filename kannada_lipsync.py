"""Illustrative timed viseme sequence for 'ಶರಣು ಶರಣಾರ್ಥಿ'.
Not a linguistically complete Kannada phoneme aligner.
"""
PHRASE = "ಶರಣು ಶರಣಾರ್ಥಿ"
# start seconds, duration seconds, viseme label, mouth opening (0..1)
VISEMES = [
    (0.00, 0.35, "SHA_OPEN", 0.70),
    (0.35, 0.35, "RA_OPEN", 0.62),
    (0.70, 0.30, "NU_ROUND", 0.78),
    (1.00, 0.35, "SHA_OPEN", 0.70),
    (1.35, 0.35, "RA_OPEN", 0.62),
    (1.70, 0.30, "NA_OPEN", 0.68),
    (2.00, 0.30, "AR_OPEN", 0.66),
    (2.30, 0.35, "THI_NARROW", 0.35),
    (2.65, 0.40, "I_NARROW", 0.28),
    (3.05, 0.55, "REST", 0.08),
]

def viseme_at(time_s: float):
    for start, duration, name, opening in VISEMES:
        if start <= time_s < start + duration:
            return {"viseme": name, "mouth_opening": opening}
    return {"viseme": "REST", "mouth_opening": 0.08}

if __name__ == "__main__":
    print("Phrase:", PHRASE)
    for item in VISEMES:
        print(item)
