"""
This module provides dataclass common Plex data object.
"""

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

__all__ = ["Actor", "Show", "Episode", "Movie"]


@dataclass
class Actor:
    """
    Represent an actor of a show or movie.
    """
    name: Optional[str] = None
    role: Optional[str] = None
    photo: Optional[str] = None


@dataclass
class Show:
    """
    Represent a show.
    """
    title: Optional[str] = None
    sort_title: Optional[str] = None
    original_title: Optional[str] = None
    content_rating: Optional[str] = None
    tagline: Optional[str] = None
    studio: Optional[str] = None
    aired: Optional[date] = None
    summary: Optional[str] = None
    rating: Optional[float] = None
    genres: List[str] = field(default_factory=list)
    collections: List[str] = field(default_factory=list)
    actors: List[Actor] = field(default_factory=list)


@dataclass
class Episode:
    """
    Represent an episode.
    """
    title: Optional[str] = None
    episode: Optional[int] = None
    aired: Optional[date] = None
    content_rating: Optional[str] = None
    summary: Optional[str] = None
    directors: List[str] = field(default_factory=list)
    writers: List[str] = field(default_factory=list)
    rating: Optional[float] = None


@dataclass
class Movie:
    """
    Represent an movie.
    """
    title: Optional[str] = None
    sort_title: Optional[str] = None
    original_title: Optional[str] = None
    content_rating: Optional[str] = None
    tagline: Optional[str] = None
    studio: Optional[str] = None
    aired: Optional[date] = None
    summary: Optional[str] = None
    rating: Optional[float] = None
    genres: List[str] = field(default_factory=list)
    collections: List[str] = field(default_factory=list)
    actors: List[Actor] = field(default_factory=list)
    writers: List[str] = field(default_factory=list)
    directors: List[str] = field(default_factory=list)
