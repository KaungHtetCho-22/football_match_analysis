import pickle
import numpy as np

def load_tracks_from_pickle(file_path):
    """Load tracks from a pickle file."""
    with open(file_path, 'rb') as f:
        tracks = pickle.load(f)
    return tracks

def evaluate_tracking_performance(tracks, max_missing_frames=5):
    """
    Evaluate tracking performance including lifespan, fragmentation, ID switches, precision, and recall.

    tracks: Dictionary of tracked objects with positions and track IDs.
    max_missing_frames: Max frames allowed without detection before a track is considered fragmented.
    """
    lifespan = {}
    fragments = {}
    id_switches = 0
    precision = 0
    recall = 0
    total_tracks = 0
    total_detections = 0

    # Store previous tracks to check for ID switches
    previous_tracks = {}

    for object_type in tracks:
        object_tracks = tracks[object_type]

        for frame_num, frame_tracks in enumerate(object_tracks):
            for track_id, track_info in frame_tracks.items():
                if track_id not in lifespan:
                    lifespan[track_id] = 0
                    fragments[track_id] = 1  # Track starts as a fragment
                
                lifespan[track_id] += 1

                # Check if the track is fragmented (lost for more than 'max_missing_frames')
                if track_info.get('fragmented', False):
                    fragments[track_id] += 1

                # Check for ID switches (i.e., if the same object has different track IDs over time)
                if track_id in previous_tracks:
                    if previous_tracks[track_id] != track_info['bbox']:
                        id_switches += 1  # Increment ID switch count
                
                previous_tracks[track_id] = track_info['bbox']

                # Precision and recall calculation (simplified approach)
                if track_info.get('detected', False):  # Assuming detection info exists
                    total_tracks += 1
                    precision += track_info.get('true_positive', 0)
                    recall += track_info.get('true_positive', 0)
                total_detections += 1

    avg_lifespan = np.mean(list(lifespan.values())) if lifespan else 0
    avg_fragments = np.mean(list(fragments.values())) if fragments else 0
    avg_id_switches = id_switches / total_tracks if total_tracks else 0
    avg_precision = precision / total_detections if total_detections else 0
    avg_recall = recall / total_tracks if total_tracks else 0

    return {
        "avg_lifespan": avg_lifespan,
        "avg_fragments": avg_fragments,
        "avg_id_switches": avg_id_switches,
        "avg_precision": avg_precision,
        "avg_recall": avg_recall
    }

# Load tracks from the pickle file
tracks = load_tracks_from_pickle('stubs/track_stubs.pkl')

# Example usage of the evaluation
metrics = evaluate_tracking_performance(tracks)
print(metrics)
