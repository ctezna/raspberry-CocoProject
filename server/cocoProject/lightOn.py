import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 24)
pixels.fill((255,255,255))
pixels.show()