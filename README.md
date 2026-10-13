### Hi, I'm Zubair

PhD researcher in machine learning at the **University of Malakand**, Pakistan, and Assistant Professor of Computer Science.

I study **when machine learning stops being trustworthy because its input is corrupted, manipulated or attacked**, and how to detect that before it causes harm. I work in two settings that share one structure:

- **Physical signals.** Noise in ECG recordings and jamming in RF spectrum hide the signal a model needs.
- **Information.** Coordinated campaigns raise the "interference floor" of online discourse and drown out authentic voices.

**The question behind every project:** can we detect, measure and remove interference without silencing the signal we care about, and can a model tell us when it should not be trusted?

Open to PhD positions in robust and trustworthy ML.

---

#### Featured: trustworthy ML under signal interference

**[Noise-robust ECG classification](https://github.com/Zubair-DLCS/Noise-robust-ECG-classification)**: a robustness and calibration audit of heartbeat classification on unseen patients (MIT-BIH, inter-patient split) under real recorded noise. Under muscle artefact, accuracy *rises* from 0.84 to 0.88 and calibration error stays below 0.05, while detection of ventricular beats falls from F1 0.74 to 0.24. Every standard metric reports a healthy model. Noise augmentation protects ventricular beats but sacrifices supraventricular ones.

<a href="https://github.com/Zubair-DLCS/Noise-robust-ECG-classification"><img src="https://raw.githubusercontent.com/Zubair-DLCS/Noise-robust-ECG-classification/main/results/fig4_per_class.png" alt="Accuracy stays high under muscle artefact while ventricular-beat F1 collapses" width="720"></a>

**SpectroJam-Net** (HEC Pakistan NRPU project, code not public): deep learning for spectrogram-based RF jamming detection with CNNs and Vision Transformers, plus the SpectroJam-Synth pipeline for synthetic signal datasets (QPSK, OFDM, STFT).

#### Trustworthy ML for information integrity

**[Discourse-SINR](https://github.com/Zubair-DLCS/Discourse-SINR)** (simulation): the bridge between my two settings. It treats coordinated influence campaigns as jammers in the information space, measures how much coordination drowns out authentic voices, tests whether detectors survive adaptive adversaries, and quantifies what mitigation costs real users.

**[Beyond Copy-Paste](https://github.com/Zubair-DLCS/beyond-copy-paste)** (real text, simulated behaviour): detecting coordinated campaigns that paraphrase with AI. Exact matching recognises 0% of AI rewrites and semantic similarity 91%. A detector trained on other campaigns holds 0.97 average precision under combined evasion. It also measures what privacy protections (hashing, coarse timestamps, differential privacy) cost detection.

**[Two Clocks](https://github.com/Zubair-DLCS/two-clocks)**: forensics of 1.79 M tweets from Russia's Internet Research Agency. Two natural experiments (US daylight-saving changes and national holidays) show that personas posing as Americans don't run on American time. Language models recover each account's role (macro-F1 0.94), and network analysis exposes units that relay identical posts within minutes.

**[Engineered Emotion](https://github.com/Zubair-DLCS/engineered-emotion)**: an emotion detector (GoEmotions, 0.59 macro-F1 vs BERT's 0.64) applied to 3,498 IRA Facebook ads with real clicks and spend. Negative emotion earned 33% higher click odds, and emotion AI systematically under-reads propaganda, which induces fear without expressing it.

**[One Language, Two Borders](https://github.com/Zubair-DLCS/south-asia-discourse)**: online hostility in Pakistani Roman Urdu and Indian Hindi-English social media. An Indian-trained detector transfers to Pakistan (AUC 0.86) but not the reverse (0.71), because the datasets define hostility differently, not because the language differs.

#### Publications
- Khan, Zubair, et al. "Taxonomy of Cybersecurity Challenges and Solutions for the Superintelligent Systems." *Information and Software Technology* (2026): 108152.
- Two further manuscripts under review (*IEEE Transactions on Cognitive Communications and Networking*; *Journal of Network and Computer Applications*).

#### Current work
- A cross-domain review of interference detection, estimation and removal across RF communications and biomedical signals (ECG, EEG, MRI).

#### Tools
Python · PyTorch · scikit-learn · NumPy/SciPy · wfdb · NetworkX · GNU Radio · LaTeX

#### Contact
[mzee.uom@gmail.com](mailto:mzee.uom@gmail.com)
