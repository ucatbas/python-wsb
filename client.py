import asyncio
import websockets
import time
import csv


def extract(results, num_clients, duration, path):
    latencies = [latency for client_latencies in results for latency in client_latencies]
    total_messages = len(latencies)
    average_latency = sum(latencies) / total_messages
    min_latency = min(latencies)
    max_latency = max(latencies)
    throughput = total_messages / duration
    throughput_per_client = throughput / num_clients

    metrics = [
        num_clients,
        total_messages,
        average_latency * 1000,
        min_latency * 1000,
        max_latency * 1000,
        throughput,
        throughput_per_client
    ]

    with open(path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(metrics)


async def connect_and_send(uri, message, duration):
    async with websockets.connect(uri) as websocket:
        end_time = time.time() + duration
        latencies = []
        while time.time() < end_time:
            start_time = time.time()
            await websocket.send(message)
            await websocket.recv()
            latencies.append(time.time() - start_time)
        
        return latencies



async def run(uri, message, num_clients, duration, path):
    tasks = [connect_and_send(uri, message, duration) for _ in range(num_clients)]
    results = await asyncio.gather(*tasks)
    extract(results, num_clients, duration, path)


async def ws():
    uri = "ws://localhost:5001"    
    for num_clients in range(100,200):
        await run(uri, 'xxx', num_clients, 3, "results/websockets.csv")

async def autobahn_ws():
    uri = "ws://localhost:5002"    
    for num_clients in range(100,200):
        await run(uri, 'xxx', num_clients, 3, "results/autobahn-ws.csv")

asyncio.run(ws())
asyncio.run(autobahn_ws())
