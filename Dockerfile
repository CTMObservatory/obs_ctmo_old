FROM lsstsqre/centos:7-stack-lsst_distrib-v21_0_0

RUN echo "source /opt/lsst/software/stack/loadLSST.bash" >> /home/lsst/.bashrc
RUN mkdir -p /opt/lsst/software/stack/stack/miniconda3-py37_4.8.2-cb4e2dc/Linux64/obs_ctmo/v1
COPY . /opt/lsst/software/stack/stack/miniconda3-py37_4.8.2-cb4e2dc/Linux64/obs_ctmo/v1
RUN eups declare obs_ctmo v1 -r ${EUPS_PATH}/Linux64/obs_ctmo/v1
RUN eups declare -t current obs_ctmo v1
RUN setup obs_ctmo v1
