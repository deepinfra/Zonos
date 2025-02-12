from setuptools import setup, find_packages

setup(
    name='zonos',
    version='0.1.0',
    description='Text-to-speech by Zyphra',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/deepinfra/Zonos',
    packages=find_packages(include=["zonos"]),
    install_requires=[
        'torch>=2.5.1',
        'setuptools',
        'packaging',
        'inflect>=7.5.0',
        'kanjize>=1.5.0',
        'numpy>=2.2.2',
        'phonemizer>=3.3.0',
        'sudachidict-full>=20241021',
        'sudachipy>=0.6.10',
        'torchaudio>=2.5.1',
        'transformers>=4.48.1',
        'soundfile>=0.13.1',
        'huggingface-hub>=0.28.1',
    ],
    extras_require={
        'compile': [
            'flash-attn>=2.7.3',
            'mamba-ssm>=2.2.4',
            'causal-conv1d>=1.5.0.post8',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
) 