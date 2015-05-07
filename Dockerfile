FROM django:python3-onbuild

RUN apt-get update

RUN apt-get install -y texlive-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra