from __future__ import annotations

import json
import os
from typing import Optional, Tuple

import pandas as pd
from geopy.distance import geodesic
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

USER_AGENT = "distancia geodesica"  # troque por algo que te identifique
ARQUIVO_CACHE = "cache_geo.json"

_geolocator = Nominatim(user_agent=USER_AGENT, timeout=10)
_geocode = RateLimiter(_geolocator.geocode, min_delay_seconds=1.1, max_retries=2)
