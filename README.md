### Hi, I'm Zubair

I am an **Assistant Professor** of Computer Science in **Higher Education Department**, Khyber Pakhtunkhwa, Pakistan. I am pursuing my PhD in Machine Learning at the **University of Malakand**, Pakistan, 

I train M.L models and then evaluate them in adversarial conditions, finding out their weaknesses and ways to improve their accuracy and reliability. my projects ask one of two questions:

- **Does the evaluation tell the truth?** A detector at 0.98 ROC-AUC can miss a third of next year's malware, and an ECG model can gain accuracy while it stops finding ventricular beats.
- **Does the model know when it should not be trusted?** It should say "not sure", raise its uncertainty when the input moves away from training, and resist text written to manipulate it.

Open to PhD positions in robust and trustworthy ML.

---

#### Featured

**[Noise-robust ECG classification](https://github.com/Zubair-DLCS/Noise-robust-ECG-classification)**: a robustness and calibration audit of heartbeat classification on unseen patients (MIT-BIH, inter-patient split) under real recorded noise. Under muscle artefact, accuracy *rises* from 0.84 to 0.88 and calibration error stays below 0.05, while detection of ventricular beats falls from F1 0.74 to 0.24. Every standard metric reports a healthy model. Noise augmentation protects ventricular beats but sacrifices supraventricular ones.

<a href="https://github.com/Zubair-DLCS/Noise-robust-ECG-classification"><img src="https://raw.githubusercontent.com/Zubair-DLCS/Noise-robust-ECG-classification/main/results/fig4_per_class.png" alt="Accuracy stays high under muscle artefact while ventricular-beat F1 collapses" width="720"></a>

**[Malicious npm drift](https://github.com/Zubair-DLCS/malicious-npm-drift)**: an explainable static detector for malicious npm packages, built on real malware from the DataDog dataset and benign packages drawn at random from the whole registry. Under a random split it scores 0.98 ROC-AUC. Trained on 2024 malware and tested on 2026, it catches 63% of malicious packages at a 1% false-alarm rate instead of 86%. The reason is in the misses: 73% of the 2026 malware it missed ships a README and only 9% uses an install hook, against 26% and 91% for the malware it caught. The malware learned to look like ordinary software.

**[Gatecrasher](https://github.com/Zubair-DLCS/Gatecrasher-Audit-Aware-Adversaries-Robustness-and-the-Verification-of-Trustworthiness-Claims-in-ML)**: what empirical audits of privacy, robustness and fairness claims can actually settle. Re-running one audit 300 times on one unchanged model leaves an indeterminate band of claim thresholds it cannot decide: 0.40 wide for an equalised-odds audit at 100 queries. A canary privacy audit passes a model with no privacy protection at all 94% of the time at 20 canaries, and the same model reports 0.82 or 0.34 robust accuracy depending only on how hard the auditor attacks. Proposes claim cards that carry the band, so PASS can be told apart from "this audit cannot tell".

#### Attacks on AI agents and on machine-made evidence

**[Poisoned Papers](https://github.com/Zubair-DLCS/Poisoned-Papers)**: can one hidden sentence in an abstract hijack an AI agent that screens papers for a systematic review? Uses real screening decisions from four software-engineering reviews (23,436 abstracts). A pattern filter that sends suspicious records to a human flags only 17 genuine abstracts (0.07%) and catches all five attacks it was written against, but none of ten other phrasings of the same attack, and it cannot see a plain relevance claim at all. The attack-and-defence grid on open models (prompt warnings, spotlighting, the filter) is running now.

**[Show, Don't Cite](https://github.com/Zubair-DLCS/show-dont-cite)**: an answer engine that backs technical claims with runnable proofs of concept instead of links, and a test for when such a proof proves nothing. For each claim the prover writes one PoC for the claim and, in a separate call, one for its negation; if both pass, the evidence is hollow. On a 66-claim benchmark whose labels are all verified by execution, a prover that hides an always-true condition gets every false claim accepted with a single PoC and slips past a static linter every time; the negation check rejects all of them without reading the code. Runs with real language models are next.

**[Campaign Investigator](https://github.com/Zubair-DLCS/campaign-investigator)**: a language-model agent that investigates coordinated networks with the Beyond Copy-Paste detectors as its tools. The detectors' clusters always contain every campaign account (perfect choice would score F1 1.00), yet the best fixed rule reaches 0.73 and two open-model agents 0.41 and 0.18: they accuse someone in every case with no campaign, ignore the signal that exposes AI-rewritten campaigns, and stop at the first campaign they find.

#### AI in my own classroom

Both apps run on an ordinary Windows laptop, keep no video or audio, and come with an installer so another teacher can try them.

**[ClassWatch](https://github.com/Zubair-DLCS/ClassWatch)**: a live webcam demo for a classroom (hands raised, head direction, phones, door in and out, faces blurred) and a research model for the hard case a teacher cannot see from the front: *thinking hard* versus *mind wandering*. It fuses gaze and head-pose features with activity logs and answers "not sure" when unsure. On simulated learners, comparing each learner with their own baseline adds 8 F1 points, more than adding a second signal (3 points). With the alert threshold set to spare thinkers, about 1 thinking student in 11 is still flagged, so the output is designed as a quiet hint to the teacher, never a mark against the student.

**[PairWatch](https://github.com/Zubair-DLCS/PairWatch)**: two students, one laptop, six C++ tasks. It measures who talks, where each student looks, whether both look at the same part of the code more often than chance, who types and how often roles switch, and sets all of it against tasks solved and compile errors. A built-in condition test measures when webcam sensing breaks in real Pakistani classrooms: dim light, a window behind the student, UPS light during a power cut, back benches, glasses, headscarves and covered faces.

#### Information integrity

**[Discourse-SINR](https://github.com/Zubair-DLCS/Discourse-SINR)** (simulation): treats coordinated influence campaigns as jammers in the information space, measures how much coordination drowns out authentic voices, tests whether detectors survive adaptive adversaries, and quantifies what mitigation costs real users.

**[Beyond Copy-Paste](https://github.com/Zubair-DLCS/beyond-copy-paste)** (real text, simulated behaviour): detecting coordinated campaigns that paraphrase with AI. Exact matching recognises 0% of AI rewrites and semantic similarity 91%. A detector trained on other campaigns holds 0.97 average precision under combined evasion. It also measures what privacy protections (hashing, coarse timestamps, differential privacy) cost detection.

**[Two Clocks](https://github.com/Zubair-DLCS/two-clocks)**: forensics of 1.79 M tweets from Russia's Internet Research Agency. Two natural experiments (US daylight-saving changes and national holidays) show that personas posing as Americans don't run on American time. Language models recover each account's role (macro-F1 0.94), and network analysis exposes units that relay identical posts within minutes.

**[Engineered Emotion](https://github.com/Zubair-DLCS/engineered-emotion)**: an emotion detector (GoEmotions, 0.59 macro-F1 vs BERT's 0.64) applied to 3,498 IRA Facebook ads with real clicks and spend. Negative emotion earned 33% higher click odds, and emotion AI systematically under-reads propaganda, which induces fear without expressing it.

**[One Language, Two Borders](https://github.com/Zubair-DLCS/south-asia-discourse)**: online hostility in Pakistani Roman Urdu and Indian Hindi-English social media. An Indian-trained detector transfers to Pakistan (AUC 0.86) but not the reverse (0.71), because the datasets define hostility differently, not because the language differs.

#### Signals, sensors and satellites

**SpectroJam-Net** (HEC Pakistan NRPU project, code not public): deep learning for spectrogram-based RF jamming detection with CNNs and Vision Transformers, plus the SpectroJam-Synth pipeline for synthetic signal datasets (QPSK, OFDM, STFT).

**[SAR flood shift](https://github.com/Zubair-DLCS/sar-flood-shift)** (experiments in progress): Sentinel-1 radar flood mapping with a U-Net and deep ensembles, trained on Sen1Floods11 and tested on a held-out country (Bolivia) and on the 2022 Sindh floods, where the event, the year and the SAR product all differ from training. The question is whether the ensemble's uncertainty map rises where its water map goes wrong: over flooded farmland, wind-roughened water and dry sand.

**[Sensors That Know](https://github.com/Zubair-DLCS/sensors-that-know)**: how much "harmless" smart-building sensors reveal about people. An office's air-quality monitor (CO2, temperature, humidity) reconstructs arrivals and departures to within about 30 minutes (occupancy AUC 0.95), and a home's bathroom humidity sensor alone keeps a diary of 158 showers in 137 days. Averaging, rounding and noise buy privacy only by breaking the device's purpose; computing alerts on the device keeps the service and cuts the leak most, but not to zero.

#### Publications
- Khan, Zubair, et al. "Taxonomy of Cybersecurity Challenges and Solutions for the Superintelligent Systems." *Information and Software Technology* (2026): 108152.
- Two further manuscripts under review (*IEEE Transactions on Cognitive Communications and Networking*; *Journal of Network and Computer Applications*).

#### Current work
- A cross-domain review of interference detection, estimation and removal across RF communications and biomedical signals (ECG, EEG, MRI).
- Running the language-model experiments for Poisoned Papers and Show, Don't Cite, and the Sindh case study for SAR flood shift.

#### Tools
Python · PyTorch · scikit-learn · SHAP · Hugging Face Transformers · Ollama · MediaPipe · OpenCV · rasterio/xarray · NumPy/SciPy · wfdb · NetworkX · GNU Radio · C++ · LaTeX

#### Contact
[mzee.uom@gmail.com](mailto:mzee.uom@gmail.com)
