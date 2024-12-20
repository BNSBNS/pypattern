def batch_data(data, batch_size):
    """Yield successive batches from data."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

data = list(range(10))  # Example data: [0, 1, ..., 9]
batch_size = 3

for batch in batch_data(data, batch_size):
    print(batch)
