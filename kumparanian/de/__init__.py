"""This module implement a command for the data engineer command group"""

from .dataset import generate_data
from .help_text import de_help_text as help_text
from .help_text import (
    evaluate_short_help,
    evaluate_usage,
    generate_short_help,
    generate_usage,
    verify_short_help,
    verify_usage,
)
from .submission import evaluate, verify

__all__ = [
    help_text,
    generate_usage,
    generate_short_help,
    generate_data,
    verify_usage,
    verify_short_help,
    evaluate_usage,
    evaluate_short_help,
    verify,
    evaluate,
]
