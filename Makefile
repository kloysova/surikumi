BUILD_DIR := build/public
PS_BUILD_DIR := build/public/problem-sets
KAISETSU_BUILD_DIR := build/public/kaisetsu
EXAMPLES := \
	examples/magazine/surikumi-confirmation.tex \
	examples/magazine/surikumi-patterns.tex \
	examples/magazine/surikumi-symbol-proof.tex
PDFS := $(patsubst examples/magazine/%.tex,$(BUILD_DIR)/%.pdf,$(EXAMPLES))

PROBLEM_SETS := $(sort $(wildcard examples/problem-sets/ps*.tex))
PS_PDFS := $(patsubst examples/problem-sets/%.tex,$(PS_BUILD_DIR)/%.pdf,$(PROBLEM_SETS))

KAISETSU := $(sort $(wildcard examples/kaisetsu/kaisetsu-*.tex))
KAISETSU_PDFS := $(patsubst examples/kaisetsu/%.tex,$(KAISETSU_BUILD_DIR)/%.pdf,$(KAISETSU))

.PHONY: all check clean problem-sets kaisetsu

all: $(PDFS) $(KAISETSU_PDFS)

# The journal-style expository articles built on surikumi-kaisetsu.sty.
kaisetsu: $(KAISETSU_PDFS)

# The ten problem-set format proposals. Kept out of `all` so the default
# build stays as fast as before; run `make problem-sets` to build them.
problem-sets: $(PS_PDFS)

check: all problem-sets

$(BUILD_DIR):
	mkdir -p "$@"

$(PS_BUILD_DIR):
	mkdir -p "$@"

$(KAISETSU_BUILD_DIR):
	mkdir -p "$@"

# config/.latexmkrc puts the in-project texmf tree on the font and input
# search paths. surikumi's default summation glyph lives there, so every
# rule loads it.
LATEXMK := latexmk -r config/.latexmkrc -lualatex -interaction=nonstopmode -halt-on-error

$(BUILD_DIR)/%.pdf: examples/magazine/%.tex surikumi.sty | $(BUILD_DIR)
	TEXINPUTS=.: $(LATEXMK) -outdir="$(BUILD_DIR)" "$<"

$(KAISETSU_BUILD_DIR)/%.pdf: examples/kaisetsu/%.tex surikumi.sty \
		surikumi-kaisetsu.sty | $(KAISETSU_BUILD_DIR)
	TEXINPUTS=.: $(LATEXMK) -outdir="$(KAISETSU_BUILD_DIR)" "$<"

$(PS_BUILD_DIR)/%.pdf: examples/problem-sets/%.tex surikumi.sty \
		examples/problem-sets/surikumi-mondaishu.sty | $(PS_BUILD_DIR)
	TEXINPUTS=.:examples/problem-sets: $(LATEXMK) -outdir="$(PS_BUILD_DIR)" "$<"

clean:
	rm -rf "$(BUILD_DIR)"
