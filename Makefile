SHELL=/bin/bash

bt_dir=benchmarks/benchmark-tool

copy-programs:
	cp -r benchmarks/programs/* $(bt_dir)/programs
copy-runscripts:
	cp benchmarks/runscripts/* $(bt_dir)/runscripts
copy-templates:
	cp benchmarks/templates/coom.pbs $(bt_dir)/templates
clean-output:
	rm -rf $(bt_dir)/output/
clean-programs:
	rm -f $(bt_dir)/programs/runlim
	rm -f $(bt_dir)/programs/coomsolver*
clean-results:
	rm -rf $(bt_dir)/results/
clean-runscripts:
	rm -f $(bt_dir)/runscripts/runscript-coom-*.xml
clean-templates:
	rm -f $(bt_dir)/templates/coom.pbs
clean:
	make clean-runscripts
	make clean-programs
	make clean-templates
	make clean-output
copy:
	make copy-programs
	make copy-runscripts
	make copy-templates
