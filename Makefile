BUILD_DIR := build/public
EXAMPLES := \
	examples/magazine/surikumi-confirmation.tex \
	examples/magazine/surikumi-patterns.tex \
	examples/magazine/surikumi-readability.tex \
	examples/magazine/surikumi-symbol-proof.tex
PDFS := $(patsubst examples/magazine/%.tex,$(BUILD_DIR)/%.pdf,$(EXAMPLES))

.PHONY: all check clean

all: $(PDFS)

check: all

$(BUILD_DIR):
	mkdir -p "$@"

$(BUILD_DIR)/%.pdf: examples/magazine/%.tex surikumi.sty | $(BUILD_DIR)
	TEXINPUTS=.: latexmk -lualatex -interaction=nonstopmode \
		-halt-on-error -outdir="$(BUILD_DIR)" "$<"

clean:
	rm -rf "$(BUILD_DIR)"
	rm -f *.ltjruby
