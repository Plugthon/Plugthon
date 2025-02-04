# Import the subprocess module for executing external commands
import subprocess

# This class represents a data center and provides methods to check the status of its servers
class DataCenter:
  def __init__(self):
    """
    Initializes the DataCenter object with a list of IP addresses 
    for each data center.
    """
    self.ip_addresses = [
      "149.154.175.50",
      "149.154.167.50",
      "149.154.175.100",
      "149.154.167.91",
      "91.108.56.130"
    ]

    # Set to store available data centers
    self.status = set([])

    # Set to store unavailable data centers
    self.failed_ping = set([])

  def GetDataCenterStatus(self, ip_addresses):
    """
    Pings the specified IP address and returns the latency in milliseconds.

    Args:
      ip_addresses: The IP address of the data center to ping.

    Returns:
      The latency in milliseconds if the ping was successful, 
      otherwise None.
    """
    try:
      output = subprocess.check_output(["ping", "-c", "1", "-n", "-q", ip_addresses], text=True)
      lines = output.splitlines()
      for line in lines:
        if "rtt min/avg/max/mdev" in line:
          latency_str = line.split("=")[1].split("/")[1]
          latency_ms = float(latency_str)
          return latency_ms
    except subprocess.CalledProcessError:
      return None

  async def DataCenterStatus(self, event):
    """
    Checks the status of all data centers and updates the event message.

    Args:
      event: The event object to update with the status message.

    Returns:
      The formatted status message string.
    """
    await event.edit("Connecting...")
    for ip in self.ip_addresses:
      latency = self.GetDataCenterStatus(ip)
      if latency:
        # If ping is successful, add to available data centers
        if ip == self.ip_addresses[0]:
          self.status.add(f"DC1 - MIA, Miami FL, USA\nAvailable, Ping: {latency:.2f} ms\n")
        elif ip == self.ip_addresses[1]:
          self.status.add(f"DC2 - AMS, Amsterdam, NL\nAvailable, Ping: {latency:.2f} ms\n")
        elif ip == self.ip_addresses[2]:
          self.status.add(f"DC3 - MIA, Miami FL, USA\nAvailable, Ping: {latency:.2f} ms\n")
        elif ip == self.ip_addresses[3]:
          self.status.add(f"DC4 - AMS, Amsterdam, NL\nAvailable, Ping: {latency:.2f} ms\n")
        elif ip == self.ip_addresses[4]:
          self.status.add(f"DC5 - SIN, Singapore, SG\nAvailable, Ping: {latency:.2f} ms")
      else:
        # If ping fails, add to unavailable data centers
        if ip == self.ip_addresses[0]:
          self.failed_ping.add(f"DC1 - MIA, Miami FL, USA is currently unavailable\n")
        elif ip == self.ip_addresses[1]:
          self.failed_ping.add(f"DC2 - AMS, Amsterdam, NL is currently unavailable\n")
        elif ip == self.ip_addresses[2]:
          self.failed_ping.add(f"DC3 - MIA, Miami FL, USA is currently unavailable\n")
        elif ip == self.ip_addresses[3]:
          self.failed_ping.add(f"DC4 - AMS, Amsterdam, NL is currently unavailable\n")
        elif ip == self.ip_addresses[4]:
          self.failed_ping.add(f"DC5 - SIN, Singapore, SG is currently unavailable\n")
    
    # Construct and return the formatted status message
    if self.status and self.failed_ping:
      self.string_status = "\n".join(sorted(self.status))
      self.string_failed_ping = "\n".join(sorted(self.failed_ping))
      self.two_status = f"Telegram's data center status is being monitored in real-time by Plugthon.\n\nAvailable Data Centers\n{self.string_status}\n\nUnavailable Data Centers\n{self.string_failed_ping}"
      self.status.clear()
      self.failed_ping.clear()
      return self.two_status

    elif self.status:
      self.string_status = "\n".join(sorted(self.status))
      self.one_status = f"Telegram's data center status is being monitored in real-time by Plugthon.\n\nAvailable Data Centers\n{self.string_status}"
      self.status.clear()
      return self.one_status

    elif self.failed_ping:
      self.string_failed_ping = "\n".join(sorted(self.failed_ping))
      self.one_failed_ping = f"Telegram's data center status is being monitored in real-time by Plugthon.\n\nUnavailable Data Centers\n{self.failed_ping}"
      self.failed_ping.clear()
      return self.one_failed_ping