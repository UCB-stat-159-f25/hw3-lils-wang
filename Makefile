.PHONY : env
env:
    conda env create -n ligo -f environment.yml || conda env update -n ligo -f environment.yml  --prune


.PHONY : html
html:
    myst build --html

.PHONY : clean
clean:
    rm -rf figures
    rm -rf audio
    rm -rf _build