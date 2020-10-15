# obs_ctmo

This repo contains code to adapt the Cristina Torres Memorial Observatory in
Brownsville, Texas to work with the LSST software stack.

Basic layout taken from [this tutorial](https://lsstcamdocs.readthedocs.io/en/latest/intro.html).

## Docker Image

To build and run a Docker container with an image of LSST Software Stack with `obs_ctmo` installed, do the following:

    % docker build --tag ctmo/lsstpipe:latest .

### Run in detached mode

Prepare to run it in [detached mode](https://pipelines.lsst.io/install/docker.html).

    % docker run -itd --name ctmo ctmo/lsstpipe:latest

This will create a container from ctmo image in detached mode.

From a shell on your host system, open a shell in the container with the docker exec command:

    % docker exec -it ctmo /bin/bash

Your prompt is now a prompt in the container with `obs_ctmo` installed.

You can repeat this process, attaching to the container multiple times, to open multiple container shells.
To close a container shell, type exit.

Finally, to stop the container entirely, run this command from your host’s shell:

    % docker stop ctmo

And delete the container after you no longer need it.

    % docker rm ctmo

---

(c) CTMO Dev Team
