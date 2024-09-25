from typing import List, TypedDict, Optional

class ExternalURLs(TypedDict):
    spotify: str

class Image(TypedDict):
    url: str
    height: int
    width: int

class Restrictions(TypedDict):
    reason: str

class Artist(TypedDict):
    external_urls: ExternalURLs
    href: str
    id: str
    name: str
    type: str
    uri: str

class Album(TypedDict):
    album_type: str
    total_tracks: int
    available_markets: List[str]
    external_urls: ExternalURLs
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str
    release_date_precision: str
    restrictions: Optional[Restrictions]
    type: str
    uri: str
    artists: List[Artist]

class ExternalIDs(TypedDict):
    isrc: str
    ean: str
    upc: str

class Track(TypedDict):
    album: Album
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIDs
    external_urls: ExternalURLs
    href: str
    id: str
    is_playable: bool
    linked_from: dict
    restrictions: Optional[Restrictions]
    name: str
    popularity: int
    preview_url: Optional[str]
    track_number: int
    type: str
    uri: str
    is_local: bool

class TrackData(TypedDict):
    added_at: str
    track: Track
