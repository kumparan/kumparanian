"""This module implement a command for the data engineer command group"""
from .help_text import de_help_text as help_text
from .help_text import generate_short_help
from .help_text import generate_usage
from .help_text import verify_short_help
from .help_text import verify_usage
from .help_text import evaluate_short_help
from .help_text import evaluate_usage
from .dataset import generate_data
from .submission import verify
from .submission import evaluate

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
    evaluate
]
