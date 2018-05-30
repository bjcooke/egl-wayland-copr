DNF=/usr/bin/dnf
RPMBUILD=/usr/bin/rpmbuild


srpm:	egl-wayland-srpm

rpm-build:
	$(DNF) -y install $@

egl-wayland-srpm:	rpm-build
	$(RPMBUILD) -bs \
		--define="_topdir `pwd`" \
		--define="_sourcedir `pwd`" \
		--define="_specdir `pwd`" \
		--define="_srcrpmdir $(outdir)" \
		$(spec)
