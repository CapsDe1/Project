K_FOLD = 10
NAME = "wavelet"

HOME_URL = ""

DATA_URL = f"{HOME_URL}/data"

LEARN_URL = f"{HOME_URL}/{NAME}"

# original url
ORIGINAL_URL_COMMON = f"{DATA_URL}/original/group"
ORIGINAL_URL = {
    "common": ORIGINAL_URL_COMMON,
    "HC": f"{ORIGINAL_URL_COMMON}/HC",
    "ADHD": f"{ORIGINAL_URL_COMMON}/ADHD"
}

# raw url
RAW_URL_COMMON = f"{DATA_URL}/raw"
RAW_URL = {
    "common": RAW_URL_COMMON,
    "HC": f"{RAW_URL_COMMON}/HC",
    "ADHD": f"{RAW_URL_COMMON}/ADHD"
}

# segment url
SEGMENTS_URL_COMMON = f"{DATA_URL}/segments"
SEGMENTS_URL = {
    "common": SEGMENTS_URL_COMMON,
    "HC": f"{SEGMENTS_URL_COMMON}/HC",
    "ADHD": f"{SEGMENTS_URL_COMMON}/ADHD"
}

# PSD url
PSD_URL_COMMON = f"{DATA_URL}/PSD"
PSD_URL = {
    "common":  PSD_URL_COMMON,
    "HC": f"{ PSD_URL_COMMON}/HC",
    "ADHD": f"{ PSD_URL_COMMON}/ADHD"
}

# augmentation url
AUGMENTATION_URL_COMMON = f"{DATA_URL}/augmentation"
AUGMENTATION_URL = {
    "common":  AUGMENTATION_URL_COMMON,
    "HC": f"{ AUGMENTATION_URL_COMMON}/HC",
    "ADHD": f"{ AUGMENTATION_URL_COMMON}/ADHD"
}

WAVELET_SEGMENTS_URL_COMMON = f"{DATA_URL}/wavelet_segmentation"
WAVELET_SEGMENTS_URL = {
    "common":  WAVELET_SEGMENTS_URL_COMMON,
    "HC": f"{ WAVELET_SEGMENTS_URL_COMMON}/HC",
    "ADHD": f"{ WAVELET_SEGMENTS_URL_COMMON}/ADHD"
}

WAVELET_CWT_URL_COMMON = f"{DATA_URL}/wavelet_CWT"
WAVELET_CWT_URL = {
    "common":  WAVELET_CWT_URL_COMMON,
    "HC": f"{ WAVELET_CWT_URL_COMMON}/HC",
    "ADHD": f"{ WAVELET_CWT_URL_COMMON}/ADHD"
}

WAVELET_CORRELATION_URL_COMMON = f"{DATA_URL}/wavelet_correlation"
WAVELET_CORRELATION_URL = {
    "common":  WAVELET_CORRELATION_URL_COMMON,
    "HC": f"{ WAVELET_CORRELATION_URL_COMMON}/HC",
    "ADHD": f"{ WAVELET_CORRELATION_URL_COMMON}/ADHD"
}



X_PATH_AND_Y_URL = [
    (f"{PSD_URL['HC']}", "HC"),
    (f"{PSD_URL['ADHD']}", "ADHD")
]

AUG_X_PATH_AND_Y_URL = [
    (f"{AUGMENTATION_URL['HC']}", "HC"),
    (f"{AUGMENTATION_URL['ADHD']}", "ADHD")
]

FOLD_URL = f"{LEARN_URL}/fold"

# fold i url
FOLD_I_URL = {
    i: {
        "test": { "HC": f"{FOLD_URL}/fold_{i}/test/HC",
                  "ADHD": f"{FOLD_URL}/fold_{i}/test/ADHD" },
        "validation": { "HC": f"{FOLD_URL}/fold_{i}/validation/HC",
                        "ADHD": f"{FOLD_URL}/fold_{i}/validation/ADHD" },
        "train": { "HC": f"{FOLD_URL}/fold_{i}/train/HC",
                   "ADHD": f"{FOLD_URL}/fold_{i}/train/ADHD" }
    }
    for i in range(K_FOLD)
}

AUG_FOLD_URL = f"{LEARN_URL}/aug_fold"
AUG_FOLD_I_URL = {
    i: {
        "test": { "HC": f"{AUG_FOLD_URL}/fold_{i}/test/HC",
                  "ADHD": f"{AUG_FOLD_URL}/fold_{i}/test/ADHD" },
        "validation": { "HC": f"{AUG_FOLD_URL}/fold_{i}/validation/HC",
                        "ADHD": f"{AUG_FOLD_URL}/fold_{i}/validation/ADHD" },
        "train": { "HC": f"{AUG_FOLD_URL}/fold_{i}/train/HC",
                   "ADHD": f"{AUG_FOLD_URL}/fold_{i}/train/ADHD" }
    }
    for i in range(K_FOLD)
}

# fold i test subject url
FOLD_I_TEST_SUBJECT_URL = {
    0 : ['v10p', 'v12p', 'v19p', 'v206', 'v20p', 'v284', 'v288', 'v111', 'v118', 'v133', 'v48p', 'v49p', 'v50p'],
    1 : ['v183', 'v204', 'v238', 'v25p', 'v33p', 'v38p', 'v120', 'v125', 'v140', 'v41p', 'v58p', 'v60p'],
    2: ['v173', 'v198', 'v200', 'v231', 'v35p', 'v3p', 'v300', 'v302', 'v307', 'v44p', 'v54p', 'v55p'],
    3: ['v215', 'v250', 'v286', 'v31p', 'v34p', 'v37p', 'v107', 'v121', 'v127', 'v151', 'v303', 'v304'],
    4: ['v227', 'v236', 'v244', 'v24p', 'v279', 'v40p', 'v113', 'v114', 'v134', 'v147', 'v43p', 'v45p'],
    5: ['v15p', 'v179', 'v190', 'v246', 'v263', 'v30p', 'v115', 'v297', 'v308', 'v42p', 'v53p', 'v56p'],
    6: ['v18p', 'v209', 'v274', 'v29p', 'v39p', 'v8p', 'v112', 'v143', 'v298', 'v305', 'v47p', 'v51p'],
    7: ['v14p', 'v213', 'v219', 'v254', 'v27p', 'v28p', 'v108', 'v109', 'v138', 'v149', 'v57p', 'v59p'],
    8: ['v181', 'v1p', 'v21p', 'v265', 'v32p', 'v6p', 'v110', 'v117', 'v123', 'v310', 'v46p', 'v52p'],
    9: ['v177', 'v196', 'v22p', 'v234', 'v270', 'v36p', 'v116', 'v129', 'v131', 'v299', 'v306', 'v309'],
}

WEIGHT_URL = f"{LEARN_URL}/weight"
# weight i url
WEIGHT_I_URL = {
    i: {
        "acc": f"{WEIGHT_URL}/fold_{i}/acc",
        "loss": f"{WEIGHT_URL}/fold_{i}/loss",
        "fitted": f"{WEIGHT_URL}/fold_{i}/fitted"
    }
    for i in range(K_FOLD)
}

HISTORY_URL = f"{LEARN_URL}/history"
# history i url
HISTORY_I_URL = {
    i: f"{HISTORY_URL}/fold_{i}"
    for i in range(K_FOLD)
}
