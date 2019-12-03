import rpi_ws281x as neopixel
import time


LED_COUNT = 72
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 100
LED_INVERT = False
LED_CHANNEL = 0


class LEDController:
    def __init__(self):
        self.strip = neopixel.Adafruit_NeoPixel(LED_COUNT,
                                                LED_PIN,
                                                LED_FREQ_HZ,
                                                LED_DMA,
                                                LED_INVERT,
                                                LED_BRIGHTNESS,
                                                LED_CHANNEL)
        self.strip.begin()

    def on(self, color_name, pattern):
        func = getattr(self, pattern)
        color = neopixel.Color(0, 0, 255)
        if color_name == 'blue':
            color = neopixel.Color(0, 0, 255)
        elif color_name == 'red':
            color = neopixel.Color(0, 255, 0)
        elif color_name == 'green':
            color = neopixel.Color(255, 0, 0)
        func(color, 10)

    def on_rainbow(self, pattern):
        func = getattr(self, pattern)
        func()

    def off(self):
        self.color_wipe(neopixel.Color(0, 0, 0), 0)

    def color_wipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def color_flash(self, color, wait_ms1=50, wait_ms2=50):
        for i in range(5):
            self.color_on(color, wait_ms1)
            self.color_on(neopixel.Color(0, 0, 0), wait_ms1)

    def color_on(self, color, wait_ms=50):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms/1000)

    def theater_chase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, color)
                self.strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)

    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return neopixel.Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return neopixel.Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return neopixel.Color(0, pos * 3, 255 - pos * 3)

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.wheel((i+j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def rainbow_cycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                color = self.wheel((int(i * 256 / self.strip.numPixels()) + j) & 255)
                self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def theater_chase_rainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(25):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, self.wheel((i+j) % 255))
                self.strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)
