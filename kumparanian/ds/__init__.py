"""This module implement a command for the data scientist command group"""
from .model import verify
from .help_text import ds_help_text as help_text
from .help_text import verify_short_help
from .help_text import verify_usage
from .help_text import evaluate_short_help
from .help_text import evaluate_usage

__all__ = [
    help_text,
    verify_usage,
    verify_short_help,
    evaluate_short_help,
    evaluate_usage,
    verify
]
