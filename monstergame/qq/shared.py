from monstergame.qq.TileCache import TileCache

__author__ = 'cbayley'
DX = [ 0, 1, 0, -1]
DY = [-1, 0, 1,  0]
MAP_TILE_WIDTH  = 24
MAP_TILE_HEIGHT = 16
SPRITE_CACHE = TileCache()
MAP_CACHE    = TileCache(MAP_TILE_WIDTH, MAP_TILE_HEIGHT)
TILE_CACHE   = TileCache(32, 32)