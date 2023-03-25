from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseSettings

from web_test.assist import project

EnvContext = Literal['local', 'prod']


class Settings(BaseSettings):
    """
    系统配置类，用于存储系统运行时需要的各种参数和配置。
    """

    context: EnvContext = 'local'

    debugging_mode: bool = True

    browser_name: str = ''
    browser_version: str = ''

    base_url: str = ''

    timeout: float = 10.0

    maximize_window: bool = False
    window_width: int = 1920
    window_height: int = 1080

    headless: bool = False
    incognito: bool = True

    remote_url: Optional[str] = ''
    remote_enableVNC: bool = True
    remote_enableVideo: bool = False
    remote_enableLog: bool = True

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> Settings:
        """
        根据指定的环境上下文或当前运行的上下文获取系统配置对象。

        :param env: 可选的环境上下文，如果为空，则使用当前运行的上下文。
        :return: 系统配置对象。
        """

        asked_or_current = env or cls().context
        return cls(
            _env_file=project.abs_path_from_project(
                f'config.{asked_or_current}.env'
            )
        )


settings = Settings.in_context()
