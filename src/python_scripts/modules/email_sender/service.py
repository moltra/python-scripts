"""
Service: email_sender – send an email using SMTP.

Credentials/config are loaded via environment variables (pydantic-settings) with
prefix EMAIL_. Do not hardcode secrets.
"""
from __future__ import annotations

import smtplib
from email.mime.text import MIMEText
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class EmailSettings(BaseSettings):
    """
    SMTP configuration for email sending.

    @env EMAIL_HOST        SMTP host
    @env EMAIL_PORT        SMTP port (default 587)
    @env EMAIL_USERNAME    Username/login
    @env EMAIL_PASSWORD    Password or app password
    @env EMAIL_FROM        Default sender address
    @env EMAIL_USE_TLS     Use STARTTLS (default true)
    """

    host: str
    port: int = 587
    username: str
    password: str
    from_addr: str
    use_tls: bool = True

    model_config = SettingsConfigDict(
        env_prefix="EMAIL_",
        env_file=".env",
        env_file_encoding="utf-8",
    )


def send_text_email(
    to: str,
    subject: str,
    body: str,
    settings: Optional[EmailSettings] = None,
) -> None:
    """
    Send a simple text email using SMTP.
    """
    cfg = settings or EmailSettings()
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = cfg.from_addr
    msg["To"] = to

    with smtplib.SMTP(cfg.host, cfg.port) as server:
        if cfg.use_tls:
            server.starttls()
        server.login(cfg.username, cfg.password)
        server.send_message(msg)
