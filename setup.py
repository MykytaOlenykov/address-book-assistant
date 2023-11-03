from setuptools import setup, find_namespace_packages

setup(
    name="bot-assistant",
    version="1",
    description="Very useful code",
    url="https://github.com/MykytaOlenykov/address-book-assistant-MCS3-team1",
    author="SITE",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["prompt_toolkit"],
    entry_points={"console_scripts": ["bot-assistant = bot_assistant.main:main"]},
    include_package_data=True,
)
