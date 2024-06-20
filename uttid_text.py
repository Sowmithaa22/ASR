import os

def read_utterance_ids(text_file_path):
    """Read utterance IDs from the text file."""
    utterance_ids = []
    with open(text_file_path, 'r') as file:
        for line in file:
            utterance_id = line.split('\t')[0]
            utterance_ids.append(utterance_id)
    return utterance_ids

def read_cluster_ids(km_file_path):
    """Read cluster IDs from a .km file."""
    with open(km_file_path, 'r') as file:
        cluster_ids = file.read().splitlines()
    return cluster_ids

def combine_ids_and_clusters(utterance_ids, cluster_ids):
    """Combine utterance IDs and cluster IDs into a dictionary."""
    combined_data = {}
    min_length = min(len(utterance_ids), len(cluster_ids))
    
    for i in range(min_length):
        combined_data[utterance_ids[i]] = cluster_ids[i]
        
    return combined_data

def save_combined_data_to_file(combined_data, output_file_path):
    """Save the combined data to a specified file."""
    with open(output_file_path, 'w') as output_file:
        for utterance_id, cluster_id in combined_data.items():
            output_file.write(f"{utterance_id}\t{cluster_id}\n")

# Example file paths (replace with your actual file paths)
text_file_path = '/nlsasfs/home/nltm-pilot/malavika/Sowmithaa/Tamil_Units/data/tamil_data/valid/text'
km_file_path = '/nlsasfs/home/nltm-pilot/malavika/Sowmithaa/Tamil_Units/all_units/2000_clus/valid.km'
output_file_path = '/nlsasfs/home/nltm-pilot/malavika/Sowmithaa/Tamil_Units/data/asr2/valid_utt_km.txt'

# Read the utterance IDs and cluster IDs
utterance_ids = read_utterance_ids(text_file_path)
cluster_ids = read_cluster_ids(km_file_path)

# Combine the IDs and clusters
combined_data = combine_ids_and_clusters(utterance_ids, cluster_ids)

# Save the combined data to the output file
save_combined_data_to_file(combined_data, output_file_path)

print(f"Combined data saved to {output_file_path}")
