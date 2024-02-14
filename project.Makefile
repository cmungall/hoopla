## Add your own custom Makefile targets here

w1 = $(word 1,$(subst /, ,$*))
w2 = $(word 2,$(subst /, ,$*))
w2b = $(word 1,$(subst -, ,$(w2)))

S=src/hoopla/schema

$(S)/%.ofn: $(S)/%.yaml
	$(RUN) linkml-data2owl -s $(S)/$(w1)/$(w1).yaml $< -C $(w2b) -o $@
