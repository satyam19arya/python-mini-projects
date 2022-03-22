import time
from plyer import notification

if __name__ == '__main__':
    notification.notify(
        title="Please drink water",
        message="About 15.5 cups (3.7 liters) of fluids a day for men",
        timeout=10
    )
  #  time.sleep(5)