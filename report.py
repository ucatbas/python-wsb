import pandas as pd
import matplotlib.pyplot as plt
import os

# Read metrics from CSV files
col_labels = ['num_clients', 'total_messages', 'average_latency', 'min_latency', 'max_latency', 'throughput', 'throughput_per_client']

df1 = pd.read_csv('results/websockets.csv', names=col_labels)
df2 = pd.read_csv('results/autobahn-ws.csv', names=col_labels)

# Plot latency metrics comparison
fig, axs = plt.subplots(3, 1, figsize=(9, 12))

# Plot average latency comparison
axs[0].plot(df1['num_clients'], df1['average_latency'], label='Avg Latency Websockets', linestyle='--', marker='o')
axs[0].plot(df1['num_clients'], df2['average_latency'], label='Avg Latency Autobahn-ws', linestyle='--', marker='x')
axs[0].set_xlabel('Number of Clients')
axs[0].set_ylabel('Latency (ms)')
axs[0].set_title('Average Latency Comparison')
axs[0].legend()
axs[0].grid(True)

# Plot minimum latency comparison
axs[1].plot(df1['num_clients'], df1['min_latency'], label='Min Latency Websockets', linestyle='-.', marker='o')
axs[1].plot(df1['num_clients'], df2['min_latency'], label='Min Latency Autobahn-ws', linestyle='-.', marker='x')
axs[1].set_xlabel('Number of Clients')
axs[1].set_ylabel('Latency (ms)')
axs[1].set_title('Minimum Latency Comparison')
axs[1].legend()
axs[1].grid(True)

# Plot maximum latency comparison
axs[2].plot(df1['num_clients'], df1['max_latency'], label='Max Latency Websockets', linestyle=':', marker='o')
axs[2].plot(df1['num_clients'], df2['max_latency'], label='Max Latency Autobahn-ws', linestyle=':', marker='x')
axs[2].set_xlabel('Number of Clients')
axs[2].set_ylabel('Latency (ms)')
axs[2].set_title('Maximum Latency Comparison')
axs[2].legend()
axs[2].grid(True)

# Adjust layout
plt.tight_layout()

# Save latency comparison figure
plt.savefig(os.path.join('results', 'latency_comparison.png'))

# Plot throughput metrics comparison
plt.figure(figsize=(12, 8))

# Plot overall throughput comparison
plt.plot(df1['num_clients'], df1['throughput'], label='Throughput Websockets', linestyle='--', marker='o')
plt.plot(df1['num_clients'], df2['throughput'], label='Throughput Autobahn-ws', linestyle='--', marker='x')

plt.xlabel('Number of Clients')
plt.ylabel('Throughput (msgs/s)')
plt.title('Overall Throughput Comparison')
plt.legend()
plt.grid(True)

# Save overall throughput comparison figure
plt.savefig(os.path.join('results', 'overall_throughput_comparison.png'))

# Plot throughput per client metrics comparison
plt.figure(figsize=(12, 8))

plt.plot(df1['num_clients'], df1['throughput_per_client'], label='Throughput per Client Websockets', linestyle='-.', marker='o')
plt.plot(df1['num_clients'], df2['throughput_per_client'], label='Throughput per Client Autobahn-ws', linestyle='-.', marker='x')

plt.xlabel('Number of Clients')
plt.ylabel('Throughput per Client (msgs/s)')
plt.title('Throughput per Client Comparison')
plt.legend()
plt.grid(True)

# Save throughput per client comparison figure
plt.savefig(os.path.join('results', 'throughput_per_client_comparison.png'))
# Show all plots
plt.show()
