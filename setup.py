#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='<寻找地区码>',
    version='<version:1.0>',
    description=(
        '<从一个乱的字符串中提取地区码>'
    ),
    long_description=open('README.rst').read(),
    author='<loo>',
    author_email='<1213788433@qq.com>',
    maintainer='<loo>',
    maintainer_email='<1213788433@qq.com',
    license='BSD License',
    packages=find_code(),
    platforms=["all"],
    url='<项目的网址，我一般都是github的url>',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
