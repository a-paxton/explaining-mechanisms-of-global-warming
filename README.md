# Multimodal dynamics of explaining the mechanisms of global warming

This repo contains the Jupyter notebooks for the analyses underlying *Multimodal dynamics of explaining the mechanisms of global warming* (Paxton, Abney, Castellanos, & Sepulveda, 2016), a poster presented at the 2016 Annual Conference of the Cognitive Science Society.

Due to ethical considerations for participant privacy, we cannot publicly share files that include participant data.

## Overview of experiment procedures

In the current experiment, we asked participants to watch a 5-minute video explaining the mechanisms behind global warming (["How Global Warming Works in Under 5 Minutes"](http://www.howglobalwarmingworks.org/); Ranney, Lamprey, Reinholz, Le, Ranney, & Goldwasser, 2013).  After watching the video (and a 30-second waiting period), participants were asked to explain the mechanisms aloud in less than 2 minutes so that a future participant could learn the information.  

Participants' gaze and attention throughout the experiment were captured using a remote eye-tracker ([SMI Red-m](https://www.smivision.com/eye-tracking/product/red250mobile-eye-tracker)).

Comprehension was derived as the similarity between each participant's explanation and the video's transcript using latent semantic analysis (LSA) implemented in the `LSAfun` package in R (Gunther, Dudschig, & Kaup, 2015).

## Overview of repo contents

This repo contains several Jupyter notebooks, supplementary analysis files, figures, and a copy of the poster.

* `dyn_exp-step2-data_cleaning.ipynb`: A Jupyter notebook running a Python kernel to clean up participants' transcripts.
* `dyn_exp-step3-data_preparation.ipynb`: A Jupyter notebook running an R kernel to prepare data for later analysis.
* `dyn_exp-step4-data_analysis.ipynb`: A Jupyter notebook running an R kernel to execute the data analysis plan for the current project.
* `dyn_exp-poster-cogsci-2016.pdf`: A PDF of the poster.
* `figures/`: A directory containing all images produced by the Jupyter notebooks.
* `supplementary_code`: A directory containing additional files to help clean the data (e.g., defining new functions, importing libraries).
* `global-warming-transcript.txt`: A transcript of the video watched by participants (["How Global Warming Works in Under 5 Minutes"](http://www.howglobalwarmingworks.org/); Ranney, Lamprey, Reinholz, Le, Ranney, & Goldwasser, 2013).
