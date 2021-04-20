import os

# ---- About bot section ----
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "!")

branding = "AIML Chatter Bot"  # Brand name for the bot
creator = "Sunrit Jana"  # Name of the creator
devs = [711194921683648523]  # ID of the developers.

# -- Logger configuration --
log_file = "logs/bot.log"
log_level = "INFO"
log_format = (
    "<green>{time:YYYY-MM-DD hh:mm:ss}</green> | <level>{level: <8}</level> | "
    "<cyan>{name: <18}</cyan> | <level>{message}</level>"
)
log_file_size = "150 MB"
