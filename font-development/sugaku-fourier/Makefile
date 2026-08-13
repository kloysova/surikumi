ROOT := ../..
BUILD_SCRIPT := build_font.py

.PHONY: all clean

all:
	python3 $(BUILD_SCRIPT)

clean:
	$(RM) -r generated
	$(RM) -r $(ROOT)/texmf/fonts/type1/public/sugaku-fourier
	$(RM) -r $(ROOT)/texmf/fonts/afm/public/sugaku-fourier
	$(RM) -r $(ROOT)/texmf/fonts/tfm/public/sugaku-fourier
	$(RM) -r $(ROOT)/texmf/fonts/map/dvips/sugaku-fourier
