# Signal processing setup
SR = 16000
FFT_HOP = 256
FFT_SIZE = 512
N_MELS = 96

# Machine learning setup
BATCH_SIZE = 1 # size of the batch during prediction

# Output labels
MTT_LABELS = ['guitar', 'classical', 'slow', 'techno', 'strings', 'drums', 'electronic', 'rock', 'fast', 'piano', 'ambient', 'beat', 'violin', 'vocal', 'synth', 'female', 'indian', 'opera', 'male', 'singing', 'vocals', 'no vocals', 'harpsichord', 'loud', 'quiet', 'flute', 'woman', 'male vocal', 'no vocal', 'pop', 'soft', 'sitar', 'solo', 'man', 'classic', 'choir', 'voice', 'new age', 'dance', 'male voice', 'female vocal', 'beats', 'harp', 'cello', 'no voice', 'weird', 'country', 'metal', 'female voice', 'choral']

MSD_LABELS = ['rock','pop','alternative','indie','electronic','female vocalists','dance','00s','alternative rock','jazz','beautiful','metal','chillout','male vocalists','classic rock','soul','indie rock','Mellow','electronica','80s','folk','90s','chill','instrumental','punk','oldies','blues','hard rock','ambient','acoustic','experimental','female vocalist','guitar','Hip-Hop','70s','party','country','easy listening','sexy','catchy','funk','electro','heavy metal','Progressive rock','60s','rnb','indie pop','sad','House','happy']

MTT_LABELS_DICT_IDX = {'genre':[1,3,6,7,16,17,29,34,37,38,46,47],
                       'instrument':[0,4,5,9,12,14,22,25,31,35,42,43,49],
                       'mood': [2,8,23,24,30,45],
                       'style':[10,32],
                       'rhythm':[11,41],
                       'vocal':[13,15,18,19,20,21,26,27,28,33,36,39,40,44,48]
                       }

MSD_LABELS_DICT_IDX = {'genre':[0,1, 2, 3, 4, 6,8,9,11,14,15,16,18,20,24,26,27,33,36,40,41,42,43,45,46,48],
                       'instrument':[32],
                       'mood': [12,17,22,35,37,38,47,49],
                       'style':[23,28,29,30],
                       'vocal':[5,13,31],
                       'eras':[7,19,21,25,34,44],
                       'other':[39]
                       }

MTT_LABELS_DICT_INV = {'genre':['classical','techno','electronic','rock','indian','opera','pop','classic','new age','dance','country','metal'],
                       'instrument':['guitar','strings','drums','piano','violin','synth','harpsichord','flute','sitar','choir','harp','cello','choral'],
                       'mood': ['slow','fast','loud','quiet','soft','weird'],
                       'style': ['ambient','solo'],
                       'rhythm':['beat','beats'],
                       'vocal':['vocal','female','male','singing','vocals','no vocals','woman','male vocal','no vocal','man','voice','male voice','female vocal','no voice','female voice']
                       }

MSD_LABELS_DICT_INV = {'genre':['rock','pop','alternative','indie','electronic','dance','alternative rock','jazz','beautiful','metal','classic rock','soul','indie rock','electronica','folk','punk','blues','hard rock','Hip-Hop','country','funk','electro','heavy metal','Progressive rock','rnb','indie pop','House'],
                       'instrument':['guitar'],
                       'mood': ['chillout','Mellow','chill','party','easy listening','sexy','sad','happy'],
                       'style':['instrumental','ambient','acoustic','experimental'],
                       'vocal':['female vocalists','male vocalists','female vocalist'],
                       'eras':['00s','80s','90s','oldies','70s','60s'],
                       'other':['catchy']
                       }


MTT_LABELS_DICT = {'guitar':'instrument',
                    'classical':'genre',
                    'slow':'mood',
                    'techno':'genre',
                    'strings':'instrument',
                    'drums':'instrument',
                    'electronic':'genre',
                    'rock':'genre',
                    'fast':'mood',
                    'piano':'instrument',
                    'ambient':'style',
                    'beat':'rhythm',
                    'violin':'instrument',
                    'vocal':'vocal',
                    'synth':'instrument',
                    'female':'vocal',
                    'indian':'genre',
                    'opera':'genre',
                    'male': 'vocal',
                    'singing':'vocal',
                    'vocals':'vocal',
                    'no vocals': 'vocal',
                    'harpsichord':'instrument',
                    'loud': 'mood',
                    'quiet':'mood',
                    'flute':'instrument',
                    'woman': 'vocal',
                    'male vocal': 'vocal',
                    'no vocal':'vocal',
                    'pop': 'genre',
                    'soft': 'mood',
                    'sitar': 'instrument',
                    'solo': 'style',
                    'man':'vocal',
                    'classic':'genre',
                    'choir': 'instrument',
                    'voice':'vocal',
                    'new age': 'genre',
                    'dance': 'genre',
                    'male voice': 'vocal',
                    'female vocal': 'vocal',
                    'beats': 'rhythm',
                    'harp': 'instrument',
                    'cello': 'instrument',
                    'no voice': 'voice',
                    'weird': 'mood',
                    'country': 'genre',
                    'metal': 'genre',
                    'female voice': 'vocal',
                    'choral': 'instrument'}

MSD_LABELS_DICT = {'rock':'genre',
                    'pop':'genre',
                    'alternative': 'genre',
                    'indie':'genre',
                    'electronic': 'genre',
                    'female vocalists': 'vocal',
                    'dance': 'genre',
                    '00s': 'eras',
                    'alternative rock': 'genre',
                    'jazz': 'genre',
                    'beautiful':'mood',
                    'metal': 'genre',
                    'chillout': 'mood',
                    'male vocalists': 'vocal',
                    'classic rock':'genre',
                    'soul': 'genre',
                    'indie rock': 'genre',
                    'Mellow': 'mood',
                    'electronica': 'genre',
                    '80s': 'eras',
                    'folk': 'genre',
                    '90s': 'eras',
                    'chill': 'mood',
                    'instrumental': 'style',
                    'punk': 'genre',
                    'oldies': 'eras',
                    'blues': 'genre',
                    'hard rock': 'genre',
                    'ambient': 'style',
                    'acoustic': 'style',
                    'experimental': 'style',
                    'female vocalist': 'vocal',
                    'guitar': 'instrument',
                    'Hip-Hop': 'genre',
                    '70s': 'eras',
                    'party': 'mood',
                    'country': 'genre',
                    'easy listening': 'mood',
                    'sexy': 'mood',
                    'catchy':'other',
                    'funk': 'genre',
                    'electro':'genre',
                    'heavy metal': 'genre',
                    'Progressive rock': 'genre',
                    '60s': 'eras',
                    'rnb':'genre',
                    'indie pop': 'genre',
                    'sad': 'mood',
                    'House':'genre',
                    'happy': 'mood'}