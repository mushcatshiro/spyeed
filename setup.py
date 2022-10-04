from setuptools import setup


setup(
    name="spyeed",
    version="",
    description="speeds up python development",
    install_requires=[],
    python_requires=">3.6",
    entry_points={
        "console_scripts": [
            "spyeed generate = spyeed.__main__:spyeed",
            "s g = spyeed.__main__:spyeed"
        ]
    }
)