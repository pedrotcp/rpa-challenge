from robocorp import log

def setup_log() -> None:
    log.setup_log(output_log_level="info")

__all__ = ["setup_log"]