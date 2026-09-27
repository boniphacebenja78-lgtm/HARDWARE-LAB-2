import os
import time
import matplotlib.pyplot as plt
import psutil


def monitor(duration=60, interval=1):
  """Samples CPU% and memory% every `interval` seconds for `duration` seconds."""
  timestamps = []
  cpu_readings = []
  mem_readings = []

  print(f"Monitoring system usage for {duration} seconds...")
  start = time.time()

  while time.time() - start < duration:
    # Sampling interval handled directly by psutil
    cpu_readings.append(psutil.cpu_percent(interval=interval))
    mem_readings.append(psutil.virtual_memory().percent)
    timestamps.append(time.time() - start)

  return timestamps, cpu_readings, mem_readings


def plot_usage(timestamps, cpu_readings, mem_readings, label):
  """Plots CPU% and memory% vs time and saves output image."""
  plt.figure(figsize=(10, 5))
  plt.plot(timestamps, cpu_readings, label="CPU %", color="crimson", linewidth=2)
  plt.plot(timestamps, mem_readings, label="Memory %", color="navy", linewidth=2)

  plt.title(f"Resource Usage Profile - Workload: {label.upper()}", fontsize=14)
  plt.xlabel("Time (seconds)", fontsize=12)
  plt.ylabel("Utilization (%)", fontsize=12)
  plt.ylim(0, 105)
  plt.grid(True, linestyle="--", alpha=0.6)
  plt.legend(loc="upper right", fontsize=11)
  plt.tight_layout()

  file_name = f"usage_{label.lower().replace(' ', '_')}.png"
  plt.savefig(file_name)
  print(f"Saved plot: {file_name}")
  plt.show()


if __name__ == "__main__":
  # Specify task label: 'idle', 'web_browsing', or 'heavy_load'
  current_task_label = "idle"

  t, c, m = monitor(duration=60, interval=1)
  plot_usage(t, c, m, label=current_task_label)