"""Parses routes.txt from GTFS."""
import re
import uuid
from enum import Enum
from typing import List
from dataclasses import dataclass


@dataclass
class Route:
    route_id: str
    agency_id: str
    route_short_name: str
    route_long_name: str
    route_desc: str
    route_type: int             # class RouteType
    route_url: int              # class URL
    route_color: int            # class HexColor
    route_text_color: int


@dataclass
class RouteType(Enum):
    """Enum to define different route types."""
    TRAM = 0
    SUBWAY = 1
    RAIL = 2
    BUS = 3
    FERRY = 4
    CABLE_TRAM = 5
    AERIAL_LIFT = 6
    FUNICULAR = 7
    TROLLEYBUS = 11
    MONORAIL = 12


@dataclass
class URL:
    """Class to validate and store a URL."""
    def __init__(self, url: str) -> None:
        if self.validate(url):
            self.url = url
            
    def validate(self, url: str) -> bool:
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # Protocol (http, https, ftp)
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # Domain
            r'localhost|'  # Localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6
            r'(?::\d+)?'  # Optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None


@dataclass
class HexColor:
    """Class to validate a 6-digit hex color."""
    def __init__(self, color: str) -> None:
        if self.validate(color):
            self.color = color
    def validate(self, color: str) -> bool:
        return bool(re.fullmatch(r'^[0-9A-Fa-f]{6}$', color))

    

def parse_route_type(value: str) -> RouteType:
    return RouteType(int(value))

def parse_url(value: str) -> URL | None:
    return URL(value) if value else None

def parse_hex_color(value: str) -> HexColor | None:
    return HexColor(value) if value else None

def parse_row_to_route(row: str) -> Route:
    columns = row.split(',')
    route_id = columns[0]
    agency_id = columns[1] if columns[1] else None
    route_short_name = columns[2]
    route_long_name = columns[3]
    route_desc = columns[4] if columns[4] else None
    route_type = parse_route_type(columns[5])
    route_url = parse_url(columns[6])
    route_color = parse_hex_color(columns[7]) if len(columns) > 7 else None
    route_text_color = parse_hex_color(columns[8]) if len(columns) > 8 else None

    return Route(
        route_id=route_id,
        agency_id=agency_id,
        route_short_name=route_short_name,
        route_long_name=route_long_name,
        route_desc=route_desc,
        route_type=route_type,
        route_url=route_url,
        route_color=route_color,
        route_text_color=route_text_color
    )

def parse_routes(rows: List[str]) -> List[Route]:
    return [parse_row_to_route(row) for row in rows]

def query_routes(routes: List[Route], **filters) -> List[Route]:
    results = routes
    for attr, value in filters.items():
        results = [route for route in results if getattr(route, attr) == value]
    return results

# Example usage to read and parse routes.txt
with open("routes.txt", 'r') as file:
    lines = file.readlines()
    routes = parse_routes(lines[1:])
    print(f"There were {len(routes)} routes loaded.")

    # Query function for convenience
    def query(**kwargs):
        for route in query_routes(routes, **kwargs):
            print(route)
