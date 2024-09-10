# Functional Suite

`test/` contains automated `testing` suite that will validate the correctness of your program for the sample input and output using python `unittest` (build-in) module.

We do not support Windows at this point in time. If you don't have access to an OSX or Linux machine, we recommend setting up a Linux machine you can develop against using something like [VirtualBox](https://www.virtualbox.org/) or [Docker](https://docs.docker.com/docker-for-windows/#test-your-installation).

This needs [Python to be installed](https://www.python.org/downloads/source/), followed by some libraries. The steps are listed below.

## Setup

First, install [Python](https://www.python.org/downloads/source/). or using wget for installation.

```
wget https://www.python.org/ftp/python/3.8.17/Python-3.8.17.tgz \
    && tar xzf Python-3.8.17.tgz
    
cd Python-3.8.17
./configure --prefix=/opt/python3.8 && make -j $(nproc) && make altinstall
...
...
Successfully installed all dependencies.

```

## Usage

You need run setup preparation for all dependencies
```
warehouse_rack $ /bin/setup
```

You can run the full suite from `warehouse_rack` by doing
```
warehouse_rack $ bin/warehouse_rack $1
```

You can run the unittest from `warehouse_rack` by doing
```
warehouse_rack $ bin/run_fuctional_tests
```

## Development References

We development Python pure using [built-in package](https://docs.python.org/3.8/library/index.html)
