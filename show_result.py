import os
import sys
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [14, 8]

from pytracking.analysis.plot_results import plot_results, print_results, print_per_sequence_results
from pytracking.evaluation import Tracker, get_dataset, trackerlist
from pytracking.analysis.playback_results import playback_two_results, playback_results


trackers = []
trackers.extend(trackerlist('bh', 'default', 1, 'bh'))

dataset = get_dataset('otb')
"""
plot_results(trackers, dataset, 'OTB', merge_results=True, plot_types=('success', 'prec'), 
             skip_missing_seq=False, force_evaluation=True, plot_bin_gap=0.05, exclude_invalid_frames=False)
"""
for seq in dataset:

   playback_two_results(trackers,seq)
